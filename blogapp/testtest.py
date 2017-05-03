from django.shortcuts import render
from blogapp.models import Article
idlist=Article.objects.all().values('id')
print(idlist)