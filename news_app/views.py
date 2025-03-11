from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import ContactForm
from .models import News, Category


# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'
    def get_queryset(self):
        return News.published.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xorij_news'] = News.published.filter(category__name='Xorijiy')[:5]
        context['mahalliy_news'] = News.published.filter(category__name='Mahalliy')[:5]
        context['sport_news'] = News.published.filter(category__name='Sport')[:5]
        context['texnik_news'] = News.published.filter(category__name='Texnika')[:5]
        return context
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/single_page.html'
    context_object_name = 'news_detail'
    def get_queryset(self):
        return News.published.filter(slug=self.kwargs['slug'])

class NewsCategoryView(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news_category'
    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs['category'])
        return News.published.filter(category=category)[:8]

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

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update.html'
    fields = ['title', 'body','image','category','status']

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('index')

class NewsCreateView(CreateView):
    model = News
    template_name = 'news/create.html'
    fields = ['title', 'body','image','category','status']
    def get_success_url(self):
        if self.object.status == 'DF':
            return reverse_lazy('index')
        return reverse_lazy('detailview', kwargs={'slug': self.object.slug})