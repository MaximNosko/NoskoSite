from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=("text","news")

class DelComment(forms.Form):
    comment_id = forms.IntegerField()