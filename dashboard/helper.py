

#Django doesnt create a Logs/LogEntry for Recent Activities unless, all changes are done directly from DjangoAdminPage. using the guide Below we Can implement the same functionality and use it in our own CRUD operation in view.py

#Check sample in dashboard/views.py 
# - imports 
# - Log Entries for Create,Update and Delete


from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType


def log_admin_action(user, obj, action_flag, message=""):
    LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=ContentType.objects.get_for_model(obj).pk,
        object_id=obj.pk,
        object_repr=str(obj),
        action_flag=action_flag,
        change_message=message,
    )
    
