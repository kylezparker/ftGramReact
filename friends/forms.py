from django import forms

from .models import Share

MAX_SHARE_LENGTH = 240

class ShareForm(forms.ModelForm):
    class Meta: 
        model = Share
        fields =['content'] 
    
    def clean_content(self):
        content= self.cleaned_data.get("content")
        if len(content) > MAX_SHARE_LENGTH:
            raise forms.ValidationError("This post is too long")
        return content