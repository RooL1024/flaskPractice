from flask import *

app = Flask(__name__)

# 路由
# @app.route("/")
# def index():
#     return "hello"
# @app.route("/user/<username>")
# def user(username):
#     return "welcome" +username

app = Flask(__name__)

#重定向练习
# @app.route('/')
# def index():
#     print(url_for('index'))
#     print(url_for('do_login', name='TengTengCai'))
#     print(url_for('get_user', user_id='1234'))
#     print(url_for('get_grade', grade_id='0987'))
#     return 'Index Page'
#
# @app.route('/login/')
# def do_login():
#     return 'Login Method'
#
# @app.route('/user/<user_id>/')
# def get_user(user_id):
#     return 'User ID is %s' % str(user_id)
#
# @app.route('/grade/<int:grade_id>/')
# def get_grade(grade_id):
#     return 'Grade ID is %s type is %s' % (str(grade_id), type(grade_id))
@app.route("/user/<test>")
def user(test):
    return "you are test" + test
# 重定向
# @app.route("/<username>")
# def login(username):
#     if username == "renle":
#         return "hello"
#     return redirect(url_for("user",test = username))
#
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return "hello get"
    return "post"

app.run(host="0.0.0.0",port=8080,debug=True)