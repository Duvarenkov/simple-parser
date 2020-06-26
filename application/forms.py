from django import forms


class URLForm(forms.Form):
    url = forms.URLField(label='Webpage URL', max_length=2048)
