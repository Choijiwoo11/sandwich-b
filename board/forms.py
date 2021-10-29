# from django.forms import forms
#
# # then I change as below field:
from django.forms import ModelForm
from django import forms
from .models import Post

from .models import Comment

from board.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_contents']
