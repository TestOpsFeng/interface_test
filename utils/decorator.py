from utils.logger import *
import functools
import sys
import logging
from utils.HTMLTestRunner_V import stdout_redirector

# logger = logging.getLogger('root')
# logging.basicConfig(stream=stdout_redirector)
# logger.error('Faild to get result', exc_info=True)

def url(url):
    def log(func):
        @functools.wraps(func)
        def post(*args, **kwargs):
            logger.info("请求地址：%s",  str(url))
            if kwargs.get('data',None) is not None:
                logger.info("请求数据：" + str( kwargs['data'] ))
            elif kwargs.get('json',None) is not None:
                logger.info("请求数据：" + str(kwargs['json']))
            elif kwargs.get('headers',None) is not None:
                logger.info("headers：" + str(kwargs['headers']))
            result = func(url,*args, **kwargs)
            logger.info("执行返回码：" + str(result.status_code))
            logger.info("执行结果：" + str(result.text))
            return result
        return post
    return log