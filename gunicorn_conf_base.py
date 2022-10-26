# gunicorn.conf

bind = "0.0.0.0:80"  # 监听所有ip的80端口
workers = 4  # 启用4个线程。一般workers = CPU核心数+1就比较合适
backlog = 2048
pidfile = "./gunicorn.pid"
accesslog = "./access.log"  # 用户访问日志位置
errorlog = "./error.log"  # 程序异常日志位置
timeout = 30
debug = False
capture_output = True
