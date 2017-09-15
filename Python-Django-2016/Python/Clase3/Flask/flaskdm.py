from flask import Flask,url_for,request
from flask import render_template

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Esto es POST!"
    else:
        return "Hello World!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    
    return render_template("hello.html",name = name)
    
@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
    return "Post %d" % post_id

@app.route('/usuario/<username>')
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username
    
if __name__ == "__main__":
    
    app.debug = True
    app.run()
