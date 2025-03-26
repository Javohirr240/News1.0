from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User

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
from .forms import ContactForm, CommentForm
from .models import News, Category
from .mixins import CustomMixins

# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'
    def get_queryset(self):
        return News.published.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xorij_news'] = News.published.filter(Q(category__name='Xorijiy')|Q(category__name='Foreign')|Q(category__name='Иностранный'))[:5]
        context['mahalliy_news'] = News.published.filter(Q(category__name='Mahalliy')|Q(category__name='Local')|Q(category__name='Местный'))[:5]
        context['sport_news'] = News.published.filter(Q(category__name='Sport')|Q(category__name='Sport')|Q(category__name='Спорт'))[:5]
        context['texnik_news'] = News.published.filter(Q(category__name='Texnika')|Q(category__name='Technique')|Q(category__name='Техника'))[:5]
        return context


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


class NewsUpdateView(CustomMixins,UpdateView):
    model = News
    template_name = 'news/update.html'
    fields = ['title', 'body','image','category','status']

class NewsDeleteView(CustomMixins,DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('index')


class NewsCreateView(CustomMixins, CreateView ):
    model = News
    template_name = 'news/create.html'
    fields = ['title', 'title_uz','title_en','title_ru','body','body_uz','body_en','body_ru','image','category','status']
    def get_success_url(self):
        if self.object.status == 'DF':
            return reverse_lazy('index')
        return reverse_lazy('detailview', kwargs={'slug': self.object.slug})

@login_required()
@user_passes_test(lambda u: u.is_superuser)
def adminView(request):
    users = User.objects.filter(is_superuser=True)
    context = {
        'users': users,
    }
    return render(request, 'news/admin.html', context)

from hitcount.views import HitCountDetailView, HitCountMixin

from hitcount.utils import get_hitcount_model

def post_detail(request, slug):
    news_detail = get_object_or_404(News, slug=slug, status=News.Status.Published)
    context = {}
    hit_count = get_hitcount_model().objects.get_for_object(news_detail)
    hits = hit_count.hits
    hitcontext = context['hitcount']= {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits += 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits
    comments = news_detail.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news_detail
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'news_detail': news_detail,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request, 'news/single_page.html', context)

class NewsDetailView(LoginRequiredMixin,DetailView):
    model = News
    template_name = 'news/single_page.html'
    context_object_name = 'news_detail'
    def get_queryset(self):
        return News.published.filter(slug=self.kwargs['slug'])

class SearchResultsView(ListView):
    model = News
    template_name = 'news/search_resault.html'
    context_object_name = 'barcha_yangiliklar'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.published.filter(Q(title__icontains=query) | Q(body__icontains=query))