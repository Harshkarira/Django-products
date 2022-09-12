from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db import connection

# Create your views here.
def home(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * from posts where softdelete = 0")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context = {
        'keyposts': posts
    }
    return render(request,'blogapp/home.html',context)
    #return HttpResponse("<h1> Hello World </h1>")
def create(request):
    return render(request,'blogapp/forms.html')
def insert(request):
    return redirect('/blog/home')
def add(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from posts where softdelete = 0")
    return redirect('/blog/home/')

def edit(request,pk):
    print(pk)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * from posts where softdelete = 0 and id = {pk} ")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context = {
        'keyposts': posts[0]
    }
    print(context)
    return render(request,'blogapp/editform.html',context)

def update(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    id = request.POST['id']
    cursor = connection.cursor()
    cursor.execute("UPDATE posts set title = %s ,content = %s  where id = %s", (title, content, id))
    cursor = connection.cursor()
    return redirect('/blog/home')

def delete(request,pk):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE posts set softdelete=1 where id={pk}")
    return redirect('/blog/home')
    
