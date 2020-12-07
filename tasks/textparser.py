from collections import defaultdict
import re
import json
from json2html import *
from django.core.mail import send_mail
from django.utils.html import strip_tags
import datetime

class TaskTextParser:
    def __init__(self, f):
        self.file = f
        self.nodes = defaultdict(list)
        self.emails = defaultdict(str) # person to hashtag
    
    def is_valid_email(self, email):  
        if(re.search(r"[^@]+@[^@]+\.[^@]+",email)):  
            return True
        return False
    
    # def getEmails(self):
    #     for line in self.file:
    #         line = line.split(":")
    #         message = line[3]
    #         if '#' not in message:
    #             continue
    #         email, person = message.split('#')
    #         email, person = email.strip(), person.strip()
    #         if self.is_valid_email(email):
    #             self.emails[email] = person
    #     return self.emails

    def _parse(self):
        for line in self.file:
            line = line.split(":")
            if len(line) > 3:
                message = line[3]
            if '#' not in message:
                continue
            task, person = message.split('#')
            task, person = task.strip(), person.strip()
            person_list = person.split(" ")
            if len(person_list) > 1 and person_list[1] == '--remove':
                if task in self.nodes[person_list[0]]:
                    self.nodes[person_list[0]].remove(task)
            elif self.is_valid_email(task):
                self.emails[task] = person
            else:
                self.nodes[person.strip()].append(task.strip()) # strip whitespaces from messages

    def getTasks(self):
        self._parse()
        return self.nodes
    
    def sendEmail(self):
        tasks = self.getTasks()
        emails = self.emails
        from_email='ans_stmp_server@outlook.com'
        now = datetime.datetime.now()

        for user_email in emails:
            data = tasks[emails[user_email]]
            message = "Thanks for using Follow Ups! on Zoom. Your tasks from your Zoom meeting on " + now.strftime("%Y-%m-%d %H:%M:%S") + " are as follows: \n\n"
            title = emails[user_email] + ', your task list from your ' + now.strftime("%Y-%m-%d %H:%M:%S") + ' Zoom Meeting'
            for i, task in enumerate(data):
                message += str(i+1) + '. ' + task + '\n'
            send_mail(
                title, 
                message, 
                from_email, 
                [user_email], 
            )
            print("Email sent")