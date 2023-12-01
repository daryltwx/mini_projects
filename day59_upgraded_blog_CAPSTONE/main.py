from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/71700f7542d1334e9b60"
response = requests.get(url=url)
all_posts = response.json()


@app.route('/')
def get_all_post():

    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post_pages(num):
    return render_template("post.html", posts=all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")



# Solution
# https://gist.github.com/angelabauer/f08f36c04065969f539f133f3b01832b