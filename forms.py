from django.forms import ModelForm
from .models import Assignment


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['due_date', 'name']