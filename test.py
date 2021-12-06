from flask import Flask,url_for,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/user/<username>')
def user(username):
    return 'Welcome:'+username

@app.route('/article/<int:id>')
def article(id):
    #进行数据库查询--》返回到python--》return 前台
    return "这是第%s篇文章"%id
@app.route('/path/<path:index>')
def path(index):
    return "您输入的路径为%s" %index

@app.route('/login/<username>')
def login(username):
    if username != "":
        return redirect(url_for('user',username=username))
    else:
        return '您还没有登录'

@app.route('/login1',methods=['GET','POST'])
def login1():
    if request.method == 'POST':
        return '尝试登录'

    return '访问登录页面'

app.run(host='0.0.0.0',port=8000,debug=True)