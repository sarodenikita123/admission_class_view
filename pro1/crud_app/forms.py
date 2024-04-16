from django import forms
from .models import Admission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"

        widgets = {
            "candidate_name ": forms.TextInput(attrs={"class": "form-control"}),
            "previous_marks": forms.TextInput(attrs={"class": "form-control"}),
            "standard": forms.TextInput(attrs={"class": "form-control"}),
            "admission_date": forms.TextInput(attrs={"type": "date"}),
        }
