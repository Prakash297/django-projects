from django.contrib import admin
from HospitalApp.models import Profile,Doctor,Appointment

class ProfileAdmin(admin.ModelAdmin):
    list_display=['bio']
admin.site.register(Profile,ProfileAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=['name','qualification','specialist','experience','rating']
admin.site.register(Doctor,DoctorAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['username','ref_no','patient_name','age','gender','mobile','city','problem','status']
admin.site.register(Appointment,AppointmentAdmin)





# Register your models here.
