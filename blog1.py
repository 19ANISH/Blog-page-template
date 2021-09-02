from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

#this is the proper blog website
#we have done the change in html file and copied files in static folder

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")

#we don't have to change the source which are from https:// these are online source so it doesn't cause much error to us

if __name__=='__main__':
    app.run(debug=True)
