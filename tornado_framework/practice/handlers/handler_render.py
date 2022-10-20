import settings
import tornado.web as web
from tornado import gen


def get_login_url(request):
    return 'http://%s/tornado/login/' % request.host


def get_websocket_url(request):
    return 'ws://%s/tornado/socket.io/' % request.host


class IndexHandler(web.RequestHandler):
    def get(self):
        is_token = 0

        ctx = {
            'static_url': settings.STATIC_URL,
            'is_token': is_token,
            'version': settings.STATIC_VERSION,
            'over_time': settings.OVERTIME,
            'SETTINGS': settings,
            'WEBSOCKET_URL': get_websocket_url(self.request),
        }
        self.render("index.html", **ctx)
