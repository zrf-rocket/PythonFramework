import logging
from django.test import TestCase, tag
from .models import Config
logger = logging.getLogger(__file__)

class TestModels(TestCase):
    """
    模型测试：对 Model 的增删改查进行测试，测试类继承 django.test.TestCase。
    在执行测试用例之前创建test_开头的测试数据库，并在执行测试用例之后销毁。
    """
    def test_config_modles(self):
        conf1 = Config.objects.create(name_zh = "配置1", name_en = "config1", conf_value = "config value1", remark = "配置1内容",conf_type = "0")
        self.assertIsNotNone(conf1)
        self.assertTrue(conf1 is not None)

        Config.objects.create(name_zh = "配置2", name_en = "config2", remark = "配置3内容", conf_type = "2")
        Config.objects.create(name_zh = "配置3", name_en = "config3", conf_value = "config value3", remark = "配置3内容")

        count = Config.objects.count()
        self.assertEqual(count, 3)
        self.assertNotEqual(count, 1)


class TestSetUpTearDown(TestCase):
    def setUp(self) -> None:
        logger.info("start init.....")
        Config.objects.create(name_zh="配置1", name_en="config1", conf_value="config value1", remark="配置1内容", conf_type="0")
        Config.objects.create(name_zh="配置2", name_en="config2", remark="配置3内容", conf_type="2")
        Config.objects.create(name_zh="配置3", name_en="config3", conf_value="config value3", remark="配置3内容")
        logger.info("end init.....")

    def tearDown(self) -> None:
        logger.warning(f"清空配置表数据.....[{Config.objects.count()}]")
        Config.objects.filter().delete()
        logger.warning(f"清空配置表数据.....[{Config.objects.count()}]")

    def test_models(self):
        self.assertIsNotNone(Config.objects.filter(name_en="config1"))
        self.assertEqual(3, Config.objects.count())

    def test_views(self):
        response = self.client.get("http://127.0.0.1:81/drf_pro/index/")
        self.assertEqual(response.status_code, 200)


class TestExample2(TestCase):
    def setUp(self) -> None:
        logger.warning("create config.....")
        Config.objects.create(name_zh="配置1", name_en="config1", conf_value="config value1", remark="配置1内容", conf_type="0")

    def tearDown(self) -> None:
        logger.warning("test over, clear db")
        Config.objects.filter().delete()

    # 添加标记1
    @tag("tag1")
    def test1(self):
        config = Config.objects.filter(name_en="config1")
        self.assertIsNotNone(config)
        self.assertEqual(1, Config.objects.count())

    # 添加标记2
    @tag("tag2")
    def test2(self):
        config2 = Config.objects.create(name_zh="配置2", name_en="config2", conf_value="config value2", remark="配置2内容", conf_type="2")
        self.assertIsNotNone(config2)
        self.assertEqual(2, Config.objects.count())