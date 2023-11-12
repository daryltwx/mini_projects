from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

# Soup is like a class now.
soup = BeautifulSoup(contents, "html.parser")
# String of the title
# print(soup.title.string)

# Better visualisation
#print(soup.prettify())

# First anchor tag
#print(soup.a)


# Get all the anchor / p tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    ## Get all the tag links.
    # print(tag.get("href"))
    pass


heading = soup.find(name="h1", id="name")
#print(heading)


section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.get("class"))

# Drill down to the particular element
company_url = soup.select_one(selector="p a")
print(company_url)

# Id tag
name = soup.select_one(selector="#name")
print(name)

# Class of heading
headings = soup.select(".heading")
print(headings)

for heading in headings:
    print(heading.getText())