# Generated by Django 4.1.5 on 2023-03-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misjuegos', '0003_remove_juego_fecha_juego_descripcion_juego_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]