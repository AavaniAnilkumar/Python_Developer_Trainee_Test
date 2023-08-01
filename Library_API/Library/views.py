# books/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import generics
from .models import Books
from .serializers import BookSerializer
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


def form(request):
    return render(request,'form.html')

def formsave(request):
    if request.method == "POST":
        t = request.POST.get('title')
        a = request.POST.get('author')
        p = request.POST.get('price')
        obj = Books(title=t, author=a, price=p)
        obj.save()
        return redirect(formtable)
    
def formtable(request):
    data = Books.objects.all()
    return render(request,"form_table.html",{'data':data})

def formedit(request,dataid):
    data = Books.objects.get(id=dataid)
    print(data)
    return render(request,"form_edit.html",{"data":data})


def formupdate(request,dataid):
    if request.method=="POST":
        t = request.POST.get('title')
        a = request.POST.get('author')
        p = request.POST.get('price')
        Books.objects.filter(id=dataid).update(title=t,author=a,price=p)
        return redirect(formtable)



def formdelete(request,dataid):
    data = Books.objects.filter(id=dataid)
    data.delete()
    return redirect(formtable)
