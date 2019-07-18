#!/usr/bin/env python

""" """

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import db


# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app
app = create_app(config_name)

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)


# 添加迁移脚本命令,命令行输入python manage.py db migrate
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    # 启动Manger实例接收命令行中的命令
    manager.run()
