from django.contrib import admin
from .models import Alumnus


class AlumnusAdmin(admin.ModelAdmin):
    fields = ['id', 'first_name', 'last_name', 'perm_email', 'mailing_list',
              'grad_semester', 'grad_school', 'job_title', 'company',
              'salary', 'created_at', 'updated_at', 'location',
              'suggestions']
    list_display = ('first_name', 'last_name', 'perm_email')
    list_filter = ['grad_semester', 'mailing_list', 'created_at',
                   'updated_at']
    search_fields = ['first_name', 'last_name', 'perm_email']


admin.site.register(Alumnus, AlumnusAdmin)

