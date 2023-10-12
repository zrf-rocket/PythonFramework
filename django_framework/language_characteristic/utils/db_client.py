##### 使用 pymongo 连接 Django 和 MongoDB
# pip install pymongo
# pip install dnspython
from pymongo import MongoClient

mongo_db = "django4"
mongo_host = "localhost"
mongo_username = ''
mongo_password = ''


# 方式1
def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host, port=int(port), username=username, password=password)
    db_handle = client['db_name']
    return db_handle, client


# 方式2
# client = MongoClient('mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority')
# db = client["db_name"]

# 方式3
# client2 = MongoClient('mongodb://localhost:27017/')
client2 = MongoClient('localhost', 27017)
db2 = client2[mongo_db]

#### 使用 MongoEngine 连接 Django 和 MongoDB
# MongoEngine 是 PyMongo 之上的 ORM 层。因此，仍然需要 PyMongo (>=3.4) 才能使用 MongoEngine。
# 使用 MongoEngine 连接 Django 和 MongoDB，您可以使用 ListField 和 DictField 等字段来处理巨大的非结构化 JSON 数据。
# pip install mongoengine mongoengine-dsl mongoengine-pagination
from mongoengine import connect

db3 = connect(db=mongo_db, host=mongo_host, username=mongo_username, password=mongo_password)
# 使用 MongoEngine，我们必须在 Django 应用程序的 models.py 文件中定义一个模式。 MongoDB 是无模式的。该架构仅在应用程序级别执行，从而使未来的任何更改都变得快速而轻松。
# MongoEngine 类似于 Django 的默认 ORM，但在 model.py 中有以下变化：


#### 使用 Djongo 连接 Django 和 MongoDB
# Djongo 是对 PyMongo 的改进，因为开发人员无需编写冗长的查询。它将 Python 对象映射到 MongoDB 文档，即对象文档映射 (ODM)。 Djongo 确保只有干净的数据才能进入数据库。
# 通过使用 Djongo 执行完整性检查、应用验证等，无需修改现有的 Django ORM。
# pip install djongo==1.3.6
# pip install pymongo==3.12.1
# pip install django==4.1.7




if __name__ == '__main__':
    # 查
    result = db2["information"].find()
    print(list(result))
    print(result.count())

    # 删
    # db2["information"].delete_one()
    # db2["information"].delete_many()

    # 改
    # db2["information"].update()
    # db2["information"].update_one()
    # db2["information"].update_many()

    # 增
    # db2["information"].insert()
    # db2["information"].insert_one()
    # 插入多条
    # db2["information"].insert_many([
    #     {"name": "python", "version": 3.11},
    #     {"name": "django", "version": 4.1},
    #     {"name": "pymongo", "version": 4.3},
    #     {"name": "mongoengine", "version": 4.3}
    # ])






    result2 = db3["information"]#.find()
    # print(list(result2))
