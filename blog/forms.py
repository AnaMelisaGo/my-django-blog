from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    class Meta:
        """
        Form meta
        """
        model = Comment
        fields = ('body',)
