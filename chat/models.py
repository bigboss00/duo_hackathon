from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', verbose_name='Получатель')
    message = models.CharField('Сообщения', max_length=1200)
    timestamp = models.DateTimeField('Время получении', auto_now_add=True)
    is_read = models.BooleanField('Получил?', default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
