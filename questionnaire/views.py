
# -*- coding: utf-8 -*-
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from .forms import ContactDetailsForm, ServiceDescriptionForm, ServiceOwnerForm, EndUserForm, AdministrativeLevelForm, DeliveryChannelForm, ServiceConsumptionForm, ReuseAndSharingForm
from django.contrib.auth.decorators import login_required
import math

     

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
            return redirect('questionnaire:administrative_level')
    else:
        form = EndUserForm()
    return render(request, 'questionnaire/enduser.html', {'form':form})

def administrative_level(request):
    if request.method == "POST":
        form = AdministrativeLevelForm(request.POST)
        if form.is_valid():
            administrative_level = form.save(commit=False)   
            administrative_level.user = request.user
            administrative_level.save() 
            return redirect('../6')
    else:
        form = AdministrativeLevelForm()
    return render(request, 'questionnaire/administrative_level.html', {'form':form})
 
def area1(request):
    return render(request, 'questionnaire/area1.html')

def imm(request):
    return render(request, 'questionnaire/imm.html')

def recommendations1(request):
    b1maturity = sum(answer.maturity for answer in Answer.objects.all()[0:4])
    b2maturity = sum(answer.maturity for answer in Answer.objects.all()[4:8])
    b3maturity = sum(answer.maturity for answer in Answer.objects.all()[8:12])
    b4maturity = sum(answer.maturity for answer in Answer.objects.all()[12:17])
    b5maturity = sum(answer.maturity for answer in Answer.objects.all()[17:21])
    b6maturity = sum(answer.maturity for answer in Answer.objects.all()[21:25])
    b7maturity = sum(answer.maturity for answer in Answer.objects.all()[25:27])
    b8maturity = sum(answer.maturity for answer in Answer.objects.all()[27:30])
    b9maturity = sum(answer.maturity for answer in Answer.objects.all()[30:34])
    b10maturity = sum(answer.maturity for answer in Answer.objects.all()[34:39])
    b11maturity = sum(answer.maturity for answer in Answer.objects.all()[39:42])
    print(b1maturity, b2maturity, b3maturity, b4maturity, b5maturity, b6maturity, b7maturity, b8maturity, b9maturity, b10maturity, b11maturity)
    return render(request, 'questionnaire/recommendations1.html', {'b1maturity':b1maturity, 'b2maturity':b2maturity, 'b3maturity':b3maturity, 'b4maturity':b4maturity, 'b5maturity':b5maturity, 'b6maturity':b6maturity, 'b7maturity':b7maturity, 'b8maturity':b8maturity, 'b9maturity':b9maturity, 'b10maturity':b10maturity, 'b11maturity':b11maturity,})

def recommendations2(request):
    c2maturity = sum(answer.maturity for answer in Answer.objects.all()[42:47])
    c3maturity = sum(answer.maturity for answer in Answer.objects.all()[47:50])
    c4maturity = sum(answer.maturity for answer in Answer.objects.all()[50:54])
    print(c2maturity, c3maturity, c4maturity)
    return render(request, 'questionnaire/recommendations2.html', {'c2maturity':c2maturity, 'c3maturity':c3maturity, 'c4maturity':c4maturity,})

def recommendations3(request):
    
    d1maturity = sum(answer.maturity for answer in Answer.objects.all()[54:59])
    d2maturity = sum(answer.maturity for answer in Answer.objects.all()[59:62])
    d3maturity = sum(answer.maturity for answer in Answer.objects.all()[62:65])
    d4maturity = sum(answer.maturity for answer in Answer.objects.all()[65:69])
    d5maturity = sum(answer.maturity for answer in Answer.objects.all()[69:71])
    d6maturity = sum(answer.maturity for answer in Answer.objects.all()[71:75])
    d7maturity = sum(answer.maturity for answer in Answer.objects.all()[75:77])
    d8maturity = sum(answer.maturity for answer in Answer.objects.all()[77:80])
    print(d1maturity, d2maturity, d3maturity, d4maturity, d5maturity, d6maturity, d7maturity, d8maturity)
    return render(request, 'questionnaire/recommendations3.html', {'d1maturity':d1maturity, 'd2maturity':d2maturity, 'd3maturity':d3maturity, 'd4maturity':d4maturity, 'd5maturity':d5maturity, 'd6maturity':d6maturity, 'd7maturity':d7maturity, 'd8maturity':d8maturity,})

def maturity(request):
    area2maturity = sum(answer.maturity for answer in Answer.objects.all()[0:42])*2
    area3maturity = sum(answer.maturity for answer in Answer.objects.all()[42:54])*5
    area4maturity = float(sum(answer.maturity for answer in Answer.objects.all()[54:80]))*3.333
    totalmaturity = sum(answer.maturity for answer in Answer.objects.all())
    return render(request, 'questionnaire/maturity.html', {'totalmaturity':totalmaturity, 'area2maturity':area2maturity, 'area3maturity':area3maturity, 'area4maturity':area4maturity,})

def initialize(request):
    for answer in Answer.objects.all():
        answer.maturity = 0
        answer.save()
    reuse_and_sharing.maturity = 0
    return redirect( 'questionnaire:contactdetails')
   
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

def service_consumption(request):
    if request.method == "POST":
        form = ServiceConsumptionForm(request.POST)
        if form.is_valid():
            service_consumption = form.save(commit=False)   
            service_consumption.save()
            return redirect('../18')
    else:
        form = ServiceConsumptionForm()
    return render(request, 'questionnaire/service_consumption.html', {'form':form})

def reuse_and_sharing (request):
    if request.method == "POST":
        form = ReuseAndSharingForm(request.POST)
        if form.is_valid():
            reuse_and_sharing = form.save(commit=False)
            q = len(reuse_and_sharing.get_choices_selected('form')) 
            if q == 1 : reuse_and_sharing.maturity=0.075
            elif q == 2 : reuse_and_sharing.maturity=0.15
            elif q == 3 : reuse_and_sharing.maturity=0.225
            elif q == 4 : reuse_and_sharing.maturity=0.3 
            else: q == 0
            print(q)
            print(reuse_and_sharing.maturity)
            for answer in Answer.objects.all()[56:56]:
                answer.maturity = reuse_and_sharing.maturity
            reuse_and_sharing.save()
            return redirect('../22')
    else:
        form = ReuseAndSharingForm()
    return render(request, 'questionnaire/reuse_and_sharing.html', {'form':form})



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
        selected_answer.maturity = selected_answer.score
        print(selected_answer.maturity)
        print(selected_answer.answer_text)
        selected_answer.save()
        if question.id == 16: 
            return redirect('questionnaire:service_consumption')
        elif question.id == 28:
            return redirect('questionnaire:maturity')
        else:
            return HttpResponseRedirect(reverse('questionnaire:detail', args=(question.id+1,)))

   
        
def place(request):
    return HttpResponse(area_text)




# Create your views here.
