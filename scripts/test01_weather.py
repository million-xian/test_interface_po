import pytest

from tool.tool import *
from api.api_weather import ApiWeather
from tool.get_log import GetLog
from tool.read_yaml import read_yaml

log = GetLog.get_logger()

class TestWeather:
    #1.初始化
    def setup_class(self):
        self.weather = ApiWeather()

    #2.测试手机号归属地接口
    @pytest.mark.parametrize("phone,key",read_yaml("./data/testcase2.yaml"))
    def test01_weather_phone_address(self,phone,key):
        respone = self.weather.api_weather_phone_address(phone,key)
        try:
            #断言
            Tool.common_assert(respone,"Return Successd!")
            #提取手机号归属地
            Tool.common_address(respone)
        except Exception as error:
            #抛异常
            log.error("断言失败，失败信息：{}".format(error))
        print(api.datas)

    #3.测试天气接口
    @pytest.mark.parametrize("city,key",read_yaml("./data/testcase3.yaml"))
    def test01_weather_querry(self,city,key):
        r = self.weather.api_weather_querry(city,key)
        try:
            #断言
            Tool.common_assert(r)
        except Exception as error:
            #写日志
            log.error("断言失败，失败信息：{}".format(error))
            #抛异常
            raise