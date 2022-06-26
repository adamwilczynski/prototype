import json
from collections import defaultdict

from bs4 import BeautifulSoup

with open("yale_website.txt") as f:
    html = BeautifulSoup(f.read(), "html.parser")

database = defaultdict(dict)
name = None

for grade, table in zip("fdcba", html.find_all("table")):
    for row in table.find_all("tr", {"class": "table__row"}):
        name, action, industry, country = (item.text for item in row.find_all("td", {"class": "table__cell"}))

        name = name.lower()

        database[name] = {
            "action": action,
            "country": country,
            "grade": grade,
        }


    # print(name, action, industry, country)

with open("database.json", "w") as outfile:
    json.dump(database, outfile)