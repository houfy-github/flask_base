from app import create_app
import os

# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
