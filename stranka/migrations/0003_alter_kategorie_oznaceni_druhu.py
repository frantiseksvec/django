# Generated by Django 3.2.2 on 2021-05-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stranka', '0002_auto_20210507_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorie',
            name='oznaceni_druhu',
            field=models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení stroje'),
        ),
    ]
