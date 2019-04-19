import unittest
from utils.HTMLTestRunner3 import HTMLTestRunner
from testcase.sub_account_manager_test import sub_account_manager_test

suite = unittest.TestLoader().loadTestsFromTestCase(sub_account_manager_test)
runner = HTMLTestRunner(
    title="OpenAPI 接口测试报告",
    description="",
    stream=open("../logs/demo.html", "wb"),
    tester='Carson'
    )
runner.run(suite)