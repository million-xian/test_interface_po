import logging
import time


class GetLog:
    __logger = None
    @classmethod
    def get_logger(cls):

        if cls.__logger is None:
            #创建日志器
            cls.__logger = logging.getLogger("million_logger")
            #设置日志最低级别，PS：低于此级别的日志会被忽略
            cls.__logger.setLevel(logging.INFO)
            #创建处理器(控制台输出)
            handler1 = logging.StreamHandler()
            #创建处理器（文件输出）
            handler2 = logging.FileHandler(filename="./log/{}_log".format(time.strftime("%Y%m%d_%H%M%S",time.localtime())),encoding="utf-8")
            #创建格式器，PS：格式固定
            format = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",datefmt="%Y/%m/%d/%X")

            #处理器添加格式器
            handler1.setFormatter(format)
            handler2.setFormatter(format)
            #日志器添加处理器,PS：一个日志器可以添加多个处理器
            cls.__logger.addHandler(handler1)
            cls.__logger.addHandler(handler2)

        return cls.__logger

            #设置日志信息，对应：%(message)s
            # cls.logger.debug("debug信息")
            # cls.logger.info("info信息")
            # cls.logger.warning("waring信息")
            # cls.logger.error("error信息")
            # cls.logger.critical("critical信息")