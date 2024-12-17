import time

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f'Задача "{title}" добавлена.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Задача "{removed_task.title}" удалена.')
        else:
            print("Неверный индекс задачи.")

    def display_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Список задач:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")


def main():
    todo_list = ToDoList()

    todo_list.add_task("Купить продукты")
    todo_list.add_task("Сделать домашнее задание")
    todo_list.add_task("Погулять с собакой")
    todo_list.display_tasks()
    todo_list.remove_task(1) 
    todo_list.display_tasks()
    todo_list.tasks[0].mark_completed()

    todo_list.display_tasks()
    
    while True:
        print("Программа работает...")
        time.sleep(5)  


if __name__ == "__main__":
    main()
