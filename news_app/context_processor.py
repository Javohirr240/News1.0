from django.db.models import Q

from .models import News ,Category
def global_context(request):
    return {
        'news_list' : News.published.all()[:10],
        'categories' : Category.objects.all(),
        'mahalliy_one' : News.published.filter(Q(category__name='Mahalliy')|Q(category__name='Local')|Q(category__name='Местный')).first(),
        'sport_one' : News.published.filter(Q(category__name='Sport')|Q(category__name='Sport')|Q(category__name='Спорт')).first(),
        'texnik_one' : News.published.filter(Q(category__name='Texnika')|Q(category__name='Technique')|Q(category__name='Техника')).first(),
        'xorij_one' : News.published.filter(Q(category__name='Xorijiy')|Q(category__name='Foreign')|Q(category__name='Иностранный')).first(),
    }
