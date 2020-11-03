from collections import defaultdict

class TaskTextParser:
    def __init__(self, f):
        self.file = f
        self.nodes = defaultdict(list)
    
    def _parse(self):
        for line in self.file:
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