import connect
from models import Author, Quote


# Функції пошуку
def quotes_by_name(args):
    list_quotes = []
    author = Author.objects(fullname=args[1].strip()).first()
    # print(f"author = {author.fullname}")
    quotes_ = Quote.objects(authors=author)
    for quote in quotes_:
        list_quotes.append(quote.quotes)
    return list_quotes


def quotes_by_tag(args):
    list_quotes = []
    quotes_ = Quote.objects(tags=args[1].strip())
    for quote in quotes_:
        list_quotes.append(quote.quotes)
    return list_quotes


def quotes_by_tags(args):
    set_quotes = set()

    for tag in args[1].split(","):
        quotes_ = Quote.objects(tags=tag.strip())
        for quote in quotes_:
            set_quotes.add(quote.quotes)
    return set_quotes


# Співвідношення команди до функції
commands = {
    "name": quotes_by_name,
    "tag": quotes_by_tag,
    "tags": quotes_by_tags,
}


# Вибір функції в залежності від команди
def run_command(args):
    return commands[args]


# Цикл вводу команд
def ent_command():
    while True:
        inp_ = input("Enter command: value\n").split(":")
        if inp_[0] == "exit":
            exit(1)
        elif len(inp_) != 2:
            print("Wrong command, try again\n")
        else:
            comm_ = run_command(inp_[0])
            res = comm_(inp_)
            for i in res:
                print(i)


if __name__ == "__main__":
    ent_command()
