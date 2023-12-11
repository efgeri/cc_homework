from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
# as means importing it with an alias, so it's easier to hivatkoz this()we don't have to use to whole file name again)

task_repository.delete_all()
user_repository.delete_all()

user1 = User("Jack", "Jarvis")
user_repository.save(user1)

user2 = User("John", "Doe")
user_repository.save(user2)


task1 = Task("Pick up milk", user1, 30)
task_repository.save(task1)

task2 = Task("Hoovering", user2, 40)
task_repository.save(task2)

task1.description = "Pick up oat milk"
task_repository.update(task1)

result = task_repository.select_all()

for task in result:
    print(f"{task.description} is assigned to {task.user.first_name}")

user1_tasks = task_repository.tasks_for_user(user1)

print(f"{user1.first_name}'s tasks:")
for task in user1_tasks:
    print(f"{task.description}")