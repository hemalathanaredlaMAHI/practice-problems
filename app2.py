from flask import Flask, render_template
app=Flask(__name__)

# creating main route, with name and dynamic name paths 

@app.route("/")
def index():
    name="Default"
    return render_template("sample1.html", n=name)

@app.route("/<name>")
def sample(name):
    hobbies=["playing Cricket", "Listening to Music", "Watching Movies"]
    return render_template("sample1.html", n=name, h=hobbies)

# @app.route("/<int:num>")
# def sample1(num):
#     return render_template("sample1.html", n=num)
