# mypackage/
#     __init__.py
#     A/
#         __init__.py
#         spam.py
#         grok.py
#     B/
#         __init__.py
#         bar.py

# 如果模块 mypackage.A.spam 要导入同目录下的模块 grok，它应该包括的 import语句如下：
# from . import grok

# 如果模块 mypackage.A.spam 要导入不同目录下的模块 B.bar，它应该使用的 import 语句如下:
# from ..B  import bar


