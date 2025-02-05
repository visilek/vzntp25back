import uuid
import datetime


def uploading_path_getter(instance, filename):
    """
    Callback for generating 'upload_to' option

    Parameters:
    instance(models.Model): object containg FileField.
    filename(str): initial uploaded file full name

    Returns:
    str: File path inside media root folder
    """
    subfolder = f"{instance._meta.app_label.replace('_','')}_{instance.__class__.__name__.lower()}"
    extention = filename.split('.')[-1]
    name = str(uuid.uuid4()).replace('-','')
    today = datetime.date.today()
    Y = today.year
    m = str(today.month).zfill(2)
    d = str(today.day).zfill(2)
    return f"{subfolder}/{Y}/{m}-{d}/{name}.{extention}"