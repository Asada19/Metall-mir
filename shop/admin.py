from django.contrib import admin
from .models import Catalog, Item, ItemField, MainPriceFile, OurProvidersLogo, OurClientsLogo
from django.utils.html import format_html


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


class ItemFieldInline(admin.StackedInline):
    model = ItemField
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemFieldInline, ]
    list_display = ('title', )

@admin.register(OurProvidersLogo)
class OurProvidersLogoAdmin(admin.ModelAdmin):
    model = OurProvidersLogo

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'

    fields = ('image', 'image_tag')
    readonly_fields = ('image_tag', )

@admin.register(OurClientsLogo)
class OurClientsLogoAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'

    fields = ('image', 'image_tag')
    readonly_fields = ('image_tag', )


@admin.register(MainPriceFile)
class PriceListAdmin(admin.ModelAdmin):
    fields = ('file', )

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.count() < 1:
            return super().add_view(request, extra_context)
        else:
            object = (self.model.objects.first()).id
            return super().change_view(request=request,
                                       extra_context=extra_context,
                                       object_id=str(object))

