import requests
from bs4 import BeautifulSoup

movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

movie_response = requests.get(url=movies_url)
movie_html = movie_response.text

soup = BeautifulSoup(movie_html, "html.parser")
article_tag = soup.find_all(name="h3", class_=["title"])
# print(article_tag)

movie_list = [articles.getText() for articles in article_tag[::-1]]
# print(movie_list)


with open("top_100_movie.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

