from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html') 

def counter(request):
    text=request.GET['usertext']
    word_text=text.split(' ')
    return render(request,'counter.html',{'key':text,'total':len(word_text)})