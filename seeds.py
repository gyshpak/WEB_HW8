import connect
from datetime import datetime
import json
from models import Author, Quote
from typing import Iterable


file_name_authors = "authors.json"
file_name_qoutes = "qoutes.json"


# Читання даних з json файлів
def input_(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Запис авторів
authors_data: Iterable[dict] = input_(file_name_authors)
for author_data in authors_data:
    Author(
        fullname=author_data.get("fullname"),
        born_date=datetime.strptime(author_data.get("born_date"), "%B %d, %Y"),
        born_location=author_data.get("born_location"),
        description=author_data.get("description"),
    ).save()


# Запис цитат
quotes_data: Iterable[dict] = input_(file_name_qoutes)
for quote_data in quotes_data:
    author_fullname = quote_data.get("author")
    author = Author.objects(
        fullname=author_fullname
    ).first()  # знаходимо об'єкт Автора для прив'язки до поля authors
    Quote(
        tags=quote_data.get("tags"),
        authors=author,
        quotes=quote_data.get("quote"),
    ).save()
