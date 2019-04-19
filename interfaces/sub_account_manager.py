from interfaces.login import *
from interfaces.base import base

class sub_account_manager(base):

    def search(self,*,json):
        '''搜索接口'''
        url = get_api("search_url")
        r = self.post(url, json=data, headers=headers)
        return r.json()