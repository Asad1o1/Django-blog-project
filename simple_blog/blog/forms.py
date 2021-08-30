from django import forms
from . import models

category_choices = models.Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'type': 'hidden', 'id': 'logged_in_username'}),
            # 'author': forms.Select(attrs={'class': 'form-control', }),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your thoughts here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Content"


class EditPostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your thoughts here'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Content"


class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'type': 'hidden', 'id': 'logged_in_username'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your Comments here'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Comment"

    
    