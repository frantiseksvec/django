from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Kategorie(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení stroje",
            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    KATEGORIE = (
        ('traktory', 'Traktory'),
        ('sklízecí mlátičky', 'Sklízecí mlátičky'),
        ('sklízecí řezačky', 'Sklízecí řezačky'),
        ('postřikovače', 'Postřikovače'),
        ('setí a hnojení', 'Setí a hnojení'),
        ('zpracování půdy', 'Zpracování půdy'),
        ('manipulační technika', 'Manipulační technika'),
        ('krmné vozy', 'Krmné vozy'),
        ('sklizen pice', 'Sklizen pice'),
    )
    kategorie = models.CharField(max_length=20, choices=KATEGORIE, blank=True, default='elektro', verbose_name="kategorie", help_text='Vyberte kategorie')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Typ stroje'
        verbose_name_plural = 'Typ stroje'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.kategorie}"


class Stroj(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název stroje", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis stroje")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    STAV = (
        (5, 'nový'),
        (4, 'málo použitý'),
        (3, 'použitý'),
        (2, 'hodně použitý'),
        (1, 'nefunkční'),
    )
    stav = models.IntegerField(choices=STAV, blank=True, default=3, verbose_name="Stav stroje", help_text='Vyberte označení stavu')
    foto = models.ImageField(upload_to='stroj/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka stroje")
    druh = models.ForeignKey(Kategorie, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Stroj'
        verbose_name_plural = 'Stroj'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


