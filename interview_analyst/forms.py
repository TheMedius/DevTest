# forms.py
from django import forms

class ManagerEvaluationForm(forms.Form):
    experience = forms.CharField(label='Experience', max_length=100)
    experience_years = forms.IntegerField(label='Experience Years')

    ans1 = forms.CharField(label='Q1 - Describe your experience with diary management and scheduling appointments', widget=forms.Textarea)
    ans2 = forms.CharField(label='Q2 - How do you handle confidential information and sensitive situations?', widget=forms.Textarea)
    ans3 = forms.CharField(label='Q3 - Provide an example of a complex problem you\'ve solved in a similar role', widget=forms.Textarea)
    ans4 = forms.CharField(label='Q4 - How do you prioritize tasks and manage your time when dealing with a busy executive\'s schedule?', widget=forms.Textarea)
    ans5 = forms.CharField(label='Q5 - How comfortable are you with liaising with high-level stakeholders and managing professional relationships?', widget=forms.Textarea)
    ans6 = forms.CharField(label='Q6 - Describe a situation where you had to handle an unexpected issue or emergency', widget=forms.Textarea)
    ans7 = forms.CharField(label='Q7 - What experience do you have with travel planning and logistics?', widget=forms.Textarea)
    ans8 = forms.CharField(label='Q8 - How do you ensure effective communication between the MD and other parties?', widget=forms.Textarea)
    ans9 = forms.CharField(label='Q9 - Provide an example of an initiative you took to improve efficiency or effectiveness in your role', widget=forms.Textarea)
    ans10 = forms.CharField(label='Q10 - How do you handle stress and pressure in managing a busy executive\'s affairs?', widget=forms.Textarea)
