'''
import flask,json
from flask import request


#创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)

#server.route()可以将普通函数转变为服务　登录接口的路径、请求方式
@server.route('/login',methods=['get','post'])
def login():
    #获取通过url请求传参的数据
    username = request.values.post('test')
    #获取url请求传的密码，明文
    pwd=request.values.get('pwd')
    #判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if test:
        if test=='test_data':
            resu={'code':200,'message':'测试成功'}
            return json.dumps(resu,ensure_ascii=False)#将字典转换为Json串，json是字符串
        else:
            resu={'code':-1,'message':'测试信息错误'}
            return json.dumps(resu,ensure_ascii=False)

    else:
        resu={'code':1001,'message':'参数不能为空'}
        return json.dumps(resu,ensure_ascii=False)

if __name__== '__main__':
    server.run(debug=True,port = 443,host='0.0.0.0')#指定端口,host,0.0.0.0代表不管几个网卡，任何ip都可访问


'''

from http.server import BaseHTTPRequestHandler
import pymysql
import json
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        
        timeout = 10
        connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-200bcff3-cjy114514-5fc0.h.aivencloud.com",
        password="AVNS_TI
        
        
        #json_data = json.dumps(data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(b'ok')
        
        
        return
    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body2=json.loads(body)
        
        
        
        theurn=body2['usernm']
        thepsw=body2['psw']
        
        #self.wfile.write(b'111')
        '''
        db = pymysql.connect(host='mysql2.sqlpub.com',port=3307,user='hyacine',password='To3gM5etInLYlIMI',database='hyacine',charset='utf8')
        
        cursor = db.cursor()
        
        cursor.execute("SELECT thepassword FROM users WHERE `theusername`= %s ;" % theurn)
        rtrn = cursor.fetchone()
        
        ''''
        #data = {"connect":"true"}

        
        if rtrn==thepsw:
            data={"rslt":"Ok!"}
        else:
            data={"rslt":"No such user!"}
        
        json_data = json.dumps(data).encode('utf-8')
        #json_data = json.dumps(body2).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json_data)
        cursor.close()
        db.close()
        return

