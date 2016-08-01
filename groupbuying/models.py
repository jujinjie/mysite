# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    ProductID=models.AutoField(primary_key=True)
    GroupID=models.IntegerField(default=0)
    ProductName=models.CharField(max_length=50)
    SalePrice=models.FloatField(max_length=8)
    ProductIntro=models.TextField()
    Color=models.CharField(max_length=50,default="")
    Size=models.IntegerField(default=0)
    MaxCount=models.IntegerField()
    Time=models.DateTimeField()
    SellCount=models.IntegerField()
    #ProductImage=models.URLField()
    IsOut=models.BooleanField(default=True)
#Startprice=models.FloatField(max_length=8)
    class Meta:
        verbose_name=u"产品"
        verbose_name_plural=u"产品"
    def __unicode__(self):
        return self.ProductName
     
class Admin(models.Model):
    AdminID=models.AutoField(primary_key=True)
    LoginName=models.CharField(max_length=50)
    LoginPwd=models.CharField(max_length=50)
    class Meta:
        verbose_name=u"管理员"
        verbose_name_plural=u"管理员"
    
class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=50)
    UserPwd=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    TelNum=models.CharField(max_length=50)
    Addr=models.CharField(max_length=50)
    #Email=models.CharField(max_length=50)
    #Age=models.IntegerField(max_length=4)
    #Sex=models.CharField(max_length=50)
    #Zipcode=models.CharField(max_length=50)
    class Meta:
        verbose_name=u"用户"
        verbose_name_plural=u"用户"
    
class Orders(models.Model):
    OrderID=models.AutoField(primary_key=True)
    ProductID=models.ForeignKey(ProductInfo)
    UserID=models.ForeignKey(User)
    OrderDate=models.DateTimeField(max_length=8)
    IsStockStatus=models.BooleanField(default=True)
    IsPay=models.BooleanField(default=False)
    IsArrave=models.BooleanField(default=False)
    IsPass=models.BooleanField(default=False)
    IsFinish=models.BooleanField(default=False)
    def __unicode__(self):
        return self.OrderID
    class Meta:
        verbose_name=u"订单"
        verbose_name_plural=u"订单"
        
class Notice(models.Model):
    Context=models.TextField()
    #Context=models.CharField(max_length=500)
    IsNotice=models.BooleanField(default=False)
    def __unicode__(self):
        return self.Context
    class Meta:
        verbose_name=u"公告"
        verbose_name_plural=u"公告"
