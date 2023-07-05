from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin




from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'last_login','roll_num','is_sac','is_admin','is_faculty','phn_num','profile_pic','file_type','bio','sac_role','admin_role','faculty_role','branch','batch','year','token','notif_settings','notif_seen','notif_count','notif_ids')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
#    add_fieldsets = (
#        (
#            None,
#            {
#                'classes': ('wide',),
#                'fields': ('email', 'password1', 'password2','username','phn_num','roll_num')
#            }
#        ),
#    )

    list_display = ('email', 'username', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)



# Register your models here.
#admin.site.register(models.User)
admin.site.register(models.PostTable)
admin.site.register(models.post_Likes)
admin.site.register(models.post_Comments)
admin.site.register(models.Lost_Found)
admin.site.register(models.LST_Comments)
admin.site.register(models.Events)
admin.site.register(models.Event_likes)
admin.site.register(models.Alerts)
admin.site.register(models.ALERT_Comments)
admin.site.register(models.Clubs_Sports)
admin.site.register(models.Clubs_Sports_likes)
#admin.site.register(models.Clubs_Sports_files)
admin.site.register(models.Mess_table)
admin.site.register(models.Academic_table)
admin.site.register(models.Time_table)
admin.site.register(models.Notifications)
admin.site.register(models.Messanger)
admin.site.register(models.CalenderEvents)



