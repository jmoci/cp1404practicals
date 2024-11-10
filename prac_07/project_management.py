"""
Time Estimate: 30min
Start Time: 5:33pm
Finish Time: 7:50pm
"""
from datetime import datetime

from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

def main():
    filename = input("Filename: ")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    display_main_menu(projects)

def display_main_menu(projects):
    """Enter the main menu loop"""
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename: ")
            #Task sheet required prompting the user for the filename every time.
            save_projects(projects,filename)
        elif choice == 'D':
            projects.sort(reverse=True)
            display_projects(projects)
        elif choice == 'F':
            display_filtered_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice. Try again")
        choice = input(">>>").upper()
    save_exit_flag = (input("Would you like to save? (Y/N): ").upper() != "N")
    if save_exit_flag:
        filename = input("Filename: ")
        save_projects(projects,filename)
    print("Have a nice day.")

def update_project(projects):
    """Update parameters of user specified project"""
    for project_number in range(len(projects)):
        print(f"{project_number}: {projects[project_number]}")
    is_valid_project = False
    while not is_valid_project:
        try:
            project_index = int(input("Project Choice: "))
            if 0 <= project_index < len(projects):
                is_valid_project = True
            else:
                raise ValueError("project index out of range")
        except ValueError:
            print("Invalid choice. Try again")
    print(projects[project_index])
    is_valid_percentage = False
    while not is_valid_percentage:
        try:
            percentage = int(input("New Percentage: ").strip("%"))
            if 0 <= percentage <= 100.0:
                is_valid_percentage = True
            else:
                raise ValueError("Percentage out of range")
        except ValueError:
            print("Invalid percentage. Try again")
    is_valid_priority = False
    while not is_valid_priority:
        try:
            priority = int(input("New Priority: "))
            if priority >= 0:
                is_valid_priority = True
            else:
                raise ValueError("Priority must be greater than or equal to zero")
        except ValueError:
            print("Invalid priority. Try again")
    #Ignore warnings. Values cannot be referenced before assignment
    projects[project_index].completion_percentage = percentage
    projects[project_index].priority = priority

def display_filtered_projects(projects):
    """Display projects that start after user specified date"""
    projects = projects_sort_by_date(projects)
    min_date = date_input("Show projects that start after date (dd/mm/yy): ")
    filtered_projects = [project for project in projects if project.start_date > min_date]
    display_projects(filtered_projects)

def add_project(projects):
    """Prompt the user to fill out details for a new project and add it to projects in memory"""
    print("Lets add a new project")
    name = input("Name: ")
    start_date = date_input("Start date (dd/mm/yy): ")
    is_priority_valid = False
    while not is_priority_valid:
        try:
            priority = int(input("Priority: "))
            is_priority_valid = True
        except ValueError:
            print("Invalid priority. Try again")
    is_cost_valid = False
    while not is_cost_valid:
        try:
            cost_estimate = int(input("Cost estimate: ").strip("$"))
            is_cost_valid = True
        except ValueError:
            print("Invalid cost. Try again")
    is_completion_valid = False
    while not is_completion_valid:
        try:
            completion = int(input("Completion: ").strip("%"))
            if 100 >= completion >= 0:
                is_completion_valid = True
            else:
                raise ValueError("Completion must be between 0 and 100")
        except ValueError:
            print("Invalid completion. Try again")
    #Reference before assignment is impossible. Ignore warnings
    project = Project(name, start_date,priority,cost_estimate,completion)
    projects.append(project)
    return projects


def load_projects(filename):
    """Parse a file and return as list of projects"""
    projects = []
    with open(filename, 'r') as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            project_date = datetime.strptime(parts[1], '%d/%m/%Y')
            projects.append(Project(parts[0], project_date, int(parts[2]),float(parts[3]), int(parts[4])))
    return projects

def save_projects(projects,filename):
    """Save projects to a file"""
    with open(filename, 'w') as file:
        file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display the list of projects"""
    incomplete_projects = [project for project in projects if project.completion_percentage<100]
    complete_projects = [project for project in projects if project.completion_percentage >= 100]
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print('\t' + str(project))
    print("Complete Projects:")
    for project in complete_projects:
        print('\t' + str(project))

def date_input(message):
    """Get and error check date from the user in dd/mm/yy format"""
    is_date_valid = False
    while not is_date_valid:
        datestring = input(message)
        try:
            start_date = datetime.strptime(datestring, '%d/%m/%y')
            is_date_valid = True
        except ValueError:
            print("Invalid date. Try again")
    return start_date

def projects_sort_by_date(projects):
    """Sort projects by date, oldest first"""
    sorted_projects = []
    for project_index in range(len(projects)):
        oldest_project = projects[0]
        for project in projects:
            if project.start_date < oldest_project.start_date:
                oldest_project = project
        sorted_projects.append(oldest_project)
        projects.remove(oldest_project)
    return sorted_projects


if __name__ == '__main__':
    main()