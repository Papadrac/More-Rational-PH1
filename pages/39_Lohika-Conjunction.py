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
# (LOHIKAL NA AT)
# --------------------------
questions = [
    {
        "statement": "Si Anna at si Ben ay parehong kasali sa isang palaro. Ano ang truth value ng '<b>si Anna at si Ben ay kasali sa palaro</b>'?",
        "answer": True,
        "image": None,
        "explanation": "Pag ginamit ang salitang 'at' (logical conjunction), ang pahayag ay tama lamang kung parehong totoo ang mga bahagi. Kung si Anna at si Ben ay parehong kasali, tama ang pahayag. Kung isa lang ang kasali, mali ang pahayag. Kung walang kasali, mali din ang pahayag.",
    },
    {
        "statement": "Si Juan ay isang grade 4 student at si Maria ay isang grade 5 student. Ang truth value ng '<b>si Juan at si Maria ay grade 4 students</b>'",
        "answer": False,
        "image": None,
        "explanation": "Pag ginamit ang 'at', ang pahayag ay tama lamang kung parehong totoo ang mga bahagi. Si Juan ay grade 4, pero si Maria ay grade 5, kaya mali ang pahayag.",
    },
    {
        "statement": "Sa group chat, mali ang update ni Carlo at tama ang update ni Bea. Ano ang truth value ng '<b>si Carlo at si Bea ay tama ang update</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa usapang magkaklase, parehong mali ang sinabi nina Miguel at Liza. Ano ang truth value ng '<b>si Miguel at si Liza ay tama ang sinabi</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa barangay assembly, parehong totoo ang sinabi ni Ramon at Nica. Ang pahayag na '<b>si Ramon at si Nica ay tama ang sinabi</b>'?",
        "answer": True,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa ulat ng presyo sa palengke, mali ang datos ni Jorge pero tama ang datos ni Mila. Ang pahayag na '<b>Si Jorge at si Mila ay tama ang datos</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa P2P bus route update, parehong mali ang anunsyo nina Paolo at Trina. Ano ang truth value ng '<b>Si Paolo at si Trina ay tama ang anunsyo</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa attendance checking, parehong tama ang claim nina Diego at Karen. Ang pahayag na '<b>Si Diego at si Karen ay tama ang claim</b>'?",
        "answer": True,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa basketball liga announcement, mali ang pahayag ni Noel at tama ang pahayag ni Aira. Ang pahayag na '<b>Si Noel at si Aira ay tama ang pahayag</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    },
    {
        "statement": "Sa family reunion planning, tama ang plano ni Enzo pero mali ang plano ni Celine. Ano ang truth value ng '<b>Si Enzo at si Celine ay tama ang plano</b>'?",
        "answer": False,
        "image": None,
        "explanation": "Sa lohikal na 'at', kailangan parehong totoo ang dalawang bahagi. Kung may mali kahit isa, mali na agad ang buong pahayag.",
    }
]

# --------------------------
# KEEP FIRST 2 FIXED, RANDOMIZE THE REST (TOTAL: 5)
# --------------------------
if not st.session_state.shuffled_questions:
    total_questions = min(5, len(questions))
    fixed_questions = questions[:2]
    remaining_questions = questions[2:]
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
    st.subheader("TAMA o MALI: *Logical Conjunction*")
    st.write(
        "Basahin ang bawat pahayag tungkol sa lohikal na p at q (p ∧ q) at tukuyin kung ito ay tama o mali."
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
            "<a href='https://morerationalph.streamlit.app/Lohika-Disjunction' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>",
            unsafe_allow_html=True,
        )

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
