from typing import TypedDict
import json

class Project(TypedDict):
    name: str
    field: str
    status: str


def create_project(name: str, field: str, status: str) -> Project:
    if not name:
        raise ValueError("Project name cannot be empty.")

    if not field:
        raise ValueError("Project field cannot be empty.")

    if not status:
        raise ValueError("Project status cannot be empty.")      

    project = {
        "name": name,
        "field": field,
        "status": status
    }

    return project



def load_projects(json_file: str) -> list[Project]:
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return []


def main():


    projects = load_projects("projects.json")

    project_name = input("Enter the name of the new project: ").strip()
    project_field = input("Enter the field of the new project: ").strip()
    project_status = input("Enter the status of the new project: ").strip()

    projects.append(create_project(project_name, project_field, project_status))

    print("All Projects:", projects)



    with open("projects.json", "w") as file:
        json.dump(projects, file, indent=4)






if __name__ == "__main__":
    main()