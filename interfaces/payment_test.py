from interfaces.login import bs_headers
import requests
from utils.decorator import url
'''
把url和headers封装好，作为一个接口调用方法，testcase传入时，只关注传入的data/json
'''

host = "http://test.shop.buckydrop.com/api"

@url(host + "/buckyshop/order/merchant/refund-confirm")
def refund_confirm(url = None , data=None, json=None, **kwargs):
    '''搜索接口'''
    r = requests.post(url, json=json, headers=bs_headers)
    return r