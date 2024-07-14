from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import blogform
from .forms import blog
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request,'home.html')
def home(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
        context = {
            'username':request.COOKIES['username'],
            'login_status':request.COOKIES.get('logged_in'),
        }
        return render(request,'home.html',context)
    else:
        return render(request,'login.html')
def create(request):
    # return render(request ,'create.html')
    if request.method=='POST':
        form=blogform(request.POST)
        if form.is_valid():
            
            form.save()
    form=blogform()
    dict_form={
        'form':form
    }
    return render(request,'create.html',dict_form)
def viewall(request):
    blog_dict={
        'blo': blog.objects.all()
                }
    return render(request,'viewall.html',blog_dict)
    # return render(request,'viewall.html')
def login(request):
    if request.method == 'GET':
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context= {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request,'home.html',context)
        else:
            return render(request,'login.html')
    if request.method == "POST":
        username=request.POST.get('email')
        context = {
            'username':username,
            'login_status':'TRUE'
        }
        response = render(request,'home.html',context)

        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response
def logout(request):
    response=HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('logged_in')
    return response

class TaskDeleteView(DeleteView):
    model= blog
    template_name='delete.html'
    success_url=reverse_lazy('pg1')

class TaskDetailview(DetailView):
    model=blog
    template_name='detailblog.html'
    context_object_name='blog'


class TaskUpdateView(UpdateView):
    model=blog
    template_name='update.html'
    fields=('blog_name','blog_discription')
    success_url=reverse_lazy('pg3')


