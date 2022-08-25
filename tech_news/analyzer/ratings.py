from tech_news.database import get_collection


# Requisito 10
# [Natã Elienai] Tech News - Tribo 16-B
# Observação: Deixando explicito que as dúvidas que fiquei com o código
# Entrei em contando com o mesmo e pedi uma explicação de como foi a lógica
# e o pensamento em dúvidas pontuais em relação ao código bem como pedir
# referencias para que eu possa desenvolver as dúvidas pontuais
def top_5_news():
    popular_news = list(
        get_collection().find({}, {"_id": False})
        .sort([("comments_count", -1), ("title", 1)])
        .limit(5)
    )
    return [(news["title"], news["url"]) for news in popular_news]


# Requisito 11
# [Natã Elienai] Tech News - Tribo 16-B
# Observação: Deixando explicito que as dúvidas que fiquei com o código
# Entrei em contando com o mesmo e pedi uma explicação de como foi a lógica
# e o pensamento em dúvidas pontuais em relação ao código bem como pedir
# # referencias para que eu possa desenvolver as dúvidas pontuais
def top_5_categories():
    categories_count = list(
        get_collection().aggregate(
            [
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
                {"$project": {"_id": 0, "name": "$_id"}},
            ]
        )
    )
    return [category["name"] for category in categories_count]
