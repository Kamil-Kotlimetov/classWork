from django import forms
from .models import News, Comment

# class NewsForm(forms.ModelForm):
#
#
#     class Meta:
#         model = News
#         # fields = '__all__'
#         exclude = ['activity_flag']

class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок Новости')
    content = forms.CharField(widget=forms.Textarea, label='Содержание')
    username = forms.CharField(max_length=20, label='Логин')
    first_name = forms.CharField(max_length=20, label='Имя')
    last_name = forms.CharField(max_length=20, label='Фамилия')
    email = forms.EmailField(max_length=50, label='email')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['news', 'published_at']