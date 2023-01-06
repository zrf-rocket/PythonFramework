# celery
### 简介
Celery 是一个简单，灵活且可靠的分布式系统，可以处理大量消息，同时为操作提供维护该系统所需的工具。这是一个任务队列，着重于实时处理，同时还支持任务调度。

任务队列是一种跨线程、跨机器工作的一种机制。

任务队列中包含称作任务的工作单元。有专门的工作进程持续不断的监视任务队列，并从中获得新的任务并处理。

Celery 通过消息进行通信，通常使用broker在 clients 和 workers 之间进行调解。要启动一个任务，客户端会在队列中放入一条消息，然后经纪人将消息传递给工人。

一个 Celery 系统可以由多个 worker 和 broker 组成，从而实现高可用性和横向扩展。

Celery 是用 Python 编写的，但协议可以用任何语言实现。除了 Python 之外，还有 Node.js 的 Node-celery，PHP 客户端，golang 的 gocelery 和 Rust 的 rusty-celery。



### 安装
pip install celery




