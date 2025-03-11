from .models import News ,Category
def global_context(request):
    return {
        'news_list' : News.published.all()[:10],
        'categories' : Category.objects.all(),
        'mahalliy_one' : News.published.filter(category__name='Mahalliy').first(),
        'sport_one' : News.published.filter(category__name='Sport').first(),
        'texnik_one' : News.published.filter(category__name='Texnika').first(),
        'xorij_one' : News.published.filter(category__name='Xorijiy').first(),
    }
