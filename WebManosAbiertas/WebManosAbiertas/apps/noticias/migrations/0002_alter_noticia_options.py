# Generated by Django 4.1.4 on 2022-12-07 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ('-publicado',)},
        ),
    ]
