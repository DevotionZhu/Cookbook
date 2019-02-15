#_*_coding:utf-8_*_
import logging
from logging import handlers


logger = logging.getLogger(__name__)
log_file = "timelog.log"

fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3) #filename定义将信息输入到指定的文件，
# when指定单位是s(秒),interval是时间间隔的频率,单位是when所指定的哟（所以，你可以理解频率是5s）；backupCount表示备份的文件个数，我这里是指定的3个文件。


formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.warning("test1")
logger.warning("test2")
logger.warning("test3")
logger.warning("test4")