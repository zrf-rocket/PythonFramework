from tornado.websocket import WebSocketHandler, websocket_connect


# 注意：WebSocket可以共用Http对端口的监听和路由的配置。
class MyWebSocketHandler(WebSocketHandler):
    # 保存连接的用户，用于后续推送消息
    connect_users = set()

    def ping(self, data: bytes = b"") -> None:
        pass

    def open(self):
        # 当一个WebSocket连接建立后被调用
        # 打开连接时将用户保存到connect_users中
        print("websocket opender {}".format(self.connect_users))
        self.connect_users.add(self)

    def on_message(self, message):
        # 当客户端发送消息message过来时被调用，注意此方法必须被重写。
        print("{} send websocket msg.....".format(self.request.remote_ip))
        send_msgs(msg=message)

    def on_close(self) -> None:
        # 当WebSocket连接关闭后被调用。
        # 关闭连接时将用户从connect_users中移除
        print("websocket close.....")
        self.connect_users.remove(self)

    def check_origin(self, origin: str) -> bool:
        # 此处用于跨域访问
        return True

    @classmethod
    def send_demand_updates(cls, message):
        # 使用@classmethod可以使类方法在调用的时候不用进行实例化
        # 给所有用户推送消息（此处可以根据需要，修改为给指定用户进行推送消息）
        print(cls.connect_users)
        for user in cls.connect_users:
            # 向客户端发送消息messagea，message可以是字符串或字典（字典会被转为json字符串）。若binary为False，则message以utf8编码发送；二进制模式（binary=True）时，可发送任何字节码。
            user.write_message(message)


def send_msgs(msg: str = "被调用"):
    """发送字符串"""
    print("send msg......{}".format(msg))


def send_numbers(num: int = 11):
    """发送数字"""
    print("send numbers.....{}".format(num))


def send_ws():
    """发送websocket信息"""
    print("websocket msg.....")


if __name__ == '__main__':
    # 向已连接的客户端发送消息
    MyWebSocketHandler.send_demand_updates({"inventoryCount": 1, "msg": "hello"})
    MyWebSocketHandler.send_demand_updates("字符串")
