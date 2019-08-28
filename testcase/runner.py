import time
import unittest
from utils.HTMLTestRunner_V import HTMLTestRunner

def create_suite():
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = '.'
    # print(test_dir)

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='*_test.py',
        top_level_dir=None
    )

    for test_case in discover:
        TestSuite.addTests(test_case)
        # print(test_case)
    return TestSuite

def report():
    now = time.strftime("%Y-%m-%d_%H_%M_%S_")
    # 需要查看每段时间的测试报告，可以这样写：
    # report_name = os.getcwd() + '\\report\\'+now+'result.html'
    report_name = '../logs/result.html'
    # print(report_name)
    return report_name



if __name__ == '__main__':
    TestSuite = create_suite()
    fp = open(report(), 'wb')
    Runner = HTMLTestRunner(
        stream=fp,
        title='Open API',
    )
    Runner.run(TestSuite)
    fp.close()
