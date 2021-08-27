import api
from tool.get_log import GetLog

log = GetLog.get_logger()
class Tool:
    #1.断言
    @classmethod
    def common_assert(cls,respone,reason="查询成功!"):
        log.info("正在调用公共断言方法")
        assert 0 == respone.json().get("error_code")
        assert reason == respone.json().get("reason")

    #2。提取手机号归属地
    @classmethod
    def common_address(cls,respone):
        phone_address = respone.json().get("result").get("city")
        api.datas["address"]=phone_address
        log.info("提取手机号归属地：{}".format(phone_address))

