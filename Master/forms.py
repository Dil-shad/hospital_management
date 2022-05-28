from django import forms
from django import forms


from .models import *


class ContactModelForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = '__all__'
