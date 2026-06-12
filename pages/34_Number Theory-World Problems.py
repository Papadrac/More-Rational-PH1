import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Number Theory*: World Problems")
    st.write("Ang bawat tanong ay tungol sa LCM o GCD. Basahin nang maigi ang bawat tanong at gamitin ang iyong kaalaman sa Number Theory upang sagutin ito.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': (
            "Si Anthony at Ben ay parehong mahilig maglaro ng basketball. Naglalaro si Anthony tuwing ika-4 na araw at si Ben tuwing ika-6 na araw. Kung sila ay nagkasabay maglaro ngayon, ilang araw kaya ulit silang magsasabay na maglaro? (LCM)"
        ),
        'choices': ["8", "12", "16", "24", "32"],
        'correct': ["12"],
        'hint': "Tip: Hanapin ang pinakamaliit na araw na parehong mahahati ng 4 at 6. Pwede mong isulat ang mga multiples ng 4 at 6, at hanapin ang unang magkapareho.",
        'how_to_solve': "❌ Mali: Dapat LCM(4,6) = 12. Ang 12 ang pinakamaliit na numero na parehong mahahati ng 4 at 6."
    },
    {
        'question': (
            "Si Maria ay may 20 na mangga at 30 na saging. Gusto niyang ilagay ang mga ito sa mga supot na may parehong dami ng prutas at walang natitira. Ano ang pinakamaraming prutas sa bawat supot? (GCD)"
        ),
        'choices': ["2", "4", "5", "10", "20"],
        'correct': ["10"],
        'hint': "Tip: Hanapin ang pinakamalaking bilang na parehong mahahati ng 20 at 30. Ito ang GCD.",
        'how_to_solve': "❌ Mali: Dapat GCD(20,30) = 10. Ang 10 ang pinakamalaking bilang na parehong mahahati ng 20 at 30."
    },
    {
        'question': (
            "Si Carlo ay may 18 na mansanas at 24 na peras. Gusto niyang ilagay ang mga ito sa pinakamaraming pantay-pantay na supot na walang natitira. Ilan ang prutas sa bawat supot?"
        ),
        'choices': ["2", "3", "6", "8", "12"],
        'correct': ["6"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamalaking bilang na parehong mahahati ng 18 at 24."
    },
    {
        'question': (
            "May 42 na tsokolate at 56 na kendi si Liza. Gusto niyang hatiin ito sa mga supot na may parehong dami ng tsokolate at kendi, at walang natitira. Ano ang pinakamaraming supot na magagawa niya?"
        ),
        'choices': ["2", "7", "8", "14", "28"],
        'correct': ["14"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamalaking bilang na parehong mahahati ng 42 at 56."
    },
    {
        'question': (
            "Ang dalawang ilaw ay sabay na bumukas. Ang una ay umiilaw tuwing ika-9 na segundo, ang pangalawa tuwing ika-12 segundo. Sa ilang segundo sila muling magsasabay na umiilaw?"
        ),
        'choices': ["9", "12", "18", "24", "36"],
        'correct': ["36"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamaliit na segundo na parehong mahahati ng 9 at 12."
    },
    {
        'question': (
            "Si Mark ay may 27 na lapis at 45 na bolpen. Gusto niyang hatiin ito sa mga kahon na may parehong dami ng lapis at bolpen, at walang natitira. Ano ang pinakamaraming kahon na magagawa niya?"
        ),
        'choices': ["3", "5", "9", "15", "27"],
        'correct': ["9"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamalaking bilang na parehong mahahati ng 27 at 45."
    },
    {
        'question': (
            "May dalawang grupo ng estudyante: 20 sa una at 30 sa pangalawa. Gusto ng guro na hatiin sila sa pinakamalaking grupo na walang natitira. Ilan ang estudyante sa bawat grupo?"
        ),
        'choices': ["2", "4", "5", "10", "20"],
        'correct': ["10"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamalaking bilang na parehong mahahati ng 20 at 30."
    },
    {
        'question': (
            "Siya ay may dalawang alarm clock: Ang isa ay tumutunog tuwing ika-6 na minuto, ang isa tuwing ika-8 minuto. Sa ilang minuto sila muling magsasabay na tumunog?"
        ),
        'choices': ["6", "8", "12", "16", "24"],
        'correct': ["24"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamaliit na minuto na parehong mahahati ng 6 at 8."
    },
    {
        'question': (
            "May 36 na mangga at 48 na saging si Tita. Gusto niyang ilagay ito sa mga basket na may parehong dami ng prutas at walang natitira. Ano ang pinakamaraming basket na magagawa niya?"
        ),
        'choices': ["6", "8", "12", "18", "24"],
        'correct': ["12"],
        'how_to_solve': "❌ Mali: Hanapin ang pinakamalaking bilang na parehong mahahati ng 36 at 48."
    },
]






# First two questions are always fixed, next three are random (no repeats, not including first two)
if 'quiz_data' not in st.session_state:
    if len(quiz_fixed) >= 5:
        fixed_qs = quiz_fixed[:2]
        rest = quiz_fixed[2:]
        random_qs = random.sample(rest, k=3) if len(rest) >= 3 else random.choices(rest, k=3)
        st.session_state['quiz_data'] = fixed_qs + random_qs
    else:
        st.session_state['quiz_data'] = random.choices(quiz_fixed, k=5)
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
# Ipakita ang hint kung meron, pagkatapos ng sagot input
if 'hint' in q:
    st.info(q['hint'])
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
            st.markdown("<a href='https://morerationalph.streamlit.app/Number_Theory-Completion' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
