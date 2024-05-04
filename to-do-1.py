import streamlit as st

# Function to add a task
def add_task(task_list, task, priority):
    task_list.append({"task": task, "priority": priority})

# Function to initialize task list if not exists
def initialize_task_list():
    if "task_list" not in st.session_state:
        st.session_state["task_list"] = []

# Function to display tasks
def display_tasks():
    st.write("### Your Tasks:")
    for i, task in enumerate(st.session_state["task_list"], start=1):
        st.write(f"{i}. {task['task']} (Priority: {task['priority']})")

# Function to remove task
def remove_task(task_list, task_to_remove):
    task_list[:] = [task for task in task_list if task["task"] != task_to_remove]

# Title
st.title("To-Do List")

# Initialize task list if not exists
initialize_task_list()

# Sidebar for adding task and priority
with st.sidebar:
    st.header("Add Task and Priority")
    task_input = st.text_input("Enter your task:")
    priority_input = st.slider("Priority (1 is the highest priority):", 1, 5, 1)
    if st.button("Add Task"):
        if task_input:
            add_task(st.session_state["task_list"], task_input, priority_input)
            st.success("Task added successfully!")

    # Button to sort tasks by priority
    if st.button("Sort by Priority"):
        st.session_state["task_list"].sort(key=lambda x: x["priority"], reverse=True)

# Display tasks
if st.session_state["task_list"]:
    display_tasks()
else:
    st.write("No tasks added yet.")

# Checkbox to remove task
if st.session_state["task_list"]:
    task_to_remove = st.selectbox("Select task to remove:", [task["task"] for task in st.session_state["task_list"]], key="remove_task_selectbox")
    if st.button("Remove Task"):
        remove_task(st.session_state["task_list"], task_to_remove)
        st.success("Task removed successfully!")
