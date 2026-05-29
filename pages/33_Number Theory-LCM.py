import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*LCM*: Least Common Multiple")
    st.write("Hanapin ang pinakamaliit na numero na pweding hatiin ng naibigay na mga numero.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': (
            "Ano ang pinakamaliit na numero na pweding hatiin ng 8 at 12.\n"
            "\n"
            "**Para sa 8, magbilang ng waluhan:** <span style='color:blue; font-weight:bold'>8, 16, 24, 32</span>  \n"
            "**para sa 12, magbilang ng labing dalawahan:** <span style='color:green; font-weight:bold'>12, 24, 36, 48</span>  \n"
            "\n"
            "Kunin ang pinakamaliit na multiple na common sa dalawang set."
        ),
        'choices': ["2", "4", "6", "8", "12"],
        'correct': ["24"],
        'how_to_solve': "❌ Mali: Dapat LCM(8,12) = 24. Sa listahan, ang pinakamaliit na common multiple ay 24."
    },
    {
        'question': (
            "Ano ang pinakamaliit na numero na pweding hatiin ng 10 at 15.\n"
            "\n"
            "**para sa 10, magbilang ng sampuan:** <span style='color:blue; font-weight:bold'>10, 20, 30, 40</span>  \n"
            "**Para sa 15, magbilang ng labing limahan:** <span style='color:green; font-weight:bold'>15, 30, 45, 60</span>  \n"
            "\n"
            "Kunin ang pinakamaliit na multiple na common sa dalawang set."
        ),
        'choices': ["2", "3", "5", "10", "15"],
        'correct': ["30"],
        'how_to_solve': "❌ Mali: Dapat LCM(10,15) = 30. Sa listahan, ang pinakamaliit na common multiple ay 30."
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 6 at 9.",
        'choices': ["1", "2", "3", "6", "9"],
        'correct': ["18"],
        'how_to_solve': "❌ Mali: Dapat LCM(6,9) = 18"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 7 at 14.",
        'choices': ["1", "2", "7", "14", "21"],
        'correct': ["14"],
        'how_to_solve': "❌ Mali: Dapat LCM(7,14) = 14"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 5 at 10.",
        'choices': ["1", "2", "5", "10", "15"],
        'correct': ["10"],
        'how_to_solve': "❌ Mali: Dapat LCM(5,10) = 10"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 9 at 12.",
        'choices': ["1", "3", "4", "6", "9"],
        'correct': ["36"],
        'how_to_solve': "❌ Mali: Dapat LCM(9,12) = 36"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 9 at 15.",
        'choices': ["1", "3", "5", "9", "15"],
        'correct': ["45"],
        'how_to_solve': "❌ Mali: Dapat LCM(9,15) = 45"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 6 at 4.",
        'choices': ["1", "2", "5", "10", "15"],
        'correct': ["12"],
        'how_to_solve': "❌ Mali: Dapat LCM(4,6) = 12"
    },
    {
        'question': "Ano ang pinakamaliit na numero na pweding hatiin ng 7 at 14.",
        'choices': ["1", "2", "7", "14", "21"],
        'correct': ["14"],
        'how_to_solve': "❌ Mali: Dapat LCM(7,14) = 14"
    },
]





# First two questions are always fixed, next two are random (no repeats, not including first two)
if 'quiz_data' not in st.session_state:
    if len(quiz_fixed) >= 4:
        fixed_qs = quiz_fixed[:2]
        rest = quiz_fixed[2:]
        random_qs = random.sample(rest, k=2) if len(rest) >= 2 else random.choices(rest, k=2)
        st.session_state['quiz_data'] = fixed_qs + random_qs
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
            st.markdown("<a href='https://morerationalph.streamlit.app/Number_Theory-World_Problems' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
