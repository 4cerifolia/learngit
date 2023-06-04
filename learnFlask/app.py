from flask import Flask, render_template
import random
app = Flask(__name__)# 创建flask应用

# http://127.0.0.1:5000

# http://127.0.0.1:5000/index
@app.route('/index')# 路由
def index():
    name = random.choice(['4cerifolia', 'garmamamamama', 'yellow green', 'lululemon'])
    #return "你<h1 style='color:green;'>好</h1>"
    return render_template("index.html", n1 = name)


    # html 超文本编辑
# CSS 样式
# GS 动态


# http://127.0.0.1:5000/login
@app.route('/login')# 路由
def login():
    return "登录"

if __name__ == '__main__':
    app.run()
