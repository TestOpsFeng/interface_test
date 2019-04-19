from testcase.base_setup import BaseSetup
from interfaces.sub_account_manager import *
instance = sub_account_manager()

class sub_account_manager_test(BaseSetup):

    def test_search1(self):
        '''测试搜索'''
        data = {"lastName":"lzbss5ci6934w2"}
        result = instance.search(json=data)
        self.assertTrue(result['success'])
