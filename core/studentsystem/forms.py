from django import forms
from .models import AddStudents

class Edit(forms.ModelForm):
    class Meta:
        model = AddStudents
        fields = ["sdtname","sdtid","sdtclass","sdttel","sdtemail","sdtday","parentname"]