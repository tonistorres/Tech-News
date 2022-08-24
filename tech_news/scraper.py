import requests
import time
from parsel import Selector


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
        print('De castigo?')
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links_urls_noticias = selector.css("h2.entry-title a::attr(href)").getall()
    return links_urls_noticias


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
    """Seu código deve vir aqui"""


# if __name__ == "__main__":

#     page_content = fetch(
#         'https://blog.betrybe.com/carreira/gestao-do-tempo-dicas-essencias/'
#         )
#     # pagina que contem tag
#     # page_content = fetch(
#     #     """https://blog.betrybe.com/noticias/orkut-voltou-o-que-se-sabe-ate-agora-sobre-o-retorno/"""
#     #     )
#     # # print(page_content)
#     scrape_noticia(page_content)
