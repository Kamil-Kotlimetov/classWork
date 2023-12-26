from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(verbose_name='birthdate')
    tel = models.CharField(max_length=16)
    news_num = models.IntegerField(default=0, verbose_name='количество публикаций')

    def __str__(self):
        return f'{self.user.email}'

# добавление от 26.12.23

class Record(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='профиль')
    title = models.CharField(max_length=256, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    class Meta:
        db_table = 'records'
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['-created_at']


class ImagesRecord(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='records/', null=True)

    class Meta:
        db_table = 'images2record'
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'