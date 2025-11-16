from django import forms
from .models import ArticleComment

class SendCommentModelForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = [
            "article",
            "text",
            "user",
            "parent"
        ]
        widgets = {
            "text": forms.Textarea(),
            "article": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "parent": forms.HiddenInput(),
            }
