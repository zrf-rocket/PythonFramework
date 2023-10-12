import tarfile
from django.core.files.uploadedfile import SimpleUploadedFile

# Django文件上传
# https://docs.djangoproject.com/zh-hans/4.1/topics/http/file-uploads/

with open("","rb") as tar_obj:
    SimpleUploadedFile("plugin.tar.gz", tar_obj.read())