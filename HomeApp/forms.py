from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'type_of_post']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your post content here...'}),
            'type_of_post': forms.Select(attrs={'class': 'form-control'}),
        }
