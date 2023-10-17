import streamlit as st
import os

# Placeholder dictionary for project statuses
project_statuses = {
    "Project A": "Completed",
    "Project B": "In Progress"
}

# Function to get the project status
def get_project_status(project_name):
    return project_statuses.get(project_name)

# Function to read the project notes
def read_project_notes(project_name):
    project_path = f"C:/Users/tony0/projects/{project_name}/notes.txt"  # Replace with your actual path
    if os.path.exists(project_path):
        with open(project_path, "r", encoding='utf-8') as file:
            return file.read()
    else:
        with open(project_path, "w", encoding='utf-8') as file:
            file.write("This is a new project. More details to be added.")
        return "A new notes.txt file has been created for this project."
            
# Title of your interface
st.title('ProjectPal Interface')

# Get a list of all projects
projects = os.listdir('C:/Users/tony0/projects/')  # Replace with your actual path

# Dropdown list for project names
project_name = st.selectbox("Select a project:", projects)

# Button to check project status
if st.button("Check Project Status"):
    status = get_project_status(project_name)
    if status:
        st.write(f"Status of {project_name}: {status}")
    else:
        st.write(f"No status found for {project_name}. Looking for notes.txt...")
        project_notes = read_project_notes(project_name)
        if project_notes:
            st.write(f"Notes for {project_name}:")
            st.text(project_notes)
        else:
            st.write(f"No notes.txt found for {project_name}. Ending conversation.")