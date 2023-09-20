from django.contrib import admin
from .models import SocialMedia, CallBack, Contacts, PhoneNumber


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    fields = ('whatsapp', 'telegram', 'instagram')

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


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    inlines = (PhoneNumberInline, )
    fields = ('email', 'address', 'maps_link')

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


@admin.register(CallBack)
class Callback(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_on', 'checked',)
    readonly_fields = ('name', 'phone_number', 'created_on')
    search_fields = ('name', 'phone_number')
    list_filter = ('checked',)
