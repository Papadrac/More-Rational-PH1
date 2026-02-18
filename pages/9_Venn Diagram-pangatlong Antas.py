import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Venn Diagram*: Pangatlong Antas")
    st.write("Gamit ang *Venn Diagram* hanapin ang mga *elements* sa tinutukoy na *set*")
st.write("--------")

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
    {"question": "Anong mga <i>elements</i> ang nilalaman ng <i>set</i> A. Ilista lahat ng mga <i>elements</i> na nasa loob ng bilog A sa larawan.",
        "choices": ["mama", "papa", "kuya", "ate", "bunso"],
        "answer": {"mama",  "ate", "bunso"},
        "image": "https://imgur.com/0JDb8ZO.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/K7ijSc9.jpg",
        "how_to_explanation": "Ang mga *elements* ng set A ay yung mga nakapaloob sa bilog A. Ang dilaw na bahagi ay kumakatawan sa set A. Ilista lahat ng mga numero na nakapaloob sa dilaw na bahagi."
        
    },
    {"question": "Anong mga <i>elements</i> ang nilalaman ng <i>set</i> B - A. Ilista lahat ng mga <i>elements</i> na nasa loob ng B lamang.",
        "choices": ["2", "3", "4", "5", "7"],
        "answer": { "4", "7"},
        "image": "https://imgur.com/dgnUjsK.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/54jHvRL.jpg",
        "how_to_explanation": "Ang mga *elements* ng set B - A ay yung mga nakapaloob sa bilog B ngunit wala sa bilog A. Ang dilaw na bahagi ay kumakatawan sa set B - A. Ilista lahat ng mga numero na nakapaloob sa dilaw na bahagi."
        
    },
    {"question": "Anong mga <i>elements</i> ang nilalaman ng <i>set</i> (A ∪ B)'. Ilista lahat ng mga <i>elements</i> na nasa labas ng bilog A at B sa larawan.",
        "choices": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "answer": {"4",  "9"},
        "image": "https://imgur.com/WQCzfKG.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/61dRwXJ.jpg",
        "how_to_explanation": "Ang mga *elements* ng set (A ∪ B)' ay yung mga wala sa bilog A at B. Ang dilaw na bahagi ay kumakatawan sa set (A ∪ B)'. Ilista lahat ng mga numero na nakapaloob sa dilaw na bahagi."
        
    },
    {"question": "Anong mga <i>elements</i> ang nilalaman ng <i>set</i> A ∩ B. Ilista lahat ng mga <i>elements</i> na nasa loob ng parehong bilog A at B.",
        "choices": ["2", "3", "4", "5", "7"],
        "answer": { "2", "3"},
        "image": "https://imgur.com/dgnUjsK.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/83cBUw3.jpg",
        "how_to_explanation": "Ang mga *elements* ng set A ∩ B ay yung mga nakapaloob sa parehong bilog A at B. Ang dilaw na bahagi ay kumakatawan sa set A ∩ B. Ilista lahat ng mga numero na nakapaloob sa dilaw na bahagi."
        
    },
    {"question": "May mga salitang nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> B?",
        "choices": ["tayo", "dito", "ako", "sila", "nina", "kina", "doon"],
        "answer": {  "ako", "sila", "nina"},
        "image": "https://imgur.com/SKvAF18.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/Zxdqx1O.jpg",
        "how_to_explanation": "Ang mga *elements* ng set B ay yung mga nakapaloob sa bilog B. Ang dilaw na bahagi ay kumakatawan sa set B."
        
    },
    {"question": "May mga salitang nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> B'?",
        "choices": ["tayo", "dito", "ako", "sila", "nina", "kina", "doon"],
        "answer": {  "tayo", "dito", "kina", "doon"},
        "image": "https://imgur.com/SKvAF18.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/pmZqBJH.jpg",
        "how_to_explanation": "Ang mga *elements* ng set B' ay yung mga wala sa bilog B. Ang dilaw na bahagi ay kumakatawan sa set B'."
        
    },
    {"question": "May mga salitang nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> A-B?",
        "choices": ["tayo", "dito", "ako", "sila", "nina", "kina", "doon"],
        "answer": {  "tayo", "dito"},
        "image": "https://imgur.com/SKvAF18.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/KkalitX.jpg",
        "how_to_explanation": "Ang mga *elements* ng set A-B ay yung mga nakapaloob sa bilog A ngunit wala sa bilog B. Ang dilaw na bahagi ay kumakatawan sa set A-B."
        
    },
    {"question": "May mga titik na nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> A'?",
        "choices": ["m", "n", "r", "s", "t", "u", "v"],
        "answer": {  "r", "s", "t", "u", "v"},
        "image": "https://imgur.com/41MqLld.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/qVadxXy.jpg",
        "how_to_explanation": "Ang mga *elements* ng set A' ay yung mga wala sa bilog A. Ang dilaw na bahagi ay kumakatawan sa set A'."
        
    },
    {"question": "May mga titik na nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> (A ∩ B)'?",
        "choices": ["m", "n", "r", "s", "t", "u", "v"],
        "answer": { "m", "r", "s", "t", "u", "v"},
        "image": "https://imgur.com/41MqLld.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/8GUzfnn.jpg",
        "how_to_explanation": "Ang mga *elements* ng set (A ∩ B)' ay yung mga wala sa intersection ng bilog A at B. Ang dilaw na bahagi ay kumakatawan sa set (A ∩ B)'."
        
    },
    {"question": "May mga titik na nakasulat sa <i>Venn Diagram</i>. Anong mga <i>elements</i> ang nilalaman ng <i>set</i> (A ∪ B)'?",
        "choices": ["m", "n", "r", "s", "t", "u", "v"],
        "answer": { "t", "u", "v"},
        "image": "https://imgur.com/41MqLld.jpg",
        "image_width": 350,
        "how_to_image": "https://imgur.com/J7NQKLw.jpg",
        "how_to_explanation": "Ang mga *elements* ng set (A ∪ B)' ay yung mga wala sa union ng bilog A at B. Ang dilaw na bahagi ay kumakatawan sa set (A ∪ B)'."
        
    },
]


# --------------------------
# RANDOMIZE AND PICK ONLY 5
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[2:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:3]  # first two + 3 random from rest


# --------------------------
# USE THE SHUFFLED QUESTION LIST
# --------------------------
q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]


# --------------------------
# DISPLAY QUESTION (logo + instructions)
# --------------------------

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

selected = st.multiselect(
    "Piliin ang lahat ng tamang sagot:",
    q["choices"],
    key=f"q{st.session_state.index}"
)


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
        how_to_img = q.get("how_to_image")
        how_to_exp = q.get("how_to_explanation")
        if how_to_img:
            st.image(how_to_img, width=400)
        if how_to_exp:
            st.write(f"**Paliwanag:** {how_to_exp}")
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
        st.markdown("<a href='https://morerationalph.streamlit.app/Venn_Diagram-Hamon_na_Tanong' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Sunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")


