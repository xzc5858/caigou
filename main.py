from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import RequestHandler
import tornado.template
import sys

define("port", default=8888, type=int, help="run on the given port")
define("domain", default=[], type=str, help="run on the given domain", multiple=True)
# define("static_path", default="/statics", type=str)
settings = {
    'template_path': 'Templates',  # html文件
    'static_path': 'statics',  # 静态文件（css,js,img）
    'static_url_prefix': '/statics/',  # 静态文件前缀
    'cookie_secret': 'suoning',  # cookie自定义字符串加盐
    # 'xsrf_cookies': True,          # 防止跨站伪造
    # 'ui_methods': mt,              # 自定义UIMethod函数
    # 'ui_modules': md,              # 自定义UIModule类
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        import os
        scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
        ls = open(scriptPath + '/list.txt', 'r', encoding="utf-8")
        myls = ls.read()
        self.render("index.html", list_info=myls.split('\n'))

    def post(self):
        import os
        scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
        ls = open(scriptPath + '/list.txt', 'a++', encoding="utf-8")
        myls = ls.read()
        self.render("index.html", list_info=myls.split('\n'))


class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('sfds')
        # loader = tornado.template.Loader("/Templates")
        # loader.load('./templates/list.html', '/index.html')
        # self.write("how are you")


class AdminHandler(RequestHandler):
    def get_login_url(self):
        return '/login'


class LoginHandler(RequestHandler):
    def get(self):
        if self.get_current_user():
            self.redirect('/')
            return
        self.render('login.html')

    # def post(self):
    #     if self.get_current_user():
    #         raise tornado.web.HTTPError(403)
    # check username and password
    # if success:
    #     self.redirect(self.get_argument('next', '/'))


class ChartsHandler(RequestHandler):
    def get(self):
        self.render('charts.html')


Handlers = [("/", MainHandler), ("/list", ListHandler), ("/charts", ChartsHandler)]

if __name__ == '__main__':
    # tornado.options.parse_command_line()  # 如果命令行没有传值，则使用默认值
    # tornado.options.parse_config_file("./config")  # 引用config文件里面的值，文件内容：port=8006
    # print(tornado.options.options.port)
    # ccgpsx = ccpgsx_spider()
    # ccgpsx.show_list()
    # app = tornado.web.Application(Handlers, login_url='/login', **settings)
    # app.listen(options.port)
    # IOLoop.current().start()
    # sockets = tornado.netutil.bind_sockets(options.port)
    # tornado.process.fork_processes(9)
    # server = HTTPServer(Handlers)
    # server.add_sockets(sockets)
    # IOLoop.current().start()
