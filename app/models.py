# models.py
from django.db import models
from django.utils.html import format_html

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['id']


def place_image_upload_to(instance, filename):
    return f'places/{instance.place.id}/{filename}'


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField('Изображение', upload_to=place_image_upload_to)
    order = models.PositiveIntegerField('Порядок', default=0, db_index=True)

    def image_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px; border-radius: 4px;" />',
                self.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Превью'

    class Meta:
        ordering = ['order']
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения места'

    def __str__(self):
        return f'Изображение для {self.place.title}'