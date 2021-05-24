from django.urls import path, include

from api_v1.views import ArticleView


app_name = 'api_v1'


article_urls = [
    path('', ArticleView.as_view(), name='articles'),
]


urlpatterns = [
    path('articles/', include(article_urls)),
]