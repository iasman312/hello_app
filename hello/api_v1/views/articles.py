import json

from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from api_v1.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        response_data = ArticleSerializer(articles, many=True).data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data=article_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response({'id': article.id})