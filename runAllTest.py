import os
import unittest
import HTMLTestRunner
from Base.BaseEmail import MyEmail
from Base.BaseLog import MyLog

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))
# print(PATH("caselist.txt"))
class AllTest:
    def __init__(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.caselist = []
        self.caselist_path = PATH("./caselist.txt")
        self.casefile_path = PATH("./testCase")
        self.email = MyEmail.get_email()

    def set_case_list(self):
        fb = open(self.caselist_path)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caselist.append(data.replace("\n",""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caselist:
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.casefile_path,pattern=case_name + ".py"
                                                           ,top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            if suit is not None:
                self.logger.info("*"*25 + "TEST START" + "*"*25)
                fp = open(PATH("./result/AllTestReport.html"),'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report'
                                                       ,description='Test Description')
                runner.run(suit)
            else:
                self.logger.info("没有测试用例，无法执行测试")
        except Exception as ex:
            self.logger.error(str(ex))
        finally:
            self.logger.info("*"*25 + "TEST END" + "*"*25)
            fp.close()
            self.email.send_email()


if __name__ == '__main__':
    aa = AllTest()
    aa.run()