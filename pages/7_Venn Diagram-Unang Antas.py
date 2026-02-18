import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Venn Diagram*: Unang Antas")
    st.write("Para makumpleto ang *Venn Diagram*, hanapin ang A ∩ B, A - B, at B - A. Pumili ng tamang sagot sa bawat tanong.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

# Fixed first 7 questions
quiz_fixed = [
    {
        'question': "Kung naalala mo ang <i>intersection</i> ang pulang parte ay nirepresenta nito. Kung ang <b>A={1,3,4,7}</b> at <b>B={2,4,5,6,7}</b>, hanapin ang A ∩ B. Hanapin ang mga <i>elements</i> na parehong nasa A at B.",
        'choices': ["{1, 3}", "{4, 7}", "{1,2,3,4,5,6,7}", "{2,5,6}"],
        'correct': ["{4, 7}"],
        'image': "https://imgur.com/ov17u4z.jpg",
        'caption': "Ang Pulang Parte: A ∩ B",
        'updated_image': "https://imgur.com/3Kn1mS7.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang *intersection* ay binubuo ng mga *elements* parehong nasa A at B."
    },
    {
        'question': "Kung naalala mo ang <i>set difference</i> ang pulang parte ay nirepresenta nito. Balikan ang mga <i>sets</i> <b>A={1,3,4,7}</b> at <b>B={2,4,5,6,7}</b>, hanapin ang A - B. Hanapin ang mga <i>elements</i> na nasa A pero wala sa B.",
        'choices': ["{1, 3}", "{4, 7}", "{1,2,3,4,5,6,7}", "{2,5,6}"],
        'correct': ["{1, 3}"],
        'image': "https://imgur.com/TmSrxF3.jpg",
        'caption': "Ang Pulang Parte: A - B",
        'updated_image': "https://imgur.com/bMG2DKh.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang A - B ay mga *element* na nasa A pero wala sa B."
    },
    {
        'question': "Kung naalala mo ang <i>set difference</i> ang pulang parte ay nirepresenta nito. Balikan ang mga <i>sets</i> <b>A={1,3,4,7}</b> at <b>B={2,4,5,6,7}</b>, ngayon hanapin naman natin ang B - A. Hanapin ang mga <i>elements</i> na nasa B pero wala sa A.",
        'choices': ["{1, 3}", "{4, 7}", "{1,2,3,4,5,6,7}", "{2, 5, 6}"],
        'correct': ["{2, 5, 6}"],
        'image': "https://imgur.com/Jcnt4Cxh.jpg",
        'caption': "Ang Pulang Parte: B - A",
        'updated_image': "https://imgur.com/cvACk3H.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang B - A ay mga *element* na nasa B pero wala sa A."
    },
    {
        'question': "Tingan naman natin kung ano ang <i>venn diagram</i> ng <b>A={p,i,n,o,y}</b> at <b>B={s,a,n,t,o,l}</b>, hanapin muna ang A ∩ B.",
        'choices': ["{n, o}", "{p, i}", "{s, a}", "{t, l}"],
        'correct': ["{n, o}"],
        'image': "https://imgur.com/ov17u4z.jpg",
        'caption': "Ang Pulang Parte: A ∩ B",
        'updated_image': "https://imgur.com/daFrGjB.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang *intersection* ay binubuo ng mga *elements* parehong nasa A at B."
    },
    {
        'question': "Kung naalala mo ang <i>set difference</i> ang pulang parte ay nirepresenta nito. Balikan ang mga <i>sets</i> <b>A={p,i,n,o,y}</b> at <b>B={s,a,n,t,o,l}</b>, hanapin ang A - B.",
        'choices': ["{p, i}", "{n, o}", "{s, a}", "{p, i, y}"],
        'correct': ["{p, i, y}"],
        'image': "https://imgur.com/fDmKtjG.jpg",
        'caption': "Ang Pulang Parte: A - B",
        'updated_image': "https://imgur.com/vmu8uZ1.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang A - B ay mga *element* na nasa A pero wala sa B."
    },
    {
        'question': "Kung naalala mo ang <i>set difference</i> ang pulang parte ay nirepresenta nito. Balikan ang mga <i>sets</i> <b>A={p,i,n,o,y}</b> at <b>B={s,a,n,t,o,l}</b>, ngayon hanapin naman natin ang B - A.",
        'choices': ["{p, i, y}", "{n, o}", "{s, a, t, l}", "{t, l}"],
        'correct': ["{s, a, t, l}"],
        'image': "https://imgur.com/lYbE3Cc.jpg",
        'caption': "Ang Pulang Parte: B - A",
        'updated_image': "https://imgur.com/wVLSFia.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang B - A ay mga *element* na nasa B pero wala sa A."
    },
    {
        'question': "Kung <b>A={a,t,e}</b> at <b>B={k,u,y,a}</b>, kompletohin ang <i>Venn Diagram</i>. Hanapin muna ang A ∩ B.",
        'choices': ["{e}", "{t}", "{k}", "{a}"],
        'correct': ["{a}"],
        'image': "https://imgur.com/RgIyB1J.jpg",
        'caption': "Venn Diagram ng A at B",
        'how_to_solve': "Paliwanag: Ang *intersection* ay binubuo ng mga *elements* parehong nasa A at B."
    },
]
# Pool for random 8th question
quiz_pool = [
    {
        'question': "Hayaan nating tingnan ang <i>sets</i> <b>A={20,23,25,28}</b> at <b>B={23,24,28,73,100}</b>, anong <i>set</i> ang tinutukoy ng pulang parte?",
        'choices': ["{20, 23}", "{20, 25}", "{24, 73, 100}", "{20, 23, 25, 28}"],
        'correct': ["{20, 25}"],
        'image': "https://imgur.com/fhSfAqt.jpg",
        'caption': "Venn Diagram ng A at B",
        'how_to_solve': "Paliwanag: Ang A - B ay mga *element* na nasa A pero wala sa B."
    },
    {
        'question': "Hayaan nating tingnan ang <i>sets</i> <b>A={20,23,25,28}</b> at <b>B={23,24,28,73,100}</b>, anong <i>set</i> ang tinutukoy ng pulang parte?",
        'choices': ["{20, 23}", "{20, 25}", "{24, 73, 100}", "{20, 23, 25, 28}"],
        'correct': ["{24, 73, 100}"],
        'image': "https://imgur.com/GBAk4vB.jpg",
        'caption': "Venn Diagram ng A at B",
        'how_to_solve': "Paliwanag: Ang B - A ay mga *element* na nasa B pero wala sa A."
    },
]
# On app start, select random 8th question
if 'random_8th' not in st.session_state:
    st.session_state['random_8th'] = random.choice(quiz_pool)
# Final quiz_data: first 7 fixed + 1 random
quiz_data = quiz_fixed + [st.session_state['random_8th']]

if 'quiz_score' not in st.session_state:
    st.session_state['quiz_score'] = 0
if 'quiz_last_scored_step' not in st.session_state:
    st.session_state['quiz_last_scored_step'] = None

step = st.session_state['quiz_step']
total = len(quiz_data)

st.subheader(f"Tanong {step} ng {total}")
st.progress(step / total)


q = quiz_data[step-1]
st.image(q['image'], width=350, caption=q['caption'])
st.markdown(f"<div style='font-size:1.2em; font-weight:400; margin-bottom:12px'>{q['question']}</div>", unsafe_allow_html=True)
feedback_placeholder = st.empty()

if step == 7:
    # Three dropdowns for Intersection, A-B, B-A
    intersection_choices = ["{a}", "{e}", "{t}", "{k}"]
    ab_choices = ["{e}", "{t}", "{t,e}", "{a}"]
    ba_choices = ["{k}", "{k,u,y}", "{y,a}", "{a}"]
    # Session state for each dropdown's answer and retry
    for key in ['q7_intersection', 'q7_ab', 'q7_ba', 'q7_intersection_retry', 'q7_ab_retry', 'q7_ba_retry']:
        if key not in st.session_state:
            st.session_state[key] = 0 if 'retry' in key else None
    col1, col2, col3 = st.columns(3)
    with col1:
        intersection_answer = st.selectbox("Intersection (A ∩ B):", intersection_choices, index=None, key="q7_intersection_select", placeholder="Pumili ng sagot", disabled=st.session_state['q7_intersection'] == 'correct' or st.session_state['q7_intersection_retry'] >= 2)
        check1 = st.button("Check", key="check7_intersection", disabled=st.session_state['q7_intersection'] == 'correct' or st.session_state['q7_intersection_retry'] >= 2)
        if check1:
            if intersection_answer == "{a}":
                st.session_state['q7_intersection'] = 'correct'
                st.session_state['q7_intersection_retry'] = 0
                st.success("Tama! Intersection: {a}")
                # Award 1 point for this dropdown if not already scored
                if 'q7_intersection_scored' not in st.session_state:
                    st.session_state['q7_intersection_scored'] = False
                if not st.session_state['q7_intersection_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q7_intersection_scored'] = True
            else:
                st.session_state['q7_intersection_retry'] += 1
                if st.session_state['q7_intersection_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry7_intersection"):
                        st.experimental_rerun()
                elif st.session_state['q7_intersection_retry'] == 2:
                    st.error("Ang tamang sagot ay: {a}")
                    st.session_state['q7_intersection'] = 'done'
    with col2:
        ab_answer = st.selectbox("A - B:", ab_choices, index=None, key="q7_ab_select", placeholder="Pumili ng sagot", disabled=st.session_state['q7_ab'] == 'correct' or st.session_state['q7_ab_retry'] >= 2)
        check2 = st.button("Check", key="check7_ab", disabled=st.session_state['q7_ab'] == 'correct' or st.session_state['q7_ab_retry'] >= 2)
        if check2:
            if ab_answer == "{t,e}":
                st.session_state['q7_ab'] = 'correct'
                st.session_state['q7_ab_retry'] = 0
                st.success("Tama! A - B: {t,e}")
                # Award 1 point for this dropdown if not already scored
                if 'q7_ab_scored' not in st.session_state:
                    st.session_state['q7_ab_scored'] = False
                if not st.session_state['q7_ab_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q7_ab_scored'] = True
            else:
                st.session_state['q7_ab_retry'] += 1
                if st.session_state['q7_ab_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry7_ab"):
                        st.experimental_rerun()
                elif st.session_state['q7_ab_retry'] == 2:
                    st.error("Ang tamang sagot ay: {t,e}")
                    st.session_state['q7_ab'] = 'done'
    with col3:
        ba_answer = st.selectbox("B - A:", ba_choices, index=None, key="q7_ba_select", placeholder="Pumili ng sagot", disabled=st.session_state['q7_ba'] == 'correct' or st.session_state['q7_ba_retry'] >= 2)
        check3 = st.button("Check", key="check7_ba", disabled=st.session_state['q7_ba'] == 'correct' or st.session_state['q7_ba_retry'] >= 2)
        if check3:
            if ba_answer == "{k,u,y}":
                st.session_state['q7_ba'] = 'correct'
                st.session_state['q7_ba_retry'] = 0
                st.success("Tama! B - A: {k,u,y}")
                # Award 1 point for this dropdown if not already scored
                if 'q7_ba_scored' not in st.session_state:
                    st.session_state['q7_ba_scored'] = False
                if not st.session_state['q7_ba_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q7_ba_scored'] = True
            else:
                st.session_state['q7_ba_retry'] += 1
                if st.session_state['q7_ba_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry7_ba"):
                        st.experimental_rerun()
                elif st.session_state['q7_ba_retry'] == 2:
                    st.error("Ang tamang sagot ay: {k,u,y}")
                    st.session_state['q7_ba'] = 'done'
    # Show updated image and feedback if all answered (correct or out of tries)
    if all(st.session_state[k] in ['correct', 'done'] for k in ['q7_intersection', 'q7_ab', 'q7_ba']):
        st.balloons()
        feedback_placeholder.success("Tapos na! Intersection: {a}, A-B: {t,e}, B-A: {k,u,y}")
        feedback_placeholder.image("https://imgur.com/WPzU0vx.jpg", width=350, caption="Updated Venn Diagram")
else:
    # All other questions: normal single-choice dropdown
    selected = st.selectbox("Pumili ng sagot:", q['choices'], index=None, key=f"single{step}", placeholder="Pumili ng sagot")
    submit = st.button("Ipadala", key=f"submit{step}")
    if f'retry_{step}' not in st.session_state or st.session_state.get('retry_step', 0) != step:
        st.session_state[f'retry_{step}'] = 0
        st.session_state['retry_step'] = step
    if submit:
        if selected == q['correct'][0]:
            st.balloons()
            feedback_placeholder.success("Tama!")
            if 'updated_image' in q:
                feedback_placeholder.image(q['updated_image'], width=350, caption=q.get('updated_caption', 'Updated Venn Diagram'))
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

# Update score display to be out of 10
nav_col1, nav_col2 = st.columns([1, 1])
with nav_col1:
    st.button("Nakaraan", on_click=lambda: st.session_state.update({'quiz_step': max(1, step-1)}), disabled=(step == 1), key=f"prev{step}")
    st.markdown(f"<div style='text-align:center; margin-top:8px; font-size:1.1em; font-weight:bold;'>Puntos: {st.session_state['quiz_score']} / 10</div>", unsafe_allow_html=True)
with nav_col2:
    st.button("Susunod", on_click=lambda: st.session_state.update({'quiz_step': min(total, step+1)}), disabled=(step == total), key=f"next{step}")

# Final score report after last question
if step == total:
    # Check if last question is answered or retries run out
    last_done = False
    if step == 7:
        # Special handling for dropdowns in question 7
        if all(st.session_state.get(k) in ['correct', 'done'] for k in ['q7_intersection', 'q7_ab', 'q7_ba']):
            last_done = True
    else:
        # For normal questions, check if correct or retries run out
        if st.session_state.get(f'retry_{step}', 0) >= 2 or st.session_state.get('quiz_last_scored_step') == step:
            last_done = True
    if last_done:
        st.markdown("---")
        col_score, col_reset, col_btn = st.columns([2,1,2])
        with col_score:
            st.markdown(f"<div style='font-size:1.3em; font-weight:bold; color:#2E8B57;'>Final Score: {st.session_state['quiz_score']} / 10</div>", unsafe_allow_html=True)
            if st.session_state['quiz_score'] == 10:
                st.success("Perfect! 🎉")
           
        with col_reset:
            if st.button("Sagutan Muli", key="reset_quiz"):
                st.session_state.clear()
                
                
        with col_btn:
            st.markdown("<a href='https://morerationalph.streamlit.app/Venn_Diagram-Pangalawang_Antas' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)





