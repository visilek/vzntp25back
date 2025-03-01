import uuid
import datetime


def uploading_path_getter(instance, filename, app_name=None, model_name=None):
    """
    Callback for generating 'upload_to' option

    Parameters:
    instance(models.Model): object containg FileField, used to get app & model names for subfolders structure
    filename(str): initial uploaded file full name
    app_name(str): django app name for creating subfolders; if instance is given, will be set automatically
    model_name: instance model name for creating subfolders; if instance is given, will be set automatically

    Returns:
    str: File path inside media root folder
    """
    app_name = app_name or instance._meta.app_label.replace("_", "")
    model_name = model_name or instance.__class__.__name__.lower()
    model_subfolder = f"{app_name}_{model_name}"

    today = datetime.date.today()
    Y = today.year
    m = str(today.month).zfill(2)
    d = str(today.day).zfill(2)
    date_subfolder = f"{Y}/{m}-{d}"

    name = str(uuid.uuid4()).replace("-", "")
    extention = filename.split(".")[-1]

    return f"{model_subfolder}/{date_subfolder}/{name}.{extention}"
