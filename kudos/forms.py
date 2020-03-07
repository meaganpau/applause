from django import forms
from .models import Kudos

class KudosForm(forms.ModelForm):
    
    class Meta:
        model = Kudos
        fields = [
            'receiver',
            'message',
            'sender'
        ]
        exclude = ['sender']
