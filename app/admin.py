from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['image_preview']  # делает поле только для чтения
    fields = ['image', 'image_preview', 'order']  # явно указываем порядок полей
    ordering = ['order']


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [PlaceImageInline]
    list_display = ('title', 'lat', 'lng')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }