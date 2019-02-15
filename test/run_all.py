import unittest
from config.config import *

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover("./")
