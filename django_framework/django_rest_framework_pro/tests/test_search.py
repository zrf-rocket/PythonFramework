import pytest
from utils import read_trace_list

from common.utils import is_url
from core.models import Catalog, Document
from core.parser import try_get_main_summary
from core.storage.markdown import MarkDown
from home.serializers.document_info import check_doc_path_exists_in_summary


@pytest.fixture()
def fake_document():
    contents = read_trace_list("summary")
    catalogs = [Catalog(**contents)]
    Catalog.objects.bulk_create(catalogs, batch_size=1000)

    content_info = set()
    for catalog in Catalog.objects.all():
        for path in catalog.get_all_doc_path():
            if is_url(path):
                continue
            md_ins = MarkDown(path, relative=True)
            data = Document(**md_ins.to_doc_model_data(catalog.id))
            content_info.add(data)
    Document.objects.bulk_create(content_info)


@pytest.mark.django_db
class TestSearch:
    @pytest.mark.parametrize(
        "source_str, target_str, prefer_version",
        [
            # target_str为None时，表示传入的路径是异常情况，无法命中对应文档
            # prefer_version为None时，表示偏好版本不存在的情况
            # 1、根据路径的正则规则是否能找到该路径对应的文档实例
            # 1.1 以下路径中正常版本写法(7.1)、无版本号写法、以及几种特殊版本号的写法可以命中对应文档
            ("ZH/DeploymentGuides/7.1/manual-install-bkce.md", "ZH/DeploymentGuides/7.1/manual-install-bkce.md", None),
            ("ZH/DeploymentGuides/7.1/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
            (
                "ZH/DeploymentGuides/manual-install-bkce.md",
                "ZH/DeploymentGuides/7.1/manual-install-bkce.md",
                None,
            ),  # 返回最新文档
            ("ZH/DeploymentGuides/7.70/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),  # 返回最新文档
            ("ZH/DeploymentGuides/7.7777/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),  # 返回最新文档
            (
                "ZH/DeploymentGuides/777.7777/install-bkce.md",
                "ZH/DeploymentGuides/7.1/install-bkce.md",
                None,
            ),  # 返回最新文档
            # 1.2 以下路径中几种特殊版本号的写法不可以命中对应文档
            ("ZH/DeploymentGuides/7/install-bkce.md", None, None),
            ("ZH/DeploymentGuides/7.1.2/install-bkce.md", None, None),
            ("ZH/DeploymentGuides/7.1-beta.2/install-bkce.md", None, None),
            ("ZH/DeploymentGuides/7..7777.../install-bkce.md", None, None),
            ("ZH/DeploymentGuides/7/.../.7777/install-bkce.md", None, None),
            # 1.3 以下语言的写法可以找到该路径对应文档实例(zh-cn 或 对应英文的是en)
            (
                "zh-cn/DeploymentGuides/7.1/manual-install-bkce.md",
                "ZH/DeploymentGuides/7.1/manual-install-bkce.md",
                None,
            ),
            # 1.4 以下语言的写法、或是不写语言则找不到该路径对应文档实例
            ("zh/DeploymentGuides/7.1/manual-install-bkce.md", None, None),
            ("DeploymentGuides/7.1/manual-install-bkce.md", None, None),
            # 1.5 文档包不存在的路径，找不到文档实例
            ("ZH/DeploymentGuides/7.1/manual-install-bkce_not_exist.md", None, None),
            # 2、如果存在目标路径自己，则取他自己，不管是否存在偏好版本
            ("ZH/DeploymentGuides/7.0/install-bkce.md", "ZH/DeploymentGuides/7.0/install-bkce.md", None),
            ("ZH/DeploymentGuides/7.0/install-bkce.md", "ZH/DeploymentGuides/7.0/install-bkce.md", "7.0"),
            ("ZH/DeploymentGuides/7.0/install-bkce.md", "ZH/DeploymentGuides/7.0/install-bkce.md", "7.1"),
            (
                "ZH/Monitor/3.6/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                "ZH/Monitor/3.6/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                "7.1",
            ),
            (
                "ZH/PaaS/DevelopTools/SaaSGuide/DevAdvanced/Django+Vue.md",
                "ZH/PaaS/DevelopTools/SaaSGuide/DevAdvanced/Django+Vue.md",
                None,
            ),
            # 3、如果不存在目标路径自己，且存在偏好版本，则根据偏好版本走
            ("ZH/DeploymentGuides/6.0/install-bkce.md", "ZH/DeploymentGuides/7.0/install-bkce.md", "7.0"),
            (
                "ZH/Monitor/3.1/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                "ZH/Monitor/3.6/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                "7.0",
            ),
            ("ZH/DeploymentGuides/install-bkce.md", "ZH/DeploymentGuides/7.0/install-bkce.md", "7.0"),
            # 4、如果不存在目标路径自己，且存在偏好版本，但跟对应的偏好版本没有匹配上，则返回最新版本
            ("ZH/DeploymentGuides/6.0/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", "1234.5678"),
            # 5、如果不存在目标路径自己，且不存在偏好版本，则返回最新版本
            ("ZH/DeploymentGuides/6.0/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
            (
                "ZH/Monitor/3.1/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                "ZH/Monitor/3.8/UserGuide/ProductFeatures/collectors/collectors_faq.md",
                None,
            ),
            ("ZH/DeploymentGuides/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
        ],
    )
    def test_search_markdown(self, source_str, target_str, prefer_version, fake_document):
        """
        测试新版路径寻址逻辑能否访问到文档内容
        """
        count = Document.objects.count()
        assert count != 0

        search_str_results = Document.objects.get_by_absolute_path_and_ver(source_str, prefer_version)
        if search_str_results != target_str:
            assert search_str_results
            assert search_str_results.path
            assert target_str == search_str_results.path
            assert isinstance(search_str_results.other_language_urls, dict)

    @pytest.mark.parametrize(
        "markdown, master_summary, prefer_version",
        [
            ("ZH/APIGateway/README.md", None, ""),
            ("ZH/APIGateway/1.10/README.md", "ZH/APIGateway/1.10/SUMMARY.md", ""),
            ("ZH/APIGateway/1.10/UserGuide/README.md", "ZH/APIGateway/1.10/SUMMARY.md", ""),
            ("ZH/APIGateway/1.10/UserGuide/README_Not_Exists.md", "ZH/APIGateway/1.10/SUMMARY.md", ""),
        ],
    )
    def test_search_summary(self, markdown, master_summary, prefer_version, fake_document):
        """
        当前文档不存在，则找主SUMMARY
        """
        summary = try_get_main_summary(markdown, prefer_version)
        if summary:
            assert summary.path == master_summary
        else:
            assert summary == master_summary

    @pytest.mark.parametrize(
        "relative_path, target_path, catalog_content, other_saas_vers",
        [
            # 6.2版本中有引用7.1版本
            (
                "v71.md",
                None,
                {"name": "v7.1", "path": "ZH/VersionLog/7.1/v71.md", "children": [], "expanded": False},
                {"6.0", "6.1", "7.0", "7.1"},
            ),
            # 7.1版本中无其他版本引用
            (
                "v71.md",
                "ZH/VersionLog/7.1/v71.md",
                {"name": "v7.1", "path": "ZH/VersionLog/7.1/v71.md", "children": [], "expanded": False},
                {"6.0", "6.1", "6.2", "7.0"},
            ),
            # 找到的路径没有版本号的情况
            (
                "Docking_enterprise_login_system/flow_chart.md",
                "ZH/UserManage/IntegrateGuide/Docking_enterprise_login_system/flow_chart.md",
                {
                    "name": "登录流程图",
                    "path": "ZH/UserManage/IntegrateGuide/Docking_enterprise_login_system/flow_chart.md",
                    "children": [],
                    "expanded": False,
                },
                {"2.2", "2.4"},
            ),
            # 在ZH/QuickStart/7.0/SUMMARY.md中找ZH/BCS/1.28/UserGuide/QuickStart/QuickStart.md
            (
                "UserGuide/QuickStart/QuickStart.md",
                "ZH/BCS/1.28/UserGuide/QuickStart/QuickStart.md",
                {
                    "name": "快速入门：容器管理套餐",
                    "path": "ZH/BCS/1.28/UserGuide/QuickStart/QuickStart.md",
                    "children": [],
                    "expanded": False,
                },
                {"6.0"},
            ),
            # 展开有路径的情况
            (
                "UserGuide/QuickStart/prepare.md",
                "ZH/Monitor/3.8/UserGuide/QuickStart/prepare.md",
                {
                    "name": "快速入门",
                    "path": None,
                    "children": [
                        {
                            "name": "入门须知",
                            "path": "ZH/Monitor/3.8/UserGuide/QuickStart/README.md",
                            "children": [],
                            "expanded": False,
                        },
                        {
                            "name": "准备工作",
                            "path": "ZH/Monitor/3.8/UserGuide/QuickStart/prepare.md",
                            "children": [],
                            "expanded": False,
                        },
                        {
                            "name": "权限申请",
                            "path": "ZH/Monitor/3.8/UserGuide/QuickStart/perm.md",
                            "children": [],
                            "expanded": False,
                        },
                    ],
                    "expanded": True,
                },
                {"3.3", "3.6"},
            ),
        ],
    )
    def test_search_doc_path_in_summary(self, relative_path, target_path, catalog_content, other_saas_vers):
        """从版本对应的 summary 中匹配出文档路径"""
        doc_path = check_doc_path_exists_in_summary(relative_path, catalog_content, other_saas_vers)
        assert doc_path == target_path
