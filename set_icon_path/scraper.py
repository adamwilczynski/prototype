import requests
from bs4 import BeautifulSoup


def get_soup(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


URL = r"https://som.yale.edu/story/2022/over-1000-companies-have-curtailed-operations-russia-some-remain"
html = get_soup(URL)

with open("yale_website.txt", "w") as f:
    f.write(str(html))


