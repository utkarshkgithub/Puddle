from django import forms
from .models import Item

Input_Class = 'w-full py-4 px-6 rounded-xl border bg-white'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name' ,'description', 'price' ,'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': Input_Class
            }),
            'name': forms.TextInput(attrs={
                'class': Input_Class
            }),
            'description': forms.Textarea(attrs={
                'class': Input_Class
            }),
            'price': forms.TextInput(attrs={
                'class': Input_Class
            }),
            'image': forms.FileInput(attrs={
                'class': Input_Class
            }),
        }