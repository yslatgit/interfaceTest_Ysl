import requests
from readConfig import ReadConfig
from Base.BaseLog import MyLog
import os

PATH = lambda p : os.path.abspath(os.path.join(os.path.dirname(__file__),p))
config_http = ReadConfig("HTTP").readconfig()

class Http:

    def __init__(self,login):
        global scheme,host,port,timeout
        scheme = config_http['scheme']

        if login == "login":
            host = config_http['baseurl_login']
        elif login == "list":
            host = config_http['baseurl_list']

        port = config_http['port']
        timeout = config_http['timeout']
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.header = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self,url):
        self.url = scheme + "://" + host + url
        self.logger.info("请求的地址为：" + self.url)

    def set_headers(self,header):
        self.headers = header
        self.logger.info("请求的Header为：" + "%s"%self.headers)

    def set_params(self,param):
        self.params = param
        self.logger.info("请求的Params为：" + "%s"%self.params)

    def set_data(self,data):
        self.data = data
        self.logger.info("请求的Data为：" + "%s" %self.data)

    def set_files(self,filename):
        self.files = {'file':open(filename,'rb')}

    def get(self):
        try:
            response = requests.get(self.url,headers=self.headers,params=self.params,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,params=self.params,data=self.data,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None


    def post_file(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

if __name__ == '__main__':
    http_request = Http()
    http_request.set_url("ysl")