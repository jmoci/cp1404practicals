"""
Time Estimate: 30min
Start Time: 5:33pm
"""
from html.parser import incomplete

from prac_07.project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""

FILEPATH = 'projects.txt'

def main():
    display_main_menu()

def display_main_menu():
    """Enter the main menu loop"""
    print(MENU)
    projects = []
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'L':
            projects = load_projects()
        elif choice == 'S':
            save_projects(projects,FILEPATH)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            pass
        elif choice == 'A':
            pass
        elif choice == 'U':
            pass
        else:
            print("Invalid choice. Try again")
        choice = input(">>>").upper()

def load_projects():
    """Parse a file and return as list of projects"""
    projects = []
    with open(FILEPATH, 'r') as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            #TODO replace parts1 with date
            projects.append(Project(parts[0], parts[1], int(parts[2]),float(parts[3]), int(parts[4])))
    return projects

def save_projects(projects,filepath):
    with open(filepath, 'w') as file:
        file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

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

if __name__ == '__main__':
    main()