from flask import Blueprint, render_template


main = Blueprint('main', __name__)

# 视图函数
@main.route('/regist/')
def regist():
    """注册
    """
    return render_template('register.html')

# 视图函数
@main.route('/login/')
def login():
    """ login
    """
    return render_template('login.html')
