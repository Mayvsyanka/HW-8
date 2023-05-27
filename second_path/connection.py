import certifi
from mongoengine import connect


uri = "mongodb+srv://mayvsyanka:1111@cluster0.whgftxb.mongodb.net/hw8_second_part?retryWrites=true&w=majority"
connection = connect(host=uri,  tlsCAFile=certifi.where(), ssl=True)
