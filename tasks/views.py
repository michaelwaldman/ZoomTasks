import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from .textparser import TaskTextParser

d = os.getcwd()
FILE = open(d+"/tasks/chat_files/meeting_saved_chat.txt", "r")

def homePageView(request):
    t = TaskTextParser(FILE)
    tasks = t.getTasks()
    return HttpResponse(json.dumps(tasks))



