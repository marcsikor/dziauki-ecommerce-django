from django import forms
from .models import PropertyPosting

class InputForm(forms.ModelForm):
    class Meta:
        model = PropertyPosting
        fields = "__all__"
        widgets = {
            'postingTitle' : forms.TextInput(
                attrs={
                    "class" : "border border-solid border-slate-300"
                }
            )
        }