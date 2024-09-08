# To-Do Like Web App

A simple To-Do List web application built with Django and MySQL, inspired by Microsoft To Do. The application allows users to manage their tasks, create multiple task lists, due dates, and mark tasks as complete.

## Features

- **User Authentication**: Register, login, and manage tasks specific to each user.
- **Task Lists**: Organize tasks into different task lists.
- **Tasks**: 
  - Add tasks with titles, descriptions, and due dates.
  - Mark tasks as completed.
  - Edit and delete tasks.
- **Task Reordering**: Reorder tasks within a task list (can be enhanced with Sortable.js).

## Tech Stack

- **Backend**: Django (Python web framework)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript (with optional usage of Sortable.js for drag-and-drop reordering)
- **Authentication**: Django's built-in authentication system
- **Other**: Celery (optional for handling reminders and background tasks)

## Prerequisites

- Python 3.x
- MySQL
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AliAbDev11/todo-webapp.git
   cd todo-webapp
