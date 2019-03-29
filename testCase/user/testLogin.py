import os
import unittest
import paramunittest
# from readConfig import ReadConfig
from bs4 import BeautifulSoup
from Base.BaseLog import MyLog
from Base.BaseHttp import Http
from Base.BaseData import GetUrl,GetData

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

url_path = PATH("../../testData/interfaceURL.xml")
data_path = PATH("../../testData/userCase.xlsx")

login_data = GetData(data_path,'login_crm').get_data()
login_url = GetUrl(url_path,'login_crm').get_url()

@paramunittest.parametrized(*login_data)
class Login(unittest.TestCase):
    def setParameters(self,case_name,method,cookie,account,password,action,check,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.cookie = str(cookie)
        self.account = str(account)
        self.password = str(password).split('.')[0]
        self.action = action
        self.check = str(check)
        self.msg = str(msg)

    def description(self):
        return self.case_name

    def setUp(self):
        self.req = Http("login")
        self.url = login_url
        self.result = None
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name + "测试开始前准备")
        self.logger.info("*"*50)
        self.logger.info(self.case_name + "测试")

    def testLogin(self):
        #拼接完整的请求接口
        self.req.set_url(self.url)
        #设置header
        header = {"cookie":self.cookie}
        self.req.set_headers(header)
        #设置params
        param = {"account":self.account,"password":self.password,"action":self.action}
        self.req.set_params(param)
        #打印发送请求的方法
        self.logger.info("请求方法为 " + self.method)
        #请求
        self.result = self.req.get().text

    def tearDown(self):
        self.req = None
        self.logger.info("断言结果是 " + "%s" %self.checkResult())
        print("测试结束，结果已输出到Log")

    def checkResult(self):
        try:
            #检查返回时网页的方法
            soup = BeautifulSoup(self.result, 'lxml')
            #找网页的title
            title = soup.find("title")
            self.assertIn(self.check,title)
            return "Pass" + "---->" + self.msg
        except Exception as ex:
            self.logger.error(str(ex))
            return "False" + "--原因-->" + self.msg









if __name__ == '__main__':
    unittest.main()