# coding:utf-8
# 依赖库：requests
import requests

class Dingtalk(object):
    def __init__(self, corpid, corpsecret):
        self.__params = {
            'corpid': corpid,
            'corpsecert': corpsecret
        }
        self.__token = self.__get_token()
        self.url_get_token = 'https://oapi.dingtalk.com/gettoken'
        self.url_get_dept_list = 'https://oapi.dingtalk.com/department/list'
        self.url_get_dept_detail = 'https://oapi.dingtalk.com/department/get'
        self.url_create_dept = 'https://oapi.dingtalk.com/department/create'
        self.url_delete_dept = 'https://oapi.dingtalk.com/department/delete'
        self.url_get_user_id_by_unionid = 'https://oapi.dingtalk.com/user/getUseridByUnionid'
        self.url_get_user_detail = 'https://oapi.dingtalk.com/user/get'
        self.__token_params = {
            'access_token': self.__token
        }

    def __raise_error(self, res):
        raise Exception('error code: %s,error message: %s' % (res.json()['errcode'], res.json()['errmsg']))

    def __get_token(self):
        res = requests.get(self.url_get_token, params=self.__params)
        try:
            return res.json()['access_token']
        except:
            self.__raise_error(res)

    def get_dept_list(self):
        res = requests.get(self.url_get_dept_list, params=self.__token_params)
        try:
            return res.json()['department']
        except:
            self.__raise_error(res)

    def get_dept_detail(self, dept_id):
        params = self.__token_params
        params.update({'id': dept_id})
        res = requests.get(self.url_get_dept_detail, params=params)
        try:
            return res.json()
        except:
            self.__raise_error(res)

    def create_dept(self, name, parentid, orderid, createdeptgroup=False):
        payload = self.__token_params
        payload.update({
            'name': name,
            'parentid': parentid,
            'orderid': orderid,
            'createDeptGroup': createdeptgroup,
        })
        res = requests.post(self.url_create_dept, data=payload)
        try:
            return res.json()['id']
        except:
            self.__raise_error(res)

    def delete_dept(self, dept_id):
        params = self.__token_params
        params.update({'id': dept_id})
        res = requests.get(self.url_delete_dept, params=params)
        try:
            return res.json()['errcode']
        except:
            self.__raise_error(res)

    def get_userid_by_unionid(self, unionid):
        params = self.__token_params
        params.update({'unionid': unionid})
        res = requests.get(self.url_get_user_id_by_unionid, params=params)
        try:
            return res.json()['userid']
        except:
            self.__raise_error(res)

    def get_user_detail(self, userid):
        params = self.__token_params
        params.update({'userid': userid})
        res = requests.get(self.url_get_user_detail, params=params)
        try:
            return res.json()
        except:
            self.__raise_error(res)




