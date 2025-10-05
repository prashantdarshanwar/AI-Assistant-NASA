import os
import sys
import streamlit as st
import google.generativeai as genai  # still required for API calls

# ------------------ Suppress gRPC warnings ------------------
stderr_fileno = sys.stderr
sys.stderr = open(os.devnull, "w")  # temporarily suppress

# ------------------ Configure API -------------------
API_KEY = "AIzaSyBnZ-O0YfOS0qKHYVxW2yQzuwlzuB_AQSk"  # replace with your key
genai.configure(api_key=API_KEY)

# Choose a valid model (check available models via list_models)
MODEL_NAME = "models/gemini-2.5-pro"  # replace if needed
model = genai.GenerativeModel(MODEL_NAME)

# Restore stderr
sys.stderr.close()
sys.stderr = stderr_fileno

# ------------------ Streamlit UI ---------------------------
st.set_page_config(page_title="🪐 Space AI Assistant", layout="centered")
st.title("🌌 Space & Exoplanet AI Assistant")

st.markdown(
    "Ask questions about **space, astronomy, or exoplanets**. "
    "The assistant will refuse unrelated queries."
)

# User input
query = st.text_input("💬 Your question:", placeholder="e.g., What is the habitable zone?")

# Generate response
if st.button("Ask"):
    if query.strip():
        SYSTEM_PROMPT = (
            "You are a strict Space Science Assistant. "
            "Answer only questions related to space, astronomy, or exoplanets. "
            "If a question is unrelated, reply: "
            "'I can only discuss space and exoplanets — please ask a related question.'"
        )

        prompt = f"{SYSTEM_PROMPT}\n\nUser question: {query}"

        with st.spinner("Generating answer..."):
            try:
                response = model.generate_content(prompt)
                st.markdown(f"**🧠 Space AI Answer:**\n\n{response.text}")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please type a question first.")

# ------------------ Sidebar -------------------------------
st.sidebar.title("About")
st.sidebar.info(
    """
This assistant answers questions about space, astronomy, and exoplanets.
"""
)
