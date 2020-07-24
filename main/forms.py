from django import forms
from .models import Bookmark    # models.py에 있는 Bookmark 받아온다.

class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label = "사이트 이름")
    site_url = forms.CharField(label = "사이트 주소")

    class Meta:
        model = Bookmark
        fields = '__all__'  # __all__ : bookmark에 있는 fields 다 가져오라는 뜻 