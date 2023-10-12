from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PdfUploadForm
from .models import Category
import PyPDF2


# Create your views here.

# FBV
def pdf_extract(request):
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            page_num = int(request.POST.get("page", 0))
            page_index = page_num - 1
            f = request.FILES['file']

            with open('original.pdf',"wb+") as pdfFileObj:
                for chunk in f.chunks():
                    pdfFileObj.write(chunk)
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    else:
        form = PdfUploadForm()
        return render(request, 'pdf/pdf_upload.html', {'form': form})



from rest_framework.response import Response

def category(request):
    if request.method == "GET":
        # root_category = Category.objects.get(name='Root Category')
        # child_categories = root_category.children.all()

        # 根据name获取他的所有父节点
        for item in Category.objects.filter(name="steverocket1.1.1").get_ancestors(include_self=True):
            print(item.name)

    elif request.method == "POST":
        root_category = Category.objects.create(name='Root Category')
        child_category1 = Category.objects.create(name='Child Category 1', parent=root_category)
        child_category2 = Category.objects.create(name='Child Category 2', parent=root_category)
    # return Response(data={})
    # return JsonResponse({"category": root_category})
    return JsonResponse({})

def whitenoise_server(request):
    # whitenoise 不支持template
    # from django.conf import settings
    # settings.STATIC_ROOT
    # return render(request, "index.html")
    pass


    # return render(request, "README.md")
    # https://gitee.com/SteveRocket/staticfiles/blob/master/staticfiles/index.html
    # return render(request, "https://gitee.com/SteveRocket/staticfiles/blob/master/staticfiles/index.html")
