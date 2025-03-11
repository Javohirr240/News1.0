from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView

from .forms import ContactForm
from .models import News, Category, Contact


# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xorij_news'] = News.objects.filter(category__name='Sport')[:5]
        context['mahalliy_news'] = News.objects.filter(category__name='Mahalliy')[:5]
        context['sport_news'] = News.objects.filter(category__name='Sport')[:5]
        context['texnik_news'] = News.objects.filter(category__name='Texnika')[:5]
        return context
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/single_page.html'
    context_object_name = 'news_detail'
    def get_queryset(self):
        return News.objects.filter(status='PB', slug=self.kwargs['slug'])

class NewsCategoryView(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news_category'
    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs['category'])
        return News.objects.filter(category=category)[:8]

class ContactsFormView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")

        return render(request, self.template_name, {'form': form})

