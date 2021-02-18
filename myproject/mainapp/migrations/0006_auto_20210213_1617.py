# Generated by Django 3.1.6 on 2021-02-13 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210213_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='car',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='car',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='image',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='title',
        ),
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='car',
            name='images',
            field=models.ImageField(default='SOME STRING', upload_to='', verbose_name='Головне зображення'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='images',
            field=models.ImageField(default='SOME STRING', upload_to='', verbose_name='Головне зображення'),
        ),
        migrations.AddField(
            model_name='services',
            name='images',
            field=models.ImageField(default='SOME STRING', upload_to='', verbose_name='Головне зображення'),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Повна назва автомобіля'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='car',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='mainapp.car'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Назва послуг'),
        ),
    ]