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
        "question": "May 4 na bola (A, B, C, D). Pipili ng 2 bola nang sabay-sabay. Ano ang probability na mapili ang bola A at B?",
        "choices": ["1/6", "1/4", "1/12", "1/8"],
        "answer": {"1/6"},
        "image": "https://imgur.com/8uTtZ92.jpg",
            "solution": "May \\(\\binom{4}{2} = 6\\) na posibleng pares. Isa lang ang tamang pares (A at B), kaya probability = 1/6.",
        "image_width": 400,
        "hint": "Hanapin ang total na posibleng pares naglalaman ng A at B at ang lahat ng posibleng pares."
    },
    {
        "question": "May 5 na libro, isa dito ay matematika. Ilan ang probability na ang librong matematika ay una pag inayos ang lahat ng libro sa isang row?",
        "choices": ["2/15", "1/10", "24/120", "3/10"],
        "answer": {"24/120"},
        "image": None,
        "solution": "May 5! = 120 na posibleng arrangements ng 5 libro. Kung ang librong matematika ay una, may 4! = 24 na posibleng arrangements para sa natitirang libro. Probability = 24/120 = 1/5.",
        "image_width": 400,
        "hint": "Isipin ang librong matematika bilang nakauna, tapos hanapin ang total arrangements para sa natitirang libro."
    },
    {
        "question": "May 5 kendi (1 asul, 4 pula). Pipili ng 2 kendi nang sabay-sabay. Ano ang probability na parehong asul ang mapili?",
        "choices": ["0", "1/10", "1/5", "2/5"],
        "answer": {"0"},
        "image": None,
            "solution": "May \\(\\binom{5}{2} = 10\\) na posibleng pares. Isa lang ang asul, kaya hindi pwedeng parehong asul ang mapili.",
        "image_width": 400,
        "hint": "Hanapin ang total na posibleng pares at ang pares na parehong asul."
    },
    {
        "question": "May 6 na estudyante. Pipili ng 3 para sa isang laro. Ano ang probability na mapili ang tatlong magkakaibigan?",
        "choices": ["1/20", "1/6", "1/12", "1/8"],
        "answer": {"1/20"},
        "image": None,
            "solution": "May \\(\\binom{6}{3} = 20\\) na posibleng grupo ng 3. Isa lang ang tamang grupo.",
        "image_width": 400
    },
    {
        "question": "May 3 pula at 2 asul na bola. Pipili ng 2 bola nang sabay-sabay. Ano ang probability na parehong asul ang mapili?",
        "choices": ["1/10", "1/5", "2/5", "1/6"],
        "answer": {"1/10"},
        "image": None,
            "solution": "May \\(\\binom{5}{2} = 10\\) na posibleng pares. May \\(\\binom{2}{2} = 1\\) paraan para parehong asul.",
        "image_width": 400
    },
    {
        "question": "May 4 na cards (A, B, C, D). Pipili ng 2 cards. Ano ang probability na makuha ang A, B, o C?",
        "choices": ["3/6", "1/12", "1/8", "1/4"],
        "answer": {"3/6"},
        "image": None,
            "solution": "May \\(\\binom{4}{2} = 6\\) na posibleng pares. May \\(\\binom{3}{2} = 3\\) paraan para makuha ang A, B, o C.",
        "image_width": 400
    }
    ,
    # Permutation-related probability questions
    
    {
        "question": "May 6 na tao. Ano ang probability na ang isang partikular na tao ay nasa unahan kapag pinapila silang lahat?",
        "choices": ["120/720", "1/36", "1/3", "2/7"],
        "answer": {"120/720"},
        "image": None,
        "solution": "Total arrangements: 6! = 720. Kung ang partikular na tao ay nasa unahan, 5! = 120 arrangements para sa natitira.",
        "image_width": 400,
        "hint": "Ilagay agad ang partikular na tao sa unahan, tapos ayusin ang natitira."
    },
    {
        "question": "May 4 na upuan at 4 na tao. Ano ang probability na si Maria ang nakaupo sa huling upuan?",
        "choices": ["6/24", "8/24", "1/9", "2/7"],
        "answer": {"6/24"},
        "image": None,
        "solution": "Total arrangements: 4! = 24. Kung si Maria ay nakaupo sa huling upuan, may 3! = 6 arrangements para sa natitira.",
        "image_width": 400,
        "hint": "Ilagay si Maria sa huling upuan, tapos ayusin ang natitira."
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
    st.subheader("*Probability*: With Combinatorics")
    st.write("Hanapin ang probability ng mga pangyayari. Gamitin ang kaalaman sa kombinasyon at permutasyon para sagutin ang mga tanong.")
    
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

# Show hint for the first and second question
if st.session_state.index in [0, 1] and q.get("hint"):
    st.info(f"Hint: {q['hint']}")


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
        solution = q.get('solution', '')
        if solution:
            # Extract LaTeX between \( and \), display as LaTeX, rest as text
            import re
            parts = re.split(r'(\\\(.*?\\\))', solution)
            for part in parts:
                if part.startswith('\\(') and part.endswith('\\)'):
                    st.latex(part[2:-2])
                elif part.strip():
                    st.info(part)
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
        solution = q.get('solution', '')
        if solution:
            import re
            parts = re.split(r'(\\\(.*?\\\))', solution)
            for part in parts:
                if part.startswith('\\(') and part.endswith('\\)'):
                    st.latex(part[2:-2])
                elif part.strip():
                    st.info(part)


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
