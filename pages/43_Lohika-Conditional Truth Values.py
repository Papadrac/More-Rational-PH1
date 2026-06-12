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
# (LOHIKAL NA KONDISYONAL)
# --------------------------
questions = [
    {
        "statement": "Totoo na umuulan (p = T) at totoo rin na basa ang kalsada (q = T). Ano ang truth value ng conditional na '<b>Kung umuulan, basa ang kalsada</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Sa conditional p → q, mali lamang ito kapag p ay totoo at q ay mali. Dahil p = T at q = T, tama ang pahayag.",
    },
    {
        "statement": "Totoo na nag-aral si Mia (p = T) pero hindi siya pumasa (q = F). Ano ang truth value ng '<b>Kung nag-aral si Mia, papasa siya</b>' (p → q)?",
        "answer": False,
        "image": None,
        "explanation": "Ito ang nag-iisang kaso na mali sa conditional: p = T at q = F. Kaya mali ang p → q.",
    },
    {
        "statement": "Hindi totoo na may kuryente (p = F), pero totoo na umiilaw ang bombilya (q = T). Ano ang truth value ng '<b>Kung may kuryente, iilaw ang bombilya</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Kapag p = F, awtomatikong tama ang p → q sa truth table ng conditional.",
    },
    {
        "statement": "Hindi totoo na nagsuot ka ng ID (p = F) at hindi ka rin pinapasok (q = F). Ano ang truth value ng '<b>Kung nagsuot ka ng ID, papapasukin ka</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Sa conditional, mali lang kapag p = T at q = F. Dahil p = F dito, tama ang pahayag.",
    },
    {
        "statement": "Totoo na may pista sa barangay (p = T) at totoo na masaya ang mga tao (q = T). Ano ang truth value ng '<b>Kung may pista sa barangay, masaya ang mga tao</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Dahil parehong totoo ang p at q, tama ang conditional p → q.",
    },
    {
        "statement": "Totoo na nagsuot ka ng uniporme (p = T) pero hindi ka pinapasok (q = F). Ano ang truth value ng '<b>Kung nagsuot ka ng uniporme, papapasukin ka</b>' (p → q)?",
        "answer": False,
        "image": None,
        "explanation": "Kapag p ay totoo at q ay mali, mali ang conditional. Ito ang exception sa p → q.",
    },
    {
        "statement": "Hindi totoo na umulan kagabi (p = F), pero totoo na basa ang lupa ngayon (q = T). Ano ang truth value ng '<b>Kung umulan kagabi, basa ang lupa</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Sa p → q, anumang kaso na p = F ay tama ayon sa truth table.",
    },
    {
        "statement": "Totoo na nag-practice ang koponan (p = T) at totoo na gumaling sila (q = T). Ano ang truth value ng '<b>Kung nag-practice ang koponan, gagaling sila</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Dahil p = T at q = T, tama ang conditional statement.",
    },
    {
        "statement": "Hindi totoo na umalis siya nang maaga (p = F), at hindi rin siya nakaabot sa klase (q = F). Ano ang truth value ng '<b>Kung umalis siya nang maaga, aabot siya sa klase</b>' (p → q)?",
        "answer": True,
        "image": None,
        "explanation": "Kapag p = F, tama pa rin ang p → q. Hindi ito kabilang sa T → F na maling kaso.",
    },
    {
        "statement": "Totoo na nagsaing ka (p = T) pero hindi naluto nang maayos ang kanin (q = F). Ano ang truth value ng '<b>Kung nagsaing ka, maluluto ang kanin</b>' (p → q)?",
        "answer": False,
        "image": None,
        "explanation": "Mali ang conditional kapag totoo ang p pero mali ang q. Kaya mali ang p → q sa sitwasyong ito.",
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
    st.subheader("TAMA o MALI: *Logical Conditional*")
    st.write(
        "Basahin ang bawat pahayag tungkol sa lohikal na p → q (conditional) at tukuyin kung ito ay tama o mali."
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
            "<a href='https://morerationalph.streamlit.app/Congratulations' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>",
            unsafe_allow_html=True,
        )

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
