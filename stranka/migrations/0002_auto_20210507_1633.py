# Generated by Django 3.2.2 on 2021-05-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stranka', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Druh',
            new_name='Kategorie',
        ),
        migrations.AlterField(
            model_name='stroj',
            name='stav',
            field=models.IntegerField(blank=True, choices=[(5, 'nový'), (4, 'málo použitý'), (3, 'použitý'), (2, 'hodně použitý'), (1, 'nefunkční')], default=3, help_text='Vyberte označení stavu', verbose_name='Stav stroje'),
        ),
    ]
