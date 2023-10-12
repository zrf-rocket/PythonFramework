from django.conf import settings
from django.test import TestCase


class TestViews(TestCase):
    """
    视图层测试：引入测试客户端，它提供了 get、post等方法实现了对视图的访问，测试客户端被封装在了django.test.Client下。
    测试类的每一个测试方法都可以直接使用测试客户端 self.client。
    每一个测试方法都会新建一个测试客户端，并且彼此之间互不影响。
    """

    def test_index_view(self):
        # GET请求 对相应视图函数的访问
        response = self.client.get("http://127.0.0.1:81/drf_pro/index/")
        # POST请求
        # self.client.post()
        response["steverocket-token"] = settings.SECRET_KEY

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["steverocket-token"], 'django-insecure-!hh4oj&-(8xp$d-17!bzmx+ilgkccym32ovkx7hr4f#9cs5y-6')
