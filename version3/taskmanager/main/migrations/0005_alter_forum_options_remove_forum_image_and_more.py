# Generated by Django 4.0.5 on 2022-06-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_forum_options_forum_image_forum_title_fio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ['created'], 'verbose_name_plural': 'Отзывы посетителей'},
        ),
        migrations.RemoveField(
            model_name='forum',
            name='image',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='title_fio',
        ),
        migrations.AlterField(
            model_name='forum',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]