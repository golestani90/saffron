# -*- encoding: utf-8 -*-
from django.shortcuts import HttpResponse
from django.shortcuts import render
#from django_ajax.decorators import ajax
from  myapp.models import News,News_pic, Product
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
    time_1 = datetime.datetime.now()
    for i in range(len(entry)):
        Object_news = News(Title_news=entry[i].title, Text_news=entry[i].description,
                           Text_news_len=entry[i].description, Time_news=time_1,
                           Num_view_news=1, Category_news=entry[i].title)
        Object_news.save()
    #print (entry[0].title)
    entry = News.objects.all()
    return render(request,'news/admin_news_rss.html', {'entry': entry})
"""========================================================="""
def admin_news_hand(request):

    return render(request, 'news/admin_news_hand.html')
"""========================================================="""
def admin_news_edit_rss(request):

    return render(request, 'news/admin_Edit_rss.html')
"""========================================================="""
def admin_news_edit_hand(request):

    return render(request, 'news/admin_Edit_hand.html')
"""========================================================="""
def view_price(request):

    return render(request, 'shop/insert_price.html')
"""========================================================="""
def insert_price(request):
    if request.method == "POST":
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        price = request.POST.get('price')
        price_g = int(price)/4.7
        price_k = price_g*1000
        #print price_g
    product = Product(Name_pro=name, State_pro=degree, Price_pro=price, Price_pro_g=price_g, Price_pro_k=price_k)
    product.save()
    messege = u"محصول با موفقیت ثبت شد!"

    return render(request, 'shop/insert_price.html', {'msg': messege})

"""===========================jquery&&ajax==========================================================================="""
def insert_news_hand(request):
    #if request.method == "GET":
    #    return render(request, 'news/admin_news_hand.html')
    if request.method == "POST":
   #img = request.FILES['pic_news'].name
   #file1 = Image.open(request.FILES['pic_news'])
   #file1.save("myapp/static/img/" + img)
        Text_news = request.POST.get('body_news')
        Text_news_len = request.POST.get('body_news_len')
        print(Text_news_len)
        Title_news = request.POST.get('title_news')
        print(Title_news)
        Category_news = request.POST.get('group_news')
        print (Category_news)
        Time_news=datetime.datetime.now()
        #news2 = News_pic(pic_news="static/img/" + img)
        #news.save()
        #news2.save()
        #saffron_db("INSERT INTO `news`(`title`,`text`) VALUES(`"+Title_news+"`,`"+Text_news+"`)")
        Object_news = News(Text_news=Text_news, Text_news_len=Text_news_len, Category_news=Category_news,
                           Title_news=Title_news, Time_news=Time_news, Num_view_news=1)
        #print(Object_news)
        Object_news.save()
        message=u"خبر با موفقیت ثبت شد!"
        return render(request, 'news/admin_news_hand.html', {'msg': message})
"""========================================================="""

def delete_news_rss(request):
    if request.method == 'POST':
        List = request.POST.get('check')
        #print(List)
        #for i in List:
        #    one_news = News.objects.filter(id=i)
        #    print one_news
            #one_news.delete()
        one = News.objects.filter(id=List)
        #print one
        one.delete()
        message = u"خبر با موفقیت حذف شد!"
        list_1 = News.objects.all()
        #for i in list_1:
         #print(i.id)
        return render(request, 'news/admin_news_rss.html', {'msg': message, 'entry': list_1})
"""========================================================="""
def delete_news_rss1(request,id_news):
    news2 = News.objects.filter(id=id_news)
    news2.delete()
    message = u"خبر با موفقیت حذف شد!"
    list_1 = News.objects.all()
    return render(request, 'news/admin_news_rss.html', {'msg': message, 'entry': list_1})
"""========================================================="""
def login (request):
    return render (request, 'login/login.html')