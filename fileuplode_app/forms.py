from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
        widgets = {

            'file': forms.FileInput(attrs={'accept':'.csv,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel'})
        }
    
    def clean_file(self):

        file = self.cleaned_data.get('file')
        if file:
            ext = file.name.split('.')[-1].lower()
            if ext not in ['csv','xlsx','xls']:
                raise forms.ValidationError("Only CSV and Excel file are allowed")

        return file