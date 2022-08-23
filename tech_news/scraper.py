import requests
import time


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
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# if __name__ == "__main__":
#     # page_content = fetch(
#     #     'https://altoalegredomaranhao.ma.gov.br/transparencia/licitacoes'
#     #     )
#     fetch('http://httpbin.org/delay/10')
#     # print(page_content.status_code)
