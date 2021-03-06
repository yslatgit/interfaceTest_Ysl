import requests
from readConfig import ReadConfig
import os
from xlrd import open_workbook
from xml.etree import ElementTree
from Base.BaseLog import MyLog
import json

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))

class GetUrl:
    """从xml读取接口信息"""
    def __init__(self,path,name):
        self.path = path
        self.name = name
        self.url_list = []

    def get_url(self):
        tree = ElementTree.parse(self.path)
        for u in tree.findall('url'):
            url_name = u.get('name')
            if url_name == self.name:
                for c in u.getchildren():
                    self.url_list.append(c.text)
        url = '/'+'/'.join(self.url_list)
        return url

class GetData:
    """从EXCEL获取测试数据的方法，初始化时增加默认参数"""
    def __init__(self,path=PATH('../testData/userCase.xlsx'),sheet_name='login_crm'):
        self.path = path
        self.sheet_name = sheet_name
        self.cls = []

    def get_data(self,n=-1):
        """根据N的值获取测试用例"""
        file = open_workbook(self.path)
        sheet = file.sheet_by_name(self.sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            #去掉字段名
            if sheet.row_values(i)[0] != u'case_name':
                if n == -1:
                    self.cls.append(sheet.row_values(i))
                if n == i:
                    self.cls.append(sheet.row_values(i))
        return self.cls

if __name__ == '__main__':
    # path1 = PATH("../testData/interfaceURL.xml")
    # print(GetUrl(path1,"login").get_url())
    #
    # path2 = PATH("../testData/userCase.xlsx")
    # r = GetData(path2,'login_crm').get_data()
    # print(str(r[0][3]).split(".")[0])
    print(GetData().get_data(1))


