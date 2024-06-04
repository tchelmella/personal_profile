from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    dic = {}
    for word in word_list:
        dic[word] = dic.get(word,0) + 1
    dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
    return render(request,'count.html',{'fulltext':full_text,'len_of_text':len(full_text.split(" ")),"word_dic":dic})
