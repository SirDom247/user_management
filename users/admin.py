from django.contrib import admin
from .models import CustomUser

class CustomerUserAdmin(admin.ModelAdmin):
  list_display = (
        'username',
        'email',
        'date_of_birth',
        'phone_number',
        'state_of_origin',
        'sex',
        'hobbies',
        'about_me',
        'address',
        'occupation',
        'department_unit',
        'is_active',
    )


admin.site.register(CustomUser, CustomerUserAdmin)

