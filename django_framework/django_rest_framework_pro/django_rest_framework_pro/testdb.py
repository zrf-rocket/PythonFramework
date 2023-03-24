
from django.http import HttpResponse,JsonResponse
# HttpResponse向前台返回字符   JsonResponse
from TestModel.models import TestAreas

#此处添加数据 需要先创建对象，然后再执行 save 函数，相当于SQL中的INSERT
#数据库操作  插入数据
def insertdb(request):
    test1 = TestAreas(name="Django mysql{}".format(TestAreas.objects.count() + 1))
    test1.save()
    return HttpResponse("数据添加成功！")


#获取数据
def getdb(request):
    #初始化
    response = ""
    response1 = ""

    # 获取表的总条数
    counts = TestAreas.objects.all().count()
    # print(counts)

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = TestAreas.objects.all()
    # for item in list:
    #     print(item)

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = TestAreas.objects.filter(id=1)
    # print(response2)

    # 获取单个对象
    response3 = TestAreas.objects.get(id=16)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = TestAreas.objects.order_by('name')[0:2]

    # 数据排序
    TestAreas.objects.order_by("id")

    # 上面的方法可以连锁使用
    TestAreas.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " <br/>"
    response = response1

    return HttpResponse("数据获取成功:<p>" + response + "</p>")


#更新数据
def updatedb(request):
    # 修改数据可以使用 save() 或 update()

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    #方式1
    # test2 = TestAreas.objects.get(id = 1)
    # test2.name = "Django mysql1"
    # test2.save()

    # 方式2
    # TestAreas.objects.filter(id=2).update(name = "Django mysql2")

    #修改所有的列
    # TestAreas.objects.all(id=2).update(name= "None")

    # TestAreas.objects.all(id=2).update(name= "None")
    TestAreas.objects.all(id=2).update(name = None)
    return HttpResponse("数据更新成功")




# 删除数据
# 删除数据库中的对象只需调用该对象的delete()方法即可
def deletedb(request):
    #方式一
    try:
        test3 = TestAreas.objects.get(id = 5)
        test3.delete()

        #方式二
        TestAreas.objects.filter(id = 6).delete()
        TestAreas.objects.filter(id = 6).delete()
    except Exception as e:
        print("已不存在要删除的数据字段。")
    # 删除所有数据
    # TestAreas.objects.all().delete()
    return HttpResponse("数据删除成功")



