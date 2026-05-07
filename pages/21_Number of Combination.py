import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Permutations*: Bilang ng Posibleng Ayos")
    st.write("Bilangin ang bilang ng posibleng ayos o pagkakasunod-sunod ng mga bagay.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': "May 8 na mag-aaral sa klase. Ilang paraan pwedeng pumili ng 3 na magiging kinatawan para sa quiz bee?",
        'choices': ["56", "336", "24", "512", "120"],
        'correct': ["56"],
        'how_to_solve': "❌ Mali: Dapat C(8,3) = 8 × 7 × 6 ÷ (3 × 2 × 1) = 56"
    },
    {
        'question': "Sa isang barangay, may 10 na kabataan. Ilang paraan pwedeng pumili ng 5 na kasali sa basketball team?",
        'choices': ["210", "252", "24", "120", "100"],
        'correct': ["252"],
        'how_to_solve': "❌ Mali: Dapat C(10,5) = 10 × 9 × 8 × 7 × 6 ÷ (5 × 4 × 3 × 2 × 1) =?"
    },
    {
        'question': "May 6 na putahe sa handaan. Ilang paraan pwedeng pumili ng 2 na ihahain sa bisita?",
        'choices': ["15", "30", "12", "36", "20"],
        'correct': ["15"],
        'how_to_solve': "❌ Mali: Dapat C(6,2) = 6 × 5 ÷ (2 × 1) = ?"
    },
    {
        'question': "May 7 na kandidato sa Sangguniang Kabataan. Ilang paraan pwedeng pumili ng 3 na mananalo bilang kagawad?",
        'choices': ["35", "210", "21", "120", "42"],
        'correct': ["35"],
        'how_to_solve': "❌ Mali: Dapat C(7,3) = 7 × 6 × 5 ÷ (3 × 2 × 1) = ?"
    },
    {
        'question': "May 5 na prutas. Ilang paraan pwedeng pumili ng 2 na ilalagay sa basket?",
        'choices': ["10", "20", "15", "5", "25"],
        'correct': ["10"],
        'how_to_solve': "❌ Mali: Dapat C(5,2) = 5 × 4 ÷ (2 × 1) = ?"
    },
    {
        'question': "May 9 na libro sa shelf. Kung hindi ikonsidera ang order, Ilang paraan pwedeng pumili ng 4 na babasahin ngayong bakasyon?",
        'choices': ["126", "3024", "36", "84", "24"],
        'correct': ["126"],
        'how_to_solve': "❌ Mali: Dapat C(9,4) = 9 × 8 × 7 × 6 ÷ (4 × 3 × 2 × 1) = ?"
    },
    {
        'question': "May 9 na estudyante. Ilang paraan pwedeng pumili ng 6 na kasali sa group project?",
        'choices': ["84", "126", "60", "504", "36"],
        'correct': ["84"],
        'how_to_solve': "❌ Mali: Dapat C(9,6) = 9 × 8 × 7 × 6 × 5 × 4 ÷ (6 × 5 × 4 × 3 × 2 × 1) = ?"
    },
    {
        'question': "May 5 na guro. Ilang paraan pwedeng pumili ng 3 na magiging panel sa contest?",
        'choices': ["10", "60", "20", "15", "5"],
        'correct': ["10"],
        'how_to_solve': "❌ Mali: Dapat C(5,3) = 5 × 4 × 3 ÷ (3 × 2 × 1) = ?"
    },
    {
        'question': "May 7 na manlalaro. Ilang paraan pwedeng pumili ng 2 na magiging kapitan ng laro?",
        'choices': ["21", "14", "42", "35", "7"],
        'correct': ["21"],
        'how_to_solve': "❌ Mali: Dapat C(7,2) = 7 × 6 ÷ (2 × 1) = ?"
    },
]




# First question is always the first in quiz_fixed, the rest are random (no repeats)
if 'quiz_data' not in st.session_state:
    if len(quiz_fixed) >= 4:
        first_q = quiz_fixed[0]
        rest = quiz_fixed[1:]
        random_qs = random.sample(rest, k=3) if len(rest) >= 3 else random.choices(rest, k=3)
        st.session_state['quiz_data'] = [first_q] + random_qs
    else:
        st.session_state['quiz_data'] = random.choices(quiz_fixed, k=4)
quiz_data = st.session_state['quiz_data']

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


# All questions: type answer (text input)
typed_answer = st.text_input("Isulat ang sagot:", value="", key=f"typed{step}")
submit = st.button("Ipadala", key=f"submit{step}")
if f'retry_{step}' not in st.session_state or st.session_state.get('retry_step', 0) != step:
    st.session_state[f'retry_{step}'] = 0
    st.session_state['retry_step'] = step
if submit:
    user_ans = typed_answer.strip()
    if user_ans == q['correct'][0]:
        st.balloons()
        feedback_placeholder.success("Tama!")
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
            # Only show how to solve, do not show the final answer
            if 'how_to_solve' in q:
                feedback_placeholder.info(q['how_to_solve'])


# Update score display to be out of 5
nav_col1, nav_col2 = st.columns([1, 1])
with nav_col1:
    st.button("Nakaraan", on_click=lambda: st.session_state.update({'quiz_step': max(1, step-1)}), disabled=(step == 1), key=f"prev{step}")
    st.markdown(f"<div style='text-align:center; margin-top:8px; font-size:1.1em; font-weight:bold;'>Puntos: {st.session_state['quiz_score']} / 4</div>", unsafe_allow_html=True)
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
            st.markdown(f"<div style='font-size:1.3em; font-weight:bold; color:#2E8B57;'>Final Score: {st.session_state['quiz_score']} / 4</div>", unsafe_allow_html=True)
            if st.session_state['quiz_score'] == 4:
                st.success("Perfect! 🎉")
        with col_reset:
            if st.button("Sagutan Muli", key="reset_quiz"):
                st.session_state.clear()
        with col_btn:
            st.markdown("<a href='https://morerationalph.streamlit.app/' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
