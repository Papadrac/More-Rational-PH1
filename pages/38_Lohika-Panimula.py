import random

import streamlit as st

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
# (SET THEORY + NUMBER THEORY)
# --------------------------
questions = [
    {
        "statement": "Ang set na {1, 2, 5} ay may 3 elemento.",
        "answer": True,
        "image": None,
        "explanation": "Tama, tatlo ang bilang ng elemento: 1, 2, at 5.",
    },
    {
        "statement": "Ang 13 ay even number.",
        "answer": False,
        "image": None,
        "explanation": "Mali, ang 13 ay odd number, hindi nahahati sa 2 nang walang remainder.",
    },
    {
        "statement": "Ang negation ng pahayag na 'Umuuulan ngayon' ay 'Hindi umuulan ngayon'.",
        "answer": True,
        "image": None,
        "explanation": "Tama. Ang negation ay kabaligtaran ng truth value ng orihinal na pahayag.",
    },
    {
        "statement": "Ang empty set (∅) ay may isang elemento.",
        "answer": False,
        "image": None,
        "explanation": "Ang empty set ay walang laman, kaya 0 ang bilang ng elemento nito.",
    },
    {
        "statement": "Kung A = {1, 2} at B = {2, 3}, ang A ∩ B ay {2}.",
        "answer": True,
        "image": None,
        "explanation": "Ang intersection ay mga elementong pareho sa A at B. Dito, si 2 lang ang pareho.",
    },
    {
        "statement": "Kung A = {1, 2} at B = {2, 3}, ang A ∪ B ay {1, 2, 3}.",
        "answer": True,
        "image": None,
        "explanation": "Ang union ay lahat ng elementong nasa A o B, walang inuulit.",
    },
    {
        "statement": "Ang {a, b} at {b, a} ay magkaibang set.",
        "answer": False,
        "image": None,
        "explanation": "Sa set theory, hindi mahalaga ang ayos ng elemento. Pareho lang ang dalawang set na ito.",
    },
    {
        "statement": "Ang bilang na 1 ay prime number.",
        "answer": False,
        "image": None,
        "explanation": "Ang prime number ay dapat may eksaktong dalawang divisor. Ang 1 ay may isang divisor lang.",
    },
    
    {
        "statement": "Kung ang isang numero ay nahahati sa 10, nahahati rin ito sa 5.",
        "answer": True,
        "image": None,
        "explanation": "Tama, dahil ang 10 = 2 × 5. Kaya kung multiple ng 10 ang numero, multiple din ito ng 5.",
    },
    {
        "statement": "Kung ang isang numero ay nahahati sa 5, siguradong nahahati rin ito sa 10.",
        "answer": False,
        "image": None,
        "explanation": "Mali. Halimbawa, 15 ay nahahati sa 5 pero hindi nahahati sa 10.",
    },
    {
        "statement": "Kung ang isang numero ay nahahati sa 8, nahahati rin ito sa 2.",
        "answer": True,
        "image": None,
        "explanation": "Tama, dahil ang 8 = 2 × 4. Kaya kung multiple ng 8 ang numero, multiple din ito ng 2.",
    },
    {
        "statement": "Kung ang isang numero ay nahahati sa siyam, siguradong nahahati rin ito sa walo.",
        "answer": False,
        "image": None,
        "explanation": "Mali. Halimbawa, 18 ay nahahati sa 9 pero hindi nahahati sa 8.",
    },
    {
        "statement": "Lahat ng triangles ay isosceles.",
        "answer": False,
        "image": None,
        "explanation": "Mali. May mga triangle na scalene, ibig sabihin walang magkaparehong haba ng sides.",
    },
    
    {
        "statement": "Ang negation ng 'Lahat ng estudyante ay pumasa' ay 'Walang estudyante ang pumasa'.",
        "answer": False,
        "image": None,
        "explanation": "Mali. Ang tamang negation ng 'lahat' ay 'may kahit isang hindi'. Kaya: 'May estudyanteng hindi pumasa'.",
    },
    {
        "statement": "Kung p: 'Si Ana ay nasa bahay', ang ~p ay 'Si Ana ay wala sa bahay'.",
        "answer": True,
        "image": None,
        "explanation": "Tama. Ang ~p (not p) ay pahayag na nagsasabing hindi totoo si p.",
    },
]

# --------------------------
# KEEP FIRST 3 FIXED, RANDOMIZE THE REST (TOTAL: 7)
# --------------------------
if not st.session_state.shuffled_questions:
    total_questions = min(7, len(questions))
    fixed_questions = questions[:3]
    remaining_questions = questions[3:]
    random.shuffle(remaining_questions)

    random_count = max(0, total_questions - len(fixed_questions))
    st.session_state.shuffled_questions = fixed_questions + remaining_questions[:random_count]

q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]

# --------------------------
# DISPLAY
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("TAMA o MALI: Lohika")
    st.write(
        "Batay sa mga natutunang konsepto, basahin ang bawat pahayag at tukuyin kung ito ay tama o mali."
    )

st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")
st.progress((st.session_state.index + 1) / len(q_list))

if q["image"]:
    image_width = q.get("image_width", 300)
    st.image(q["image"], width=image_width)

st.markdown(
    f"<div style='font-size:22px; margin-bottom:15px'>{q['statement']}</div>",
    unsafe_allow_html=True,
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
            unsafe_allow_html=True,
        )
        st.session_state.wrong = True

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
        st.markdown(
            f"<span style='font-size:1.3em; font-weight:bold;'>Panghuling Marka: {st.session_state.score} / {len(q_list)}</span>",
            unsafe_allow_html=True,
        )
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
        st.markdown(
            "<a href='/Pages/1_Set Theory-Rewriting Sets' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>",
            unsafe_allow_html=True,
        )

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
