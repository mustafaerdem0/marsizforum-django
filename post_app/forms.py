from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import post,Comments


class CreatePost(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget = CKEditorWidget(),)

        model = post
        fields = ["title","category","content"]
        
  
class CreateComment(forms.ModelForm):
    class Meta:
        comment_content = forms.CharField(widget=CKEditorWidget())
        model = Comments
        fields = ['comment_content']
    def __init__(self, *args, **kwargs):
        super(CreateComment, self).__init__(*args, **kwargs)
        self.fields['comment_content'].label = ""