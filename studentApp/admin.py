from django.contrib import admin
from .models import Student, Department

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'roll_number', 'department')
    search_fields = ('name', 'roll_number')
    list_filter = ('department',)
    ordering = ('name',)

# Register models with admin site
admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
#admin.site.register(Student)
# Register your models here.
