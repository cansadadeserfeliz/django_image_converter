from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ImageForm(forms.Form):
    image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Convert'))