## 高效常用的Flask第三方组件

1. Connexion：构建一个不错的REST API以及交互式文档

2. Flask-Classful:基于类的视图

3. Flask-SQLalchemy：用于连接SQL数据库的库（与SQLAlchemy交互）。可以帮助您轻松地操作数据库，并提供了许多有用的功能，如模型映射、查询和事务数据库等操作。  

4. Flask-script：插入脚本

5. Flask-migrate：提供数据库迁移支持（管理迁移数据库）

6. Flask-Session：为Flask应用添加会话支持（Session存储方式指定）

7. Flask-WTF：提供Web表单处理支持，用于生成表单的库，提供了一系列的表单组件和验证器。

8. Flask-Mail：用于发送电子邮件的扩展库，并支持 SMTP、Gmail 和 Amazon SES 等多种邮件服务。

9. Flask-Bable：提供多语言支持、国际化和本地化支持，翻译。

10. Flask-Login：用于管理用户会话和用户认证的库，并提供了许多有用的功能，如重定向、请求拦截和用户管理、添加用户认证和会话支持（认证用户状态）等。

11. Flask-OpenID：认证

12. Flask-RESTful：用于开发RESTful API的库，并提供了许多有用的功能，如请求解析、数据验证和异常处理等。

13. Flask-Bootstrap：用于在Flask应用中集成前端Twitter Bootstrap框架的库。

14. Flask-Moment：本地化日期和时间

15. Flask-Admin：用于生成后台管理界面的库，可以帮助您轻松地管理数据和用户。简单而可扩展的管理接口的框架，提供基于Web的应用程序管理界面。

16. Flask-RESTX：flask框架开发接口框架

    Flask-restfull 是flask开发API接口的一个框架。 Flask-RESTPlus 是Flask-restfull 升级版，可以生成swagger在线文档。这个项目不再维护，迁移到Flask-RESTX。
    Flask-RESTX 与 Flask-RESTPlus 的 API保持 100% 兼容。

17. Flask-Principle：Flask扩展的框架。包含：Identity，Needs，Permission，IdentityContext。

18. Flask-Security：登录和注册用户

19. Flask-marshmallow：轻量级的数据格式转换的模块，序列化和反序列化模块。
    官方文档：https://marshmallow.readthedocs.io/en/latest/
    可以通过安装flask-sqlalchemy和marshmallow-sqlalchemy集成到项目即可，常用于将复杂的orm模型对象与python原生数据类型之间相互转换。

20. Flask-PyMongo：用于连接MongoDB数据库的库。

21. Flask-Caching：用于缓存的库，支持多种缓存后端，如Redis、Memcached等。

22. Flask-DebugToolbar：用于调试和优化Flask应用程序。

23. Flask-Assets：用于处理静态文件。

24. Flask-Uploads：用于处理上传的文件。

25. Flask-Cors：允许跨域资源共享

26. Flask-SocketIO：在Flask应用中使用WebSocket