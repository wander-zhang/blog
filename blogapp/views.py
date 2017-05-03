from django.shortcuts import render
from bs4 import BeautifulSoup
from blogapp.models import Article
def index(request):
    idnum=len(Article.objects.all().values('id'))
    """A view of all bands."""
    top=Article.objects.order_by("-readtime")[0:5]
    indextitle=[]
    for i in range(idnum-3,idnum+1):
        indextitle.append(Article.objects.get(id=i))
    return render(request, 'index.html',{'id0':indextitle[0].id,'title0':indextitle[0].title,'data0':BeautifulSoup(indextitle[0].contentdata).get_text()[0:500],'date0':indextitle[0].createdate,
                                         'id1':indextitle[1].id,'title1': indextitle[1].title, 'data1': BeautifulSoup(indextitle[1].contentdata).get_text()[0:500],'date1': indextitle[1].createdate,
                                         'id2':indextitle[2].id,'title2': indextitle[2].title, 'data2': BeautifulSoup(indextitle[2].contentdata).get_text()[0:500],'date2': indextitle[2].createdate,
                                         'id3':indextitle[3].id,'title3': indextitle[3].title, 'data3': BeautifulSoup(indextitle[3].contentdata).get_text()[0:500],'date3': indextitle[3].createdate,
                                         'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
                                         })
def article(request):
    """A view of all bands."""
    idnum = len(Article.objects.all().values('id'))
    """A view of all bands."""
    indextitle = []
    if idnum<=7:
        for i in range(idnum, 0,-1):
            indextitle.append(Article.objects.get(id=i))
        return render(request, 'article.html',
                      {'id0': indextitle[0].id,'title0': indextitle[0].title,
                       'data0': BeautifulSoup(indextitle[0].contentdata).get_text()[0:500],
                       'date0': indextitle[0].createdate,'count0': indextitle[0].readtime,
                       'id1': indextitle[1].id,'title1': indextitle[1].title,
                       'data1': BeautifulSoup(indextitle[1].contentdata).get_text()[0:500],
                       'date1': indextitle[1].createdate,'count1': indextitle[1].readtime,
                       'id2': indextitle[2].id,'title2': indextitle[2].title,
                       'data2': BeautifulSoup(indextitle[2].contentdata).get_text()[0:500],
                       'date2': indextitle[2].createdate,'count2': indextitle[2].readtime,
                       'id3': indextitle[3].id,'title3': indextitle[3].title,
                       'data3': BeautifulSoup(indextitle[3].contentdata).get_text()[0:500],
                       'date3': indextitle[3].createdate,'count3': indextitle[3].readtime,
                       'id4': indextitle[4].id,'title4': indextitle[4].title,
                       'data4': BeautifulSoup(indextitle[4].contentdata).get_text()[0:500],
                       'date4': indextitle[4].createdate,'count4': indextitle[4].readtime,
                       # 'title5': indextitle[5].title,
                       # 'data5': BeautifulSoup(indextitle[5].contentdata).get_text()[0:500],
                       # 'date5': indextitle[5].createdate,
                       # 'title6': indextitle[6].title,
                       # 'data6': BeautifulSoup(indextitle[6].contentdata).get_text()[0:500],
                       # 'date6': indextitle[6].createdate,
                       # 'title7': indextitle[7].title,
                       # 'data7': BeautifulSoup(indextitle[7].contentdata).get_text()[0:500],
                       # 'date7': indextitle[7].createdate,
                       })
    if idnum>7:
        for i in range(idnum, idnum-8,-1):
            indextitle.append(Article.objects.get(id=i))
        return render(request, 'article.html',
                      {'id0': indextitle[0].id,'title0': indextitle[0].title, 'data0': BeautifulSoup(indextitle[0].contentdata).get_text()[0:500],
                       'date0': indextitle[0].createdate,'count0': indextitle[0].readtime,
                       'id1': indextitle[1].id,'title1': indextitle[1].title, 'data1': BeautifulSoup(indextitle[1].contentdata).get_text()[0:500],
                       'date1': indextitle[1].createdate,'count1': indextitle[1].readtime,
                       'id2': indextitle[2].id,'title2': indextitle[2].title, 'data2': BeautifulSoup(indextitle[2].contentdata).get_text()[0:500],
                       'date2': indextitle[2].createdate,'count2': indextitle[2].readtime,
                       'id3': indextitle[3].id,'title3': indextitle[3].title, 'data3': BeautifulSoup(indextitle[3].contentdata).get_text()[0:500],
                       'date3': indextitle[3].createdate,'count3': indextitle[3].readtime,
                       'id4': indextitle[4].id,'title4': indextitle[4].title,
                       'data4': BeautifulSoup(indextitle[4].contentdata).get_text()[0:500],
                       'date4': indextitle[4].createdate,'count4': indextitle[4].readtime,
                       'id5': indextitle[5].id,'title5': indextitle[5].title,
                       'data5': BeautifulSoup(indextitle[5].contentdata).get_text()[0:500],
                       'date5': indextitle[5].createdate,'count5': indextitle[5].readtime,
                       'id6': indextitle[6].id,'title6': indextitle[6].title,
                       'data6': BeautifulSoup(indextitle[6].contentdata).get_text()[0:500],
                       'date6': indextitle[6].createdate,'count6': indextitle[6].readtime,
                       'id7': indextitle[7].id,'title7': indextitle[7].title,
                       'data7': BeautifulSoup(indextitle[7].contentdata).get_text()[0:500],
                       'date7': indextitle[7].createdate,'count7': indextitle[7].readtime,
                       })
def personaldata(request):
    """A view of all bands."""

    return render(request, 'personaldata.html')
# Create your views here.
def content(request):
    """A view of all bands."""
    title=Article.objects.get(id=4)
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,
    })
def id5(request):
    """A view of all bands."""
    top = Article.objects.order_by("-readtime")[0:5]
    title=Article.objects.get(id=5)
    title.readtime+=1
    title.save()
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
    })
def id4(request):
    """A view of all bands."""
    top = Article.objects.order_by("-readtime")[0:5]
    title=Article.objects.get(id=4)
    title.readtime+=1
    title.save()
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
    })
def id3(request):
    """A view of all bands."""
    top = Article.objects.order_by("-readtime")[0:5]
    title=Article.objects.get(id=3)
    title.readtime+=1
    title.save()
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
    })
def id2(request):
    """A view of all bands."""
    top = Article.objects.order_by("-readtime")[0:5]
    title=Article.objects.get(id=2)
    title.readtime+=1
    title.save()
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
    })
def id1(request):
    """A view of all bands."""
    top = Article.objects.order_by("-readtime")[0:5]
    title=Article.objects.get(id=1)
    title.readtime+=1
    title.save()
    return render(request, 'content.html',{
        'title': title.title,
        'content': title.contentdata.encode(),
        'date': title.createdate,'top1': top[0].title,'top1id':top[0].id,'top2': top[1].title,'top2id':top[1].id,'top3': top[2].title,'top3id':top[2].id,
                                         'top4': top[3].title,'top4id':top[3].id,'top5': top[4].title,'top5id':top[4].id,
    })
# Create your views here.
