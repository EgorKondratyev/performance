# Generated by Django 4.2.1 on 2023-05-29 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Cумма')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_out', to='main.students', verbose_name='Студент')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_out', to='main.subjects', verbose_name='Предмет')),
            ],
        ),
    ]
