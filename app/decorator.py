# -*- coding:utf-8 -*-
from flask import request, render_template
from functools import wraps



def templated(template=None):

    '''
    模板装饰器:url:http://docs.jinkan.org/docs/flask/patterns/viewdecorators.html
    如果没有模板名被指定，那么他会使用 URL 映射的最后一部分， 然后将点转换为反斜杠，最后添加上 '.html' 作为模板的名字。当装饰器包装的函数返回，返回的字典就会被传递给模板渲染函数。
    如果 None 被返回了，那么相当于一个空的字典。如果非字典类型的对象被返回，函数将照原样将那个对象再次返回。这样您就可以继续使用重定向函数或者返回简单的字符串了
    '''

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)

        return decorated_function

    return decorator
