from interfaces.login import *
from utils.decorator import log


class base():
    @log
    def post(self,url, data=None, json=None, **kwargs):
        # logger.info("请求地址：" + str(url))
        # if data is not None:
        #     logger.info("请求数据：" + str(data))
        # elif json is not None:
        #     logger.info("请求数据：" + str(json))
        # elif kwargs is not None:
        #     logger.info("其他：" + str(kwargs))
        result = requests.post(url, data=None, json=None, **kwargs)
        # logger.info("执行返回码：" + str(result.status_code))
        return result




