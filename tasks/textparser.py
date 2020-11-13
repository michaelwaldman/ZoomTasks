from collections import defaultdict

class TaskTextParser:
    def __init__(self, f):
        self.file = f
        self.nodes = defaultdict(list)

    def _parse(self):
        for line in self.file:
            line = line.split(":")
            message = line[3]
            if '#' not in message:
                continue
            task, person = message.split('#')
            task, person = task.strip(), person.strip()
            person_list = person.split(" ")
            if len(person_list) > 1 and person_list[1] == '--remove':
                if task in self.nodes[person_list[0]]:
                    self.nodes[person_list[0]].remove(task)
            else:
                self.nodes[person.strip()].append(task.strip()) # strip whitespaces from messages

    def getTasks(self):
        self._parse()
        return self.nodes

    def sendEmail(self):
        #TODO
        pass