from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/do/register")
def do_register():
    print(request.args)
    username = request.args.get('user')
    password = request.args.get('pwd')
    gender = request.args.get('sex')
    city = request.args.get('city')
    hobby = request.args.getlist('hob')
    more = request.args.get('more')
    line = '{}|{}|{}|{}|{}|{}\n'.format(username, password, gender, city, hobby, more)

    file_object = open("db.txt", mode='a', encoding='utf-8')
    file_object.write(line)
    file_object.close()
    return redirect('/user/list')

@app.route('/user/list')
def user_list():
    datalist = []
    file_object = open("db.txt", mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        datalist.append(line)
    file_object.close()
    return render_template('user_list.html',v1 = datalist)

@app.route("/login")
def login():
    pass


if __name__ == "__main__":
    app.run()
