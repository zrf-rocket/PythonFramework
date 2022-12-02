from twisted.internet import protocol, reactor, endpoints
# Twisted使实现自定义网络应用程序变得容易。这是一个TCP服务器，它会回显写入的所有内容
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        #self.transport.writeSequence(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

ports = "tcp:1234"
endpoints.serverFromString(reactor, ports).listen(EchoFactory())
print("server running, listening {0}".format(ports))
reactor.run()

"""
# writing servers writing clients

"""