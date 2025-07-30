from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
        widgets = {
            'message': CKEditorWidget(),
        }