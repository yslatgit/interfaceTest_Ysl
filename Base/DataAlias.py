#coding:utf-8

"""数据---下标  关系"""

class Relation:
    login_crm_relation={
        "case_name":0,
        "method":1,
        "url":2,
        "cookie":3,
        "username":4,
        "password":5,
        "action":6,
        "check":7,
        "msg":8,
    }

if __name__ == '__main__':
    print(Relation.login_crm_relation)