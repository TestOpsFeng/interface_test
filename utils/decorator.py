from utils.logger import *
import functools

def log(func):
    @functools.wraps(func)
    def post(*args, **kwargs):
        logger.info("请求地址：" + str(args[1]))
        if kwargs.get('data',None) is not None:
            logger.info("请求数据：" + str( kwargs['data'] ))
        elif kwargs.get('json',None) is not None:
            logger.info("请求数据：" + str(kwargs['json']))
        elif kwargs.get('headers',None) is not None:
            logger.info("其他：" + str(kwargs['headers']))
        result = func(*args, **kwargs)
        logger.info("执行返回码：" + str(result.status_code))
        return result
    return post