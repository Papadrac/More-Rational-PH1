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
    # WITH REPLACEMENT
    {
        "question": "May dalawang spin. Sa unang spin may 1 sa 4 na parte ay pula, sa pangalawa naman may dalawa sa anim na parte ay pula. Ano ang probability na parehong pulang parte ang mapili sa dalawang spin?",
        "choices": ["1/16", "2/24", "1/4", "10/12"],
        "answer": {"2/24"},
        "image": "https://imgur.com/44onusr.jpg",
        "solution": "Probability ng pulang bola sa unang pick = 1/4. Probability ng pulang bola sa pangalawang pick = 2/6. Kaya 1/4 × 2/6 = 2/24. Kailangan i-multiply ang probabilities ng bawat spin dahil gusto natin malaman ang probability na parehong pulang parte ang mapili sa dalawang spin.",
        "image_width": 400
    },
    {
        "question": "(Without replacement) May garapon na may 4 na bola (1 asul, 2 pula, at 1 dilaw). Pipili ng bola, hindi ibabalik, at pipili ulit. Ano ang probability na ang unang bola ay asul at ang pangalawang bola ay pula?",
        "choices": ["2/12", "1/4", "1/12", "1/8"],
        "answer": {"2/12"},
        "image": "https://imgur.com/BHfD5DA.jpg",
        "solution": "Probability na makuha ang asul sa una = 1/4. Matitira 3 bola (2 pula at 1 dilaw), kaya probability na pula sa pangalawa = 2/3. Kaya 1/4 × 2/3 = 2/12=1/6.",
        "image_width": 400
    },
    {
        "question": "Isang dice ang inihagis at isang coin ang inihagis. Ano ang probability na makakuha ng 6 sa dice at Head sa coin?",
        "choices": ["1/12", "1/6", "1/2", "1/8"],
        "answer": {"1/12"},
        "image": "https://imgur.com/OOLWUpt.jpg",
        "solution": "Probability na makakuha ng 6 sa dice = 1/6. Probability na makakuha ng Head sa coin = 1/2.",
        "image_width": 400
    },
    {
        "question": "May garapon na may 4 na bola (1 itim, 3 puti). Kung pipili ng bola, ibabalik ito, at pipili ulit ng bola, ano ang probability na parehong itim na bola ang mapili?",
        "choices": ["1/16", "1/8", "1/4", "1/12"],
        "answer": {"1/16"},
        "image": None,
        "solution": "Probability ng itim na bola sa unang pick = 1/4. Dahil ibinalik, probability sa pangalawa = 1/4 din.",
        "image_width": 400
    },
    {
        "question": "May 5 kendi (1 asul, 4 pula). Pipili ng kendi, hindi ibabalik, at pipili ulit. Ano ang probability na pula ang una at asul sa pangalawa?",
        "choices": ["4/20", "1/10", "1/5", "1/20"],
        "answer": {"4/20"},
        "image": None,
        "solution": "Probability ng pula sa unang pick = 4/5. Probability ng asul sa pangalawa = 1/4.",
        "image_width": 400
    },
    # WITHOUT REPLACEMENT
    {
        "question": "May garapon na may 4 na bola (1 pula, 3 puti). Kung pipili ng bola, hindi ibabalik, at pipili ulit, ano ang probability na parehong pulang bola ang mapili?",
        "choices": ["0", "1/12", "1/16", "1/4"],
        "answer": {"0"},
        "image": None,
        "solution": "Pagkatapos makuha ang pulang bola sa una, wala nang pulang bola sa pangalawa.",
        "image_width": 400
    },
    {
        "question": "May 5 kendi (1 asul, 4 pula). Pipili ng kendi, hindi ibabalik, at pipili ulit. Ano ang probability na parehong asul ang mapili?",
        "choices": ["0", "1/20", "1/25", "1/5"],
        "answer": {"0"},
        "image": None,
        "solution": "Pagkatapos makuha ang asul sa una, wala nang asul sa pangalawa.",
        "image_width": 400
    },
    # MIXED (WITH REPLACEMENT)
    {
        "question": "Pipili ng isang card mula sa 4 na baraha, ibabalik, at pipili ulit. May isang barahang A. Ano ang probability na parehong barahang A ang mapili?",
        "choices": ["1/16", "1/8", "1/4", "1/12"],
        "answer": {"1/16"},
        "image": None,
        "solution": "Probability ng A sa unang pick = 1/4. Dahil ibinalik, probability sa pangalawa = 1/4 din.",
        "image_width": 400
    },
    # MIXED (WITHOUT REPLACEMENT)
    {
        "question": "Pipili ng isang card mula sa 4 na baraha, hindi ibabalik, at pipili ulit. May dalawang barahang A. Ano ang probability na parehong barahang A ang mapili?",
        "choices": ["2/12", "1/12", "1/16", "1/4"],
        "answer": {"2/12"},
        "image": None,
        "solution": "Pagkatapos makuha ang unang A sa una, may isa pang A sa pangalawang pili. Probability ng A sa una = 2/4. Probability ng A sa pangalawa = 1/3.",
        "image_width": 400
    }
]


# --------------------------
# RANDOMIZE AND PICK ONLY 5
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[2:]
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:2]  # first two + 2 random from rest (total 4)


# --------------------------
# USE THE SHUFFLED QUESTION LIST
# --------------------------
q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]

# --- RANDOMIZE CHOICES ORDER FOR EACH QUESTION ---
if "shuffled_choices" not in st.session_state:
    st.session_state.shuffled_choices = {}

if st.session_state.index not in st.session_state.shuffled_choices:
    choices = list(q["choices"])
    random.shuffle(choices)
    st.session_state.shuffled_choices[st.session_state.index] = choices
else:
    choices = st.session_state.shuffled_choices[st.session_state.index]


# --------------------------
# DISPLAY QUESTION (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Probability*: Independent/Dependent Events")
    st.write("Hanapin ang probability ng mga pangyayari. Bawat tanong i-multiply ang probability ng bawat pangyayari para makuha ang final na sagot.")
    
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


# Use the randomized choices order
choices_with_blank = [""] + choices
selected = st.selectbox(
    "Piliin ang tamang sagot:",
    choices_with_blank,
    key=f"q{st.session_state.index}_single"
)
# Only treat as answered if a real choice is selected
selected = [selected] if selected and selected != "" else []


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
    
    st.write(f"Iyong sagot: **{_format_as_set(selected)}**")
    
    if set(selected) == q["answer"]:
        st.success("Tama! 🎉")
        if not st.session_state.wrong and not st.session_state.answered:
            st.session_state.score += 1
            st.balloons()
        st.session_state.answered = True
        st.session_state.wrong = False
    else:
        st.error("Mali ❌, subukan muli.")
        st.info(f"Paano sagutan: {q.get('solution', '')}")
        st.session_state.answered = True
        st.session_state.wrong = True

    # final-question completion handled below after retry logic


# --------------------------
# RETRY WRONG ANSWER
# --------------------------

if "retry_counts" not in st.session_state:
    st.session_state.retry_counts = {}

MAX_RETRIES = 1

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
        def _format_as_set(a):
            if isinstance(a, (set, list, tuple)):
                items = list(a)
                if all(isinstance(x, (int, float)) for x in items):
                    items = sorted(items)
                else:
                    items = sorted(items, key=lambda x: str(x))
                return "{" + ", ".join(map(str, items)) + "}"
            return str(a)

        st.info(f"Tamang sagot: **{_format_as_set(ans)}**")
        st.info(f"Paano sagutan: {q.get('solution', '')}")


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
        st.markdown("<a href='https://morerationalph.streamlit.app/Probability-with_Combinatorics' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
