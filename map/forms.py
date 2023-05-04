from django import forms
from .models import Unimaze_Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Unimaze_Post
        fields = ('title','category', 'text',)