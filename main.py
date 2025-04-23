# app.py
import streamlit as st
import pandas as pd
from streamlit_chat import message  # Replace with working chat module

st.session_state.graph_messages = []
st.session_state.text_messages = []

# Imports
from miner.text_miner import TextMiner
from miner.graph_miner import GraphMining

# Load data
df = pd.read_csv("data/Final_students_data.csv")
docs = list(df["Bio"])

# Page config
st.set_page_config(page_title="TextMiner & GraphMiner", layout="centered")
st.markdown("# DataMiner Chat Assistant")

# Sidebar Navigation with Icons
st.sidebar.title("Navigation")

# Create buttons for navigation
if st.sidebar.button("🔍 TextMiner Chat"):
    st.session_state.page = "TextMiner"
    st.session_state.messages = []

if st.sidebar.button("📊 GraphMiner Chat"):
    st.session_state.page = "GraphMiner"
    st.session_state.messages = []



# Default to "TextMiner" if no page is selected
if "page" not in st.session_state:
    st.session_state.page = "TextMiner"

# Chat session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "graph_mode" not in st.session_state:
    st.session_state.graph_mode = "By Name"

# ---- TEXTMINER CHAT ----
if st.session_state.page == "TextMiner":
    st.markdown("## TextMiner")

    for msg in st.session_state.messages:
        message(msg["text"], is_user=msg["is_user"])

    user_input = st.chat_input("Ask something about student bios")

    if user_input:
        message(user_input, is_user=True)
        st.session_state.messages.append({"text": user_input, "is_user": True})

        with st.spinner("⛏️ Mining the bios..."):
            miner = TextMiner(docs.copy(), df.copy())
            output, ranks = miner.search(user_input)

        if isinstance(output, str):
            bot_reply = f"⚠️ {output}"
            message(bot_reply, is_user=False)
            st.session_state.messages.append({"text": bot_reply, "is_user": False})
        else:
            for line in output[:5]:  # Limit top 5 for clarity
                try:
                    similarity, rest = line.split("] ", 1)
                    reply = f"🔎 **{similarity}]** {rest}"
                except ValueError:
                    reply = f"- {line}"
                message(reply, is_user=False)
                st.session_state.messages.append({"text": reply, "is_user": False})

# ---- GRAPHMINER CHAT ----
elif st.session_state.page == "GraphMiner":
    st.markdown("## GraphMiner")
    st.markdown("#### Select Graph Mode:")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🧑‍💻 By Name", key="by_name"):
            st.session_state.graph_mode = "By Name"
    with col2:
        if st.button("🎓 By Certificate", key="by_certificate"):
            st.session_state.graph_mode = "By Certificate"

    for msg in st.session_state.messages:
        message(msg["text"], is_user=msg["is_user"])

    prompt = "Type a name (e.g., Yousef Wael)" if st.session_state.graph_mode == "By Name" else "Type a certificate (e.g., CompTIA Security+)"
    user_input = st.chat_input(prompt)

    if user_input:
        message(user_input, is_user=True)
        st.session_state.messages.append({"text": user_input, "is_user": True})

        with st.spinner("📊 Generating Graph..."):
            graph_miner = GraphMining(df)
            if st.session_state.graph_mode == "By Name":
                if graph_miner.create_graph_by_name(user_input) == 0:
                    reply = f"✅ Graph for **{user_input}** (by name) has been displayed."
                else:
                    reply = f"The name **{user_input}** hasn't been found in our system."
            else:
                if graph_miner.create_graph_by_certificate(user_input) == 0:
                    reply = f"✅ Graph for **{user_input}** (by certificate) has been displayed."
                else:
                    reply = f"The certificate **{user_input}** hasn't been found in our system."


        message(reply, is_user=False)
        st.session_state.messages.append({"text": reply, "is_user": False})
