# 1. Create an empty list called `task_list`

task_list = []

# 2. Add a few `str` elements, representing some everyday tasks e.g. 'Make Dinner'

task_list.append("Brush teeth")
task_list.append("Pack bag")
task_list.append("Find keys")
task_list.append("Eat lunch")
task_list.append("Watch Netlix")
task_list.append("Sleep")

# 3. Print out `task_list`

print(task_list)

# 4. Remove the last task

task_list.pop()

# 5. Print out `task_list`

print(task_list)

# 6. Print out the number of elements in `task_list`

print(len(task_list))

task_list.insert(3, "Heat up lunch")
print(task_list)