import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Counting*: Unang Antas")
    st.write("Bilangin ang mga *elements* na tinutukoy sa bawat tanong")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': "Hayaan ang <i>set</i> A={1,2,3,4,5,6}. Ilan ang bilang ng mga <i>elements</i> sa set A?",
        'choices': ["1", "3", "4", "6", "7"],
        'correct': ["6"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set A. Ang set A ay binubuo ng mga numero 1, 2, 3, 4, 5, at 6. Kaya ang bilang ng mga *elements* sa set A ay 6."
    },
    {
        'question': "Ang mga kasama sa isang ganap ay pweding ilarawan bilang isang <i>set</i> <span style='display:inline-block; background:#f0f0f0; border-radius:6px; padding:2px 8px; font-weight:bold;'>A=&#123;tatay, nanay, kuya, kapitan, lola, guro, doktor, ate&#125;</span>.<br><span style='display:inline-block; margin-top:8px;'>Ilan dito ang matuturing na miyembro ng isang pamilya?</span>",
        'choices': ["3", "4", "5", "6", "7"],
        'correct': ["5"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set A na maaring maging miyembro ng pamilya."
    },
    {
        'question': "Hayaan ang <i>set</i> A={8,9,3,15,17,26,50}. Ilan ang bilang ng mga <i>elements</i> sa set A?",
        'choices': ["1", "3", "4", "6", "7"],
        'correct': ["7"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set A. Ang set A ay binubuo ng mga numero 8, 9, 3, 15, 17, 26, at 50."
    },
    {
        'question': "Hayaan ang <i>set</i> B={3,5,7,9,10,11,12,13}. Ilan dito ay <i>even numbers</i>?",
        'choices': ["2", "3", "4", "5"],
        'correct': ["2"],
        'how_to_solve': "Ang mga *even numbers* ay mga buong numero na kayang hatiin sa dalawa nang walang natitirang bahagi."
    },
    {
        'question': "Hayaan ang <i>set</i> A={1,2,3,4,5,6}. Ilan ang bilang ng mga <i>elements</i> sa set A na <i>prime numbers</i>?",
        'choices': ["1", "3", "4", "6", "7"],
        'correct': ["3"],
        'how_to_solve': "Ang mga *prime numbers* ay mga buong numero na mas malaki sa 1 at walang ibang mga *divisors* maliban sa 1 at ang kanilang sarili. Gaya ng 3 dahil wala ng pweding hatiin sa 3 maliban sa 1 at 3."
    },
    {
        'question': "Hayaan ang <i>set</i> A={10,11,12,13,14,15}. Ilan ang bilang ng mga <i>elements</i> sa set A na <i>prime numbers</i>?",
        'choices': ["1", "2", "3", "4", "5"],
        'correct': ["2"],
        'how_to_solve': "Ang mga *prime numbers* ay mga buong numero na mas malaki sa 1 at walang ibang mga *divisors* maliban sa 1 at ang kanilang sarili. Gaya ng 11 at 13 dahil wala ng pweding hatiin sa kanila maliban sa 1 at sa kanilang sarili."
    },
    {
        'question': "Ang mga hayop na meron si Jhon ay pweding ilarawan bilang isang <i>set</i> <span style='display:inline-block; background:#f0f0f0; border-radius:6px; padding:2px 8px; font-weight:bold;'>H=&#123;kambing, baka, manok, aso, pusa, pato, baboy, kalapati, parrot&#125;</span>.<br><span style='display:inline-block; margin-top:8px;'>Ilan dito ang may mga pakpak?</span>",
        'choices': ["3", "4", "5", "6", "7"],
        'correct': ["4"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set H na may mga pakpak."
    },
    {
        'question': "Hayaan ang <i>set</i> B={3,5,6,7,8,9,10}. Ilan dito ang mga numerong pweding hatiin sa tatlo?",
        'choices': ["1", "3", "4", "6", "7"],
        'correct': ["3"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set B na kayang hatiin sa tatlo. Ang mga numerong kayang hatiin sa tatlo ay 6, 9, at 3. Kaya ang bilang ng mga *elements* sa set B na kayang hatiin sa tatlo ay 3."
    },
    {
        'question': "Hayaan ang <i>set</i> B={3,5,6,7,8,9,10}. Ilan dito ang mga numerong pweding hatiin sa lima?",
        'choices': ["1", "3", "4", "6", "7"],
        'correct': ["2"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set B na kayang hatiin sa lima. Ang mga numerong kayang hatiin sa lima ay 5 at 10."
    },
    {
        'question': "Hayaan ang <i>set</i> F={1,2,3,4,5,6}. Ilan dito ang mga numerong <i>factors of 12</i>?",
        'choices': ["1", "3", "4", "5", "6"],
        'correct': ["5"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set F na kayang humati sa 12 gaya ng 2."
    },
    {
        'question': "Hayaan ang <i>set</i> F={2,3,5,7,8,9,12,15}. Ilan dito ang mga numerong <i>factors of 36</i>?",
        'choices': ["1", "3", "4", "5", "6"],
        'correct': ["4"],
        'how_to_solve': "Sa tanong na ito, kailangan nating bilangin ang mga *elements* sa set F na kayang humati sa 36 gaya ng 3 at 9."
    },
]


# Only first two are fixed, the rest are random
quiz_fixed_questions = quiz_fixed[:2]
quiz_pool = quiz_fixed[2:]
if 'random_3' not in st.session_state:
    st.session_state['random_3'] = random.sample(quiz_pool, k=3) if len(quiz_pool) >= 3 else random.choices(quiz_pool, k=3)
quiz_data = quiz_fixed_questions + st.session_state['random_3']

if 'quiz_score' not in st.session_state:
    st.session_state['quiz_score'] = 0
if 'quiz_last_scored_step' not in st.session_state:
    st.session_state['quiz_last_scored_step'] = None

step = st.session_state['quiz_step']
total = len(quiz_data)

st.subheader(f"Tanong {step} ng {total}")
st.progress(step / total)


q = quiz_data[step-1]
## st.image(q['image'], width=350, caption=q['caption'])
st.markdown(f"<div style='font-size:1.2em; font-weight:400; margin-bottom:12px'>{q['question']}</div>", unsafe_allow_html=True)
feedback_placeholder = st.empty()


# All questions: normal single-choice dropdown
selected = st.selectbox("Pumili ng sagot:", q['choices'], index=None, key=f"single{step}", placeholder="Pumili ng sagot")
submit = st.button("Ipadala", key=f"submit{step}")
if f'retry_{step}' not in st.session_state or st.session_state.get('retry_step', 0) != step:
    st.session_state[f'retry_{step}'] = 0
    st.session_state['retry_step'] = step
if submit:
    if selected == q['correct'][0]:
        st.balloons()
        feedback_placeholder.success("Tama!")
        # if 'updated_image' in q:
        #     feedback_placeholder.image(q['updated_image'], width=350, caption=q.get('updated_caption', 'Updated Venn Diagram'))
        last = st.session_state['quiz_last_scored_step']
        # Only score if not already scored and retries not exhausted
        if last != step and st.session_state[f'retry_{step}'] < 2:
            st.session_state['quiz_score'] += 1
            st.session_state['quiz_last_scored_step'] = step
        st.session_state[f'retry_{step}'] = 0
    else:
        st.session_state[f'retry_{step}'] += 1
        if st.session_state[f'retry_{step}'] == 1:
            retries_left = 2 - st.session_state[f'retry_{step}']
            feedback_placeholder.error(f"Mali. Subukan muli! ({retries_left} natitirang subok)")
            if 'how_to_solve' in q:
                feedback_placeholder.info(q['how_to_solve'])
            if st.button("Subukan Ulit", key=f"retry{step}"):
                st.experimental_rerun()
        elif st.session_state[f'retry_{step}'] == 2:
            feedback_placeholder.error(f"Ang tamang sagot ay: {', '.join(q['correct'])}")
            # Do NOT reset retry counter here, so final score logic can detect retries are finished
            # st.session_state[f'retry_{step}'] = 0


# Update score display to be out of 5
nav_col1, nav_col2 = st.columns([1, 1])
with nav_col1:
    st.button("Nakaraan", on_click=lambda: st.session_state.update({'quiz_step': max(1, step-1)}), disabled=(step == 1), key=f"prev{step}")
    st.markdown(f"<div style='text-align:center; margin-top:8px; font-size:1.1em; font-weight:bold;'>Puntos: {st.session_state['quiz_score']} / 5</div>", unsafe_allow_html=True)
with nav_col2:
    st.button("Susunod", on_click=lambda: st.session_state.update({'quiz_step': min(total, step+1)}), disabled=(step == total), key=f"next{step}")

# Final score report after last question
if step == total:
    # For normal questions, check if correct or retries run out
    last_done = False
    if st.session_state.get(f'retry_{step}', 0) >= 2 or st.session_state.get('quiz_last_scored_step') == step:
        last_done = True
    if last_done:
        st.markdown("---")
        col_score, col_reset, col_btn = st.columns([2,1,2])
        with col_score:
            st.markdown(f"<div style='font-size:1.3em; font-weight:bold; color:#2E8B57;'>Final Score: {st.session_state['quiz_score']} / 5</div>", unsafe_allow_html=True)
            if st.session_state['quiz_score'] == 5:
                st.success("Perfect! 🎉")
        with col_reset:
            if st.button("Sagutan Muli", key="reset_quiz"):
                st.session_state.clear()
        with col_btn:
            st.markdown("<a href='https://morerationalph.streamlit.app/Counting-Pangalawang_Antas' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Parami pang Darating na Pahina, return Home &#8594;</button></a>", unsafe_allow_html=True)
