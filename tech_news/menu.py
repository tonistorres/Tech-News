import sys
# importando o módulo que
from tech_news.analyzer.ratings import top_5_categories, top_5_news

# fazendo a importação as funções contidas no módulo
# de busca de conteudos
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)

# importando modulo que raspa  os dados no conteudo html
from tech_news.scraper import get_tech_news


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )


def full_menu():
    analyzer_menu()
    print()
    option = int(input("Digite uma das opções acima:"))
    if option == 0:
        populate_database()
    elif option == 1:
        search_title()
    elif option == 2:
        search_date()
    elif option == 3:
        search_tag()
    elif option == 4:
        search_category()
    elif option == 5:
        list_top_5_news()
    elif option == 6:
        list_top_5_categories()
    else:
        show_exit_message()


def populate_database():
    numbers_notices = int(input("Digite quantas notícias serão buscadas:"))
    result = get_tech_news(numbers_notices)
    print()
    print('----------------------------------------------------------------')
    print('                      Report Noticies                           ')
    print('----------------------------------------------------------------')
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'O Dicionario tem {len(result)} notícias quentinhas para você :)')
    print('----------------------------------------------------------------')


# Notícia bacana
def search_title():
    title = input("Digite o título:")
    print()
    print('----------------------------------------------------------------')
    print('                      Report Title                              ')
    print('----------------------------------------------------------------')
    result = search_by_title(title)
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'A Tupla com {len(result)}')
    print('----------------------------------------------------------------')


# 07/04/2022
def search_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print()
    print('----------------------------------------------------------------')
    print('                      Report Date Formated                      ')
    print('----------------------------------------------------------------')
    result = search_by_date(date)
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'A Tupla com {len(result)}')
    print('----------------------------------------------------------------')


# Tecnologia
def search_tag():
    tag = input("Digite a tag:")
    print()
    print('----------------------------------------------------------------')
    print('                         Report Tag                             ')
    print('----------------------------------------------------------------')
    result = search_by_tag(tag)
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'A Tupla com {len(result)}')
    print('----------------------------------------------------------------')


# Novidades
def search_category():
    category = input("Digite a categoria:")
    print()
    print('----------------------------------------------------------------')
    print('                         Report Category                        ')
    print('----------------------------------------------------------------')
    result = search_by_category(category)
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'A Tupla com {len(result)}')
    print('----------------------------------------------------------------')


def list_top_5_news():
    print()
    print('----------------------------------------------------------------')
    print('                         Report Top 5                           ')
    print('----------------------------------------------------------------')
    result = top_5_news()
    print(result)
    print()
    print('----------------------------------------------------------------')
    print(f'Numero de Dados Triados {len(result)}')
    print('----------------------------------------------------------------')


def list_top_5_categories():
    print()
    print('----------------------------------------------------------------')
    print('                         Report Top 5                           ')
    print('----------------------------------------------------------------')
    result = top_5_categories()
    print()
    print('----------------------------------------------------------------')
    print(f'Numero de Dados Triados {len(result)}')
    print('----------------------------------------------------------------')


def show_exit_message():
    print('----------------------------------------------------------------')
    print('                         Ops!!! Error                           ')
    print('----------------------------------------------------------------')
    print("Encerrando script")
    sys.stderr


if __name__ == "__main__":
    full_menu()
