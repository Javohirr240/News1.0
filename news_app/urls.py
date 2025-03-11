from django.urls import path
from .views import (
    NewsListView,
    NewsDetailView,
    NewsCategoryView,
    ContactsFormView,
    NewsUpdateView,
    NewsDeleteView,
    NewsCreateView,
)
from django.views.generic import TemplateView
urlpatterns = [
    path('', NewsListView.as_view(), name='index'),  # Asosiy sahifa
    path('news/', NewsListView.as_view(), name='newsview'),  # Yangiliklar ro‘yxati
    path('news/create/', NewsCreateView.as_view(), name='createview'),  # Yangilik yaratish
    path('news/<slug:slug>/update/', NewsUpdateView.as_view(), name='updateview'),  # Yangilikni yangilash
    path('news/<slug:slug>/delete/', NewsDeleteView.as_view(), name='deleteview'),  # Yangilikni o‘chirish
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='detailview'),  # Yangilik tafsilotlari
    path('categories:<str:category>/', NewsCategoryView.as_view(), name='categoryview'),  # Kategoriya bo‘yicha yangiliklar
    path('contact/', ContactsFormView.as_view(), name='contact'),  # Aloqa formasi
    path('404/', TemplateView.as_view(template_name='news/404.html'), name='404'),  # 404 sahifasi
]