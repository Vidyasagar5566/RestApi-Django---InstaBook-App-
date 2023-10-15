from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin




from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username','domain',

                           'roll_num','phn_num','profile_pic','file_type','bio','course','branch','batch','year','skills','date_of_birth',

                           'is_student_admin','is_admin','is_faculty','is_instabook','student_admin_role','admin_role','faculty_role','instabook_role',

                           'user_mark','star_mark',

                           'notif_settings','notif_seen','notif_count','notif_ids',

                           'token','platform','is_details',
                            )}),
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

    list_display = ('email', 'username', 'is_staff', 'last_login','platform')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(models.AllClubs)
admin.site.register(models.Clubs_likes)
admin.site.register(models.AllSports)
admin.site.register(models.Sports_likes)
admin.site.register(models.AllFests)
admin.site.register(models.Fests_likes)

admin.site.register(models.SAC_MEMS)

admin.site.register(models.Notifications)
admin.site.register(models.Reports)






















