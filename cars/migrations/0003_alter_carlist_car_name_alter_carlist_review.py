# Generated by Django 4.0.2 on 2022-02-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_text_comment_comment_carlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='car_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='carlist',
            name='review',
            field=models.TextField(max_length=400),
        ),
    ]
