import requests
from Base.BaseLog import MyLog
from Base.BaseData import *
from Base.DataAlias import Relation
import os

PATH = lambda p : os.path.abspath(os.path.join(os.path.dirname(__file__),p))
R = Relation.login_crm_relation

class Login2:

    def __init__(self,data=GetData().get_data(1)):
        self.data = data[0]
        # print(self.data)
        # self.log = MyLog.get_log()
        # self.logger = self.log.get_logger()
        # self.logger("测试准备工作已就绪")

    def set_params(self):
        params = {}
        params["username"] = self.data[R["username"]]
        params["password"] = self.data[R["password"]]
        params["action"] = self.data[R["action"]]
        return params

    def requset_get(self):
        res = requests.get(url=self.data[R["url"]],params=self.set_params())
        return res.text


    def __str__(self):
        return "%s"%self.data

if __name__ == '__main__':
   print(Login2())
