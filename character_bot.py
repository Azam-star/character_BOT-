import streamlit as st
import ollama

# ---------- Stark Nano Theme ----------
st.markdown("""
<style>
/* ===== Stark typing dots ===== */
.stark-typing {
    display: flex;
    gap: 6px;
    padding: 6px 2px;
}

.stark-dot {
    width: 8px;
    height: 8px;
    background: #ffd700;
    border-radius: 50%;
    animation: starkBlink 1.4s infinite ease-in-out both;
    box-shadow: 0 0 6px rgba(255, 215, 0, 0.8);
}

.stark-dot:nth-child(2) { animation-delay: 0.2s; }
.stark-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes starkBlink {
    0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
    40% { transform: scale(1); opacity: 1; }
}
/* ===== Main background ===== */
.stApp {
    background: radial-gradient(circle at top,
        #060b1a 0%,
        #030611 40%,
        #01030a 100%);
    color: #e6edf3;
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #070b18, #02040a);
    border-right: 1px solid rgba(255, 215, 0, 0.25);
}

/* ===== Title glow ===== */
h1 {
    text-shadow: 0 0 14px rgba(255, 215, 0, 0.7);
}

/* ===== Chat bubbles ===== */
[data-testid="stChatMessage"] {
    border-radius: 16px;
    backdrop-filter: blur(6px);
}

/* ===== User bubble (arc reactor blue) ===== */
[data-testid="stChatMessage"]:has(span:contains("🙂")) {
    background: linear-gradient(135deg, #0b3d91, #00cfff);
}

/* ===== Assistant bubble (Stark gold/red) ===== */
[data-testid="stChatMessage"]:has(img) {
    background: linear-gradient(135deg, #7a0000, #b8860b);
    box-shadow: 0 0 12px rgba(255, 215, 0, 0.35);
}

/* ===== Slider accent ===== */
.stSlider > div > div {
    color: gold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="https://img.icons8.com/fluency/96/iron-man.png" width="60">
        <h1 style="margin-left: 15px;">Tony stark's QNA Session</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar (Controls)
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model = "gemma3:latest"
    col1, col2 = st.columns([1,6])

    with col1:
        st.image("reactor.png", width=40)

    with col2:
        temperature = st.slider(
        "Reactor Output",
        min_value=0.0,
        max_value=1.5,
        value=0.6,
        step=0.1
        )

    if st.button("🧹 Clear chat"):
        st.session_state.messages = [
        st.session_state.messages[0],  # keep system
        {
            "role": "assistant",
            "content": "Memory wiped. Try not to break anything this time, kid."
        }
        ]
        st.rerun()

# -----------------------------
# Session Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are Tony Stark — Iron Man.

PERSONALITY:
- Witty, sarcastic, genius-level intelligent.
- Billionaire confidence. Slightly arrogant but charming.
- Uses clever, punchy responses (not long boring paragraphs).
- Occasionally calls the user "kid", "buddy", or "cap".
- Speaks like a fast-talking tech genius, NOT like a polite assistant.

STYLE RULES:
- Be concise but sharp.
- Add light sarcasm where appropriate.
- Never sound like Jarvis or a generic AI assistant.
- Stay in character at all times.

IMPORTANT:
- Still give accurate technical answers when asked.
- Personality enhances the answer — never replace correctness.
"""
        },
        {
            "role": "assistant",
            "content": "Alright, I'm online. Try not to ask anything too boring, kid."
        }
    ]
    

# -----------------------------
# Render Chat History
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] != "system":

        avatar = (
            "https://img.icons8.com/color/96/iron-man.png"
            if msg["role"] == "assistant"
            else "🙂"
        )

        with st.chat_message(msg["role"], avatar=avatar):
            st.write(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # ---- SINGLE assistant container ----
    with st.chat_message(
        "assistant",
        avatar="https://img.icons8.com/color/96/iron-man.png"
    ):
        message_placeholder = st.empty()

        # 🔵 show typing dots
        message_placeholder.markdown("""
        <div class="stark-typing">
            <div class="stark-dot"></div>
            <div class="stark-dot"></div>
            <div class="stark-dot"></div>
        </div>
        """, unsafe_allow_html=True)

        # ---- LLM call ----
        response = ollama.chat(
            model=model,
            messages=st.session_state.messages,
            options={"temperature": temperature}
        )

        reply = response["message"]["content"]

        # 🔥 replace dots with real text
        message_placeholder.markdown(reply)

    # store AFTER rendering
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
