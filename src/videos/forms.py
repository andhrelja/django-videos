from django import forms
from .models import Video

class VideoModelForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = ("name",
                  "description",
                  "category_type",
                  "category_subtype",
                  "video")
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "category_type": forms.Select(attrs={'class': 'custom-select', 'onchange': 'toggleVideoCategories()'}),
            "category_subtype": forms.Select(attrs={'class': 'custom-select'}),
            "video": forms.FileInput(attrs={'class': 'form-control'})
        }
