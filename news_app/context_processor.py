from .models import News ,Category

def global_context(request):
    return {
        'news_list' : News.objects.filter(status='PB')[:10],
        'categories' : Category.objects.all(),
        'mahalliy_one' : News.objects.filter(category__name='Mahalliy').first(),
        'sport_one' : News.objects.filter(category__name='Sport').first(),
        'texnik_one' : News.objects.filter(category__name='Texnika').first(),
        'xorij_one' : News.objects.filter(category__name='Xorijiy').first(),
    }