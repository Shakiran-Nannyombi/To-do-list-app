import streamlit as st

# Create a list of menu options
menu = ["Home", "Tasks", "Analysis"]

# Add a navigation menu using a selectbox in the sidebar
st.sidebar.title("Navigation Menu")
choice = st.sidebar.selectbox("Go to", menu)

# Define content for the main page
if choice == "Home":
    st.title("Welcome to the To-Do List App")
    st.image("todo.svg")
    st.subheader("Manage your tasks efficiently")
    st.page_link("pages/tasks.py", label="Go to Tasks")
    st.page_link("pages/analysis.py", label="Go to Analysis")

elif choice == "Tasks":
    st.switch_page("pages/tasks.py")

elif choice == "Analysis":
    st.switch_page("pages/analysis.py")
