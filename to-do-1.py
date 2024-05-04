import streamlit as st

# Title
st.title("To-Do List")

# Function to add a task
def add_task(task, priority):
    st.session_state["task_list"].append({"task": task, "priority": priority})

# Initialize task list if not exists
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# Sidebar for adding task and priority
with st.sidebar:
    st.header("Add Task and Priority")
    task_input = st.text_input("Enter your task:")
    priority_input = st.slider("Priority (1 is the highest priority):", 1, 5, 1)
    if st.button("Add Task"):
        if task_input:
            add_task(task_input, priority_input)
            st.success("Task added successfully!")

    # Button to sort tasks by priority
    if st.button("Sort by Priority"):
        st.session_state["task_list"].sort(key=lambda x: x["priority"],reverse=True)

# Display tasks
st.write("### Your Tasks:")
for i, task in enumerate(st.session_state["task_list"], start=1):
    st.write(f"{i}. {task['task']} (Priority: {task['priority']})")

# Checkbox to remove task
if st.session_state["task_list"]:
    task_to_remove = st.selectbox("Select task to remove:", [task["task"] for task in st.session_state["task_list"]], key="remove_task_selectbox")
    if st.button("Remove Task"):
        st.session_state["task_list"] = [task for task in st.session_state["task_list"] if task["task"] != task_to_remove]
        st.success("Task removed successfully!")
else:
    ""