from .models import Config

############ 增
#
Config.objects.save()

Config.objects.bulk_create()

Config.objects.abulk_create()


############ 删
#
############ 改
#
Config.objects.bulk_update()
Config.objects.update_or_create()
# 更新
# conf_item.update()
# 批量更新
# conf_item.bulk()
# 批量更新
# conf_item.bulk_update()

############ 查

# 模糊查询
Config.objects.filter(name_en__contains="color")

# 查询多个

# 查询多个 - 按指定字典排序


# 查询单条







