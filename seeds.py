import connect
from datetime import datetime
import json
from models import Author, Quote
from typing import Iterable


file_name_authors = "authors.json"
file_name_qoutes = "qoutes.json"


def input_(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


some_iterable: Iterable[dict] = input_(file_name_authors)
for i in some_iterable:
    Author(
        fullname=i.get("fullname"),
        born_date=datetime.strptime(i.get("born_date"), "%B %d, %Y"),
        born_location=i.get("born_location"),
        description=i.get("description"),
    ).save()

some_iterable: Iterable[dict] = input_(file_name_qoutes)
for i in some_iterable:
    Quote(
        tags=i.get("tags"),
        authors=i.get("author"),
        quotes=i.get("quote"),
    ).save()
