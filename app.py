import streamlit as st
from backend import get_ai_response

# 1. Page Config
st.set_page_config(
    page_title="TermChat LT",
    page_icon="🟢",
    layout="wide"
)

# 2. Custom CSS for Terminal Dark Mode
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
    .stTextInput > div > div > input {
        background-color: #001100;
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', monospace;
    }
    .stChatMessage {
        background-color: #001100;
        border-left: 3px solid #00ff00;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Sidebar
with st.sidebar:
    st.title("🟢 TERMCHAT LT")
    st.write("AI SETTINGS")
    use_api = st.checkbox("Smart Mode (API)", value=False)
    st.markdown("---")
    st.caption("Powered by termAi")

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Handle User Input
if prompt := st.chat_input("RAŠYKITE ŽINUTĘ..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("TERMAI GALVOJA..."):
            response = get_ai_response(prompt, use_api)
            st.markdown(response)
    
    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response})