from testcase.base_setup import BaseSetup
from interfaces.sub_account_manager import search

class sub_account_manager_test(BaseSetup):

    def test_search1(self):
        '''测试搜索'''
        json = {"lastName":"123"}
        result = search(json=json)
        print(result.text)

