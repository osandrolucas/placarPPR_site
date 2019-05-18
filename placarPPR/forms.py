from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('publicador', 'title', 'meta_ano', 'meta_acum', 'real_acum', 'qt_salarios', 'obs',)
