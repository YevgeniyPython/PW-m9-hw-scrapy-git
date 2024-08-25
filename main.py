import json
from models import Author, Tag, Quote
from mongoengine import connect


with open('authors.json', 'r', encoding="UTF8") as file:
    author_list = json.load(file)
with open('quotes.json', 'r', encoding="UTF8") as file:
    quote_list = json.load(file)
connect(host=f"""mongodb+srv://itpython2023:my_pass@cluster0.vfyc1.mongodb.net/PW-m9-scrapy-project?retryWrites=true&w=majority""", ssl = True)
for element in author_list:
    author = Author(fullname = element.get("fullname"), born_date = element.get("born_date"), born_location = element.get("born_location"),\
                    description = element.get("description")).save()

for element in quote_list:
    quote = Quote(tags = [Tag(name=tag) for tag in element.get('tags')], author = Author.objects(fullname=element.get("author"))[0],\
                  quote=element.get("quote")).save()

