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
def read_project_notes(project_path):
    notes_path = f"{project_path}/notes.txt"
    if os.path.exists(notes_path):
        with open(notes_path, "r") as file:
            return file.read()
    return None  # Return None if notes.txt does not exist

# Title of your interface
st.title('ProjectPal Interface')

# Input field for project name
project_name = st.text_input("Enter project name:")

# Button to check project status
if st.button("Check Project Status"):
    status = get_project_status(project_name)
    if status:
        st.write(f"Status of {project_name}: {status}")
    else:
        st.write(f"No status found for {project_name}. Looking for notes.txt...")
        project_path = f"path/to/{project_name}"  # Adjust the path to your projects
        project_notes = read_project_notes(project_path)
        if project_notes:
            st.write(f"Notes for {project_name}:")
            st.text(project_notes)
        else:
            st.write(f"No notes.txt found for {project_name}. Ending conversation.")

# Adjust the path to your projects accordingly and ensure the project name entered matches the folder name of your project.
