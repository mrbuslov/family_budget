from django.contrib import admin
from account.models import Account, Family
from django.contrib.auth.admin import UserAdmin





class AccountAdmin(UserAdmin): 
    list_display = ('email','member')
    search_fields = ('email','member')
    ordering=('email',)
    list_filter=('member',)
    fieldsets = (
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name', 'member')}),
        ('Others', {'fields': ('date_joined','last_login', 'is_admin','is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    
    readonly_fields = ('date_joined','last_login')

    class Meta:
        model = Account




admin.site.register(Account, AccountAdmin)
admin.site.register(Family)