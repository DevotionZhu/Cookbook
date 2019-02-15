import logging


logging.basicConfig(
     level=logging.ERROR,                                                     #设置告警级别为ERROR；
     format="%(asctime)s---%(lineno)s----%(name)s: %(message)s",     #自定义打印的格式；
     filename="wmm.txt",                                                    #将日志输出到指定的文件中；
     filemode="a",
)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")