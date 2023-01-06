# 最简单的twisted程序
def twisted_func():
    print("this is twisted reactor loop")

# twisted是实现Reactor模式，因此它必然会有一个对象来代表这个reactor或者说是事件循环，而这正是twisted的核心。
# 引入reactor
from twisted.internet import reactor

# callWhenRunning 传给一个想调用的函数的引用来实现twisted_func函数的调用。必须在启动reactor之前完成这些工作。
reactor.callWhenRunning(twisted_func)
# 由于Twisted循环是独立于我们的代码，业务代码与reactor核心代码的绝大多数交互都是通过使用Twisted的APIs回调我们的业务函数来实现。

print("twisted reactor server staring...")
# 启动事件循环。Twisted的reactor只有通过调用reactor.run()来启动。
reactor.run()

# 运行服务后，这里并不是一个在不停运行的简单循环。
# 这个循环体不会带来任何CPU性能损失。
# reactor循环是在其开始的进程中运行，也就是运行在主进程中。
# 一旦启动，就会一直运行下去。reactor就会在程序的控制下（或者具体在一个启动它的线程的控制下）
# 并不需要显式的创建reactor，只需要引入即可。

# 在Twisted中，reactor是Singleton（也是一种模式），即在一个程序中只能有一个reactor，并且只要引入它就相应地创建一个。
# 上面引入的方式这是twisted默认使用的方法，twisted还有其它可以引入reactor的方法。  可以使用twisted.internet.pollreactor中的系统调用来poll来代替select方法。
