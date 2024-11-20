tasks = [
    {'id': 1, 'name' : 'dishes', 'subtasks': None, 'priority': 1},
    {'id': 2, 'name' : 'shopping', 'subtasks': [{'id': 4, 'name' : 'check fridge', 'subtasks': None, 'priority': 2}, {'id': 7, 'name' : 'make list', 'subtasks': None, 'priority': 2}], 'priority': 3},
    {'id': 3, 'name' : 'cleaning', 'subtasks': [{'id': 6, 'name' : 'trash', 'subtasks': None, 'priority': 6}, {'id': 8, 'name' : 'dusting', 'subtasks': None, 'priority': 6}], 'priority': 5}
]

newtasks = []

def schedule_tasks(arr):
    for task in arr:
        newtasks.append(task)
        if isinstance(task['subtasks'], list) and task['subtasks']:
            schedule_tasks(task['subtasks'])
        
    x = sorted(newtasks, key=lambda x: x.get('priority'))
    return x


zoom = schedule_tasks(tasks)
for task in zoom:
    print(task)

#time & space complexity: for smaller cases this should work efficiently, but for larger 
#or deeply nested data sets, recursion could be more system intensive than iterative traversal
#using a stack or queue. If priorities are in a discrete range, a bucket sort might be
#more efficient