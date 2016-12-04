from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from users.models import *
from django.core.mail import send_mail

from datetime import datetime

def index(request):
    template = loader.get_template('website/index.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)



    # context = RequestContext(request, { 'officers': officers })
    # return HttpResponse(template.render(context))
    return render(request, 'website/index.html', { 'officers': officers })

def oh(request):
    return render(request, 'website/oh.html', {})

def ir(request):
	return render(request, 'website/ir.html', {})

def interview(request):
	time_dict = {9: "9:00am - 10:00am", 10: "10:00am - 11:00am", 11: "11:00am - 12:00pm", 12: "12:00pm - 1:00pm", 13: "1:00pm - 2:00pm",
				14: "2:00pm - 3:00pm", 15: "3:00pm - 4:00pm", 16: "4:00pm - 5:00pm"}
	days_of_week = [0, 1, 2, 3, 4, 5, 6]
	start_times = {0: 9, 1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
	interview_slot_list = InterviewSlot.objects.all()

	time_slot_dict = {}
	start_time = 9
	for _ in range(len(time_dict)):
		filter_start_time = interview_slot_list.filter(hour=start_time)
		imputed_start_time = []
		for day in days_of_week:
			slot = filter_start_time.filter(day_of_week=day)
			if len(slot) == 0:
				imputed_start_time.append(None)
			else:
				#There should only be one slot from this filter 
				imputed_start_time.append(slot[0])
		time_slot_dict[start_time] = imputed_start_time
		start_time += 1

	now = datetime.now()
	date = datetime.day

	context = {'interview_slot_list': interview_slot_list, 'day': now.strftime("%A"), 'date': date, 
	"time_dict": time_dict, "time_slot_dict": time_slot_dict, "start_times": start_times, 
	"range": range(len(start_times))}

	return render(request, 'website/interview.html', context)

def book_interview(request, slot_id):
	all_slots = InterviewSlot.objects.all()
	for slot in all_slots:
		if slot.slot_id == slot_id:
			context = {'time_slot': slot}
			break
	return render_to_response('website/book_interview.html', RequestContext(request, context))

def confirm_interview(request):
	if request.method == 'POST':
		all_slots = InterviewSlot.objects.all()
		booked_slot = None
		for slot in all_slots:
			if slot.get_date() == request.POST['date'] and slot.hour == int(request.POST['day_hour'][1:]):
				booked_slot = slot
				break
		#if booked_slot == None:
		#	return oh(request)
		booked_slot.student = request.POST['name']
		booked_slot.student_email = request.POST['email']
		booked_slot.availability = False
		booked_slot.save()
		send_confirmation_email(booked_slot)
		return interview(request)
	else:
		return interview(request)

def send_confirmation_email(slot):
	student_email = slot.student_email
	interviewer = slot.officer_username
	profiles = UserProfile.objects.all()
	interviewer_email = None
	for profile in profiles:
		if profile.user.username == interviewer:
			interviewer_email = profile.user.email
	if interviewer_email == None:
		print('oops')
		return
	send_mail(
	    'UPE Technical Interview Confirmation',
	    'You have successfully booked an interview with UPE {}, {}, at {}.'.format(slot.day_of_week, slot.date, slot.hour),
	    'webdev.upe@berkeley.edu',
	    [interviewer_email, student_email],
	    fail_silently=False,
	)
