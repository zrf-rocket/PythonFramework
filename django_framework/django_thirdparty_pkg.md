## 高效常用的Django第三方包
```
总结收纳日常Django项目开发中增效的第三方组件库
```
Django是围绕“可重用的应用，reusable app”的思想建立的。Django有一个丰富多样的由各种可以重用的应用组建起来的生态系统, 选择一些好的第三方包可以大大简化Web APP开发。

1. Django-allauth - 用户注册登录管理
    官网地址：https://django-allauth.readthedocs.io/en/latest/  
    * django-allauth 是一个能够解决的注册和认证需求的、可重用的 Django 应用。无论需要构建本地注册系统还是社交账户注册系统，django-allauth 都能够帮做到。
    * 这个应用支持多种认证体系，比如用户名或电子邮件。一旦用户注册成功，它还可以提供从无需认证到电子邮件认证的多种账户验证的策略。同时，它也支持多种社交账户和电子邮件账户。它还支持插拔式注册表单，可让用户在注册时回答一些附加问题。
    * django-allauth 支持多于 20 种认证提供者，包括 Facebook、Google、微博 和 微信。如果发现了一个它不支持的社交网站，很有可能通过第三方插件提供该网站的接入支持。这个项目还支持自定义后端，可以支持自定义的认证方式，对每个有定制认证需求的人来说这都很棒。
    * django-allauth 易于配置，且有完善的文档。该项目通过了很多测试，所以可以相信它的所有部件都会正常运作。

2. Django-haystack - 全文检索引擎

    官网地址：https://django-haystack.readthedocs.io/en/master/  
    全文检索不同于标题的简单匹配，是一件技术难度比较高的活。当文章很长时，很难找到精确的匹配，同时搜索全文需要消耗大量的计算资源。有了haystack，在django中直接添加搜索功能，像搜索标题一样搜索全文，而无需关注索引建立、搜索解析等技术问题。haystack支持多种搜索引擎，不仅仅是whoosh，使用solr、elasticsearch等搜索，也可通过haystack，而且直接切换引擎即可，甚至无需修改搜索代码。

3. Django-ckeditor - 富文本编辑器

    官网地址：https://django-ckeditor.readthedocs.io/en/latest/  
    django没有提供官方的富文本编辑器，而ckeditor恰好是内容型网站后台管理中不可或缺的控件。ckeditor是一款基于javascript，使用非常广泛的开源网页编辑器。它允许用户直接编写图文，插入列表和表格，并支持文本和HTML格式代码输入。

4. Django-imagekit - 自动化处理图像
    
    官网地址：https://django-imagekit.readthedocs.io/en/latest/  
    现代网站开发一般免不了处理一些图片，例如头像、用户上传的图片等内容。django-imagekit 帮配合 django 的 model 模块自动完成图片的裁剪、压缩、生成缩略图、加水印等一系列图片相关的操作。

5. Django-crispy-forms - 快速美化django表单首选
    
    官网地址：https://django-crispy-forms.readthedocs.io/en/latest/  
    大大增强 Django 内置的表单功能，Django 内置的表单生成原生的 HTML 表单代码还可以，但为其设置样式是一个麻烦的事情。django-crispy-forms 帮助使用一行代码渲染一个 Bootstrap 样式的表单，当然它还支持其它一些热门的 CSS 框架样式的渲染。

6. Django-debug-toolbar - django项目调试利器

    官网地址：https://django-debug-toolbar.readthedocs.io/en/latest/  
    该工具给django web开发提供了强大的调试功能，包括查看执行的sql语句，db查询次数，request，headers，调试概览等。通过安装插件Pympler，还可以了解内存使用情况。

7. Django-celery - 执行异步任务或定时任务的最佳选择

    官网地址：http://docs.celeryproject.org/en/latest/django/index.html  
    https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html  
    Celery 是一款非常简单、灵活、可靠的分布式系统，可用于处理大量消息，并且提供了一整套操作此系统的一系列工具。另外，Celery 是一款消息队列工具，可用于处理实时数据以及任务调度。官网给出了 Celery 如下四个特点：
    ```
    • 简单：开箱机用，维护简单，不需要使用配置文件；
    • 高可靠性：如果连接丢失或者出现故障，客户端进程会自动重试。一些 broker 会以主/主或者主/备的方式维持系统的高可靠性；
    • 快速：单个 Celery 进程每分钟内可以处理数百万个任务，往返的延迟在毫秒级别(使用RabbitMQ 做中间件，再加上一些优化的设置)；
    • 灵活：几乎 Celery 的每个部分都可以自行扩展，如使用自定义池、序列化器，压缩方案、日志记录，调度程序，消费者，生产者，代理传输等等。
    ```
    注意到基于 Django 框架构建的 Web 系统实际上是一个同步服务。这意味着当客户端发起一个请求时，后端只有在视图函数处理完后才会返回结果。如果这个请求背后要做的工作比较耗时，或者因为某种原因导致非常耗时，那么此时客户端会一直等待请求的响应，这非常影响用户体验。对于一个优秀的网站而言，良好的用户体验十分重要，这也说明了一个支持异步功能的第三方插件的重要性。为了能让 Django 搭建的 Web 系统支持这样的异步功能，于是 django-celery 便应运而生。django-celery项目之后也被移到 celery 下进行统一管理。
    django-celery是django web开发中执行异步任务或定时任务的最佳选择。它的应用场景包括:
    ```
    * 异步任务: 当用户触发一个动作需要较长时间来执行完成时，可以把它作为任务交给celery异步执行，执行完再返回给用户。这点和在前端使用ajax实现异步加载有异曲同工之妙。
    * 定时任务。假设有多台服务器，多个任务，定时任务的管理是很困难的，要在不同电脑上写不同的crontab，而且还不好管理。Celery可以帮助快速在不同的机器设定不同任务。
    * 其他可以异步执行的任务。比如发送短信，邮件，推送消息，清理/设置缓存等。这点还是比较有用的。
    ```
8. Django-rest-framework开发REST API的最佳工具

    官网地址：http://www.django-rest-framework.org/  
    （djangorestframework）REST API 正在迅速成为现代 Web 应用的标准功能。可以制作自己的视图，设置合适的Content-Type，然后返回 JSON 而不是渲染后的 HTML 响应。这是在像Django Rest Framework（下称 DRF）这样的 API 框架发布之前，大多数人所做的。
   如果对 Django 的视图类很熟悉，会觉得使用 DRF 构建 REST API 与使用它们很相似，不过 DRF 只针对特定 API 使用场景而设计。一般的 API 设置只需要一点代码，所以没有提供一份让兴奋的示例代码，而是强调了一些可以让生活的更舒适的 DRF 特性：
    ```
    • 可自动预览的 API 可以使的开发和人工测试轻而易举。可以查看 DRF 的示例代码。可以查看 API 响应，并且不需要做任何事就可以支持 POST/PUT/DELETE 类型的操作。
    • 便于集成各种认证方式，如 OAuth, Basic Auth, 或API Tokens。
    • 内建请求速率限制。
    • 当与 django-rest-swagger 组合使用时，API 文档几乎可以自动生成。
    • 广泛的第三方库生态。
    ```
    具体使用请参考《DRF实战总结》系列内容：  
    * [1、DRF实战总结：DRF特点、序列化与RESTful API规范](https://blog.csdn.net/zhouruifu2015/article/details/129761606)
    * [2、DRF实战总结：基于函数的视图API以及自定义序列化器（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129761750)
    * [3、DRF实战总结：基于类的视图APIView, GenericAPIView和GenericViewSet视图集（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129761752)
    * [4、DRF实战总结：序列化器(Serializer)、数据验证、重写序列化器方法详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129965351)
    * [5、DRF实战总结：认证(Authentication)与权限(Permission)（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129965342)
    * [6、DRF实战总结：认证及使用Token认证，代码示例详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129965353)
    * [7、DRF实战总结：JWT认证原理和使用及第三方库simplejwt 的详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980628)
    * [8、DRF实战总结：分页(Pagination)及DRF提供的分页类详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980604)
    * [9、DRF实战总结：过滤(filter)与排序，以及第三方库django-filter的使用（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980612)
    * [10、DRF实战总结：限流(throttle)、限流的使用方式详解与代码示例（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980623)
    * [11、DRF实战总结：使用cache_page和第三方库drf-extensions进行缓存（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130023827)
    * [12、DRF实战总结：DRF序列化模型与序列化关系模型详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130023832)
    * [13、DRF实战总结：重写DRF的to_representation和to_internal_value方法的作用详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130031072)
    * [14、DRF实战总结：获取Django请求路径的方法以及各自的区别](https://blog.csdn.net/zhouruifu2015/article/details/130023839)
    * [15、DRF实战总结：2023 DRF框架序列化性能优化和cProfile性能基准测试（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130031818)

    
10. Django-xadmin - 更美观更强大的后台

    官网地址：https://django-xadmin.readthedocs.io/en/latest/  
    如果不喜欢django自带后台admin简陋的样式，可以使用xadmin。xadmin是基于bootstrap和admin的一个更强大的后台管理系统，简单易用而且又好看的后台管理系统。官网宣传语便是：打造管理系统从未如此简单。其宣称的几个核心特点如下：
     ```
     • 基于 Bootstrap3，适合多种屏幕显示；
     • 内置功能丰富，除了基本的 CURD 功能外，还有丰富的插件功能，如数据的导出、书签、图表、图片相册等多种扩展功能；
     • 强大的插件系统，通过制作 Xadmin 插件可以扩展系统的任何一个功能点；
     • 完善的权限系统，可配置、可定制，安全可靠；
     ```

11. Django-constance - 常量管理

    官网地址：https://django-constance.readthedocs.io/en/latest/  
    有时会在 django 的 settings 中设置一些常量，但是有可能会进行变更。利用这个包，只需简单的配置就可以自动生成 admin 管理后台可以修改管理常量。

12. Django-filter - 过滤数据使用

    官网地址：https://django-filter.readthedocs.io/en/latest/  
    Django-filter允许用户模型字段进一步过滤从数据库查得到的queryset，从而筛选显示用户想要的查询结果，这样避免了对数据库的再次查询，大大提升了效率。比如用户访问文章列表页面，已经看到了文章清单，但用户还希望通过标题关键词进一步在查询结果中筛选出自己感兴趣的文章清单(而不必重新查询数据库)，这时使用Django-filter就可以轻松帮实现上述需求。    
    具体使用请参考：[9、DRF实战总结：过滤(filter)与排序，以及第三方库django-filter的使用（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980612)

13. Cookiecutter-django

    官网地址：https://cookiecutter-django.readthedocs.io/en/latest/  
    Github地址：https://github.com/cookiecutter/cookiecutter-django  
    使用cookiecutter-django创建一个新项目比使用django-admin.py的命令创建新项目有更多优势，比如它会给提供一个更加合适的项目目录结构，并允许在创建项目之初就选择需要安装配置的库比如(compressor, celery), 只要选择yes或no就行了。小编我喜欢自行配置项目，所以把它放在了第二位。  
    ```
    它的主要特色包括：
    • 默认支持SSL
    • 优化开发和生产配置
    • 默认集成django-allauth
    • 默认使用自定义的User model
    • 支持使用Anymail发送邮件
    • 支持配置使用S3或者Google Storage Cloud做云存储
    • 支持Docker，支持docker-compose
    • 默认使用postgresql
    • 支持celery
    ```

14. Django-grappelli

    官网地址：http://grappelliproject.com/  
    大家都知道django自带admin功能无比强大，学会django admin的定制与使用后就根本不需要开发自己的后台了，然而其界面却是非常简陋的。虽然xadmin很美观，但安装使用复杂。只要不是对后台界面的外观太过挑剔，使用django-grappeli可以迅速给一个看上去专业的管理后台。   
    Django-grappelli是Django的第三方应用程序，是一个 Django 的后台管理系统组件，基于 jQuery UI 和 Bootstrap用于增强Django自带的管理后台。  
    它提供了一套漂亮的管理界面，包含了各种常用的 CRUD 操作和插件支持。  
    它提供了更加漂亮的UI、更加灵活的布局、更多的小部件。  

15. Django-guardian

    官网地址：https://django-guardian.readthedocs.io/en/stable/index.html  
    在介绍Django权限管理时，提到过Django没有提供对象（Object）级别的权限控制。一个用户如果对Article模型有修改的权限，那么他将对所有Article对象有修改权限。使用django-guardian可以帮助实现对对象级别（比如某篇具体文章）的权限控制。
    
16. Django-taggit

    官网地址：https://github.com/jazzband/django-taggit  
    当在django项目中需要对任何对象（文章，用户）打上一个标签（tags）时，一个最好的方式就是使用django-taggit。可以像使用django模型自带的一个字段一样使用它快速创立多对多的关系，而且可以对的标签进行集中管理。

17. Django-ompressor

    官网地址：https://github.com/jazzband/django-compressor  
    使用django-compressor可将页面中链接的以及直接编写的JavaScript和CSS打包到一个单一的缓存文件中，以减少页面对服务器的请求数，加快页面的加载速度。当的用户很少时，可能不用关注压缩文件提升性能这些小事，但当用户非常多时，就会发现任何能够改善性能的事都是值得做的。

18. Django-reversion

    官网地址：https://github.com/etianen/django-reversion  
    如果经常使用Git对的代码进行版本控制，那么可能用不上这个包。它的作用为模型提供版本控制功能，相当于给买了杯后悔药。配置好后可以恢复已经删除掉的模型或者回滚到模型历史中的任何一点。

19. Django-activity-stream

    官网地址：https://github.com/justquick/django-activity-stream   
    Django-activity-stream是一个Django应用程序，用于记录和显示活动流，例如用户活动、社交事件和系统通知。它可以帮助开发人员更好地跟踪和展示应用程序中的活动。  
    如果要开发一个社交类网站，需要实现用户关注、收藏、点赞、用户动态等功能时，这个第三方库可以快速帮实现并提供用户的活动流。出于学习目的话，该项目的源码也是一个很好的学习对象。  
    
20. Django-anymail
    
    官网地址：https://anymail.io/  
    如果需要通过第三方邮件服务器比如Amazon SES, Mailgun, Mailjet, Postmark, SendinBlue, SendGrid和SparkPost等发送电子邮件，django-anymail可以轻松帮完成配置。个人学习时可以配置QQ邮箱发送邮件，但商用时还是需要使用专业邮件服务商。有些邮件服务商比如Mailgun每月提供一些免费邮件额度，还是不错的（非广告)。

21. Django-pure-pagination

    官网地址：https://github.com/jamespacileo/django-pure-pagination  
    Django虽然自带强大分页给功能，但当页数非常多时显示结果对用户并不友好。比如有1000页，那么1到1000每个数字都会出现页面上。使用django-pure-pagination则可以快速实现如下按范围展示的完美分页方式，值得一试。

21. Django Guardian

    官网地址：https://django-guardian.readthedocs.io/en/stable/、https://django-guardian.readthedocs.io/en/latest/ 、[GitHub地址](https://github.com/django-guardian/django-guardian)    
    Django 仅仅提供的是一种全局权限。这种简单的全局权限控制机制在很多场景下并不适用，因此需要引入另一种更细的权限机制：对象权限 (object permission)。所谓的 Object Permission 其实是一种对象颗粒度上的权限机制，它允许为每个具体对象授权 ，在 Django 中其实已经包含了 object permission 的模块，但没有具体实现，必须要使用第三方的插件完成相应的功能。django-guardian 是目前比较活跃的一个 django extension，提供了一种有效的 object permission 控制机制，与 django 原生机制一脉相承，而且能快速整合到 django-admin 中，十分推荐使用。
    具体使用参考：
    
22. Django-rules

    官网地址：https://github.com/dfunckt/django-rules    
    Django-rules是一个Django应用程序，用于定义简单的规则系统，在运行时根据这些规则授权、限制或过滤用户行为。它可以帮助开发人员更轻松地实现复杂的授权和权限管理。  
    一个小巧但是强大的应用，提供对象级别的权限管理，且不需要使用数据库。
        
23. django-scheduler

    官网地址：https://github.com/dbader/django-scheduler  
    django-scheduler是一个Django应用程序，用于管理日程安排和预约。它可以帮助开发人员更轻松地实现预约和安排功能。

24. django-import-export

    官网地址：https://django-import-export.readthedocs.io/en/latest/
    django-import-export是一个Django应用程序，用于导入和导出数据到和从多种格式，例如CSV、JSON、Excel等。它可以帮助开发人员更方便地管理数据导入和导出。
    
25. django-watchman

    官网地址：https://django-watchman.readthedocs.io/en/stable/  
    django-watchman是一个Django应用程序，用于监控Django应用程序运行状况、数据库连接、缓存、文件改变等。它可以帮助开发人员更实时地监测应用程序的状态。

26. django-redis

    官网地址：https://github.com/jazzband/django-redis  
    django-redis是一个Django应用程序，用于管理Redis数据库连接和缓存。它可以帮助开发人员更高效地处理Redis缓存和数据存储。

27. django-cors-headers

    官网地址：https://github.com/ottoyiu/django-cors-headers  
    django-cors-headers是一个Django应用程序，用于跨域资源共享，过滤cors。它可以帮助开发人员更轻松地处理跨域请求和响应。


30. pymysql - 连接mysql数据库

    官网地址：https://github.com/PyMySQL/PyMySQL  
    pymysql是Python的一个MySQL数据库接口，可以帮助开发人员更方便地连接和操作MySQL数据库。
    
31. Django-mysql

    官网地址 https://django-mysql.readthedocs.io/en/latest/index.html  
    Django-mysql是一个Django的扩展，提供了更多的MySQL数据库支持，例如存储过程、自定义查询等。它可以帮助开发人员更灵活地处理MySQL数据库。
    
32. Django-simpleui

    官网地址：https://github.com/newpanjing/simpleui  
    Django-simpleui是一个Django的扩展，提供了基于Bootstrap的后台模板和界面组件。它可以帮助开发人员更快速地创建美观的后台管理界面。

33. Django-tables2

    官网地址：https://django-tables2.readthedocs.io/en/latest/  
    Django-tables2是一个Django应用程序，用于生成数据表格和排序。它可以帮助开发人员更方便地处理数据表格的生成和显示。
    
34. Django-rest-framework-condition

    官网地址：https://github.com/caxiam/django-rest-framework-condition  
    Django-rest-framework-condition是一个Django REST框架的扩展，提供了基于条件的视图处理和响应机制。它可以帮助开发人员更轻松地控制REST视图的条件响应。
    
35. Django-jinja

    官网地址：https://github.com/niwinz/django-jinja  
    Django-jinja是一个Django应用程序，用于使用Jinja2模板引擎代替Django默认的模板引擎。它可以帮助开发人员更灵活地处理模板和视图。
    
36. Django-versionlog
    
    官网地址：https://github.com/datamade/django-versionlog  
    Django-versionlog是一个Django应用程序，用于轻松记录和显示模型记录的历史版本。它可以帮助开发人员更方便地跟踪和管理模型的历史变化。
    
37. Django-elasticsearch-dsl

    官网地址：https://django-elasticsearch-dsl.readthedocs.io/en/latest/index.html  
    Django-elasticsearch-dsl是一个Django应用程序，用于更方便地与Elasticsearch搜索引擎集成。它可以帮助开发人员更轻松地处理搜索和过滤逻辑。
    
38. Django-prometheus

    官网地址：https://github.com/korfuri/django-prometheus  
    Django-prometheus是一个Django应用程序，用于与Prometheus监控系统集成，提供更好的应用程序性能和运行状态监控。它可以帮助开发人员更实时地监测和处理应用程序运行状况。
    
39. Django-bulk-update

    官网地址：https://github.com/aykut/django-bulk-update  
    Django-bulk-update是一个Django应用程序，用于更高效地批量更新Django模型。它可以帮助开发人员更快速地更新和处理模型数据。

40. restful-Api使用
    
    官网地址 https://restfulapi.net/  
    restful-Api是一种设计和开发Web API的方式，是一种基于HTTP协议的、符合RESTful风格的Web API，可以用于前后端分离的Web开发，通过对资源的描述和HTTP动词的定义，实现对客户端的请求和响应。
    
41. openpyxl - excel\csv表格操作
    
    官网地址：https://openpyxl.readthedocs.io/en/stable/  
    openpyxl是一个用Python编写的处理Excel表格的库，可以读取和创建Excel文档，提供了对Excel的元素（如单元格，行和列）进行操作的方法。
   
42. grpcio - rpc通信的第三方库
    
    官网地址：https://grpc.io/  
    grpcio是一个通用的、高性能的RPC框架，基于Google开发的gRPC协议，支持多种编程语言和平台，在分布式系统中应用广泛。其主要作用是简化服务之间的通信，提高效率和可维护性。
   
43. simplejwt - 用于登录认证的权限

    官网地址：https://django-rest-framework-simplejwt.readthedocs.io/en/latest/  
    simplejwt是对Django REST framework的一个插件，用于提供基于JSON Web Tokens (JWT)的认证系统，可以用于开发安全的RESTful API服务。  
    具体使用参考：[7、DRF实战总结：JWT认证原理和使用及第三方库simplejwt 的详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/129980628)

44. drf-yasg
    
    官网地址：https://drf-yasg.readthedocs.io/en/stable/  
    drf-yasg是一个为Django REST framework设计的OpenAPI文档生成工具，可以自动生成API文档，提供Swagger UI和Redoc两种风格的API文档展示方式。
   
45. django-extensions
    
    官网地址：https://django-extensions.readthedocs.io/en/latest/  
    django-extensions是一个Django扩展模块，可以提供一些工具和命令，方便开发者进行Django应用的开发和调试，包括但不限于Shell命令增强、数据库命令简化、代码检查等。    
    具体使用参考：[七、Django进阶：第三方库Django-extensions的开发使用技巧详解（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130023822)

46. drf-extensions

    官网地址：https://drf-extensions.readthedocs.io/en/latest/  
    drf-extensions是对Django REST framework的一个扩展，提供了一系列常用的、易用的DRF功能增强，包括但不限于缓存、过滤、排序、搜索等。这些增强能够降低开发难度，提高WebAPI性能和可用性。  
    具体使用参考：[11、DRF实战总结：使用cache_page和第三方库drf-extensions进行缓存（附源码）](https://blog.csdn.net/zhouruifu2015/article/details/130023827)




