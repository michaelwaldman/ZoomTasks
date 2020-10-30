from django.shortcuts import render
from django.http import HttpResponse
import json
f = open("/Users/mwaldman/Desktop/taskapp/TaskApp/tasks/meeting_saved_chat.txt", "r")
from collections import defaultdict

# Get file

class TaskTextParser:
    def __init__(self, f):
        self.file = f
        self.nodes = defaultdict(list)
    
    def _parse(self):
        for line in f:
            line = line.split(":")
            message = line[3]
            print(message)
            if '#' not in message:
                continue
            task, person = message.split('#') # finish backend , itay
            self.nodes[person].append(task)
    
    def getTasks(self):
        self._parse()
        return self.nodes
    
    def sendEmail(self):
        #TODO
        pass

def homePageView(request):
    t = TaskTextParser(f)
    tasks = t.getTasks()
    return HttpResponse(json.dumps(tasks))



