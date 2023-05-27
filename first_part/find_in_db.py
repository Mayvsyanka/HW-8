from first_part.models import Quote, Author
from .connection import connection



def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    print("------------------------------")
    print("Quotes with tag '{}':".format(tag))
    for quote in quotes:
        print("~ {}".format(quote.quote))
    print ("------------------------------")


def search_by_author(name):
    auth = Author.objects(fullname=name).first()
    if auth:
        quotes = Quote.objects(author=auth)
        print("------------------------------")
        print("'{}'s quotes':".format(name))
        for quote in quotes:
            print("~ {}".format(quote.quote))
    else:
        print("Author '{}' is not defined.".format(name))
    print("------------------------------")


def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    print("------------------------------")
    print("Quotes with tags '{}':".format(tags))
    for quote in quotes:
        print("~ {}".format(quote.quote))
    print("------------------------------")



def parse_commands():
    while True:
        raw_command = input(">>>")

        command = raw_command.split(":")
    
        if command[0].lower() == "name":
            data = command[1].strip()
            search_by_author(data)

        elif command[0].lower() == "tag":
            data = command[1].strip()
            search_by_tag(data)

        elif command[0].lower() == "tags":
            data = command[1].strip()
            search_by_tags(data)

        elif command[0].lower() == "exit":
            print("Good job) \nBye")
            break

        else:
            print("Incorrect command, try again)")


if __name__ == "__main__":

    parse_commands()