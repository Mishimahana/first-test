#coding=utf-8
import os

#日志配置 路径 等级
log_path = os.path.join(os.path.dirname(__file__),"logs/log") 
log_level = "debug"


#Application配置参数
settings = dict(
        static_path = os.path.join(os.path.dirname(__file__),"static"),
        cookie_secret = "LKLZYUkLRumYkxl21g0GlEMhSX0CHEFblCS1PzN28tA=",
        #xsrf_cookies = True,
        debug = True
    )

#mysql配置
mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password="123qwe"
)

#redis配置
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="