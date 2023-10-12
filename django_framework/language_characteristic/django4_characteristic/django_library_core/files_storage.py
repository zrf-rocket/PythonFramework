from django.db import models



from django.core.files.storage import (
    default_storage,
    FileSystemStorage
)
from django.core.files.base import ContentFile

# Django默认使用的文件存储系统 django.core.files.storage.FileSystemStorage 是一个本地存储系统，由settings中的DEFAULT_FILE_STORAGE值确定。
# class FileSystemStorage(location=None, base_url=None, file_permissions_mode=None, directory_permissions_mode=None)
# FileSystemStorage类实现了本地文件系统的基本文件存储。它继承自 Storage 类，并提供了其中所有公开方法的实现。
# location  存放文件的目录的绝对路径。默认值是settings中的MEDIA_ROOT值
# base_url 为存储在此位置的文件提供服务的URL。默认值是settings中的MEDIA_URL值。
# file_permissions_mode 保存文件时，文件系统将获得的权限。默认为 FILE_UPLOAD_PERMISSIONS。
# directory_permissions_mode  保存目录时，该目录将获得的文件系统权限，默认为 FILE_UPLOAD_DIRECTORY_PERMISSIONS。
# 注意：如果给定的文件名不存在，FileSystemStorage.delete() 方法不会引发异常。
# get_created_time(name) 返回系统 ctime 的 datetime，即 os.path.getctime()。在某些系统上（如 Unix），这是最后一次修改元数据的时间，而在其他系统上（如 Windows），这是文件的创建时间。

# 当定义location参数时，可以无视MEDIA_ROOT值来存储文件
# fs = FileSystemStorage(location='/media/imgs')

# class ProductImgs(models.Model):
#     product_image = models.ImageField(storage=fs)  # 文件会存储在/media/imgs文件夹

# FileSystemStorage类的_save方法存储文件
# 先判断文件存储的目录是否存在，如果不存在，使用os.mkdirs()依次创建目录
# 根据directory_permissions_mode参数来确定创建的目录的权限。
# 然后使用os.open()创建文件，flags参数为(os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_BINARY', 0))，
# 这样当文件已存在时，则报EEXIST异常，使用get_available_name()方法重新确定文件的名字。
# mode为0o666，权限为(0666 &~umask)。
# content为FILE对象，如一切正常，使用FILE.chunks()依次将内容写入文件。
# 最后，根据file_permissions_mode参数，修改创建文件的权限。




# 可以直接使用Django的文件存储系统来存储文件
img_path = default_storage.save('/media/imgs_pro', ContentFile("new images"))
default_storage.size(img_path)
default_storage.open(img_path).read()
default_storage.delete(img_path)
default_storage.exists(img_path)
