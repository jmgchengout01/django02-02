# Generated by Django 5.0.6 on 2024-06-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_populate_categories'),
        ('employees', '0001_initial'),
        ('privileges', '0002_populate_privileges'),
        ('tags', '0002_populate_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='categories',
            field=models.ManyToManyField(to='categories.category'),
        ),
        migrations.AddField(
            model_name='employee',
            name='privileges',
            field=models.ManyToManyField(to='privileges.privilege'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tags',
            field=models.ManyToManyField(to='tags.tag'),
        ),
    ]