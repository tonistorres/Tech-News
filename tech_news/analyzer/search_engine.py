from tech_news.database import search_news
# https://pymongo.readthedocs.io/en/stable/tutorial.html
# https://www.geeksforgeeks.org/python-mongodb-query/


# Requisito 6
def search_by_title(title):
    # https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598
    titles = search_news({"title": {"$regex": title, "$options": "i"}})

    arr_tuple = []

    for title in titles:
        assembled_tuple = (title['title'], title['url'])
        arr_tuple.append(assembled_tuple)

    return arr_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     data = 'Rescisão indireta: como funciona essa demissão [7 exemplos]'
#     result = search_by_title(data)
#     print(result)
