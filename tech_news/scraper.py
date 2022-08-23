import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, timeout=3):
    try:
        response = requests.get(
            url,
            timeout=timeout
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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
