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

                           'clz_clubs_head','clz_sports_head','clz_fests_head','clz_sacs_head','clz_users_head',

                           'clz_clubs','clz_sports','clz_fests','clz_sacs',

                           'notif_settings','notif_seen','notif_count','notif_ids',

                           'token','platform','is_details','update_mark',
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



# Register your models here.
admin.site.register(models.PostTable)
admin.site.register(models.post_Likes)
admin.site.register(models.post_Comments)
admin.site.register(models.Lost_Found)
admin.site.register(models.LST_Comments)
admin.site.register(models.Events)
admin.site.register(models.Event_likes)
admin.site.register(models.Alerts)
admin.site.register(models.ALERT_Comments)
admin.site.register(models.Messanger)
admin.site.register(models.CalenderEvents)



admin.site.register(models.UniBranches)
admin.site.register(models.BranchSub)
admin.site.register(models.BranchSubYears)
admin.site.register(models.BranchSubFiles)
admin.site.register(models.Ratings)


admin.site.register(models.Mess_table)
admin.site.register(models.Academic_table)
admin.site.register(models.Time_table)















