class ToDoList():
    def __init__(self, *tasks):
        self._tasks=list(tasks)
    def see_list(self):
        if len(self._tasks)==0:
            return "Nothing in the list"
        return [f"{task.id}. {task.title} : {'Done' if task.status == True else 'Pending'}" for task in self._tasks]
    def add_task(self, task):
        self._tasks.append(task)
    def delete_task(self, id):
        if id>=len(self._tasks):
            print("Nothing with that ID!")
        else:    
            for i in self._tasks:
                if i.id==id:
                    self._tasks.remove(i)
                    break
                   


class Task():
    task_id=0
    def __init__(self, title):
        self._title=title
        self._status=False
        self._id=Task.task_id
        Task.task_id+=1
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
    @property
    def id(self):
        return self._id         

task1=Task('Piano')
list1=ToDoList()
list1.add_task(task1)
print(list1.see_list())
list1.delete_task(1)
print(list1.see_list())         