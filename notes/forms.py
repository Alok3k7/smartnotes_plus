from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from .models import Note

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Note
        fields = ['title', 'content', 'is_public','tags']