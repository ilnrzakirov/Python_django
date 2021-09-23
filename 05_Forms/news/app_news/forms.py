from django import forms
from .models import News, NewsComment

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Выбрать статус"

    class Meta:
        model = News
        fields = '__all__'
        widgets ={
            'description': forms.Textarea(attrs={'cols': 70, 'rows': 10})
        }


class NewsCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].empty_label = "Автор не выбран"
        self.fields['news'].empty_label = 'Выберите новость'

    class Meta:
        model = NewsComment
        fields = ['username', 'comment_text', 'news']
        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }