from django.urls import path

from article.views import (
    IndexView,
    ArticleView,
    CreateArticleView,
    ArticleUpdateView,
    ArticleCommentCreate,
    ArticleDeleteView,
    LikeView,
    LikeCommentView
)


app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('add/', CreateArticleView.as_view(), name='add'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
    path('like/<int:pk>/', LikeView.as_view(), name='like_article'),
    path('like_comment/<int:pk>/', LikeCommentView.as_view(), name='like_comment'),
]
