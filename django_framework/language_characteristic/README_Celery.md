
## django celery

celery -A language_characteristic.mycelery beat -l info --settings=FasterRunner.settings.dev


celery -A language_characteristic.celery beat -l info --settings=language_characteristic.settings
celery -A language_characteristic worker -l info -P eventlet --settings=language_characteristic.settings
celery -A language_characteristic.celery worker -l info -P eventlet --settings=language_characteristic.settings

celery  worker -l info -P eventlet --settings=language_characteristic.settings
Celery -A language_characteristic worker -l info -P eventlet
下面的能正常启动
celery  beat -l info -P eventlet
celery  worker -l info -P eventlet
正常启动django的celery
celery -A language_characteristic worker -l INFO


celery -A language_characteristic beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler  #启动beat 调度器使用数据库

celery worker -A language_characteristic -l info #启动woker

