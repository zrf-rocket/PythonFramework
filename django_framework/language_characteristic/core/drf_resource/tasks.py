import logging

from celery import shared_task, current_task, subtask
from celery.result import AsyncResult
logger = logging.getLogger(__name__)


# @task(bind=True, queue="celery_resource")
@shared_task(bind=True, queue="celery_resource")
def run_perform_request(self, resource_obj, username, request_data):
    """
    将resource作为异步任务执行
    :param self: 任务对象
    :param resource_obj: Resource实例
    :param username: 用户
    :param request_data: 请求数据
    :return: resource处理后的返回数据
    """
    resource_obj._task_manager = self
    validated_request_data = resource_obj.validate_request_data(request_data)
    response_data = resource_obj.perform_request(validated_request_data)
    validated_response_data = resource_obj.validate_response_data(response_data)
    return validated_response_data
