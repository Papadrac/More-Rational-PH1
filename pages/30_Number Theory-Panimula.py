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
        "statement": "Ang 4 ay isang prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 4 ay hindi prime dahil ito ay 2 × 2."
    },
    {
        "statement": "Ang 3 ay isang prime number.",
        "answer": True,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 3 ay isang prime number dahil wala itong ibang divisor kundi 1 at 3."
    },
    {
        "statement": "Ang 6 ay isang prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 6 ay hindi prime dahil ito ay 2 × 3."
    },
    {
        "statement": "Ang 8 ay isang prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 8 ay hindi prime dahil ito ay 2 × 4."
    },
    {
        "statement": "Ang 3 ay isang prime number.",
        "answer": True,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 3 ay isang prime number dahil wala itong ibang divisor kundi 1 at 3."
    },
    {
        "statement": "Ang 13 ay isang prime number.",
        "answer": True,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 13 ay isang prime number dahil wala itong ibang divisor kundi 1 at 13."
    },
    {
        "statement": "Ang 23 ay isang prime number.",
        "answer": True,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 23 ay isang prime number dahil wala itong ibang divisor kundi 1 at 23."
    },
    {
        "statement": "Ang 15 ay isang prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 15 ay hindi prime dahil ito ay 3 × 5."
    },
    {
        "statement": "Ang 17 ay isang prime number.",
        "answer": True,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 17 ay isang prime number dahil wala itong ibang divisor kundi 1 at 17."
    },
    {
        "statement": "Ang 21 ay isang prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito. Ang 21 ay hindi prime dahil ito ay 3 × 7."
    }
]

# --------------------------
# RANDOMIZE AND PICK ONLY 7
# --------------------------
if not st.session_state.shuffled_questions:
    questions_copy = questions[:]
    random.shuffle(questions_copy)
    st.session_state.shuffled_questions = questions_copy[:5]

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
    st.subheader("TAMA o MALI: *Prime Number o Hindi*")
    st.write("Ang *prime number* ay isang numero na may eksaktong dalawang positibong divisor: 1 at ang sarili nito.")
    
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
        st.markdown("<a href='https://morerationalph.streamlit.app/Number_Theory-Divisibility_and_Multiples' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
