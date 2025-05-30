import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ensure tasks is always initialized
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Task Analysis")

# Check if tasks exist in session state
if "tasks" in st.session_state and st.session_state.tasks:
    st.write("Analysis of your tasks:")

    # Create a DataFrame from the tasks list
    df = pd.DataFrame(st.session_state.tasks)

    st.dataframe(df)

    st.subheader("Task Summary")
    completed_count = df["completed"].sum()
    pending_count = len(df) - completed_count

    st.write(f"Total tasks: {len(df)}")
    st.write(f"Completed tasks: {completed_count}")
    st.write(f"Pending tasks: {pending_count}")

    # Visualizations
    st.subheader("Task Completion Status Distribution")

    # Prepare data for plotting
    status_counts = (
        df["completed"].value_counts().rename({True: "Completed", False: "Pending"})
    )

    fig, ax = plt.subplots()
    status_counts.plot(kind="bar", ax=ax, color=["green", "orange"])
    ax.set_ylabel("Number of Tasks")
    ax.set_xlabel("Status")
    ax.set_title("Completed vs Pending Tasks")
    st.pyplot(fig)

else:
    st.info(
        "No tasks available for analysis. Please add some tasks on the To-Do List page."
    )
