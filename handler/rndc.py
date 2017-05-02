#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler
from tornado.web import authenticated as Auth
from modules.rndc import rndc


class StatusHandler(BaseHandler):

    @Auth
    def get(self):
        ops = self.get_options()
        r = rndc(ops['rndc_host']['value'], ops['rndc_port']['value'], ops['rndc_algo']['value'],ops['rndc_secret']['value'])
        status = r.get_status_original()
        return self.jsonReturn({'code': 0, 'msg': 'Success', 'data': status})


class ReloadHandler(BaseHandler):
    @Auth
    def get(self):
        return self.jsonReturn({'code': 0, 'msg': 'Success'})


class ReconfigHandler(BaseHandler):
    @Auth
    def get(self):
        return self.jsonReturn({'code': 0, 'msg': 'Success'})

