# Generated by Django 2.0.2 on 2018-02-05 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
