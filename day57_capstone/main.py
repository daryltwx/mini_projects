from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    all_post = blog_response.json()
    return render_template("index.html", posts=all_post)


@app.route('/blog/<int:num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url=blog_url)
    all_post = blog_response.json()
    return render_template("post.html", posts=all_post, num=num)




if __name__ == "__main__":
    app.run(debug=True)
