import os
from flask import Flask, render_template
from app.config import config
from app import extensions

# 建立一个基础路径，用于静态文件static，templates的调用
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


# 将创建app的动作封装成一个函数
def create_app(config_name='default'):
    """
    初始化，创建app
    """

    from app import services
    from app import routes
    from app import models

    # 建立静态文件static，templates的路径
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    # 创建app实例对象
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    # 加载配置
    # app.config.from_object(config.get(config_name) or 'default')
    app.config.from_object(config.get(config_name))
    # 执行额外的初始化
    config.get(config_name).init_app(app)

    # 设置debug=True,让toolbar生效
    # app.debug=True

    # 加载扩展
    extensions.init_app(app)

    # 配置蓝本
    routes.init_app(app)

    # 配置全局错误处理
    config_errorhandler(app)

    models.init_app(app)

    services.init_app(app)

    # 返回app实例对象
    return app


def config_errorhandler(app):
    # 如果在蓝本定制，则只针对蓝本的错误有效。
    # 可以使用app_errorhandler定制全局有效的错误显示
    # 定制全局404错误页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html', e=e)
