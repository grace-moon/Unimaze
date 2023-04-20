from django import forms
from .models import Map_Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Map_Post
        fields = ('building_name','building_num', 'door_num','vectary_viewer_key', 'text',)