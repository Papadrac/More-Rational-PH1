import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Combinatorics*: Word Problems")
    st.write("Bilangin ang bilang ng posibleng ayos o pagkakasunod-sunod ng mga bagay.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    # Permutation questions (order matters)
    {
        'question': "May 8 na mag-aaral sa klase. Ilang paraan pwedeng pumili ng president, vice president, at secretary (3 positions, 3 tao, order matters)?",
        'choices': ["336", "56", "24", "512", "120"],
        'correct': ["336"],
        'how_to_solve': "Order matters dahil bawat posisyon ay natatangi (president ≠ vice president ≠ secretary). Ginagamit ang permutation: P(8,3) = 8 × 7 × 6 = 336."
    },
    {
        'question': "May 10 na kabataan. Ilang paraan pwedeng pumili ng 5 na magkakaibang posisyon sa basketball team (hal. captain, co-captain, scorer, etc.)?",
        'choices': ["30240", "252", "120", "100", "210"],
        'correct': ["30240"],
        'how_to_solve': "Order matters dahil bawat posisyon ay may natatanging tungkulin. Ginagamit ang permutation: P(10,5) = 10 × 9 × 8 × 7 × 6 = ?."
    },
    {
        'question': "May 6 na putahe. Ilang paraan pwedeng ayusin ang 2 na ihahain sa bisita (unang putahe at pangalawang putahe, order matters)?",
        'choices': ["30", "15", "12", "36", "20"],
        'correct': ["30"],
        'how_to_solve': "Order matters dahil magkaiba ang unang putahe at pangalawang putahe. Ginagamit ang permutation: P(6,2) = 6 × 5 = ?."
    },
    {
        'question': "May 7 kandidato. Ilang paraan pwedeng pumili ng 3 na magkakaibang posisyon sa SK (hal. chairman, secretary, treasurer)?",
        'choices': ["210", "35", "21", "120", "42"],
        'correct': ["210"],
        'how_to_solve': "Order matters dahil bawat posisyon ay natatangi. Ginagamit ang permutation: P(7,3) = 7 × 6 × 5 = ?."
    },
    {
        'question': "May 5 na prutas. Ilang paraan pwedeng ayusin ang 2 na ilalagay sa basket (may pagkakasunod-sunod)?",
        'choices': ["20", "10", "15", "5", "25"],
        'correct': ["20"],
        'how_to_solve': "Order matters dahil magkaiba ang una at pangalawang prutas sa basket. Ginagamit ang permutation: P(5,2) = 5 × 4 = ?."
    },
    {
        'question': "May 9 na libro. Ilang paraan pwedeng pumili ng 4 na babasahin sa tiyak na pagkakasunod-sunod (reading order matters)?",
        'choices': ["3024", "126", "36", "84", "24"],
        'correct': ["3024"],
        'how_to_solve': "Order matters dahil mahalaga ang pagkakasunod-sunod ng pagbasa. Ginagamit ang permutation: P(9,4) = 9 × 8 × 7 × 6 = ?."
    },
    # Combination questions (order does not matter)
    {
        'question': "May 9 na estudyante sa klase. Kung pipili ng 6 na kasali sa group project, ilang iba't ibang grupo ang maaaring mabuo?",
        'choices': ["84", "126", "60", "504", "36"],
        'correct': ["84"],
        'how_to_solve': "Order does not matter dahil grupo lang ang mahalaga, hindi ang posisyon. Ginagamit ang combination: C(9,6) = 9 × 8 × 7 × 6 × 5 × 4 ÷ (6 × 5 × 4 × 3 × 2 × 1) = ?."
    },
    {
        'question': "May 5 na guro na maaaring maging panel sa isang contest. Kung pipili ng 3 na magiging panel, ilang iba't ibang grupo ng panel ang maaaring mabuo?",
        'choices': ["10", "60", "20", "15", "5"],
        'correct': ["10"],
        'how_to_solve': "Order does not matter dahil grupo ng panel lang ang mahalaga, hindi ang pagkakasunod-sunod. Ginagamit ang combination: C(5,3) = 5 × 4 × 3 ÷ (3 × 2 × 1) = ?."
    },
    {
        'question': "May 7 na manlalaro sa isang laro. Kung pipili ng 2 na magiging kapitan, ilang iba't ibang pares ng kapitan ang maaaring mapili?",
        'choices': ["21", "14", "42", "35", "7"],
        'correct': ["21"],
        'how_to_solve': "Order does not matter dahil pares lang ng kapitan ang mahalaga, hindi kung sino ang una. Ginagamit ang combination: C(7,2) = 7 × 6 ÷ (2 × 1) = ?."
    },
    {
        'question': "May 12 na kandidato sa isang talent show. Kung pipili ng 4 na magpe-perform sa grand finals, ilang iba't ibang grupo ng performers ang maaaring mapili?",
        'choices': ["495", "792", "11880", "1365", "330"],
        'correct': ["495"],
        'how_to_solve': "Order does not matter dahil grupo lang ng performers ang mahalaga, hindi ang pagkakasunod-sunod ng performance. Ginagamit ang combination: C(12,4) = 12 × 11 × 10 × 9 ÷ (4 × 3 × 2 × 1) = ?."
    },
    {
        'question': "May 8 na klase sa isang araw. Kung pipili ng 3 na subject na bibigyan ng project, ilang iba't ibang kombinasyon ng subject ang maaaring mapili?",
        'choices': ["56", "24", "336", "120", "512"],
        'correct': ["56"],
        'how_to_solve': "Order does not matter dahil subject lang ang pipiliin, hindi ang pagkakasunod-sunod. Ginagamit ang combination: C(8,3) = 8 × 7 × 6 ÷ (3 × 2 × 1) = ?."
    },
    {
        'question': "May 15 na estudyante na gustong sumali sa field trip. Kung 5 lang ang pwedeng isama, ilang iba't ibang grupo ng estudyante ang maaaring mapili?",
        'choices': ["3003", "5005", "1365", "6435", "2002"],
        'correct': ["3003"],
        'how_to_solve': "Order does not matter dahil grupo lang ng estudyante ang pipiliin, hindi ang posisyon o pagkakasunod-sunod. Ginagamit ang combination: C(15,5) = 15 × 14 × 13 × 12 × 11 ÷ (5 × 4 × 3 × 2 × 1) = ?."
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
            st.markdown("<a href='https://morerationalph.streamlit.app/Combinatorics_Challenging_Questions' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
