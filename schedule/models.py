from django.db import models
from user.models import UsersGroup


# TODO: продумать как хранить расписание (В разных таблицах для каждого дня?)
class Schedule(models.Model):
    '''
    Моделька, определяющая расписание для студентов
    Связана с моделью UserGroup по ключу "один к одному"
    '''
    day = models.CharField(default="N/A", max_length=10)
    subject_order = models.IntegerField(default=0)
    subject_name = models.CharField(default='N/A', max_length=50)
    group = models.OneToOneField(UsersGroup, primary_key=True)

    def __str__(self):
        '''Стринг формат объекта класса Schedule'''
        return "Schedule of group: ".format(self.group.group_name)
