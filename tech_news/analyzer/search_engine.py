from tech_news.database import search_news
from datetime import datetime
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
# https://docs.python.org/pt-br/3/library/datetime.html
# classmethod date.fromisoformat(date_string)
# Retorna um date correspondendo a date_string fornecido no formato YYYY-MM-DD:
# strftime e strptime - Todos os objetos date, datetime e time dão suporte ao
#  método strftime(format), para criar uma string representando o tempo sob
#  o controle de uma string de formatação explícita.
# %d - Dia do mês como um número decimal com zeros a esquerda.
# %m - Mês como um número decimal com zeros a esquerda.
# %y - Ano sem século como um número decimal com zeros a esquerda.
def search_by_date(date):
    try:
        # data recebida por parâmetro é tratada pelo métodos
        #  strftime e fromisoformat
        treated_data = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        # buscando por data no banco mongo por meio da função search_news
        # conteúdos relacionado a data passada por argumento
        data_content = search_news({"timestamp": treated_data})
        # criando array com conteúdos filtrado do banco
        content_filter = []
        # percorrer data_content que possui o conteúdo filtrado
        # pela função search_nwes que recebeu por parâmetro uma 
        # data filtrada
        for new in data_content:
            # montando minha forma de tupla para ser lançada no array
            # para isso pegando a value title e url de data_content 
            date_format_tuple = (new['title'], new['url'])
            # adicionando minha tupla montanda ao array content_filter
            content_filter.append(date_format_tuple)
        return content_filter
    except ValueError:
        raise ValueError('Data inválida')


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
