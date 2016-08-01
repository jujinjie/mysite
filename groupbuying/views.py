#coding:utf-8
#from django.shortcuts import render, render_to_response,RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from groupbuying.models import Notice, ProductInfo
#from django.template import Template, Context 
#from _mysql import NULL
#from django import forms
#from django.contrib.auth.models import User

# Create your views here.
def gs_main(request):
    my_notice=Notice.objects.filter(IsNotice=True)
    now_sale_id=ProductInfo.objects.filter(IsOut=False).values('GroupID').distinct()
    dic_context={}
    lst_con=[]
    if  (len(now_sale_id)>=2):
        for now_sale_id_s in now_sale_id:
            now_sale_goods=ProductInfo.objects.filter(GroupID=now_sale_id_s['GroupID'])
            lst_con.append(now_sale_goods)
        dic_context['item_list']=lst_con
    if (len(now_sale_id)==1):
        now_sale_goods=ProductInfo.objects.filter(GroupID=now_sale_id)
        dic_context['item_list']=now_sale_goods
    if len(my_notice)>0:
        dic_context['myNotice']=my_notice[0]
        
    else:
        dic_context['item_list']=now_sale_goods

    return  render_to_response('index.html',dic_context)



def selectpost(request):
    #ctx ={}
    #ctx.update(csrf(request))
    if 'check' in request.GET:    
        #message = 'You searched for: %r' %request.GET.getlist('check')
        message=''
        messagelist=request.GET.getlist('check')
        for m in messagelist:
            p=ProductInfo.objects.filter(GroupID=m)
            print p
            #mm='%s'%m
            #message+=mm
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
    #    ctx['rlt'] = request.POST['q']
    #return render(request, "index.html", ctx)
    

