# Generated by Django 4.1.5 on 2023-01-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_employee_emp_ad_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_ad_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
