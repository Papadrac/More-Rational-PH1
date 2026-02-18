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


# --------------------------
# QUIZ DATA (ORIGINAL LIST)
# --------------------------
questions = [
    {
        "question": "Anong <i>set</i> ang tinutukoy ng pulang parte sa <i>Venn diagram</i>?",
        "choices": ["A", "B", "A-B", "B-A","A ∩ B", "A ∪ B", "Walang tama"],
        "answer": {"A-B"},
        "image": "https://imgur.com/fhSfAqt.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng pulang bahagi ay mga *elements* na nasa A peru wala sa B."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng lilang parte sa <i>Venn diagram</i>?",
        "choices": ["A'", "B'", "(A-B)'", "B-A","(A ∩ B)'", "A ∪ B", "Walang tama"],
        "answer": {"B'"},
        "image": "https://imgur.com/itylpc6.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng lilang bahagi ay mga *elements* na wala sa B."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng lilang parte sa <i>Venn diagram</i>?",
        "choices": ["A'", "B'", "(A-B)'", "B-A","(A ∩ B)'", "(A ∪ B)'", "Walang tama"],
        "answer": {"(A ∪ B)'"},
        "image": "https://imgur.com/iQ5Zoyu.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng lilang bahagi ay mga *elements* na wala sa A o B."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng lilang parte sa <i>Venn diagram</i>?",
        "choices": ["A'", "B'", "(A-B)'", "B-A","(A ∩ B)'", "(A ∪ B)'", "Walang tama"],
        "answer": {"(A ∩ B)'"},
        "image": "https://imgur.com/EiJMI4V.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng lilang bahagi ay mga *elements* na wala sa *intersection* ng A at B."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng lilang parte sa <i>Venn diagram</i>?",
        "choices": ["A", "B", "A-B", "B-A","(A ∩ B)'", "A ∪ B", "Walang tama"],
        "answer": {"A"},
        "image": "https://imgur.com/YslKs7y.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng lilang bahagi ay mga *elements* na nasa A."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng berdeng parte sa <i>Venn diagram</i>?",
        "choices": ["A ∩ B ∩ C", "A ∪ B ∪ C", "(A ∪ B ∪ C)'", "A - (B ∪ C)", "A ∪ B", "Walang tama"],
        "answer": {"A - (B ∪ C)"},
        "image": "https://imgur.com/EhjLMRx.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng berdeng bahagi ay mga *elements* na nasa A lamang, tanggalin ang mga *elements* nasa B o C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng berdeng parte sa <i>Venn diagram</i>?",
        "choices": ["A ∩ B ∩ C", "A ∪ B ∪ C", "(A ∪ B ∪ C)'", "A - (B ∪ C)", "A ∪ B", "Walang tama"],
        "answer": {"A ∩ B ∩ C"},
        "image": "https://imgur.com/cSTTlPL.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng berdeng bahagi ay mga *elements* na makikita sa parehong set A, B at C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng berdeng parte sa <i>Venn diagram</i>?",
        "choices": ["(A ∩ B) - C", "C - (A ∩ B)", "(A ∪ B ∪ C)'", "A - (B ∪ C)", "A ∪ B", "Walang tama"],
        "answer": {"(A ∩ B) - C"},
        "image": "https://imgur.com/bfi9tQB.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng berdeng bahagi ay mga *elements* na nasa parehong A at B peru wala sa C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng berdeng parte sa <i>Venn diagram</i>?",
        "choices": ["A ∪ B ∪ C", "C - (A ∩ B)", "(A ∪ B ∪ C)'", "A - (B ∪ C)", "B ∩ C", "Walang tama"],
        "answer": {"B ∩ C"},
        "image": "https://imgur.com/7ubh6gz.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng berdeng bahagi ay mga *elements* na nasa parehong B at C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng berdeng parte sa <i>Venn diagram</i>?",
        "choices": ["A ∪ B ∪ C", "A ∪ B ∪ C", "A", "B", "B ∩ C", "Walang tama"],
        "answer": {"Walang tama"},
        "image": "https://imgur.com/f7bULD1.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng berdeng bahagi ay mga *elements* na nasa C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng dilaw na parte sa <i>Venn diagram</i>?",
        "choices": ["(A ∪ B ∪ C)'", "A ∪ B ∪ C", "(A ∪ B ∪ C)'", "B", "B ∩ C", "Walang tama"],
        "answer": {"(A ∪ B ∪ C)'"},
        "image": "https://imgur.com/ahv03kA.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng dilaw na bahagi ay mga *elements* na hindi mo makikita sa A, B o sa C."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng dilaw na parte sa <i>Venn diagram</i>?",
        "choices": ["A", "B", "C", "A'", "B'", "C'", "Walang tama"],
        "answer": {"A'"},
        "image": "https://imgur.com/dds1yEg.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng dilaw na bahagi ay mga *elements* na hindi mo makikita sa *set* A."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng dilaw na parte sa <i>Venn diagram</i>?",
        "choices": ["C - (A ∩ B)", "A ∪ C", "A ∪ B ∪ C", "(A ∩ C)'", "(B ∩ C)'", "(A ∩ B)'", "Walang tama"],
        "answer": {"(A ∩ B)'"},
        "image": "https://imgur.com/ao7ueQZ.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng dilaw na bahagi ay mga *elements* na hindi mo makikita sa parehong *set* A at B."
    },
    {
        "question": "Anong <i>set</i> ang tinutukoy ng dilaw na parte sa <i>Venn diagram</i>?",
        "choices": ["C - (A ∩ B)", "A ∪ C", "A ∪ B ∪ C", "A ∩ C", "B ∩ C", "A ∩ B", "Walang tama"],
        "answer": {"A ∩ C"},
        "image": "https://imgur.com/tGqBmVO.jpg",
        "image_width": 350,
        "howto_solve": "Ang nilalaman ng dilaw na bahagi ay mga *elements* na  makikita sa parehong *set* A at C."
    },
    
]


# --------------------------
# RANDOMIZE AND PICK ONLY 5
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[2:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:4]  # first two + 3 random from rest


# --------------------------
# USE THE SHUFFLED QUESTION LIST
# --------------------------
q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]


# --------------------------
# DISPLAY QUESTION (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Venn Diagram*: Hamon na Tanong")
    st.write("Piliin ang *set* na tinutukoy bawat tanong. Maglaan ng ilang sandali upang pag-isipan ang bawat tanong bago pumili ng sagot.")
    
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")

# Progress bar for this page's quiz (full width)
progress_value = (st.session_state.index + 1) / len(q_list)
st.progress(progress_value)


if q["image"]:
    image_width = q.get("image_width", 400)  # Default to 400 if not specified
    st.image(q["image"], width=image_width)

st.markdown(
    f"<div style='font-size:19px; margin-bottom:10px'>{q['question']}</div>",
    unsafe_allow_html=True
)


# Use dropdown (selectbox) for single-answer, multiselect for multiple-answer
if len(q["answer"]) == 1:
    selected = st.selectbox(
        "Piliin ang tamang sagot:",
        [""] + list(q["choices"]),
        key=f"q{st.session_state.index}"
    )
    selected_set = {selected} if selected else set()
else:
    selected = st.multiselect(
        "Piliin ang lahat ng tamang sagot:",
        q["choices"],
        key=f"q{st.session_state.index}"
    )
    selected_set = set(selected)


# --------------------------
# SUBMIT
# --------------------------
if st.button("Ipadala"):
    def _format_as_set(a):
        if isinstance(a, (set, list, tuple)):
            items = list(a)
            if all(isinstance(x, (int, float)) for x in items):
                items = sorted(items)
            else:
                items = sorted(items, key=lambda x: str(x))
            return "{" + ", ".join(map(str, items)) + "}"
        return str(a)
    def _format_as_list(a):
        if isinstance(a, (set, list, tuple)):
            items = list(a)
            if all(isinstance(x, (int, float)) for x in items):
                items = sorted(items)
            else:
                items = sorted(items, key=lambda x: str(x))
            return ", ".join(map(str, items))
        return str(a)
    st.write(f"Iyong sagot: **{_format_as_list(selected_set)}**")
    if selected_set == q["answer"]:
        st.success("Tama! 🎉")
        if not st.session_state.wrong and not st.session_state.answered:
            st.session_state.score += 1
            st.balloons()
        st.session_state.answered = True
        st.session_state.wrong = False
    else:
        st.error("Mali ❌, subukan muli.")
        howto_solve = q.get("howto_solve")
        if howto_solve:
            st.info(f"Paliwanag: {howto_solve}")
        else:
            st.write("Paliwanag: Ang *intersection* ay naglalaman lamang ng mga elemento na parehong nasa *sets*.")
        st.session_state.answered = True
        st.session_state.wrong = True

    # final-question completion handled below after retry logic


# --------------------------
# RETRY WRONG ANSWER
# --------------------------

if "retry_counts" not in st.session_state:
    st.session_state.retry_counts = {}

MAX_RETRIES = 2

if st.session_state.wrong:
    retry_count = st.session_state.retry_counts.get(st.session_state.index, 0)
    if retry_count < MAX_RETRIES:
        if st.button("🔄 Subukan Ulit"):
            st.session_state.retry_counts[st.session_state.index] = retry_count + 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()
        st.write(f"Natitirang subukan ulit: {MAX_RETRIES - retry_count}")
    else:
        st.write("Walang natitirang subukan para sa tanong na ito.")
        ans = q.get("answer")
        def _format_as_list(a):
            if isinstance(a, (set, list, tuple)):
                items = list(a)
                if all(isinstance(x, (int, float)) for x in items):
                    items = sorted(items)
                else:
                    items = sorted(items, key=lambda x: str(x))
                return ", ".join(map(str, items))
            return str(a)
        st.info(f"Tamang sagot: **{_format_as_list(ans)}**")


# If this is the last question, mark the quiz complete when it's been submitted and is correct, or when retries exhausted
if st.session_state.index == len(q_list) - 1:
    last_retry = st.session_state.retry_counts.get(st.session_state.index, 0)
    if st.session_state.answered and (not st.session_state.wrong or last_retry >= MAX_RETRIES):
        st.session_state.submitted_last = True
    else:
        st.session_state.submitted_last = False


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
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()


# --------------------------
# SHOW RESULTS WHEN FINISHED
# --------------------------
if st.session_state.submitted_last:
    st.markdown("---")
    st.markdown("### 🎉 Kumpleto ang Pagsusulit!")
    row = st.columns([2, 1, 1])
    with row[0]:
        st.markdown(f"<span style='font-size:1.3em; font-weight:bold;'>Huling Puntos: {st.session_state.score} / {len(q_list)}</span>", unsafe_allow_html=True)
    with row[1]:
        if st.button("Suriin Muli"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.submitted_last = False
            st.session_state.selected = None
            st.session_state.selected_text = None
            st.session_state.show_explanation = {}
            st.session_state.shuffled_questions = []
            if "last_scored_index" in st.session_state:
                del st.session_state["last_scored_index"]
            if "selected_index" in st.session_state:
                del st.session_state["selected_index"]
            st.rerun()
    with row[2]:
        st.markdown("<a href='/Pages/2_Set Theory-Union.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
