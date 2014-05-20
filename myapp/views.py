# -*- encoding: utf-8 -*-
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from django_ajax.decorators import ajax
from  myapp.models import News,News_pic
import datetime
#from feedreader import *
from myapp.tst_db import saffron_db
import feedparser
# Create your views here.
"""===============Display pages======================================================================================"""

def admin_parent(request):

    return render(request, 'parent/admin_parent.html')
"""========================================================="""

def admin_news_rss(request):
    feed1 = feedparser.parse('http://www.irna.ir/fa/rss.aspx?kind=-1')
    entry = feed1.entries
    return render(request,'news/admin_news_rss.html',{'entry': entry})
"""========================================================="""
def admin_news_hand(request):

    return render(request, 'news/admin_news_hand.html')
"""========================================================="""
def admin_news_edit_rss(request):

    return render(request, 'news/admin_Edit_rss.html')
"""========================================================="""
def admin_news_edit_hand(request):

    return render(request, 'news/admin_Edit_hand.html')



"""===========================jquery&&ajax==========================================================================="""

def insert_news_hand(request):
    if request.method == "POST":
   #img = request.FILES['pic_news'].name
   #file1 = Image.open(request.FILES['pic_news'])
   #file1.save("myapp/static/img/" + img)
        Text_news=request.POST.get('body_news')
        Title_news=request.POST.get('Title_news')
        Category_news=request.POST.get('group_news')
        #group_link=request.POST.get('select')

        Time_news=datetime.datetime.now()

        #news2 = News_pic(pic_news="static/img/" + img)
        #news.save()
        #news2.save()
        #
        #saffron_db("INSERT INTO `news`(`title`,`text`) VALUES(`"+Title_news+"`,`"+Text_news+"`)")
        Object_news = News(Text_news=Text_news, Category_news=Category_news, Title_news=Title_news, Time_news=Time_news)
        Object_news.save()

        message=u"تغییرات با موفقیت انجام شد."
        return HttpResponse(message)
"""========================================================="""

#def delete_news_rss(request, List):
#    for i in List:
#        one_news = News.objects.filter(i)
#        one_news.delete()
#    message=u"تغییرات با موفقیت انجام شد."
#    return (message)


       