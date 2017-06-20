
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import ContactDetailsForm, ServiceDescriptionForm, ServiceOwnerForm, EndUserForm, AdministrativeLevelForm, DeliveryChannelForm, AccessibilityForm, ServiceConsumptionForm, ReuseAndSharingForm
from django.contrib.auth.decorators import login_required

     

def contactdetails(request):
    if request.method == "POST":
        form = ContactDetailsForm(request.POST)
        if form.is_valid():
            contact_details = form.save(commit=False)   
            contact_details.user = request.user
            contact_details.save() 
            return redirect('questionnaire:servicedescription')
    else:
        form = ContactDetailsForm()
    return render(request, 'questionnaire/contactdetails.html', {'form':form})

def servicedescription(request):
    if request.method == "POST":
        form = ServiceDescriptionForm(request.POST)
        if form.is_valid():
            service_description = form.save(commit=False)   
            service_description.user = request.user
            service_description.save() 
            return redirect('questionnaire:serviceowner')
    else:
        form = ServiceDescriptionForm()
    return render(request, 'questionnaire/servicedescription.html', {'form':form})

def serviceowner(request):
    if request.method == "POST":
        form = ServiceOwnerForm(request.POST)
        if form.is_valid():
            service_owner = form.save(commit=False)   
            service_owner.user = request.user
            service_owner.save() 
            return redirect('questionnaire:enduser')
    else:
        form = ServiceOwnerForm()
    return render(request, 'questionnaire/serviceowner.html', {'form':form})

def enduser(request):
    if request.method == "POST":
        form = EndUserForm(request.POST)
        if form.is_valid():
            end_user = form.save(commit=False)   
            end_user.user = request.user
            end_user.save() 
            return redirect('questionnaire:administrativelevel')
    else:
        form = EndUserForm()
    return render(request, 'questionnaire/enduser.html', {'form':form})

def administrativelevel(request):
    if request.method == "POST":
        form = AdministrativeLevelForm(request.POST)
        if form.is_valid():
            administrative_level = form.save(commit=False)   
            administrative_level.user = request.user
            administrative_level.save() 
            return redirect('../6')
    else:
        form = AdministrativeLevelForm()
    return render(request, 'questionnaire/administrativelevel.html', {'form':form})
 
def area1(request):
    return render(request, 'questionnaire/area1.html')

def maturity(request):
    return render(request, 'questionnaire/maturity.html')

   
def servicedelivery(request):
    return render(request, 'questionnaire/servicedelivery.html')

def deliverychannel(request):
    if request.method == "POST":
        form = DeliveryChannelForm(request.POST)
        if form.is_valid():
            traditional_channel = form.save(commit=False)   
            traditional_channel.save()
            digital_channel = form.save(commit=False)   
            digital_channel.save()

            if digital_channel.form == NULL:
                return render( 'questionnaire/accessibity.html')                
            else:
                return redirect('questionnaire:area3')
    else:
        form = DeliveryChannelForm()
    return render(request, 'questionnaire/deliverychannel.html', {'form':form})

def serviceconsumption(request):
    if request.method == "POST":
        form = ServiceConsumptionForm(request.POST)
        if form.is_valid():
            service_consumption = form.save(commit=False)   
            service_consumption.save()
            return redirect('../18')
    else:
        form = ServiceConsumptionForm()
    return render(request, 'questionnaire/serviceconsumption.html', {'form':form})

def reuseandsharing (request):
    if request.method == "POST":
        form = ReuseAndSharingForm(request.POST)
        if form.is_valid():
            reuse_and_sharing = form.save(commit=False)   
            reuse_and_sharing.save()
            return redirect('../22')
    else:
        form = ReuseAndSharingForm()
    return render(request, 'questionnaire/reuseandsharing.html', {'form':form})



class Area2View(generic.ListView):
    template_name = 'questionnaire/area2.html'
    context_object_name = 'area2_question_list'

    def get_queryset(self):
        return Question.objects.filter(area_id=2)  

class Area3View(generic.ListView):
    template_name = 'questionnaire/area3.html'
    context_object_name = 'area3_question_list'

    def get_queryset(self):
        return Question.objects.filter(area_id=3) 

class Area4View(generic.ListView):
    template_name = 'questionnaire/area4.html'
    context_object_name = 'area4_question_list'

    def get_queryset(self):
        return Question.objects.filter(area_id=4) 


def accessibility(request):
     if request.method == "POST":
        form = AccessibilityForm(request.POST)
        if form.is_valid():
            accessibility = form.save(commit=False)
            accessibility.save()
            return redirect( 'questionnaire:prefillingform')                
     else:
        form = AccessibilityForm()
     return render(request, 'questionnaire/accessibility.html', {'form':form})

def prefillingform(request):
    return render(request, 'questionnaire/prefillingform.html')


def index(request):
    area_list = Area.objects.order_by('symbol')[:]
    context = {'area_list': area_list}
    return render(request, 'questionnaire/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'questionnaire/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'questionnaire/results.html'
  

def score(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_answer = question.answer_set.get(pk=request.POST['answer'])     
    except (KeyError, Answer.DoesNotExist):
        return render(request, 'questionnaire/detail.html', {
            'question': question,
            'error_message': "Δεν επιλέξατε απάντηση.",
        })
    else:
        selected_answer_mat = question.weight*selected_answer.score
        print(selected_answer_mat)
        print(selected_answer.answer_text)
        selected_answer_id = selected_answer.id
        selected_answer.save()
        return HttpResponseRedirect(reverse('questionnaire:results', args=(question.id,)))

   
        

def place(request):
    return HttpResponse(area_text)




# Create your views here.
