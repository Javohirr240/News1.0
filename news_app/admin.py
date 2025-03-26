from django.contrib import admin
from .models import News, Category, Contact, Comment

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','image','published_time','status']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','body','created_time','active']
    search_fields = ['user','body']
    list_filter = ['active','created_time']
    actions = ['disable_comments','activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activate_comments(self, request, queryset):
        queryset.update(active=True)