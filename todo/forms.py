from django import forms
from django.utils import timezone

tag_list =(
    ("1", "Very Important"),
    ("2", "Important"),
    ("3", "Less Important"),
    ("4", "Not Important"),
)

status_list =(
    ("1", "Completed"),
    ("2", "Incompleted"),
)

# creating a form 
class Taskinput(forms.Form):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(widget=forms.Textarea)
    tag = forms.ChoiceField(choices = tag_list)
    status = forms.ChoiceField(choices = status_list)
    # created_date = forms.DateTimeField(default = timezone.now)
    updated_date = forms.DateTimeField()