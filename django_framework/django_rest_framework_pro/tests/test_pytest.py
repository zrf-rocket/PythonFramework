import pytest


@pytest.fixture()
def fake_document():
    print("other operator......")


@pytest.mark.django_db
class TestSearch:
    @pytest.mark.parametrize(
        "source_str, target_str, prefer_version",
        [
            ("ZH/DeploymentGuides/7.1/manual-install-bkce.md", "ZH/DeploymentGuides/7.1/manual-install-bkce.md", None),
            ("ZH/DeploymentGuides/7.1/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
            (
                    "ZH/DeploymentGuides/manual-install-bkce.md",
                    "ZH/DeploymentGuides/7.1/manual-install-bkce.md",
                    None,
            ),
            ("ZH/DeploymentGuides/7.70/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
            ("ZH/DeploymentGuides/7.7777/install-bkce.md", "ZH/DeploymentGuides/7.1/install-bkce.md", None),
            (
                    "ZH/DeploymentGuides/777.7777/install-bkce.md",
                    "ZH/DeploymentGuides/7.1/install-bkce.md",
                    None,
            )
        ],
    )
    def test_search_markdown(self, source_str, target_str, prefer_version, fake_document):
        """
        测试新版路径寻址逻辑能否访问到文档内容
        """
        assert source_str == target_str
