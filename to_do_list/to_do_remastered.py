class ToDoList():
    def __init__(self, *tasks):
        for task in tasks:
            if not isinstance(task, Task):
                raise ValueError("Please enter only Task objects!")
        self._tasks=list(tasks)
    def __len__(self):
        return len(self._tasks)
    def __iter__(self):
        return iter(self._tasks)
    def __repr__(self):
        return f"{[i.title for i in self._tasks]}"
    def see_list(self):
        if len(self._tasks)==0:
            return "Nothing in the list"
        return [f"{i}. {task.title} : {'Done' if task.status else 'Pending'}" for i,task in enumerate(self._tasks, start=1)]
    def add_task(self, task):
        if isinstance(task, Task):
            self._tasks.append(task)
        else:
            raise TypeError('Please, only Task objects!')
    def delete_task(self, id):
        if 0<id<=len(self._tasks):
            self._tasks.pop(id-1)
            return
        raise ValueError('Nothing with that ID')
    
    def get_json(self, filename):
        import json, os
        PATH=os.path.join(os.path.dirname(__file__),filename)
        try:
            with open(PATH, 'r') as file:
                data=json.load(file)
        except [json.JSONDecodeError, FileNotFoundError]:
            return f"{filename} file was not found"
        self._tasks=[Task(title=task['title']) for task in data]
        for i,j in zip(self._tasks, data):
            i.status=j['status']
    def clear_list(self, filename):
        import json, os
        PATH=os.path.join(os.path.dirname(__file__),filename)
        with open(PATH, 'w') as file:
            json.dump([], file)


        
        
        
    def set_json(self, filename):
        import json, os 
        data=[{'title':task.title, 'status':task.status} for task in self._tasks]
        PATH=os.path.join(os.path.dirname(__file__),filename)
        with open(PATH, 'w') as file:
            json.dump(data, file, indent=4)

        
                   
class Task():
    def __init__(self, title):
        self._title=title
        self._status=False
    def mark_as_complete(self):
        self._status=True

    def __repr__(self):
        return f"Task({self.title})"
    @property
    def title(self):
        return self._title
    @property
    def status(self):
        return self._status 
    @status.setter
    def status(self, value):
        if not isinstance(value, bool):
            raise ValueError("Status value must be True or False")
        self._status=value
    
task1=Task('Running')
task2=Task("Exercising")
list1=ToDoList()
list2=ToDoList(task1, task2)


list2.set_json('todo_list.json')

list1.get_json('todo_list.json')


list1.clear_list('todo_list.json')

print(list1, list2)




           


