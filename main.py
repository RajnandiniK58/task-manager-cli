import argparse

from task_manager.manager import (
    add_task,
    list_tasks,
    mark_task_done,
    delete_task
)


def main():
    parser = argparse.ArgumentParser(
        description="Simple Task Manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    # list command
    subparsers.add_parser("list", help="List all tasks")

    # done command
    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Added task [{task['id']}] {task['title']}")

    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            status = "✔" if task["done"] else "✗"
            print(f"[{task['id']}] {task['title']} - {status}")

    elif args.command == "done":
        task = mark_task_done(args.id)
        if task:
            print(f"Task [{task['id']}] marked as done.")
        else:
            print("Task not found.")

    elif args.command == "delete":
        delete_task(args.id)
        print("Task deleted.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
