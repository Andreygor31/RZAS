# Generated by Django 4.2.6 on 2023-12-10 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(verbose_name='Номер класса')),
                ('letter', models.TextField(verbose_name='Литера класса')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предметы',
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='ФИО')),
                ('DOB', models.TextField(verbose_name='Дата рождения')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('phone_number', models.TextField(verbose_name='Телефон')),
                ('parents_phone_number', models.TextField(verbose_name='Телефон родителя')),
                ('email', models.TextField(verbose_name='Почта')),
                ('parents_DOB', models.TextField(verbose_name='ФИО родителя')),
            ],
            options={
                'verbose_name': 'Ученик',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField(verbose_name='Должность')),
                ('email', models.TextField(verbose_name='Почта')),
                ('DOB', models.TextField(verbose_name='Дата рождения')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('experience', models.TextField(verbose_name='Стаж')),
                ('full_name', models.TextField(verbose_name='ФИО')),
                ('education', models.TextField(verbose_name='Образование')),
                ('category', models.TextField(verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Учитель',
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='StudentsCabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_teacher', models.TextField(verbose_name='Классный руководитель')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.cabinet', verbose_name='Код класса')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.student', verbose_name='Код ученика')),
            ],
            options={
                'verbose_name': 'Кабинеты учеников',
                'db_table': 'students_cabinet',
            },
        ),
        migrations.CreateModel(
            name='StudentAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.student', verbose_name='Код ученика')),
            ],
            options={
                'verbose_name': 'Поступление ученика',
                'db_table': 'studentadmission',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(verbose_name='Номер занятия')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.cabinet', verbose_name='Код класса')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.class', verbose_name='Код предмета')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.teacher', verbose_name='Код учителя')),
            ],
            options={
                'verbose_name': 'Расписание',
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('presence', models.TextField(verbose_name='Присутствие')),
                ('assessment', models.TextField(verbose_name='Оценка')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.cabinet', verbose_name='Код класса')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.class', verbose_name='Код предмета')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.schedule', verbose_name='Номер занятия')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.student', verbose_name='Код ученика')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.teacher', verbose_name='Код учителя')),
            ],
            options={
                'verbose_name': 'Журнал',
                'db_table': 'journal',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(verbose_name='Номер договора')),
                ('date', models.DateField(verbose_name='Дата договора')),
                ('time', models.TextField(verbose_name='Срок')),
                ('salary', models.TextField(verbose_name='Оклад')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders_app.teacher', verbose_name='Код учителя')),
            ],
            options={
                'verbose_name': 'Договоры',
                'db_table': 'contarc',
            },
        ),
    ]
