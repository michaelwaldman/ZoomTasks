import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from .textparser import TaskTextParser
from json2html import *

d = os.getcwd()
FILE = open(d+"/tasks/chat_files/meeting_saved_chat.txt", "r")

def homePageView(request):
    t = TaskTextParser(FILE)
    tasks = t.getTasks()
    tData = json.dumps(tasks)
    tableData = json2html.convert(json = tData)
    line_index = 8
    lines = None
    with open("homepage.html", 'r') as file:
        lines = file.readlines()

    lines[line_index] = tableData

    with open("homepage.html", "w") as file:
        file.writelines(lines)
    return HttpResponse(tData)