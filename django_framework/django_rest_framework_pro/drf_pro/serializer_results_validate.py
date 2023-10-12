# 如何在Django中验证JSON对象
# 通过Serializer校验请求响应的结果
from rest_framework.serializers import Serializer
from rest_framework import serializers

class MDSerialzer(Serializer):
    content = serializers.CharField(min_length=0)
    # content = serializers.CharField()

    # update_time = serializers.CharField(min_length=0)
    # update_time = serializers.DateTimeField()
    update_time = serializers.CharField()

    md_is_exist = serializers.ListField()
    catalog_version = serializers.JSONField()  # 如果catalog_version空{}   序列化结果则也为{}

    edit_url = serializers.CharField()
    current_version = serializers.CharField(label='version')

    prefix_url_list = serializers.ListField()  # 如果prefix_url_list为空 序列化结果为[]

    # pdf_url = serializers.CharField()  # 如果pdf_url为空   则序列化失败
    # pdf_url = serializers.CharField(min_length=0)  # 如果pdf_url为空   则序列化失败
    # pdf_url = serializers.CharField(allow_null=True, allow_blank=True)  # 如果pdf_url为空   则序列化失败
    pdf_url = serializers.CharField(allow_blank=True)
    # pdf_url = serializers.CharField(min_length=0)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['new_fileds'] = True
        data['version'] = instance["current_version"]
        return data

class ResponseSerialzer(Serializer):
    result = serializers.BooleanField(label='结果', help_text='请求结果', default='res')
    code = serializers.IntegerField()
    message = serializers.CharField()
    is_old_docs = serializers.BooleanField(default=True)  # 这个字段可以在data中不做传递，作为返回值默认值
    # 如果想添加默认值  也可以to_representation方法 在方法里面定义字段
    data = MDSerialzer()





"""
我正在使用AJAX将JSON提交到django视图。JSON如下所示：
{
   "code":"9910203040", // required
   "name":"Abc", // required
   "payments":[
      {
         "amount":300, // required
         "name":"efg", // required,
         "type": 2 // can be empty
      },
      {
         "amount":100,
         "name":"pqr",
         "type": 3
      }
   ]
}
付款清单可以是任何大小。如何在Django中验证？是否可以使用Django Forms进行验证？如果是Spring，我将创建Request类并在字段上使用注释，但无法弄清楚如何在Django中执行此操作。
"""
# class PaymentSerializer(Serializer):
#     amount = serializers.IntegerField
#     name = serializers.CharField(required=True, max_length=128)
#     type = serializers.IntegerField(required=True, min_value=0)
#
# class ValidateFormSerializer(Serializer):
#     code = serializers.CharField(required=True, max_length=32)
#     name = serializers.CharField(required=True, max_length=128)
#     payments = serializers.ListField(child=PaymentSerializer)

# 需要这样才能在“视图”部分中对其进行验证-
# import ValidateFormSerializer
#
# # add this snippet in your view section
#  valid_ser = ValidateFormSerializer(data=request.data)
#  if valid_ser.is_valid():
#        post_data = valid_ser.validated_data
#  else:
#       print(valid_ser.errors)