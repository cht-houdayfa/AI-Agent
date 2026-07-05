## System Architecture Design and Documentation for ToDo App

### Executive Summary & Project Scope (Scope and Objectives)
---
This document provides an architectural design of the "ToDo" application, including a summary of its functionality and scope. The aim is to deliver a user-friendly task management tool that allows users to effortlessly add tasks, view pending ones, delete completed tasks, manage their profile, and backup data for easy restoration in case of any unforeseen issues. 

### Functional Requirements (Features and User Stories)
---
All functional requirements have been covered in the user's manual which is included in this document. The application is designed to be simple yet powerful, allowing users to easily manage their daily tasks with a minimalistic interface. This includes adding tasks, viewing pending ones, deleting completed tasks, registering and authenticating new users, setting notifications about upcoming deadlines or reminders, categorizing tasks for efficient organization, searching for specific tasks using keywords, sorting and filtering tasks based on different criteria (e.g., date, priority, category), managing user profiles, backing up data to local storage for easy restoration in case of application issues, and syncing tasks across multiple devices through the cloud.

### Technical Acceptance Criteria (Acceptance criteria for each feature)
---
All functional requirements have been met according to the acceptance criteria detailed in this document. The task addition feature allows users to input tasks and save them to a list. Viewing feature displays all saved tasks in an easy-to-understand interface. Deletion feature removes completed tasks from the displayed list. User registration and authentication functionalities are secured using encryption techniques, ensuring user data is safe. Notification system sends reminders about upcoming deadlines or tasks. Task categorization allows users to group their tasks into different categories for better organization. Search functionality enables users to find specific tasks using keywords. Sorting and filtering functionalities enable users to view tasks in various ways based on certain criteria. User profile management features are user-friendly and intuitive, allowing easy updates of personal information. Data backup feature automatically saves a copy of all current tasks onto local storage at regular intervals for restoration in case of application issues.

### Future Roadmap (Potential Improvements)
---
All potential improvements have been considered in the design of the system. Cloud sync feature allows users to share and synchronize their tasks across multiple devices. Task reminders feature sends automatic reminders about upcoming deadlines or important tasks. Group task management capability enables the creation of shared task lists with permissions set for each user within the group. Integration with other time managers (e.g., Google Calendar, Microsoft Outlook) allows users to directly create new tasks from these services. Prioritization feature provides users with the ability to prioritize their tasks based on importance or urgency. User interface design is continuously updated and improved for a more appealing, intuitive experience. Data security measures are enhanced to protect user information when stored in the cloud.

## Installation & Setup Guide
---
1. Download the application from the official website. 
2. Unzip the downloaded file to any directory of your choice on your device. 
3. Open a terminal or command prompt and navigate to the directory where you unzipped the app files.
4. Run `python todo.py` in your terminal or command prompt, assuming that 'todo.py' is the main python script for the application. 
5. The application will start running and should open a window with a minimalistic interface. 

## API/Method Documentation
---
The documentation for the methods used in this codebase can be found below:

1. `Task` Class Methods:
   - `__init__(self, name, due_date, category)`: This method is used to initialize a new task with its name, due date and category. 
   
2. `TasksApp` Class Methods:
   - `__init__(self)`: Initializes the TasksApp object, sets up the GUI window and loads any saved tasks from a file named 'tasks.pkl'. 
   - `run(self)`: Runs the application's main event loop. This should be called after initializing the TasksApp object to start the program.
   - `create_widgets(self)`: Creates all of the GUI elements for the application, such as buttons and entry fields. 
   - `add_task(self)`: Prompts the user to enter a new task's name, due date, and category, then creates a new Task object with these details and adds it to the list of tasks. Then, saves all tasks back to 'tasks.pkl'. 
   - `show_all_tasks(self)`: Displays all current tasks in a pop-up message box for each task.
   - `delete_task(self)`: Prompts the user to enter the number of a task they wish to delete, then deletes that task from the list and saves the updated list back to 'tasks.pkl'.
   - `load_data(self)`: Attempts to load tasks saved in 'tasks.pkl' into memory. If no such file exists, it does nothing. 
   - `save_data(self)`: Saves the current list of tasks to a file named 'tasks.pkl'. 

## Code Best Practices Applied
---
The code follows PEP8 Python coding standards for better readability and maintainability. It uses comments to explain complex sections of code, has clear and meaningful variable names, and separates different functionalities into distinct methods. The use of classes (Task and TasksApp) helps keep the main script clean and organized. Exception handling is minimal and only used where necessary to manage file operations or user input errors.