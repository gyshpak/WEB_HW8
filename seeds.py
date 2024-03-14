import json
from models import Author, Quote
import connect
from typing import Iterable


file_name_authors = "authors.json"
file_name_qoutes = "qoutes.json"

def input_(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# some_iterable: Iterable[dict] = (input_(file_name_authors))
# for i in some_iterable:
#     # print(f"name={i.get('fullname')},\n born_date={i.get('born_date')},\n born_location={i.get('born_location')},\n description={i.get('description')}")
#     author = Author(fullname=i.get("fullname"), born_date=i.get("born_date"), born_location=i.get("born_location"), description=i.get("description"))
#     # Author(fullname=i.get("fullname"), born_date=i.get("born_date"), born_location=i.get("born_location"), description=i.get("description")).save()
#     print(author.fullname)

some_iterable: Iterable[dict] = (input_(file_name_qoutes))
for i in some_iterable:
    # print(f"tags={i.get('tags')},\n author={i.get('author')},\n quote={i.get('quote')}")
    quote = Quote(tags=i.get("tags"), authors=i.get("author"), quotes=i.get("quote"))
    # Quote(tags=i.get("tags"), author=i.get("author"), quote=i.get("quote")).save()
    print(quote.quotes)
