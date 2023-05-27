import json
from first_part.models import Quote, Author
from .connection import connection

def get_authors_data(path):
    with open(path, 'r') as file:
        data = json.load(file)
        for item in data:
            document = Author(**item)
            document.save()


def get_quotes_data(path):
    with open(path, 'r') as file:
        data = json.load(file)
        for item in data:
            author_name = item['author']
            author = Author.objects(fullname=author_name).first()
            if not author:
                author = Author(fullname=author_name)
                author.save()

            quote = Quote(
                author=author, quote=item['quote'], tags=item['tags'])
            quote.save()



if __name__ == "__main__":
    get_authors_data("authors.json")
    get_quotes_data("quotes.json")
