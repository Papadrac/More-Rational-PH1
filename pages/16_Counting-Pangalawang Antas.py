import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Counting*: Pangalawang Antas")
    st.write("Bilangin ang mga *elements* na tinutukoy sa bawat tanong")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': "Ilang buong numero ang merun mula 13 hanggang 19?",
        'choices': ["19", "7", "13", "6", "11"],
        'correct': ["7"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 13 hanggang 19 ay 13, 14, 15, 16, 17, 18, at 19. Ilang numero ito?"
    },
    {
        'question': "Ilang <i>even numbers</i> merun mula 9 hanggang 24?",
        'choices': ["9", "24", "13", "7", "8"],
        'correct': ["8"],
        'how_to_solve': "❌ Mali: Ang mga even numbers mula 9 hanggang 24 ay 10, 12, 14, 16, 18, 20, 22, at 24. Ilang numero ito?"
    },
    {
        'question': "Mula 12 hanggang 27, Ilan dito ay <i>even numbers</i>?",
        'choices': ["9", "24", "13", "7", "8"],
        'correct': ["8"],
        'how_to_solve': "❌ Mali: Ang mga even numbers mula 12 hanggang 27 ay 12, 14, 16, 18, 20, 22, 24, at 26. Ilang numero ito?"
    },
    {
        'question': "Ilang buong numero ang merun mula 25 hanggang 36?",
        'choices': ["12", "25", "13", "6", "11"],
        'correct': ["12"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 25 hanggang 36 ay 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, at 36. Ilang numero ito?"
    },
    {
        'question': "Ilang buong numero mula 17 hanggang 105 na nagtatapos sa 0 gaya ng 20, 30, 40, ...?",
        'choices': ["10", "24", "105", "9", "8"],
        'correct': ["9"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 17 hanggang 105 na nagtatapos sa 0 ay 20, 30, 40, 50, 60, 70, 80, 90, at 100. Ilang numero ito?"
    },
    {
        'question': "Ilang buong numero mula 57 hanggang 105 na kayang hatiin sa 5 gaya ng 60, 65, 70, ...?",
        'choices': ["10", "24", "105", "9", "8"],
        'correct': ["10"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 57 hanggang 105 na kayang hatiin sa 5 ay 60, 65, 70, 75, 80, 85, 90, 95, 100, at 105. Ilang numero ito?"
    },
    {
        'question': "Mula 7 hanggang 25, ilan ang pweding kayang hatiin sa tatlo gaya ng 9, 12, 15, ...?",
        'choices': ["10", "7", "6", "9", "8"],
        'correct': ["6"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 7 hanggang 25 na kayang hatiin sa 3 ay 9, 12, 15, 18, 21, at 24. Ilang numero ito?"
    },
    {
        'question': "Mula 7 hanggang 49, ilan ang pweding kayang hatiin sa pito gaya ng 7 at 14?",
        'choices': ["10", "7", "6", "9", "8"],
        'correct': ["7"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 7 hanggang 49 na kayang hatiin sa 7 ay 7, 14, 21, 28, 35, 42, at 49."
    },
   {
        'question': "Mula 7 hanggang 49, ilan ang pweding kayang hatiin sa walo gaya ng 8 at 16?",
        'choices': ["10", "7", "6", "9", "8"],
        'correct': ["6"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 7 hanggang 49 na kayang hatiin sa 8 ay 8, 16, 24, 32, 40, at 48."
    },
    {
        'question': "Mula 50 hanggang 79, ilan ang pweding kayang hatiin sa apat gaya ng 52, 56, 60, ...?",
        'choices': ["7", "8", "6", "9", "10"],
        'correct': ["6"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 50 hanggang 79 na kayang hatiin sa 4 ay 52, 56, 60, 64, 68, 72 at 76."
    },
    {
        'question': "Mula 50 hanggang 79, ilan ang pweding kayang hatiin sa sampu?",
        'choices': ["1", "2", "3", "4", "5"],
        'correct': ["3"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 50 hanggang 79 na kayang hatiin sa 10 ay 50, 60, at 70."
    },
    {
        'question': "Mula 10 hanggang 30, ilan ang pweding kayang hatiin sa tatlo?",
        'choices': ["5", "6", "7", "8", "9"],
        'correct': ["7"],
        'how_to_solve': "❌ Mali: Ang mga buong numero mula 10 hanggang 30 na kayang hatiin sa 3 ay 12, 15, 18, 21, 24, 27, at 30."
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
            st.markdown("<a href='https://morerationalph.streamlit.app/Number_of_Arrangement-Tutorial' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
