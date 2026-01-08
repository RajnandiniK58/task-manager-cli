from task_manager.storage import load_tasks, save_tasks


def add_task(title):
    tasks = load_tasks()

    task_id = 1
    if tasks:
        task_id = tasks[-1]["id"] + 1

    new_task = {
        "id": task_id,
        "title": title,
        "done": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task


def list_tasks():
    return load_tasks()


def mark_task_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return task

    return None


def delete_task(task_id):
    tasks = load_tasks()

    # Remove the task with matching ID
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    # Reindex IDs so they stay continuous (1, 2, 3, ...)
    for index, task in enumerate(updated_tasks, start=1):
        task["id"] = index

    save_tasks(updated_tasks)
    return updated_tasks
