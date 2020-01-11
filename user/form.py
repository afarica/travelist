from django import forms
from .models import Tag, Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'slug', 'body', 'tags', 'wherefrom', 'whereto', 'when', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'wherefrom': forms.TextInput(attrs={'class': 'form-control'}),
            'whereto': forms.TextInput(attrs={'class': 'form-control'}),
            'when': forms.TextInput(attrs={'class': 'form-control'})
        }

        class TagForm(forms.ModelForm):
            class Meta:
                model = Tag
                fields = ['title', 'slug']

                widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'slug': forms.TextInput(attrs={'class': 'form-control'})}


