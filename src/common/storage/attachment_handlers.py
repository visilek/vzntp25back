import os


def post_delete_attachment_delete_handler(sender, instance, **kwargs):
    """
    Signal reciever for deleting attached file
    after deleting the model instance itself

    Note:
    Model class must provide "attachment_field_name" attribute
    """

    try:
        fieldname = sender.attachment_field_name
    except Exception as e:
        print(e)
        return

    if attachment := getattr(instance, fieldname):
        if os.path.isfile(attachment.path):
            # Delete the file
            os.remove(attachment.path)
            # Delete file's folder if it's empty now
            dirpath = os.path.dirname(attachment.path)
            dir_empty = len(os.listdir(dirpath)) == 0
            if dir_empty:
                os.rmdir(dirpath)


def pre_save_attachment_update_handler(sender, instance, **kwargs):
    """
    Signal reciever for deleting previous attached file
    when a new file has been attached to a model instance

    Note:
    Model class must provide "attachment_field_name" attribute
    """

    try:
        fieldname = sender.attachment_field_name
    except Exception as e:
        print(e)
        return
    
    if not instance.pk:
        return

    try:
        old_attachment = getattr(sender.objects.get(pk=instance.pk), fieldname)
        old_attachment_path = old_attachment.path
    except Exception as e:
        print(e)
        return

    new_attachment = instance.file

    if not old_attachment == new_attachment:
        print(f"{instance} instance's file updated")
        if os.path.isfile(old_attachment_path):
            # Delete the old file
            os.remove(old_attachment_path)
            # Delete the old file's folder if it's empty now
            dirpath = os.path.dirname(old_attachment_path)
            dir_empty = len(os.listdir(dirpath)) == 0
            if dir_empty:
                os.rmdir(dirpath)
