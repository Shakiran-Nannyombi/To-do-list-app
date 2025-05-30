import streamlit as st

# App title
st.title("Your Tasks")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "new_task" not in st.session_state:
    st.session_state.new_task = ""

# refresh the text input for new task
if "new_task" in st.session_state and st.session_state.new_task is None:
    st.session_state.new_task = ""

# Task input
new_task = st.text_input(
    "Add new task",
    value=st.session_state.new_task,
    placeholder="Enter a new task here...",
)

# Add task button
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.session_state.new_task = ""  # Clear the input
        st.success(f"Task '{new_task}' added successfully!")
    else:
        st.error("Please enter a task. Task cannot be empty.")

# Display tasks
st.subheader("Your Tasks")
if not st.session_state.tasks:
    st.info("No tasks yet. Add some tasks to get started!")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        # Use markdown for strikethrough effect
        if task["completed"]:
            st.markdown(f"~~{task['task']}~~")
            st.caption("Completed")
        else:
            st.write(task["task"])
            st.caption("Pending")
    with col2:
       if st.checkbox("Done", key=i):
            st.session_state.tasks[i]["completed"] = True
            
# Clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [
        task for task in st.session_state.tasks if not task["completed"]
    ]
    st.success("Cleared completed tasks!")
