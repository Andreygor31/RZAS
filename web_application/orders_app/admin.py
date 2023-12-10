from django.contrib import admin
from .models import Class, Teacher, Student, Cabinet, Contract, StudentsCabinet, StudentAdmission, Schedule, Journal


class ClassAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'name')
    # поля для поиска
    search_fields = ('name',) 

class TeacherAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'position', 'email', 'DOB', 'address', 'experience', 'full_name', 'education', 'category')
    # поля для поиска
    search_fields = ('position', 'email', 'DOB', 'address', 'experience', 'full_name', 'education', 'category') 

class StudentAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'full_name', 'DOB', 'address', 'phone_number', 'parents_phone_number', 'email', 'parents_DOB')
    # поля для поиска
    search_fields = ('full_name', 'DOB', 'address', 'phone_number', 'parents_phone_number', 'email', 'parents_DOB') 

class CabinetAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'number', 'letter')
    # поля для поиска
    search_fields = ('number', 'letter') 

class ContractAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('number', 'id', 'date', 'time', 'salary')
    # поля для поиска
    search_fields = ('number', 'date', 'time', 'salary') 

class StudentsCabinetAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('cabinet', 'student', 'classroom_teacher')
    # поля для поиска
    search_fields = ('classroom_teacher',) 

class StudentAdmissionAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('id', 'student', 'date')
    # поля для поиска
    search_fields = ('date',) 

class ScheduleAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('classes', 'number', 'teacher', 'cabinet')
    # поля для поиска
    search_fields = ('number',) 

class JournalAdmin(admin.ModelAdmin):
    # поля для отображения
    list_display = ('classes', 'student', 'date', 'schedule', 'teacher', 'cabinet', 'presence', 'assessment')
    # поля для поиска
    search_fields = ('date', 'presence', 'assessment') 

admin.site.register(Class, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Cabinet, CabinetAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(StudentsCabinet, StudentsCabinetAdmin)
admin.site.register(StudentAdmission, StudentAdmissionAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Journal, JournalAdmin)