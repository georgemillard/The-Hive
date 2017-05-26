from django.conf import settings

# from . import models
# from itertools import chain

def get_file_directory_path(instance, filename):
    """
    Returns an updated directory path for FileField uploads
    Because boto3 knows the base root, this must be removed
    Needs to have filename as a separate argument as this is expected when
    used as a callback by the uploads_to function on a FileField
    """
    path = instance.parent.get_path() + '/' + filename
    if path.startswith(settings.MEDIAFILES_LOCATION):
        path = path.partition('/')[2]
    return path.lower()

# --------------------- Functions used by User Interface --------------------- #

# def get_folder(folder_path):
#     """
#     Returns a Folder model object from a given folder path
#     Note the folder path, taken from the URL, will not have a trailing slash
#     but the S3 Folder Key must, to denote it as a folder
#     """
#     return models.Folder.objects.get(s3_key=(folder_path+'/')) if folder_path else None
#
# def get_file(file_path):
#     """
#     Returns a File model object from a given file path
#     """
#     return models.File.objects.get(s3_key=file_path) if file_path else None
#
# def get_child_folders(current_folder):
#     """
#     Returns a QuerySet of all child folders,
#     or all level one folders if the current_folder is None (ie root)
#     """
#     if(current_folder):
#         folders = current_folder.folder_set.all()
#     else:
#         folders = models.Folder.objects.filter(parent__isnull=True)
#
#     return folders
