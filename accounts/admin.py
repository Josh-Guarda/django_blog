from django.contrib import admin
from django.contrib.admin.models import LogEntry
# Register your models here.


#This Creates the Log entries in DjangoAdminDashboard 
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("action_time", "user", "content_type", "object_repr", "action_flag", "change_message")
    list_filter = ("action_flag", "user", "content_type")
    search_fields = ("object_repr", "change_message")
    ordering = ("-action_time",)
    

