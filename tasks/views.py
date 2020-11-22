import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from .textparser import TaskTextParser
from json2html import *
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

d = os.getcwd()
FILE = open(d+"/tasks/chat_files/meeting_saved_chat.txt", "r")

def homePageView(request):
    t = TaskTextParser(FILE)
    tasks = t.getTasks()
    tData = json.dumps(tasks)
    return HttpResponse(tData)

def emailView(request):
    t = TaskTextParser(FILE)
    tasks = t.getTasks()
    tData = json.dumps(tasks)
    user_email = request.GET.get('email')
    #print(user_email)
    html_msg = json2html.convert(json = tData)
    #html_message = render_to_string(html_msg, {'context': 'values'})
    plain_msg = strip_tags(html_msg)
    from_email='ans_stmp_server@outlook.com'

    send_mail(
        'Your Zoom Task List',
        tData,
        from_email,
        [user_email],
        #html_message=tData,
        )

    return HttpResponse(request.GET.get('email'))

class RenderedTaskView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = TaskTextParser(FILE)
        tasks = t.getTasks()
        t.sendEmail()
        context['users'] = dict(tasks)
        return context
