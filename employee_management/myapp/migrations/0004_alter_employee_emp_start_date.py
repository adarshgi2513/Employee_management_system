# Generated by Django 5.0.6 on 2024-05-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_start_date',
            field=models.DateField(default='M/D/Y'),
        ),
    ]
