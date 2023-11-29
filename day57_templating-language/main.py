from flask import Flask, render_template
import datetime
import requests


app = Flask(__name__)


now_year = datetime.date.today().year

@app.route('/')
def home():
    return render_template("index.html", year=now_year)

@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    return render_template("guess.html", year=now_year, gender=gender, name=name.title(), age=age)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    all_post = blog_response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)


