from .users import user_bp
from .main import main



DEFAULT_BLUEPRINT = (
    (user_bp, '/users'),
    (main, '/main')
)


# 封装配置蓝本的函数
def init_app(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
