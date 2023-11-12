from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(name=["span", "a"], class_="titleline")

# if article_tag:
#     article_tag = article_tag[0]
#     article_text = article_tag.getText()
#     article_link = article_tag.get("href")
#     print(article_link)


name = soup.select(".titleline")[0].find_all(name="a")[0]
print(name.get("href"))




# soup = BeautifulSoup(yc_web_page, "html.parser")

# article_texts = []
# article_links = []
# for article in name:
#     article_link = name.get("href")
#     article_links.append(article_link)
#     article_text = name.getText()
#     article_texts.append(article_text)
#
# print(article_texts)
# print(article_links)
#article_upvote = soup.find_all(name="span", class_="score").getText()
#print(article_upvote)
# article_upvote = soup.select(".subline")[0].find(class_="score", id="score_38232767").getText()
# print(article_upvote)


# article_tag = soup.find(name="a", class_="storylink")
# article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span, class_="score").getText())