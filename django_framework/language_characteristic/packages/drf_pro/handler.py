


def custom_migrate(sender, **kwargs):
    """
    参数：sender
    参数：**kwargs
    """
    print("post_migrate custom_migrate running.......")


def custom_migrate2(sender, **kwargs):
    print("running2......", kwargs)