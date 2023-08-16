from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ['is_superuser', 'is_admin', 'is_staff', 'is_active']
    list_display = ['email'] + [field.name for field in CustomUser._meta.fields if field.name not in ["password", "email", "auth_token"]]

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets = [
            ('Personal Information', {'fields': ('email','first_name', 'last_name')}),
            ('Status', {'fields': ('is_active', 'is_superuser', 'is_staff', 'is_admin','is_verified')}),
            ('Tokens', {'fields': ('auth_token',)}),
        ]
        return fieldsets
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj != request.user:
            return [field.name for field in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)
    
admin.site.register(CustomUser, CustomUserAdmin)
