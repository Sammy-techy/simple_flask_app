from flask import Flask
from flask import render_template, request, redirect
from models.database import db, init_db
from models.friendform import Friendform
from models.posts import Posts


app = Flask(__name__)


#this is to get the db initialized before program execution
@app.before_first_request
def init():
    init_db()


@app.route('/')
def index():
    friendform = Friendform.query.all()
    return render_template('index.html', nav='data', friendform=friendform, pagetitle="Add A New Friend", message="WELCOME TO SAMMY's BLOG")


@app.route('/add_friend', methods=['GET', 'POST'])
def add_friend():
    if request.method=="POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        good = Friendform(first_name=first_name, last_name=last_name)
        db.session.add(good)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_friend.html")


@app.route("/comment", methods=['GET', 'POST'])
def comment():
    if request.method == "POST":
        title = request.form.get('title')
        comment = request.form.get('comment')
        all = Posts(comment=comment, title=title)
        db.session.add(all)
        db.session.commit()
        return redirect("/forum")
    return render_template("comment.html")

@app.route("/forum")
def display():
    posts = Posts.query.all()
    return render_template("forum.html", nav=all, posts=posts)




def datetimeformat(value):
    return value.strftime('%Y-%m-%d %H:%M:%S')
app.jinja_env.filters['datetime'] = datetimeformat


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(debug=True, port=200)

