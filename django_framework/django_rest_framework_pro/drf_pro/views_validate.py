from rest_framework.response import Response

from .serializer_results_validate import ResponseSerialzer

from httpx import get

from rest_framework.views import APIView


class HttpRequest():
    @classmethod
    def get(cls, url):
        response = get(url)
        if response.status_code == 200:
            return response.json()


class RequestMD(APIView):
    def get(self, request):
        # data = {
        #     "result": True,
        #     "code": 0,
        #     "message": "OK",
        #     "data": {
        #         "content": "产品简介",
        #         "update_time": "2023-04-14 10:53:36",
        #         "md_is_exist": [
        #             "6.0/152/6962",
        #             "6.1/197/22734",
        #             "7.0/245/39686"
        #         ],
        #         "catalog_version": {
        #             "7.0": "7.0/245/0",
        #             "6.1": "6.1/197/0",
        #             "6.0": "6.0/152/0",
        #             "5.1": "5.1/226/0"
        #         },
        #         "edit_url": "https://github.com/TencentBlueKing/BKDocs/blob/master/ZH/7.0/配置平台/产品白皮书/产品简介/Overview.md",
        #         "current_version": "7.0",
        #         "prefix_url_list": [
        #             "ZH",
        #             "7.0",
        #             "配置平台",
        #             "产品白皮书",
        #             "产品简介"
        #         ],
        #         "pdf_url": "https://bkdocs-1252002024.file.myqcloud.com/ZH/7.0/配置平台/配置平台.pdf"
        #     },
        #     "request_id": "",
        #     "name": "SteveRocket"
        # }

        data = {
            'result': True, 'code': 0, 'message': 'OK', 'data': {
                'content': 'CMDB如何管理自定义模型及实例',
                'update_time': '2023-07-31 16:17:31',
                'md_is_exist': ['测试数据/202/1234'],
                'catalog_version': {},
                'edit_url': 'ZH/CMDB/Vedios.md',
                'current_version': '7.0',
                'prefix_url_list': ['ZH', 'CMDB'],
                'pdf_url': ''
            },
            'request_id': ''
        }
        # data = {'result': True, 'code': 0, 'message': 'OK'}  # 校验通过

        # data = {}  # 序列化不通过
        # data = None  # 序列化不通过
        serializer = ResponseSerialzer(data=data)
        if serializer.is_valid():
            print("校验通过.....")
            return Response(serializer.data)
        return Response(data={})
