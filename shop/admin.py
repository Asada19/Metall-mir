from django.contrib import admin
from .models import Catalog, Item, ItemField, Parameters, Field
from django.utils.html import format_html
from django import forms


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{url}" width="auto" height="200px"/>'.format(url=obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ('id', 'title', 'description', 'image_tag')
    list_display_links = ('id', 'title')
    readonly_fields = ('image_tag', )


class ItemFieldAdminForm(forms.ModelForm):
    # class Meta:
    #     model = ItemField
    #     fields = ['value']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # import pdb;pdb.set_trace()
        # if self.instance and self.instance.itcem:
        #     self.fields['title'].queryset = self.instance.item.catalog.parameters.fields.all()


class ItemFieldInline(admin.TabularInline):
    form = ItemFieldAdminForm
    model = ItemField
    extra = 0

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.model.title.get_queryset().filter(title = 'rest 1')

    # def get_queryset(self, request):
    #     return ItemField.objects.all()
        # import pdb; pdb.set_trace()

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemFieldInline, ]
    list_display = ('title', )

    def get_queryset(self, request):
        import pdb; pdb.set_trace()


class FieldInline(admin.StackedInline):
    model = Field
    extra = 1


@admin.register(Parameters)
class ParametersAdmin(admin.ModelAdmin):
    inlines = [FieldInline]
