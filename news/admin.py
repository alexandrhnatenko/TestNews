from django.contrib import admin

from news.models import Post, Comment


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    model = Post
    list_display = (
        'title', 'author_name', 'creation_date', 'votes', 'link',)
    search_fields = ('author_name', 'title',)
    list_filter = ('title', 'author_name', 'votes',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = (
        'post', 'author_name', 'creation_date', 'content')
    search_fields = ('post__title', 'author_name',)
    list_filter = ('post__title', 'author_name')
