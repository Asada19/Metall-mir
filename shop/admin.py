from django.contrib import admin
from .models import Catalog, Item, ItemField
from django.utils.html import format_html


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ('id', 'title', 'description', 'image_tag')
    list_display_links = ('id', 'title')
    readonly_fields = ('image_tag', )


class ItemFieldInline(admin.StackedInline):
    model = ItemField
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemFieldInline, ]
    list_display = ('title', )

