
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
#from .models import Post
#from .forms import PostForm,LoginForm #, UserRegistrationForm, UserEditForm, ProfileEditForm

from .models import *
from django.contrib.auth import authenticate, login#, logout
from django.views.generic.edit import FormView
from .forms import ContactDetailsForm, ServiceDescriptionForm, ServiceOwnerForm, EndUserForm, AdministrativeLevelForm
from django.contrib.auth.decorators import login_required
#from django.contrib import messages 
#from .models import Profile

#def user_login(request):
#    if request.method == 'POST':
#        form = LoginForm(request.POST)
 #       if form.is_valid():
 #           cd = form.cleaned_data
 #           user = authenticate(username=cd['username'], password=cd['password'])
 #           if user is not None:
 #               if user.is_active:
 #                   login(request, user)
 #                   return HttpResponse('Authenticated successfully')
 #               else:
 #                   return HttpResponse('Disabled account')
 #           else:
 #               return HttpResponse('Invalid login')
 #   else:
 #       form = LoginForm()
 #   return render(request, 'questionnaire/login.html', {'form': form})

    
#def service_context(request):
 #   if request.method == "POST":
  #      form = ServiceContextForm(request.POST)
   #     if form.is_valid():
    #        service_context = form.save(commit=False)   
     #       service_context.user = request.user
      #      service_context.save() 
       #     return redirect(request, 'questionnaire/service_delivery.html')
   # else:
    #    form = ServiceContextForm()
    #return render(request, 'questionnaire/service_context.html', {'form':form})
     

def contact_details(request):
    if request.method == "POST":
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            contact_details = form.save(commit=False)   
            contact_details.user = request.user
            contact_details.save() 
            return redirect('service_description', user=request.user)
    else:
        form = ContactDetailsForm()
    return render(request, 'questionnaire/contact_details.html', {'form':form})

def service_description(request):
    if request.method == "POST":
        form = ServiceDescriptionForm(request.POST)
        if form.is_valid():
            service_description = form.save(commit=False)   
            service_description.user = request.user
            service_description.save() 
            return redirect('service_owner', user=request.user)
    else:
        form = ServiceDescriptionForm()
    return render(request, 'questionnaire/service_description.html', {'form':form})

def service_owner(request):
    if request.method == "POST":
        form = ServiceOwnerForm(request.POST)
        if form.is_valid():
            service_owner = form.save(commit=False)   
            service_owner.user = request.user
            service_owner.save() 
            return redirect('end_user', user=request.user)
    else:
        form = ServiceOwnerForm()
    return render(request, 'questionnaire/service_owner.html', {'form':form})

def end_user(request):
    if request.method == "POST":
        form = EndUserForm(request.POST)
        if form.is_valid():
            end_user = form.save(commit=False)   
            end_user.user = request.user
            end_user.save() 
            return redirect('administrative_level', user=request.user)
    else:
        form = EndUserForm()
    return render(request, 'questionnaire/end_user.html', {'form':form})

def administrative_level(request):
    if request.method == "POST":
        form = AdministrativeLevelForm(request.POST)
        if form.is_valid():
            administrative_level = form.save(commit=False)   
            administartive_level.user = request.user
            administrative_level.save() 
            return redirect('service_delivery', user=request.user)
    else:
        form = AdministrativeLevelForm()
    return render(request, 'questionnaire/administrative_level.html', {'form':form})

   
def service_delivery(request):
    return render(request, 'questionnaire/service_delivery.html')

def index(request):
    area_list = Area.objects.order_by('symbol')[:]
    context = {'area_list': area_list}
    return render(request, 'questionnaire/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionnaire/results.html', {'question': question})


def score(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, AnswerDoesNotExist):
        return render(request, 'questionnaire/detail.html', {
            'question': question,
            'error_message': "Δεν επιλέξατε απάντηση.",
        })
    else:
        selected_answer.save()
        return HttpResponseReDirect(reverse('questionnaire:results', args=(question_id,)))


def place(request):
    return HttpResponse(area_text)

#def post_list(request):
#    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'questionnaire/post_list.html', {'posts':posts})

#def post_detail(request, pk):
#    post=get_object_or_404(Post, pk=pk)
#    return render(request, 'questionnaire/post_detail.html', {'post':post})

#def post_new(request):
#    if request.method == "POST":
 #       form = PostForm(request.POST)
 #       if form.is_valid():
  #          post = form.save(commit=False)
   #         post.author = request.user
    #        post.published_date = timezone.now()
     #       post.save()
      #      return redirect('post_detail', pk=post.pk)
    #else:
    #    form = PostForm()
    #return render(request, 'questionnaire/post_edit.html', {'form': form})

#def post_edit(request, pk):
#    post = get_object_or_404(Post, pk=pk)
 #   if request.method == "POST":
  #      form = PostForm(request.POST, instance=post)
   #     if form.is_valid():
    #        post = form.save(commit=False)
     #       post.author = request.user
      #      post.published_date = timezone.now()
       #     post.save()
        #    return redirect('post_detail', pk=post.pk)
  #  else:
   #     form = PostForm(instance=post)
   # return render(request, 'questionnaire/post_edit.html', {'form': form})

#def login(request):
 #   return render(request, 'questionnaire/login.html', {})

# Create your views here.
