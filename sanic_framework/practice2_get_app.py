# 应用注册表
import app.sanic_app
from sanic import Sanic

# 当实例化Sanic实例时，可以从Sanic应用程序注册表检索该实例。例如，如果您需要从以其他方式无法访问的位置访问Sanic实例。
# Sanic.get_app("sanic_framework22")  # sanic.exceptions.SanicException: Sanic app name "sanic_framework22" not found.

Sanic.get_app("sanic_framework2", force_create=True)
# 如果调用Sanic.get_app("non-existing")在不存在的应用程序上，它将引发 SanicException 异常。相反，可以强制该方法返回 Sanic ，使用参数force_create即可


app = Sanic.get_app("sanic_framework")
# http://localhost/app1


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

