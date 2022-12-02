# Twisted

Twisted是一个基于Reactor模式的异步IO网络框架。基于Reactor模式抽象出了异步编程模型以及各种非阻塞的io模块（tcp、http、ftp等），使我们很方便地进行异步编程。

## 什么是Reactor模式

Reactor模式就是利用循环体来等待事件发生，然后处理发生的事件的模式。
Reactor主要有如下两个功能：

* 监视一系列与你I/O操作相关的文件描述符（description)。监视文件描述符的过程是异步的，也就是说整个循环体是非阻塞的；
* 不停地向你汇报那些准备好的I/O操作的文件描述符。









































[Github](https://github.com/twisted/twisted)
[参考文档](https://docs.twisted.org/en/stable/core/howto/index.html)

https://zhuanlan.zhihu.com/p/84036822