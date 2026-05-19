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
        "question": "Kasama ka may siyam na studyante na pwedi piliin para sa recitation. Ano ang probability na mapili ka?",
        "choices": ["1/6", "1/9", "1/2", "1/3"],
        "answer": {"1/9"},
        "image": None,
        "solution": "May 9 na studyante, kaya ang probability na mapili ka ay isa sa siyam, o 1/9.",
        "image_width": 400
    },
    {
        "question": "Base sa larawan, ang bilog ay hinati sa walong magkakaparehong bahagi. Ano ang probabilidad na mapili ang bahagi na kulay berde?",
        "choices": ["3/8", "1/4", "1/3", "4/8"],
        "answer": {"4/8"},
        "image": "https://imgur.com/mQwDrQV.jpg",
        "solution": "May 4 bahagi na berde sa 8 na bahagi. Kaya 4/8 = 1/2.",
        "image_width": 200
    },
    {
        "question": "Ang mga hayop sa itaas ay pag-aari ni Ana. May anim na hayop: 2 pusa, 1 aso, 1 manok, 1 kalabaw, at 1 pato. Ano ang probabilidad na mapili ang isang aso?",
        "choices": ["1/6", "1/4", "3/6", "4/8"],
        "answer": {"1/6"},
        "image": "https://imgur.com/2irCZ7i.jpg",
        "solution": "May 1 aso sa 6 na hayop. Kaya 1/6.",
        "image_width": 200
    },
    {
        "question": "Tingnan ang garapon sa itaas. Ano ang probabilidad na makapili ay dilaw na bola?",
        "choices": ["1/2", "1/4", "1/3", "2/3"],
        "answer": {"1/4"},
        "image": "https://imgur.com/eEhLMaT.jpg",
        "solution": "May 1 dilaw na bola sa 4 na bola.",
        "image_width": 200
    },
    {
        "question": "May limang titik na nakasulat sa itaas. Ano ang probabilidad na ang mapili ay isang patinig?",
        "choices": ["1/2", "2/5", "1/3", "2/3"],
        "answer": {"2/5"},
        "image": "https://imgur.com/SfnIpxs.jpg",
        "solution": "Ang mga patinig ay A, E, I, O, U. Sa limang titik, ilan ang mga patinig dito?",
        "image_width": 200
    },
    {
        "question": "Sa larong sipa, may 2 batang lalaki at 2 batang babae na pwedeng mapili bilang unang maglalaro. Ano ang probability na babae ang mapili?",
        "choices": ["2/4", "1/4", "1/3", "2/3"],
        "answer": {"2/4"},
        "image": None,
        "solution": "May 2 babae sa 4 na bata. Kaya 2/4 = 1/2.",
        "image_width": 400
    },
    {
        "question": "Sa <i>set</i> <b>A={2,3,5,6,7,8,9}</b>, ano ang probabilidad na makapili ay isang <i>even number</i>?",
        "choices": ["1/3", "1/2", "3/7", "4/7"],
        "answer": {"3/7"},
        "image": None,
        "solution": "May 3 even numbers sa 7 na numbers, yon ang mga 2,6,8.",
        "image_width": 400
    },
    {
        "question": "May 6 na piraso ng puto, 5 dito ay may ube, 1 ay plain. Ano ang probability na makapili ng may ube?",
        "choices": ["5/6", "1/6", "1/2", "2/3"],
        "answer": {"5/6"},
        "image": None,
        "solution": "May 5 putong ube sa 6 na puto. Kaya 5/6.",
        "image_width": 400
    },

    
    {
        "question": "May 8 na parol na nakasabit: 5 pula, 2 berde, 1 dilaw. Ano ang probability na makapili ng parol na berde?",
        "choices": ["5/8", "1/8", "1/4", "2/8"],
        "answer": {"1/4"},
        "image": None,
        "solution": "May 2 berde sa 8 parol. Kaya 2/8 = 1/4.",
        "image_width": 400
    },
    {
        "question": "Sa laro ng pabitin, may 12 premyo: 6 kendi, 4 laruan, 2 barya. Ano ang probability na makakuha ng laruan?",
        "choices": ["1/6", "1/2", "4/12", "1/3"],
        "answer": {"1/3"},
        "image": None,
        "solution": "May 4 laruan sa 12 premyo. Kaya 4/12 = 1/3.",
        "image_width": 400
    },
    {
        "question": "May 7 na pamaypay: 3 papel, 2 abaniko, 2 plastic. Ano ang probability na makapili ng pamaypay na abaniko?",
        "choices": ["1/7", "2/7", "2/5", "1/2"],
        "answer": {"2/7"},
        "image": None,
        "solution": "May 2 abaniko sa 7 pamaypay.",
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


# --------------------------
# DISPLAY QUESTION (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Probability*: Panimula")
    st.write("Ang *probability* ay ang posibilidad na mangyari ang isang kaganapan.")
    
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

choices_with_blank = [""] + q["choices"]
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
        st.markdown("<a href='https://morerationalph.streamlit.app/Probability-Independent_Events' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
