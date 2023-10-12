# 支持django单元测试的视图
class DigitCalculater:
    @staticmethod
    def add(num1, num2):
        result = num1 + num2
        return result


class CollectorHandler:
    def update_or_create(self, params: dict):
        transfer_api = TransferApi()
        result = transfer_api.create_data_id()
        params.update(result)
        print(params)
        params["students"] = transfer_api.create_student_information()
        print(params)
        return params


class TransferApi:
    def create_data_id(self):
        return {"request_id": "****************************"}

    def create_student_information(self):
        return {"name": "Django", "age": "22", "score": 80.5}
