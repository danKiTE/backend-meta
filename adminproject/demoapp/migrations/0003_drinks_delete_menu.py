# Generated by Django 4.1.5 on 2023-01-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_rename_cuisine_menu_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinks', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
