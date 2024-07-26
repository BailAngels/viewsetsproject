from django import forms 

from apps.blogs.models import Blog
from apps.tags.models import Tag


class BlogForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget = forms.CheckboxSelectMultiple())

    class Meta:
        model = Blog
        fields = ['tag','title','description']