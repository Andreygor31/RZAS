from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models
from datetime import datetime


class Class(models.Model):
    """Предметы"""

    class Meta:
        db_table = "class"
        verbose_name = "Предметы"

    name = models.TextField(verbose_name="Название предмета")

class Teacher(models.Model):
    """Учитель"""

    class Meta:
        db_table = "teacher"
        verbose_name = "Учитель"

    position = models.TextField(verbose_name="Должность")
    email = models.TextField(verbose_name="Почта")
    DOB = models.TextField(verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    experience = models.TextField(verbose_name="Стаж")
    full_name = models.TextField(verbose_name="ФИО")
    education = models.TextField(verbose_name="Образование")
    category = models.TextField(verbose_name="Категория")

class Student(models.Model):
    """Ученик"""

    class Meta:
        db_table = "student"
        verbose_name = "Ученик"

    full_name = models.TextField(verbose_name="ФИО")
    DOB = models.TextField(verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    phone_number = models.TextField(verbose_name="Телефон")
    parents_phone_number = models.TextField(verbose_name="Телефон родителя")
    email = models.TextField(verbose_name="Почта")
    parents_DOB = models.TextField(verbose_name="ФИО родителя")

class Cabinet(models.Model):
    """Кабинет"""

    class Meta:
        db_table = "cabinet"
        verbose_name = "Кабинет"

    number = models.TextField(verbose_name="Номер класса")
    letter = models.TextField(verbose_name="Литера класса")


class Contract(models.Model):
    """Договоры"""

    class Meta:
        db_table = "contarc"
        verbose_name = "Договоры"

    number = models.TextField(verbose_name="Номер договора")
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT, verbose_name="Код учителя")
    date = models.DateField(verbose_name="Дата договора")
    time = models.TextField(verbose_name="Срок")
    salary = models.TextField(verbose_name="Оклад")

class StudentsCabinet(models.Model):
    """Кабинеты учеников"""

    class Meta:
        db_table = "students_cabinet"
        verbose_name = "Кабинеты учеников"

    cabinet = models.ForeignKey(Cabinet, on_delete=models.RESTRICT, verbose_name="Код класса")
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, verbose_name="Код ученика")
    classroom_teacher = models.TextField(verbose_name="Классный руководитель")

class StudentAdmission(models.Model):
    """Поступление ученика"""

    class Meta:
        db_table = "studentadmission"
        verbose_name = "Поступление ученика"

    student = models.ForeignKey(Student, on_delete=models.RESTRICT, verbose_name="Код ученика")
    date = models.DateField(verbose_name="Дата")

class Schedule(models.Model):
    """Расписание"""

    class Meta:
        db_table = "schedule"
        verbose_name = "Расписание"

    classes = models.ForeignKey(Class, on_delete=models.RESTRICT, verbose_name="Код предмета")
    number = models.TextField(verbose_name="Номер занятия")
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT, verbose_name="Код учителя")
    cabinet = models.ForeignKey(Cabinet, on_delete=models.RESTRICT, verbose_name="Код класса")

class Journal(models.Model):
    """Журнал"""

    class Meta:
        db_table = "journal"
        verbose_name = "Журнал"

    classes = models.ForeignKey(Class, on_delete=models.RESTRICT, verbose_name="Код предмета")
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, verbose_name="Код ученика")
    date = models.DateField(verbose_name="Дата")
    schedule = models.ForeignKey(Schedule, on_delete=models.RESTRICT, verbose_name="Номер занятия")
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT, verbose_name="Код учителя")
    cabinet = models.ForeignKey(Cabinet, on_delete=models.RESTRICT, verbose_name="Код класса")  
    presence = models.TextField(verbose_name="Присутствие")
    assessment = models.TextField(verbose_name="Оценка")