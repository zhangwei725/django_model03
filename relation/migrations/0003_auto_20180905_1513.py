# Generated by Django 2.1.1 on 2018-09-05 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_auto_20180905_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studetail',
            name='stu_id',
        ),
        migrations.AddField(
            model_name='studetail',
            name='stu',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='relation.Student'),
        ),
    ]