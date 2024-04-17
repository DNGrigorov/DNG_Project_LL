from django import forms
from .models import Post, Comment
from AccountApp.models import Rating

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'type_of_post']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your post content here...'}),
            'type_of_post': forms.Select(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
                        'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Comment here...'}),

        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),  # Customize textarea attributes
        }

class RatingForm(forms.ModelForm):
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('German', 'German'),
        ('Japanese', 'Japanese'),
    ]

    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    stars = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter stars here'}))

    class Meta:
        model = Rating
        fields = ['language', 'stars']