from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello World</h1>")
    
def about(request):
    cursor=connection.cursor()
    cursor.execute("select * from post")
    columns = [col[0] for col in cursor.description]
    # print(cursor.fetchall())
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
            ]
    print(posts)
    context={'keyposts':posts}
    return render(request,'harsh/home.html',context) 

def insert(request):
    return render(request,'harsh/form.html')
    
def match(request):
    print(request)
    Name = request.POST['blogTitle']
    Summary = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO post (`Name`,`Summary`) VALUES ( %s, %s );", (Name, Summary))
    return redirect('/text/about')     

def edit(request,pk):
    print(pk)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * from post where softdelete = 0 and pid = {pk} ")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context = {
        'keyposts': posts[0]
    }
    print(context)
    return render(request,'harsh/form.html',context)

# def delete(request,pk):
#     print(pk)
#     cursor = connection.cursor()
#     cursor.execute(f"UPDATE post set softdelete=1 where pid={pk}")   
#     return render(request,'harsh/form.html')

def delete(request,pk):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE post set softdelete=1 where pid={pk}")
    return redirect('/text/about/')