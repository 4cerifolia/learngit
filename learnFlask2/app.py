from flask import Flask, render_template, request


app = Flask(__name__)  # 创建flask应用


# http://127.0.0.1:5000
# http://127.0.0.1:5000/index
@app.route('/index')  # 路由
def index():
    return render_template("index.html")


# http://127.0.0.1:5000/search
@app.route('/search')
def search():
    data = request.args.get('wd')
    print(data)
    data1 = "4cerifolia's mida"
    data2 = "4cerifolia's miga"
# 数据集中根据关键字搜索数据
    return render_template('search.html', v1=data1, v2=data2)


# http://127.0.0.1:5000/login
@app.route('/login')  # 路由
def login():
    return "登录"


if __name__ == '__main__':
    app.run()
