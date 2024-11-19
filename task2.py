tasks = [
    {'id': 1, 'name' : 'dishes', 'subtasks': None, 'priority': 1},
    {'id': 2, 'name' : 'shopping', 'subtasks': [{'id': 4, 'name' : 'check fridge', 'subtasks': None, 'priority': 2}, {'id': 7, 'name' : 'make list', 'subtasks': None, 'priority': 2}], 'priority': 3},
    {'id': 3, 'name' : 'cleaning', 'subtasks': [{'id': 6, 'name' : 'trash', 'subtasks': None, 'priority': 6}, {'id': 8, 'name' : 'dusting', 'subtasks': None, 'priority': 6}], 'priority': 5}
]

newtasks = []

def schedule_tasks(arr):
    for task in arr:
        if task not in newtasks:
            newtasks.append(task)
            if isinstance(task['subtasks'], list) and task['subtasks']:
                schedule_tasks(task['subtasks'])
        
        
    x = sorted(newtasks, key=lambda x: x.get('priority'))
    for y in x:
        print(y)

schedule_tasks(tasks)