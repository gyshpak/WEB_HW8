import connect
from models import Author, Quote

def all_quotes_by_name(args):
    author = Author.objects(fullname=args[1].strip()).first()
    print(f"author = {author.fullname}")
    quotes_ = Quote.objects(authors=author)
    list_quotes = []
    for quote in quotes_:
        # print(f'quote: {quote.quotes}')
        list_quotes.append(quote.quotes)



   

def com_for_authors(args):
    print(args)


def com_for_quote(args):
    print(args[0].strip())


def com_for_quotes(args):
    print(args)


commands = {
    "name": all_quotes_by_name,
    "names": com_for_authors,
    "tag": com_for_quote,
    "tags": com_for_quotes,
    # "born_data": com_for_author,
    # "location": com_for_author,
}

def run_command(args):
    return commands[args]


def ent_command():
    while True:
        inp_ = input("Enter command: value\n").split(":")
        if inp_[0] == "exit":
            exit(1)
        elif len(inp_) != 2:
            print("Wrong command, try again\n")
        else:
            comm_ = run_command(inp_[0])
            comm_(inp_)
            # res = comm_(inp_)
            # for i in res:
            #     print(i)


if __name__ == "__main__":
    ent_command()
