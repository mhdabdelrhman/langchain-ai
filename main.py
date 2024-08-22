import streamlit as st
from tempfile import NamedTemporaryFile
from chat import Chat
import chat_core.utils as ut

files_path = "./files"
# Initialize the chat
chat = Chat()
# set chat history
if "ch" not in st.session_state:
    st.session_state["ch"] = chat.chat_history
else:
    chat.set_chat_history(st.session_state["ch"])

# Set the page
st.set_page_config(page_title="Langchain chat app", page_icon=":tada:")
st.html("""
        <style>
        .message {
            border-radius: 15px;
            padding: 10px;
            display: inline-block;
            min-width: 100px;
        }
        
        .user {
            background: #8b8b8b;
            color: black;
        }
        
        .agent {
            background: #313131;
        }
        </style>
        """)
st.title("Langchain Chat App")
st.markdown("---")

with st.sidebar:
    st.title("Chat Store 📖")
    st.markdown("---")
    uploaded_file = st.file_uploader("Select a PDF file", type="pdf", key="upload_file")
    if uploaded_file is not None:
        with NamedTemporaryFile(dir=files_path, suffix=".pdf", delete=False) as tmpFile:
            tmpFile.write(uploaded_file.getbuffer())

        button = st.button(
            "Upload 📤",
            use_container_width=True,
        )
        if button:
            try:
                with st.spinner("Uploading..."):
                    chat.store_pdf_file(tmpFile.name)
                st.success("Uploaded!")
                ut.delete_files_in_directory(files_path)
            except Exception as e:
                st.error(e)


def show_messages(history):
    with container_place:
        with st.container(height=450, border=True):
            if history:
                for user, agent in history:
                    st.html(f"""
                            <div style='text-align: right;'>
                            <div>🤵</div>
                            <div class='message user'>{user}</div>
                            </div>
                    """)
                    st.html(f"""
                            <div style='text-align: left;'>
                            <div>🚀</div>
                            <div class='message agent'>{agent}</div>
                            </div>
                    """)


def submit_question():
    question = st.session_state.question_input
    if question is not None and question != "":
        st.session_state.question_input = ""
        with spiner_place:
            with st.spinner("Processing..."):
                chat.ask(question)
        st.session_state["ch"] = chat.chat_history
        show_messages(chat.chat_history)


st.subheader("Chat History 💬")
container_place = st.empty()
show_messages(chat.chat_history)

question = st.text_input(
    "Question",
    key="question_input",
    placeholder="Ask a question...",
    on_change=submit_question,
)
spiner_place = st.empty()
