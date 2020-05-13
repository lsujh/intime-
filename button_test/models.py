from django.db import models

class AppleId(models.Model):
    apple_id = models.EmailField('Apple Id')
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия', max_length=25)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.last_name + ' ' + self.first_name
