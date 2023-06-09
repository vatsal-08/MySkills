from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['last_login', 'joining_date']
    list_display = ['email'] + [field.name for field in CustomUser._meta.fields if field.name not in ["password", "email"]]

    def get_exclude(self, request, obj=None):
        exclude = super().get_exclude(request, obj)
        if exclude is None:
            exclude = []
        return exclude + ['password']
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        for fieldset in fieldsets:
            if 'fields' in fieldset[1]:
                fieldset[1]['fields'] = tuple(filter(lambda x: x != 'password', fieldset[1]['fields']))
        return fieldsets

admin.site.register(CustomUser, CustomUserAdmin)
