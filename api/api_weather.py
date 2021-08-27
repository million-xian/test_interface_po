import api
import requests
from tool.get_log import GetLog

log = GetLog.get_logger()
class ApiWeather:
    #1.初始化
    def __init__(self):
        #1.手机归属地查询接口url
        self.url_phone_address = api.host+"/mobile/get"
        log.info("初始化手机归属地查询接口url:{}".format(self.url_phone_address))
        #2。天气查询接口uel
        self.url_weather_querry = api.host+"/simpleWeather/query"
        log.info("初始化天气查询接口url:{}".format(self.url_weather_querry))

    #2.手机归属地查询接口
    def api_weather_phone_address(self,phone,key):
        data = f"phone={phone}&key={key}"
        log.info("正在调用手机归属地查询接口，请求数据为：{}".format(data))
        return requests.get(self.url_phone_address,params=data)

    #3.查询天气接口
    def api_weather_querry(self,city,key):
        data = f"city={city}&key={key}"
        log.info("正在调用天气查询接口，数据为：{}".format(data))
        return requests.get(self.url_weather_querry,params=data)
