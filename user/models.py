from django.db import models
from django.contrib.auth.models import User


class UsersGroup(models.Model):
    '''
    Моделька, определяющая группы студентов
    Связана с моделью User по ключу "один ко многим"
    '''
    user = models.ForeignKey(User)
    group_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        '''Стринг формат объекта класса UsersGroup'''
        return "Group name: {}".format(self.group_name)
