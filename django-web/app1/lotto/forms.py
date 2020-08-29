from django import forms 
from .models import GuessNumber

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumber
        fields = ('name', 'text', )
        