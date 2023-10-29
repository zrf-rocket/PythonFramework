from string import punctuation as punctuation_en

import pytest
from utils import read_markdown
from zhon.hanzi import punctuation as punctuation_zh

from core.storage.core import create_search_index, search


@pytest.fixture()
def create_index():
    whoosh_writer = create_search_index().writer()
    path, cnt = read_markdown()
    whoosh_writer.add_document(
        file_name="测试Markdown",
        title="测试",
        path=path,
        content=cnt,
        bookname="bookname",
        product_name="产品文档",
        version="7.1",
        big_versions=['6.1', '7.1'],
        directory="directory",
    )
    whoosh_writer.commit()


@pytest.mark.django_db
class TestWhooshSearch:
    @pytest.mark.parametrize(
        "keyword,name,label,version",
        [
            ("运维,./,./+-\\|", "docs", "产品文档", "7.1"),
            (f"运维{punctuation_zh}", "docs", "产品文档", "7.1"),
            (f"运  维{punctuation_zh}", "docs", "产品文档", "7.1"),
            (f"{punctuation_zh}内解析域名失败{punctuation_en}", "docs", "产品文档", "7.1"),
        ],
    )
    def test_search_keywords(self, keyword, name, label, version, create_index):
        """
        根据关键字
        创建索引然后请求API
        """
        res = search(raw_query=keyword, name=name, label=label, version=version)
        assert isinstance(res, tuple)
        assert res[0]
