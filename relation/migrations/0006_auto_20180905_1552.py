# Generated by Django 2.1.1 on 2018-09-05 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0005_auto_20180905_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studetail',
            name='stu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='relation.Student'),
        ),
    ]