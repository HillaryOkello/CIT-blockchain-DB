# Generated by Django 3.1.1 on 2021-11-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0002_auto_20211129_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='aws_ml_exam',
            field=models.CharField(choices=[('pass', 'PASS'), ('fail', 'FAIL')], default='pass', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='aws_practitioner_exam',
            field=models.CharField(choices=[('pass', 'PASS'), ('fail', 'FAIL')], default='pass', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='blockchain_exam',
            field=models.CharField(choices=[('pass', 'PASS'), ('fail', 'FAIL')], default='pass', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='python_associate_exam',
            field=models.CharField(choices=[('pass', 'PASS'), ('fail', 'FAIL')], default='pass', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='python_entry_level',
            field=models.CharField(choices=[('pass', 'PASS'), ('fail', 'FAIL')], default='pass', max_length=10),
        ),
    ]
