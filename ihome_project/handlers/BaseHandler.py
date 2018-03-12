#coding=utf-8

import json
from utils.session import Session
from tornado.web import RequestHandler,StaticFileHandler


class BaseHandler(RequestHandler):

	@property
	def db(self):
		return self.application.db
	
	@property
	def redis(self):
		return self.application.redis


	def prepare(self):
		"""预解析json数据"""
		if self.request.headers.get("Content-Type","").startswith("application/json"):
			self.json_args = json.loads(self.request.body)
		else:
			self.json_args = {}

	def set_default_headers(self):
		"""设置默认json格式"""
		self.set_header("Content-Type","application/json; charset=UTF-8")

	def initailize(self):
		pass

	def write_error(self):
		pass

	def get_current_user(self):
		self.session = Session(self)
		return self.session.data


class StaticFileBaseHandler(StaticFileHandler):
	"""自定义静态类，重写加入新的功能 在用户获取html页面时设置xsrf的cookie"""
	def __init__(self,*args,**kwargs):
		super(StaticFileBaseHandler,self).__init__(*args,**kwargs)
		self.xsrf_token
