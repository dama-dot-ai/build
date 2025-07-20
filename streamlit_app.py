import streamlit as st

# Hardcoded user credentials
user_credentials = {
    "daniel": {"password": "godblessdama123$$", "name": "Daniel M"},
    "alice": {"password": "godblessdama123$$", "name": "Alice Sharon"},
    "neelima": {"password": "godblessdama123$$", "name": "Neelima"},
    "romilton": {"password": "godblessdama123$$", "name": "Romilton"}
}

# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# Login screen
def login_screen():
    st.title("Welcome to DAMA.AI")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in user_credentials and user_credentials[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = user_credentials[username]["name"]
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# Main application screen
def main_screen():
    st.sidebar.write(f"👋 Hello, {st.session_state.user}")
    nav = st.sidebar.radio("Navigate", ["Job Requisitions", "Candidates", "Applications"])

    st.title("GPT Chat Window")
    st.info("This is where GPT chat and summaries will appear based on the selected section.")

    st.write("Right panel will dynamically display data based on left nav selection.")
    st.write("→ Example: If you click on 'Job Requisitions', the open roles will show here.")

    st.sidebar.markdown("---")
    st.sidebar.write("Summary Stats")
    st.sidebar.write("🟢 5 Open Reqs")
    st.sidebar.write("🔵 23 Candidates")
    st.sidebar.write("🟠 8 In Interview")

if not st.session_state.logged_in:
    login_screen()
else:
    main_screen()
    # Render chat input at the bottom
user_prompt = st.chat_input("Ask a question about this data...")
if user_prompt:
    st.chat_message("user").write(user_prompt)

    # Placeholder GPT response — later will integrate actual LLM
    st.chat_message("assistant").write("Let me analyze that for you... 🧠")
