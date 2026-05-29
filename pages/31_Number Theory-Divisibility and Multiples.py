import streamlit as st
import random

# --------------------------
# SESSION STATE
# --------------------------
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "wrong" not in st.session_state:
    st.session_state.wrong = False
if "submitted_last" not in st.session_state:
    st.session_state.submitted_last = False
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = []
if "selected" not in st.session_state:
    st.session_state.selected = None

# --------------------------
# TRUE/FALSE QUESTIONS
# (NOW INCLUDING EXPLANATIONS)
# --------------------------
questions = [
    {
        "statement": "Ang 12 ay kaya bang hatiin sa 3?",
        "answer": True,
        "image": None,
        "explanation": "Ang 12 ay kayang hatiin sa 3 dahil 12 ÷ 3 = 4. May apat na 3s ang 12."
    },
    {
        "statement": "Ang 6 ay kayang humati sa 18.",
        "answer": True,
        "image": None,
        "explanation": "Ang 18 ay kayang hatiin sa 6 dahil 18 ÷ 6 = 3. May tatlong 6s ang 18."
    },
    {
        "statement": "Ang 25 ay kaya bang hatiin sa 4?",
        "answer": False,
        "image": None,
        "explanation": "Ang 25 ay hindi kayang hatiin sa 4 dahil 25 ÷ 4 = 6.25, hindi buo."
    },
    
    {
        "statement": "Ang 30 ay kaya bang hatiin sa 7?",
        "answer": False,
        "image": None,
        "explanation": "Ang 30 ay hindi kayang hatiin sa 7 dahil 30 ÷ 7 = 4.285..., hindi buo."
    },
    {
        "statement": "Ang 8 ay kayang hatiin sa 24?",
        "answer": True,
        "image": None,
        "explanation": "Ang 24 ay kayang hatiin sa 8 dahil 24 ÷ 8 = 3."
    },
    {
        "statement": "Ang 35 ay kaya bang hatiin sa 5?",
        "answer": True,
        "image": None,
        "explanation": "Ang 35 ay kayang hatiin sa 5 dahil 35 ÷ 5 = 7."
    },
    {
        "statement": "Ang 4 ay kayang hatiin sa 14?",
        "answer": False,
        "image": None,
        "explanation": "Ang 14 ay hindi kayang hatiin sa 4 dahil 14 ÷ 4 = 3.5, hindi buo."
    },
    {
        "statement": "Ang 40 ay kayang hatiin sa 8?",
        "answer": True,
        "image": None,
        "explanation": "Ang 40 ay kayang hatiin sa 8 dahil 40 ÷ 8 = 5."
    },
    {
        "statement": "Ang 9 ay kayang hatiin sa 27?",
        "answer": True,
        "image": None,
        "explanation": "Ang 27 ay kayang hatiin sa 9 dahil 27 ÷ 9 = 3."
    },
    {
        "statement": "Ang 22 ay kayang hatiin sa 6?",
        "answer": False,
        "image": None,
        "explanation": "Ang 22 ay hindi kayang hatiin sa 6 dahil 22 ÷ 6 = 3.666..., hindi buo."
    }
]

# --------------------------
# RANDOMIZE AND PICK ONLY 7
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]
    remaining = questions[2:]
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:3]

q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]

# --------------------------
# DISPLAY
# --------------------------
# Place logo to the left of the heading/introduction
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("TAMA o MALI: *Kayang Hatiin o Hindi*")
    st.write("Ang *kayang hatiin* ay kapag ang isang numero ay eksaktong nahahati ng isa pang numero.")
    
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")
# Progress bar (full width)
st.progress((st.session_state.index + 1) / len(q_list))

if q["image"]:
    image_width = q.get("image_width", 300)  # Default to 300 if not specified
    st.image(q["image"], width=image_width)

st.markdown(
    f"<div style='font-size:22px; margin-bottom:15px'>{q['statement']}</div>",
    unsafe_allow_html=True
)

# --------------------------
# TRUE / FALSE BUTTONS
# --------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("TAMA", disabled=st.session_state.answered):
        st.session_state.selected = True
        st.session_state.answered = True

with col2:
    if st.button("MALI", disabled=st.session_state.answered):
        st.session_state.selected = False
        st.session_state.answered = True

# --------------------------
# CHECK ANSWER
# --------------------------
if st.session_state.answered:
    if st.session_state.selected == q["answer"]:
        st.success("Tama! 🎉")
        if not st.session_state.wrong:
            last = st.session_state.get("last_scored_index", None)
            if last != st.session_state.index:
                st.session_state.score += 1
                st.session_state.last_scored_index = st.session_state.index
                st.balloons()
        st.session_state.wrong = False

    else:
        st.error("Mali ❌")
        st.markdown(
            f"<div style='background:#fce8e6;padding:12px;border-radius:8px;'>"
            f"<b>Paano Solusyunan:</b><br>{q['explanation']}</div>",
            unsafe_allow_html=True
        )
        st.session_state.wrong = True

    # mark last question submitted (answered) — show final regardless of correctness
    if st.session_state.index == len(q_list) - 1 and st.session_state.answered:
        st.session_state.submitted_last = True

# --------------------------
# RETRY WRONG ANSWER
# --------------------------
if st.session_state.wrong:
    if st.button("🔄 Subukan Ulit"):
        st.session_state.answered = False
        st.session_state.wrong = False
        st.session_state.selected = None
        st.rerun()

# --------------------------
# NAVIGATION BUTTONS
# --------------------------
col1, col2 = st.columns(2)

with col1:
    if st.session_state.index > 0:
        if st.button("← Nakaraang"):
            st.session_state.index -= 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.rerun()

# --------------------------
# FINAL RESULTS
# --------------------------
if st.session_state.submitted_last:
    st.markdown("---")
    col_left, col_mid, col_right = st.columns([2, 2, 2])
    with col_left:
        st.markdown("### 🎉 Kumpleto ang Pagsusulit!")
        st.markdown(f"<span style='font-size:1.3em; font-weight:bold;'>Panghuling Marka: {st.session_state.score} / {len(q_list)}</span>", unsafe_allow_html=True)
    with col_mid:
        if st.button("Suriin Muli ang Pagsusulit"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.submitted_last = False
            st.session_state.selected = None
            st.session_state.shuffled_questions = []
            if "last_scored_index" in st.session_state:
                del st.session_state["last_scored_index"]
            st.rerun()
    with col_right:
        st.markdown("<a href='/Pages/1_Set Theory-Rewriting Sets' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
