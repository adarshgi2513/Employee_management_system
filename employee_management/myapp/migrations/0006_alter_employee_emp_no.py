# Generated by Django 5.0.6 on 2024-05-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_employee_emp_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_no',
            field=models.IntegerField(max_length=20, unique=True),
        ),
    ]