import logging
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)


class CustomException(APIException):
    # todo 和core.errors 结合
    status_code = 500
    default_detail = "A custom exception occurred."
    default_code = "custom_exception"

    def __init__(self, message=None, data=None, code=None):
        """
        :param message: 错误信息
        :param data: 错误数据
        :param code: 错误码
        """
        if message is None:
            message = self.default_detail

        self.detail = message
        self.message = message
        self.data = data
        self.code = code
