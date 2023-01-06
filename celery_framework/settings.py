import global_settings_base

# REDIS_URL = f'redis://{global_settings_base.REDIS_PASSWORD}:{global_settings_base.REDIS_PORT}@{global_settings_base.REDIS_HOST}/{global_settings_base.REDIS_DB}'
REDIS_URL = f'redis://:{global_settings_base.REDIS_PORT}@{global_settings_base.REDIS_HOST}/{global_settings_base.REDIS_DB}'
