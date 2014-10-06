from django.db import models
from django.forms import ModelForm



# Create your models here.
#=========================================================================
class Product(models.Model):

    Name_pro = models.CharField(max_length=100)
    State_pro = models.CharField(max_length=100)
    Price_pro = models.IntegerField()
    Price_pro_g = models.IntegerField()
    Price_pro_k = models.IntegerField()
    id_pro = models.AutoField(primary_key=True)
#=========================================================================
class News(models.Model):

    #Link_news = models.CharField(max_length=100, primary_key=True)
    Text_news = models.CharField(max_length=100)
    Text_news_len = models.CharField(max_length=1000)
    Category_news = models.CharField(max_length=200)
    Title_news = models.CharField(max_length=300)
    Time_news = models.DateTimeField()
    Num_view_news = models.IntegerField()
    id = models.AutoField(primary_key=True)

#create table News(
#  Link_news varchar(100) primary key,
#  Text_news varchar(500),
#  Text_large_news varchar(100000),
#Category_news char(200),
#  Title_news char(300),
#  Time_news timestamp(),
#  Num-view_news numeric(3,0),
#);
#=========================================================================


class News_pic(models.Model):

    Link_news = models.ForeignKey(News)
    #Pic_news = models.ImageField()


#create table News_pic(
#   Pic_news varchar(1000),
#   foreign key (Link_news) references News);
#=========================================================================
class News_topic(models.Model):

    Link_news = models.ForeignKey(News)
    Topic_news = models.CharField(max_length=100)

#create table News_topic(
#   Topic_news varchar(100),
#   foreign key (Link_news) references News);
