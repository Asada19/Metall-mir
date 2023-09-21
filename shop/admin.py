from django.contrib import admin
from .models import Catalog, Item, ItemField, Parameters, Field
from django.utils.html import format_html
# from django import forms


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


# class ItemFieldAdminForm(forms.ModelForm):
#     class Meta:
#         model = ItemField
#         fields = ['value']  # Указываем, какие поля включить в форму
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Ограничиваем выбор полей только теми, которые относятся к каталогу товаров данного Item
#         if self.instance and self.instance.item:
#             self.fields['title'].queryset = self.instance.item.catalog.parameters.fields.all()
#

class FieldInline(admin.StackedInline):
    # form = ItemFieldAdminForm
    model = Field
    extra = 1


@admin.register(Parameters)
class ParametersAdmin(admin.ModelAdmin):
    inlines = [FieldInline]

