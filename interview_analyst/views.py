from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import ManagerEvaluationForm
from .utils import CustomChatGPT, create_gpt_input, process_excel_file
from . tasks import send_email_task



class EvaluateManagerView(View):
    """View for evaluating manager responses.

    This view renders a form for collecting manager evaluation responses.
    Upon form submission, it processes the responses, generates a final string,
    passes it to the CustomChatGPT function to generate a GPT reply,
    and renders a success template with the GPT reply.

    Attributes:
        template_name (str): The name of the template to render.
    """
    template_name = 'evaluate_manager.html'

    def get(self, request, *args, **kwargs):
        """Handles GET requests.

        Renders the manager evaluation form.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The HTTP response containing the rendered template.
        """
        form = ManagerEvaluationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Handles POST requests.

        Processes the manager evaluation form data, generates a final string,
        uses CustomChatGPT to generate a GPT reply, and renders a success template
        with the GPT reply.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The HTTP response containing the rendered template.
        """
        form = ManagerEvaluationForm(request.POST)
        if form.is_valid():
            # Get responses from the form
            final_string = create_gpt_input(form.cleaned_data)
            gpt_reply  =  CustomChatGPT(final_string)
            return render(request, 'success.html', {'final_string': gpt_reply})
        else:
            return render(request, self.template_name, {'form': form})



def home(request):
    """Render the home page.

    Returns:
        HttpResponse: The HTTP response containing the rendered home page template.
    """
    return render(request, 'home.html')

class UploadFileView(View):
    """View for uploading files."""
    template_name = 'upload_file.html'

    def get(self, request):
        """Handle GET requests.

        Render the upload file form.

        Returns:
            HttpResponse: The HTTP response containing the rendered template.
        """
        return render(request, self.template_name)

    def post(self, request):
        """Handle POST requests.

        Process the uploaded file, send an email with the processed data,
        and display a success or error message.

        Returns:
            HttpResponse: The HTTP response containing the rendered template.
        """        
        if request.method == 'POST':
            uploaded_file = request.FILES.get('file')
            if uploaded_file:
                data = process_excel_file(uploaded_file)
                if data is not None:
                    send_email_task.delay(data)
                    messages.success(request, 'File processed successfully. You will receive an email shortly.')
                    return render(request, 'home.html', {'data': data})
                else:
                    messages.error(request, 'Error processing the file. Please try again.')
        else:
            messages.error(request, 'No file uploaded.')
        return render(request, 'upload_file.html')
