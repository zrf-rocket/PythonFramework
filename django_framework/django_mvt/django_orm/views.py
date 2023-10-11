from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

from mvt_design.models import Article, User
from django.shortcuts import get_object_or_404
from django_orm.models import Product, Order
from django.forms import model_to_dict


def search(request):
    """
    查询操作
    :param request:
    :return:
    """
    # product = Product.objects.get(name="python3") 精确查询，查不到就会抛异常
    # django_orm.models.Product.DoesNotExist: Product matching query does not exist.
    # product = Product.objects.get(name="Python3")
    # print(product.name, product.price, product.description)

    # product2 = Product.objects.filter(stock=22)
    # print(product2)  # <QuerySet [<Product: Python3>, <Product: Golang>]>

    # product3 = Product.objects.all().values()
    # product4 = Product.objects.all().values("name")
    # print(product3)
    # print(product4)
    # <QuerySet [{'id': 1, 'name': 'Python3', 'price': Decimal('6.25'), 'stock': 22, 'description': 'Python3进阶的书籍', 'create': datetime.datetime(2023, 8, 18, 16, 41, 54, 153079, tzinfo=datetime.timezone.utc)}, {'id': 2, 'name': 'Django4', 'price': Decimal('22.25'), 'stock': 10, 'description': '公众号：CTO Plus', 'create': datetime.datetime(2023, 8, 18, 16, 44, 52, 484827, tzinfo=datetime.timezone.utc)}, {'id': 3, 'name': 'Golang', 'price': Decimal('26.00'), 'stock': 22, 'description': 'Golang进阶的书籍', 'create': datetime.datetime(2023, 8, 18, 16, 41, 54, 153079, tzinfo=datetime.timezone.utc)}, {'id': 4, 'name': 'CPP', 'price': Decimal('32.00'), 'stock': 10, 'description': '公众号：CTO Plus', 'create': datetime.datetime(2023, 8, 18, 16, 44, 52, 484827, tzinfo=datetime.timezone.utc)}]>
    # <QuerySet [{'name': 'Python3'}, {'name': 'Django4'}, {'name': 'Golang'}, {'name': 'CPP'}]>

    # product5 = Product.objects.all().values_list()
    # product6 = Product.objects.all().values_list("name")
    # product7 = Product.objects.all().values_list("name", flat=True)
    # print(product5)
    # print(product6)
    # print(product7)
    # <QuerySet [(1, 'Python3', Decimal('6.25'), 22, 'Python3进阶的书籍', datetime.datetime(2023, 8, 18, 16, 41, 54, 153079, tzinfo=datetime.timezone.utc)), (2, 'Django4', Decimal('22.25'), 10, '公众号：CTO Plus', datetime.datetime(2023, 8, 18, 16, 44, 52, 484827, tzinfo=datetime.timezone.utc)), (3, 'Golang', Decimal('26.00'), 22, 'Golang进阶的书籍', datetime.datetime(2023, 8, 18, 16, 41, 54, 153079, tzinfo=datetime.timezone.utc)), (4, 'CPP', Decimal('32.00'), 10, '公众号：CTO Plus', datetime.datetime(2023, 8, 18, 16, 44, 52, 484827, tzinfo=datetime.timezone.utc))]>
    # <QuerySet [('Python3',), ('Django4',), ('Golang',), ('CPP',)]>
    # <QuerySet ['Python3', 'Django4', 'Golang', 'CPP']>

    # product8 = Product.objects.filter(description__contains="cto")
    # print(product8)
    # product9 = Product.objects.filter(description__icontains="cto")
    # print(product9)

    # product10 = Product.objects.filter(id__range=[2,4])
    # print(product10)
    # 输出<QuerySet [<Product: Django4>, <Product: Golang>, <Product: CPP>]>

    # product11 = Product.objects.filter(name__in=["Python3", "Django4"])
    # print(product11)
    # 输出<QuerySet [<Product: Python3>, <Product: Django4>]>

    user = get_object_or_404(User, pk=1)
    res = model_to_dict(user)
    print(res)
    data = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "is_superuser": user.is_superuser,
    }
    return JsonResponse(data)


def create(request):
    """
    新增
    :param request:
    :return:
    """

    # article1 = Article(
    #     title="模板",
    #     body="模板(Template)的设计，工作原理及常用过滤器与标签介绍,Django的模板是静态的html文件，它只决定了一个页面的样式或外观。它需要视图View传递过来的变量(Variable)或内容对象(Context object)才能被渲染成一个完整的页面。这样做的好处是实现了样式与业务逻辑的分离，便于前端和后端Web开发人员各自完成自己的开发工作。",
    #     status='d',
    #     author_id=2
    # )
    # # 直接插入新的一条数据
    # article1.save()

    # article = Article.objects.create(
    #     title="视图",
    #     body="公众号：CTO Plus",
    #     status='d',
    #     author_id=3
    # )

    # # 如果不存在，则创建  created为true
    # # 如果存在，则跳过 created为false
    # obj, created = Article.objects.get_or_create(
    #     title="模型",
    #     body="公众号：CTO Plus",
    #     status='d',
    #     author_id=2
    # )
    # print(obj) # 返回Models中定义的__str__中的字段，此处是：“模型”
    # print(created) # False

    # Article.objects.bulk_create([
    #     Article(title="SteveRocket01", body="公众号：CTO Plus", status='p', author_id=1),
    #     Article(title="SteveRocket02", body="公众号：CTO Plus", status='p', author_id=2),
    #     Article(title="SteveRocket03", body="公众号：CTO Plus", status='p', author_id=3),
    # ])

    # 如果存在则更新，不存在则插入
    res = Product.objects.update_or_create(
        name="Python3",
        defaults={
            "name": "Python3",
            "price": 12,
            "stock": 22,
            "description": "Python3进阶的书籍",
        },
    )
    print(res)
    obj, created = Product.objects.update_or_create(
        name="Django4",
        defaults={
            "name": "Django4",
            "price": 22,
            "stock": 10,
            "description": "公众号：CTO Plus",
        },
    )
    # 将name="Django4"的price加22
    Product.objects.update_or_create(
        name="Django4", defaults={"price": F("price") + 22}
    )
    return JsonResponse({})


def delete(reqeust):
    """
    删除
    :param reqeust:
    :return:
    """
    # product = Product.objects.get(name="Python3") # 存在多条结果 报错：django_orm.models.Product.MultipleObjectsReturned: get() returned more than one Product -- it returned 4!
    # product = Product.objects.get(id=2)
    # print(product)
    # product.delete()

    # product2 = Product.objects.filter(name__icontains="python").delete()
    # print(product2)  # 有数据删除，则返回(4, {'django_orm.Product': 4})  否则(0, {})

    # 删除所有
    Product.objects.all().delete()

    return HttpResponse({})


def update(request):
    """
    修改
    :param request:
    :return:
    """
    # product = Product.objects.get(name="Golang")
    product = Product.objects.get(id=3)
    product.price = 100
    product.save()

    # product2 = Product.objects.get(id=4).update(price=100)  # AttributeError: 'Product' object has no attribute 'update'

    # 批量更新
    # product2 = Product.objects.filter(name="Golang").update(price=100, stock=50)

    product2 = Product.objects.filter(name__icontains="django").update(price=200)
    print(product2)
    return HttpResponse()


from django.db.models import Q, F


def F_methods(reqeust):
    # 查询价格大于库存的商品
    # res = Product.objects.filter(price__gt=F("stock"))

    # 将所有商品价格加上0.5
    # Product.objects.update(price=F("price") + 0.5)
    Product.objects.all().update(price=F("price") * 0.5)

    # res = Order.objects.filter(product__price__gt=F("product__price"))
    return JsonResponse({})


def Q_methods(request):
    product1 = Product.objects.filter(Q(name__contains="P"))
    print(product1)

    res = Product.objects.filter(Q(price__gt=20) | Q(stock__lt=20))
    print(res)

    # product2 = Product.objects.filter(name__icontains="p", Q(price__gte=20))
    # SyntaxError: positional argument follows keyword argument

    # 组合使用  Q对象必须在类属性的前面
    product2 = Product.objects.filter(Q(price__gte=20), name__icontains="p")
    print(product2)

    product3 = Product.objects.filter(Q(name__startswith="dj"))
    print(product3)
    product4 = Product.objects.filter(
        Q(name__startswith="p") | Q(description__icontains="CTO")
    )
    print(product4)

    query = request.GET.get("query", "cto plus")
    product5 = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )
    return render(request, "django_orm/product_list.html", {"products": product5})
