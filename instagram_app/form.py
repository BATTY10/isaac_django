from django.forms import ModelForm
from .models import Comment, Post


class Create_Comment_Form(ModelForm):
    class Meta:
        model = Comment
        fields ='__all__'
        
class Create_PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'