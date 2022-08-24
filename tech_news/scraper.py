import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"user-agent": "Fake user-agent"}
            )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.HTTPError:
        return 'Instabilidade no serviço'
    except requests.ReadTimeout:
        return None


# Requisito 2
# https://blog.betrybe.com/
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_pages = selector.css("h2.entry-title a::attr(href)").getall()
    return links_pages


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next = selector.css(".nav-links .next::attr(href)").get()
    if not next:
        return None

    return next


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    dict_info = {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": len(selector.css("div.comment-body").getall()),
        "summary": ''.join(selector.css(
          '.entry-content > p:first-of-type ::text').getall()).strip(),
        "tags": selector.css('.post-tags a[rel="tag"]::text').getall(),
        "category": selector.css(".meta-category span.label::text").get(),
    }
    return dict_info


# Requisito 5
def get_tech_news(amount):
    # cirar uma lista receber noticias
    list = []
    # Função Requisito 1
    # url para raspagem
    url_default = "https://blog.betrybe.com/"
    # enquanto o tamanho da lista for menor que amount execute esse laço
    while len(list) < amount:
        # a função fetch irá trazer o conteúdo da pagina url em formato text
        content_page = fetch(url_default)
        # Função Requisito 3
        # Retorna sempre a url da próxima página
        next = scrape_next_page_link(content_page)
        # Função Requisito 2
        # urls recebe os links dos title dos cards
        # ex.: page 1 tem 12 title e cards
        urls = scrape_novidades(content_page)
        # percorrer os links dos cards da pagina atual
        for url in urls:
            # o tamanho da lista form igual ao valor inteiro passado
            # break (pare) saia do laço for
            if len(list) == amount:
                break
            # Nesse ponto irei setar a url referente ao title
            # atual do laço e passá-la como argumento para a
            # função fetch e guardar o conteudo da pagina em
            # content_atual_loop
            content_atual_loop = fetch(url)
            # Nesse pronto irei pegar o conteudo de cada pagina 
            # conforme link capturado pelo laço em urls e passar
            # esse conteúdo como argumento para a função scrap_noticia
            # que irá organizar as informações em um dicionário já customizado
            data = scrape_noticia(content_atual_loop)
            # Agora irei pegar esse dicionario organizado e adicionar
            # em minha list por meio do método append
            list.append(data)
        # na saída do for eu troco a url_default por next que pega a proxima
        # página
        # e o ciclo continua pois ainda estou em while
        url_default = next
    # na saída de while eu salvo a minha lista personalizada
    # com a função create_news do módulo database e adiciono 
    # no meu banco mongo db
    create_news(list)
    # retorno a lista
    return list


# result = get_tech_news(2)
# print(result)
# print('---------------------------------------------')
# print(f"Numero de noticias capturadas: {len(result)}")
# print('---------------------------------------------')
# # if __name__ == "__main__":
#     # -----------------------------
#     # Testando Retorno Requesito 2
#     # -----------------------------
#     page = fetch('https://blog.betrybe.com/')
#     links_pages = scrape_novidades(page)
#     print(links_pages)
#     # print('Nº de Title de Cards Page 1:', len(links_pages))
#     # -----------------------------
#     # Testando Retorno Requesito 3
#     # -----------------------------
#     # result = scrape_next_page_link(page)
#     # print(result)

# #     page_content = fetch(
# #         'https://blog.betrybe.com/carreira/gestao-do-tempo-dicas-essencias/'
# #         )
# #     # pagina que contem tag
# #     # page_content = fetch(
# #     #     """https://blog.betrybe.com/noticias/orkut-voltou-o-que-se-sabe-ate-agora-sobre-o-retorno/"""
# #     #     )
# #     # # print(page_content)
# #     scrape_noticia(page_content)
