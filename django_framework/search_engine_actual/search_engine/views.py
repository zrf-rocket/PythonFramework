from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


# 使用分词函数
from .utils import segmant_text


def my_jieba_view(request):
    text = "这是一段需要分词的中文文本，My Name is steverocket"
    segmented_text = segmant_text(text)
    return render(request, 'my_template.html', {"segmented_text": segmented_text})





def my_haystack_view(request):
    return JsonResponse({})
