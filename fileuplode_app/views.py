from django.shortcuts import render, redirect
from .forms import FileUploadForm
import pandas as pd 
# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload_file = form.save()

            if upload_file.file.name.endswith('.csv'):
                df = pd.read_csv(upload_file.file.path)
            
            else:
                df = pd.read_excel(upload_file.file.path)
            
            columns = df.columns.tolist()
            return render(request,'upload_success.html',{'columns':columns})

          
    else:
        form = FileUploadForm()
    return render(request,'upload.html',{'form':form})

def upload_success(request):
    return render(request,'upload_success.html')

