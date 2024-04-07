from django.urls import path
from .views import EvaluateManagerView, home, UploadFileView

urlpatterns = [
    path('evaluate-manager/', EvaluateManagerView.as_view(), name='evaluate_manager'),
    path('', home, name='home'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    # path('display-final-string/', display_final_string, name='display_final_string'),
]
