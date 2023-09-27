from django.contrib import admin
from .models import Catalog, Item, ItemField, OurProvidersLogo, OurClientsLogo
from django.utils.html import format_html
from django import forms


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))
        return 'Нет изображения'

    image_tag.short_description = 'Image'
    list_display = ('id', 'title', 'description', 'image_tag')
    list_display_links = ('id', 'title')
    readonly_fields = ('image_tag', )


class ItemFieldInline(admin.TabularInline):
    model = ItemField
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemFieldInline, ]
    list_display = ('title', )


class OurProvidersLogoAdmin(admin.ModelAdmin):
    model = OurProvidersLogo

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'

    fields = ('image', 'image_tag')
    readonly_fields = ('image_tag', )


class OurClientsLogoAdmin(admin.ModelAdmin):
    model = OurClientsLogo

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'

    fields = ('image', 'image_tag')
    readonly_fields = ('image_tag', )


admin.site.register(OurProvidersLogo, OurProvidersLogoAdmin)
admin.site.register(OurClientsLogo, OurClientsLogoAdmin)