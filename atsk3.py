def schedule_tasks(tasks):
    """
    Schedules tasks based on priority, ensuring subtasks are handled recursively.
    
    Args:
        tasks (list): A list of tasks to be scheduled.
    
    Returns:
        list: A sorted list of tasks by priority.
    """
    all_tasks = []

    def collect_tasks(task_list):
        for task in task_list:
            all_tasks.append(task)
            if isinstance(task['subtasks'], list) and task['subtasks']:
                collect_tasks(task['subtasks'])

    # Collect all tasks and subtasks
    collect_tasks(tasks)

    # Sort tasks by priority (lower values = higher priority)
    return sorted(all_tasks, key=lambda x: x.get('priority'))

# Input data
tasks = [
    {'id': 1, 'name': 'dishes', 'subtasks': None, 'priority': 1},
    {'id': 2, 'name': 'shopping', 'subtasks': [
        {'id': 4, 'name': 'check fridge', 'subtasks': None, 'priority': 2},
        {'id': 7, 'name': 'make list', 'subtasks': None, 'priority': 2}
    ], 'priority': 3},
    {'id': 3, 'name': 'cleaning', 'subtasks': [
        {'id': 6, 'name': 'trash', 'subtasks': None, 'priority': 6},
        {'id': 8, 'name': 'dusting', 'subtasks': None, 'priority': 6}
    ], 'priority': 5}
]

# Run the function
scheduled_tasks = schedule_tasks(tasks)

# Print the scheduled tasks
for task in scheduled_tasks:
    print(task)