from testcase.base_setup import BaseSetup
from interfaces.payment_test import refund_confirm


class payment_test(BaseSetup):

    def test_refund_confirm(self):
        '''测试搜索'''
        json = {
            "confirmResult": 7,
            "orderCode": "19OHr5C0KzX8L1WiT8CmGb",
            "refuseReason": "不给退款，哈哈哈哈，霸王条款！"
        }
        result = refund_confirm(json=json)
        print(result.text)
