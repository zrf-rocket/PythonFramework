from django.db.models import signals

signals.pre_delete.send()
signals.pre_save.send()
signals.pre_migrate.send()
signals.pre_init.send()

signals.post_delete.send()
signals.post_save.send()
signals.post_migrate.send()
signals.post_init.send()

signals.class_prepared.send()
signals.m2m_changed.send()




















