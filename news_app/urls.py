from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCategoryView, ContactsFormView
from django.views.generic import TemplateView
urlpatterns = [
    path('',NewsListView.as_view(),name='index'),
    path('contact/',ContactsFormView.as_view(),name='contact'),
    path('404/',TemplateView.as_view(template_name='news/404.html'),name='404'),
    path('news', NewsListView.as_view(), name='newsview'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='detailview'),
    path('news/<str:category>', NewsCategoryView.as_view(), name='categoryview'),
]