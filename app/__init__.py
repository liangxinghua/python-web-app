# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# 初始化flask 应用
app = Flask(__name__)
app.config.from_object("config")

# 初始化数据库
db = SQLAlchemy(app)

# 初始化登录
lm=LoginManager()
lm.setup_app(app)

from app import views, models,error_handler,filter,decorator

'''
    1.Flask 程序对象的创建必须在 __init__.py 文件里完成， 这样我们就可以安全的导入每个模块，而 __name__ 变量将会被分配给正确的包。
    2.所有（上面有 route() 装饰器的那些）视图函数必须导入到 __init__.py 文件。此时，请通过模块而不是对象本身作为路径导入这些视图函数。
    必须在应用对象创建之后 导入视图模块。

'''
'''
循环导入:
每个 Python 程序员都会讨厌他们，而我们反而还添加了几个进去:
循环导入(在两个模块相互依赖对方的时候，就会发生循环导入)。在这里 views.py 依赖于 __init__.py。
通常这被认为是个不好的主意，但是在这里实际上不会造成问题。之所以如此，是因为我们实际上没有在 __init__.py 里使用这些视图，
而仅仅是保证模块被导入了。并且，我们是在文件的结尾这么做的。

'''