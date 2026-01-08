# Task Manager (CLI + GUI)

A simple yet powerful task manager built using Python.  
It supports both a **Command Line Interface (CLI)** and a **Graphical User Interface (GUI)** using Tkinter.

This project was built to practice clean software architecture, Git workflow, and real-world Python development.

---

## Features

## CLI Features

- Add tasks
- List tasks
- Mark tasks as done
- Delete tasks

## GUI Features (Tkinter)

- Add tasks using input box
- Mark tasks as done by ID
- Delete tasks by ID
- Scrollable task list
- Persistent storage (tasks remain after restart)

## Tech Stack

- Python
- Tkinter
- argparse
- JSON

## How to Run

## Run CLI

```bash
# Show available commands
python main.py --help
# Add a new task
python main.py add "Learn Git"
# List all tasks
python main.py list
```

## RUN GUI

python ui.py

---

What I Learned

Clean separation of concerns (UI, logic, storage)
Building CLI tools using argparse
Creating GUI applications with Tkinter
Managing persistent data using JSON
