import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("*Venn Diagram*: Pangalawang Antas")
    st.write("Para Makumpleto ang *Venn Diagram*, hanapin A ∩ B, A - B, B - A, at (A ∪ B)'. Pumili ng tamang sagot sa bawat tanong.")
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

# Fixed first 5 questions
quiz_fixed = [
    {
        'question': "Ngayon may <i>Universal set</i> tayo <b>U={a,b,e,k,m,t,u,y}</b>. Hayaan ang mga <i>sets</i> <b>A={a,t,e}</b> at <b>B={k,u,y,a}</b>, hanapin ang A ∩ B. Hanapin ang mga <i>elements</i> na parehong nasa A at B.",
        'choices': ["a", "b", "e", "k","m","t","u","y"],
        'correct': {"a"},
        'image': "https://imgur.com/6tF94PG.jpg",
        'caption': "Ang Berdeng Parte: A ∩ B",
        'updated_image': "https://imgur.com/O2VPhst.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang *intersection* ay binubuo ng mga *elements* parehong nasa A at B."
    },
    {
        'question': "Gamit parin ang <i>Universal set</i> <b>U={a,b,e,k,m,t,u,y}</b> at ang mga <i>sets</i> <b>A={a,t,e}</b> at <b>B={k,u,y,a}</b>, hanapin ang A - B. Hanapin ang mga <i>elements</i> na nasa A pero wala sa B.",
        'choices': ["a", "b", "e", "k","m","t","u","y"],
        'correct': {"t","e"},
        'image': "https://imgur.com/7I1Xeot.jpg",
        'caption': "Ang Berdeng Parte: A - B",
        'updated_image': "https://imgur.com/YZz2IQl.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang A - B ay mga *element* na nasa A pero wala sa B."
    },
    {
        'question': "Gamit parin ang <i>Universal set</i> <b>U={a,b,e,k,m,t,u,y}</b> at ang mga <i>sets</i> <b>A={a,t,e}</b> at <b>B={k,u,y,a}</b>, hanapin ang B - A. Hanapin ang mga <i>elements</i> na nasa B pero wala sa A.",
        'choices': ["a", "b", "e", "k","m","t","u","y"],
        'correct': {"k","u","y"},
        'image': "https://imgur.com/rcF58tk.jpg",
        'caption': "Ang Berdeng Parte: B - A",
        'updated_image': "https://imgur.com/64bZ5p0.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang B - A ay mga *element* na nasa B pero wala sa A."
    },
    {
        'question': "Gamit parin ang <i>Universal set</i> <b>U={a,b,e,k,m,t,u,y}</b> at ang mga <i>sets</i> <b>A={a,t,e}</b> at <b>B={k,u,y,a}</b>, hanapin ang (A ∪ B)'. Hanapin ang mga <i>elements</i> sa <i>Universal set</i> na hindi pa naililista.",
        'choices': ["a", "b", "e", "k","m","t","u","y"],
        'correct': {"b","m"},
        'image': "https://imgur.com/Q0Fyvad.jpg",
        'caption': "Ang Berdeng Parte: (A ∪ B)'",
        'updated_image': "https://imgur.com/hfjHjwz.jpg",
        'updated_caption': "Updated Venn Diagram",
        'how_to_solve': "Paliwanag: Ang (A ∪ B)' ay binubuo ng mga *elements* na wala sa A o B."
    },
    {
        'question': "Kung ang <i>Universal set</i> <b>U={1,2,3,4,5,6,7}</b> at ang mga <i>sets</i> <b>A={2,5,7}</b> at <b>B={2,3,4,7}</b>, kompletohin ang <i>Venn Diagram</i>. Hanapin muna ang A ∩ B.",
        'choices': ["1", "2", "3", "4", "5", "6", "7"],
        'correct': {"2","7"},
        'image': "https://imgur.com/Y04SE2a.jpg",
        'caption': "Venn Diagram ng A at B",
        'how_to_solve': "Paliwanag: Ang *intersection* ay binubuo ng mga *elements* parehong nasa A at B."
    },
]
# Pool for random 8th question
quiz_pool = [
     {
        'question': "Hayaan ang <i>Universal set</i> <b>U={3,7,8,9,13,15}</b> at ang mga <i>sets</i> <b>A={3,8,13}</b> at <b>B={8,9,15}</b>. Anong mga numero ang makikita mo sa berdeng bahagi ng Venn Diagram?",
        'choices': ["3", "7", "8", "9", "13", "15"],
        'correct': {"8"},
        'image': "https://imgur.com/0VSWWM1.jpg",
        'caption': "Hanapin ang mga numero sa berdeng bahagi",
        'updated_image': "https://imgur.com/bdUM9VX.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang berdeng bahagi ay ang *intersection* ng A at B. Hanapin ang mga numero na parehong nasa A at B."
    },
    {
        'question': "Hayaan ang <i>Universal set</i> <b>U={3,7,8,9,13,15}</b> at ang mga <i>sets</i> <b>A={3,8,13}</b> at <b>B={8,9,15}</b>. Anong mga numero ang makikita mo sa berdeng bahagi ng Venn Diagram?",
        'choices': ["3", "7", "8", "9", "13", "15"],
        'correct': {"7"},
        'image': "https://imgur.com/evi1hRl.jpg",
        'caption': "Hanapin ang mga numero sa berdeng bahagi",
        'updated_image': "https://imgur.com/bdUM9VX.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay ang (A ∪ B)'. Hanapin ang mga numero na wala sa A o B."
    },
    {
        'question': "May mga hayop na pweding ilarawan bilang isang <i>Universal set</i> <b>U={aso, pusa, kambing, kalabaw, manok}</b>. Kung ang <i>set</i> <b>A={aso, manok, kambing}</b> at <b>B={aso, pusa, kambing}</b>, hanapin ang mga hayop na tinutukoy ng berdeng parte.",
        'choices': ["aso", "pusa", "kambing", "kalabaw", "manok"],
        'correct': {"manok"},
        'image': "https://imgur.com/lWc5Z9U.jpg",
        'caption': "Hanapin ang mga hayop sa berdeng bahagi",
        'updated_image': "https://imgur.com/PBzT9Xb.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay A - B. Hanapin ang mga hayop na nasa A pero wala sa B."
    },
    {
        'question': "May mga hayop na pweding ilarawan bilang isang <i>Universal set</i> <b>U={aso, pusa, kambing, kalabaw, manok}</b>. Kung ang <i>set</i> <b>A={aso, manok, kambing}</b> at <b>B={aso, pusa, kambing}</b>, hanapin ang mga hayop na tinutukoy ng berdeng parte.",
        'choices': ["aso", "pusa", "kambing", "kalabaw", "manok"],
        'correct': {"pusa"},
        'image': "https://imgur.com/HbzCX9E.jpg",
        'caption': "Hanapin ang mga hayop sa berdeng bahagi",
        'updated_image': "https://imgur.com/PBzT9Xb.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay B - A. Hanapin ang mga hayop na nasa B pero wala sa A."
    },
    {
        'question': "May mga hayop na pweding ilarawan bilang isang <i>Universal set</i> <b>U={aso, pusa, kambing, kalabaw, manok}</b>. Kung ang <i>set</i> <b>A={aso, manok, kambing}</b> at <b>B={aso, pusa, kambing}</b>, hanapin ang mga hayop na tinutukoy ng berdeng parte.",
        'choices': ["aso", "pusa", "kambing", "kalabaw", "manok"],
        'correct': {"kalabaw"},
        'image': "https://imgur.com/evi1hRl.jpg",
        'caption': "Hanapin ang mga hayop sa berdeng bahagi",
        'updated_image': "https://imgur.com/PBzT9Xb.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay (A ∪ B)'. Hanapin ang mga hayop na wala sa A o B."
    },
    {
        'question': "May isang pamilya na pweding ilarawan bilang isang <i>Universal set</i> <b>U={mama, papa, kuya, ate, bunso}</b>. Kung ang <i>set</i> <b>A={mama, kuya, bunso}</b> at <b>B={papa, bunso}</b>, hanapin ang mga miyembro ng pamilya na tinutukoy ng berdeng parte.",
        'choices': ["mama", "papa", "kuya", "ate", "bunso"],
        'correct': {"mama", "ate"},
        'image': "https://imgur.com/lWc5Z9U.jpg",
        'caption': "Hanapin ang mga miyembro ng pamilya sa berdeng bahagi",
        'updated_image': "https://imgur.com/0JDb8ZO.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay A - B. Hanapin ang mga miyembro ng pamilya na nasa A pero wala sa B."
    },
    {
        'question': "May isang pamilya na pweding ilarawan bilang isang <i>Universal set</i> <b>U={mama, papa, kuya, ate, bunso}</b>. Kung ang <i>set</i> <b>A={mama, kuya, bunso}</b> at <b>B={papa, bunso}</b>, hanapin ang mga miyembro ng pamilya na tinutukoy ng berdeng parte.",
        'choices': ["mama", "papa", "kuya", "ate", "bunso"],
        'correct': {"papa"},
        'image': "https://imgur.com/HbzCX9E.jpg",
        'caption': "Hanapin ang mga miyembro ng pamilya sa berdeng bahagi",
        'updated_image': "https://imgur.com/0JDb8ZO.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay B - A. Hanapin ang mga miyembro ng pamilya na nasa B pero wala sa A."
    },
    {
        'question': "May isang pamilya na pweding ilarawan bilang isang <i>Universal set</i> <b>U={mama, papa, kuya, ate, bunso}</b>. Kung ang <i>set</i> <b>A={mama, kuya, bunso}</b> at <b>B={papa, bunso}</b>, hanapin ang mga miyembro ng pamilya na tinutukoy ng berdeng parte.",
        'choices': ["mama", "papa", "kuya", "ate", "bunso"],
        'correct': {"kuya"},
        'image': "https://imgur.com/evi1hRl.jpg",
        'caption': "Hanapin ang mga miyembro ng pamilya sa berdeng bahagi",
        'updated_image': "https://imgur.com/0JDb8ZO.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay (A ∪ B)'. Hanapin ang mga miyembro ng pamilya na wala sa A o B."
    },
    {
        'question': "May isang pamilya na pweding ilarawan bilang isang <i>Universal set</i> <b>U={mama, papa, kuya, ate, bunso}</b>. Kung ang <i>set</i> <b>A={mama, kuya, bunso}</b> at <b>B={papa, bunso}</b>, hanapin ang mga miyembro ng pamilya na tinutukoy ng berdeng parte.",
        'choices': ["mama", "papa", "kuya", "ate", "bunso"],
        'correct': {"bunso"},
        'image': "https://imgur.com/0VSWWM1.jpg",
        'caption': "Hanapin ang mga miyembro ng pamilya sa berdeng bahagi",
        'updated_image': "https://imgur.com/0JDb8ZO.jpg",
        'updated_caption': "Kompletong Venn Diagram",
        'how_to_solve': "Paliwanag: Ang Berdeng bahagi ay A ∩ B. Hanapin ang mga miyembro ng pamilya na nasa parehong A at B."
    },
]

# On app start, select random last 3 questions
if 'random_last3' not in st.session_state or len(st.session_state['random_last3']) != 3:
    st.session_state['random_last3'] = random.sample(quiz_pool, 3)
# Final quiz_data: first 5 fixed + 3 random
quiz_data = quiz_fixed + st.session_state['random_last3']

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

if step == 5:
    # Four dropdowns for Intersection, A-B, B-A, (A ∪ B)'
    for key in ['q5_intersection', 'q5_ab', 'q5_ba', 'q5_comp', 'q5_intersection_retry', 'q5_ab_retry', 'q5_ba_retry', 'q5_comp_retry']:
        if key not in st.session_state:
            st.session_state[key] = 0 if 'retry' in key else None
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        intersection_answer = st.multiselect("Intersection (A ∩ B):", ["1", "2", "3", "4", "5", "6", "7"], key="q5_intersection_select", disabled=st.session_state['q5_intersection'] == 'correct' or st.session_state['q5_intersection_retry'] >= 2)
        check1 = st.button("Check", key="check5_intersection", disabled=st.session_state['q5_intersection'] == 'correct' or st.session_state['q5_intersection_retry'] >= 2)
        if check1:
            if set(intersection_answer) == {"2","7"}:
                st.session_state['q5_intersection'] = 'correct'
                st.session_state['q5_intersection_retry'] = 0
                st.success("Tama! Intersection: {2,7}")
                if 'q5_intersection_scored' not in st.session_state:
                    st.session_state['q5_intersection_scored'] = False
                if not st.session_state['q5_intersection_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q5_intersection_scored'] = True
            else:
                st.session_state['q5_intersection_retry'] += 1
                if st.session_state['q5_intersection_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry5_intersection"):
                        st.experimental_rerun()
                elif st.session_state['q5_intersection_retry'] == 2:
                    st.error("Ang tamang sagot ay: {2,7}")
                    st.session_state['q5_intersection'] = 'done'
    with col2:
        ab_answer = st.multiselect("A - B:", ["1", "2", "3", "4", "5", "6", "7"], key="q5_ab_select", disabled=st.session_state['q5_ab'] == 'correct' or st.session_state['q5_ab_retry'] >= 2)
        check2 = st.button("Check", key="check5_ab", disabled=st.session_state['q5_ab'] == 'correct' or st.session_state['q5_ab_retry'] >= 2)
        if check2:
            if set(ab_answer) == { "5"}:  # A-B is A minus the intersection
                st.session_state['q5_ab'] = 'correct'
                st.session_state['q5_ab_retry'] = 0
                st.success("Tama! A - B: {5}")
                if 'q5_ab_scored' not in st.session_state:
                    st.session_state['q5_ab_scored'] = False
                if not st.session_state['q5_ab_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q5_ab_scored'] = True
            else:
                st.session_state['q5_ab_retry'] += 1
                if st.session_state['q5_ab_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry5_ab"):
                        st.experimental_rerun()
                elif st.session_state['q5_ab_retry'] == 2:
                    st.error("Ang tamang sagot ay: {5}")
                    st.session_state['q5_ab'] = 'done'
    with col3:
        ba_answer = st.multiselect("B - A:", ["1", "2", "3", "4", "5", "6", "7"], key="q5_ba_select", disabled=st.session_state['q5_ba'] == 'correct' or st.session_state['q5_ba_retry'] >= 2)
        check3 = st.button("Check", key="check5_ba", disabled=st.session_state['q5_ba'] == 'correct' or st.session_state['q5_ba_retry'] >= 2)
        if check3:
            if set(ba_answer) == {"3", "4"}:
                st.session_state['q5_ba'] = 'correct'
                st.session_state['q5_ba_retry'] = 0
                st.success("Tama! B - A: {3,4}")
                if 'q5_ba_scored' not in st.session_state:
                    st.session_state['q5_ba_scored'] = False
                if not st.session_state['q5_ba_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q5_ba_scored'] = True
            else:
                st.session_state['q5_ba_retry'] += 1
                if st.session_state['q5_ba_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry5_ba"):
                        st.experimental_rerun()
                elif st.session_state['q5_ba_retry'] == 2:
                    st.error("Ang tamang sagot ay: {3,4}")
                    st.session_state['q5_ba'] = 'done'
    with col4:
        comp_answer = st.multiselect("(A ∪ B)':", ["1", "2", "3", "4", "5", "6", "7"], key="q5_comp_select", disabled=st.session_state['q5_comp'] == 'correct' or st.session_state['q5_comp_retry'] >= 2)
        check4 = st.button("Check", key="check5_comp", disabled=st.session_state['q5_comp'] == 'correct' or st.session_state['q5_comp_retry'] >= 2)
        if check4:
            if set(comp_answer) == {"1", "6"}:
                st.session_state['q5_comp'] = 'correct'
                st.session_state['q5_comp_retry'] = 0
                st.success("Tama! (A ∪ B)': {1,6}")
                if 'q5_comp_scored' not in st.session_state:
                    st.session_state['q5_comp_scored'] = False
                if not st.session_state['q5_comp_scored']:
                    st.session_state['quiz_score'] += 1
                    st.session_state['q5_comp_scored'] = True
            else:
                st.session_state['q5_comp_retry'] += 1
                if st.session_state['q5_comp_retry'] == 1:
                    st.error("Mali. Subukan muli! (1 natitirang subok)")
                    if st.button("Subukan Muli", key="retry5_comp"):
                        st.experimental_rerun()
                elif st.session_state['q5_comp_retry'] == 2:
                    st.error("Ang tamang sagot ay: {1,6}")
                    st.session_state['q5_comp'] = 'done'
    # Show updated image and feedback if all answered (correct or out of tries)
    if all(st.session_state[k] in ['correct', 'done'] for k in ['q5_intersection', 'q5_ab', 'q5_ba', 'q5_comp']):
        st.balloons()
        feedback_placeholder.success("Tapos na! Intersection: {2,7}, A-B: {5}, B-A: {3,4}, (A ∪ B)': {1,6}")
        feedback_placeholder.image("https://imgur.com/30zxG96.jpg", width=350, caption="Updated Venn Diagram")
else:
    # All other questions: multiselect instead of single-choice dropdown
    selected = st.multiselect("Piliin lahat ng tamang sagot:", q['choices'], key=f"multi{step}")
    submit = st.button("Ipadala", key=f"submit{step}")
    if f'retry_{step}' not in st.session_state or st.session_state.get('retry_step', 0) != step:
        st.session_state[f'retry_{step}'] = 0
        st.session_state['retry_step'] = step
    if submit:
        correct_set = set(q['correct'])
        selected_set = set(selected)
        if selected_set == correct_set:
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

nav_col1, nav_col2 = st.columns([1, 1])
with nav_col1:
    st.button("Nakaraan", on_click=lambda: st.session_state.update({'quiz_step': max(1, step-1)}), disabled=(step == 1), key=f"prev{step}")
    st.markdown(f"<div style='text-align:center; margin-top:8px; font-size:1.1em; font-weight:bold;'>Puntos: {st.session_state['quiz_score']} / 11</div>", unsafe_allow_html=True)
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
            st.markdown(f"<div style='font-size:1.3em; font-weight:bold; color:#2E8B57;'>Final Score: {st.session_state['quiz_score']} / 11</div>", unsafe_allow_html=True)
            if st.session_state['quiz_score'] == 11:
                st.success("Perfect! 🎉")
       
        with col_reset:
            if st.button("Sagutan Muli", key="reset_quiz"):
                st.session_state.clear()
                
                
        with col_btn:
            st.markdown("<a href='https://morerationalph.streamlit.app/' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
