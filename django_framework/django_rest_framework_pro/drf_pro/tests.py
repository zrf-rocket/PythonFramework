import json
from django.test import TestCase

# Create your tests here.

class TestSerializers(TestCase):
    def setUp(self) -> None:
        print("单元测试开始")

    def tearDown(self) -> None:
        print("单元测试结束")

    def testjson(self):
        infos = {"name": "SteveRocket", "language": "Python", "version": 3.11}
        dump_infos = json.dumps(infos)
        print(dump_infos, type(dump_infos))
