# Generated by Django 3.2.4 on 2021-08-09 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210808_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(default=15, verbose_name="O'quvchini yoshi"),
        ),
        migrations.AddField(
            model_name='student',
            name='brith',
            field=models.CharField(default=datetime.datetime(2021, 8, 9, 17, 42, 8, 764734, tzinfo=utc), max_length=50, verbose_name="Tug'ulgan sanasi"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='brith',
            field=models.CharField(default=datetime.datetime(2021, 8, 9, 17, 42, 22, 572558, tzinfo=utc), max_length=50, verbose_name="Tug'ulgan sanasi"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_img/', verbose_name="O'quvchi rasmi"),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_img/', verbose_name="O'qituvchi rasmi"),
        ),
    ]