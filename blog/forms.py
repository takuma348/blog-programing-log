from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from .models import Comment, ReComment, File


class PostSerachForm(forms.Form):

    keyword = forms.CharField(
        label='キーワード', required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control mr-sm-2', 'placeholder': 'クイックサーチ'}),
    )


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text', 'icon')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
            }),
            'icon': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


class ReCommentCreateForm(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ('name', 'text', 'icon')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
            }),
            'icon': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }


FileInlineFormSet = generic_inlineformset_factory(
    File, fields=('src',), can_delete=False, extra=1,
)