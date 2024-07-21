tasks = []


def addTheTask():
  task = input("Enter the task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")


def listTheTasks():
  if not tasks:
    print("There are no tasks.")
  else:
    print("Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task {index}.) {task}")


def deleteTheTask():
  listTheTasks()
  try:
    taskToDelete = int(input("Enter the task number to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task {taskToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  print("Lets get things done!")
  while True:
    print("\n")
    print("What do you want to do?")
    print("------------------------------------------")
    print("1. Add task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")
    print("------------------------------------------")
    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTheTask()
    elif (choice == "2"):
      deleteTheTask()
    elif (choice == "3"):
      listTheTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("See you Soon Buddy")
