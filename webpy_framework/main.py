import web

# 定义URL结构：
# URL与类名组成对出现：匹配URL的正则表达式，圆括号表示捕捉对应的数据以便后面使用。 接受请求的类名称。
urls = (
    '/blog/\d+', 'Blog',
    '/index', 'Index',
    '/home/(.*)', 'WebPyFramework',
    '/upper/(.*)', 'Upper'
)

# 创建一个列举这些url的application
app = web.application(urls, globals())
# 去创建一个基于刚提交的URL列表的application。这个application会在这个文件的全局命名空间中查找对应类。找不到，请求时则会报错。

# 告诉web.py到模板目录中去查找模板。若报错找不到摸板文件，可以尝试把路径改为绝对路径。
render = web.template.render("templates")


class WebPyFramework:
    def GET(self, name):
        if not name:
            name = "Web.py"
        return "Hello, " + name + "!"


class Blog:
    def GET(self):
        return "this is blog GET request"

    def POST(self):
        return "this is blod post request"


class Index:
    def GET(self):
        name = "SteveRocket"
        return render.hello(name=name)


class Upper:
    # GET必须大写
    def GET(self, text):
        # text = "hello"
        # hello.html的名称很重要，和下面的render.hello是对应的，$content是传入的参数名称。
        return render.base(content=text.upper())


if __name__ == '__main__':
    print("This is web.py framework")
    app.run()
    # default port:8080
    # target port run:python main.py 80
