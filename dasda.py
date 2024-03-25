class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Задача '{task}' добавлена в список.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Задача '{task}' удалена из списка.")
        else:
            print(f"Задачи '{task}' нет в списке.")

    def show_tasks(self):
        if self.tasks:
            print("Текущие задачи:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("Список задач пуст.")

my_todo_list = ToDoList()

my_todo_list.add_task("Выучить Python")
my_todo_list.add_task("Сделать покупки")
my_todo_list.add_task("Погулять с собакой")

my_todo_list.show_tasks()

my_todo_list.remove_task("Сделать покупки")

my_todo_list.show_tasks()