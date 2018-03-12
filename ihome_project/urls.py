#coding=utf-8
import os
from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from handlers import VerifyCode,Passport,Profile,House

urls = [
	(r"/api/profile/auth",Profile.AuthHandler),
	(r"/api/house/area",House.AreaInfoHandler),
	(r"/api/profile/avatar",Profile.AvatarHandler),
	(r"/api/logout",Passport.LogoutHandler),
	(r"/api/profile/name",Profile.NameHandler),
	(r"/api/profile",Profile.ProfileHandler),
	(r"/api/check_login",Passport.CheckLoginHandler),
	(r"/api/register",Passport.RegisterHandler),
	(r"/api/login",Passport.LoginHandler),
	(r"/api/piccode",VerifyCode.PicCodeHandler),
	(r"/api/smscode",VerifyCode.SMSCodeHandler),
	(r"/(.*)",StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__),"html"),default_filename = "index.html"))
]