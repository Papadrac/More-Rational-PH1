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
        'question': "Isang komite para sa pista ng barangay ay bubuuin ng 5 katao mula sa 7 tatay at 6 nanay. Ilang paraan puwedeng mabuo ang komite kung dapat ay may 3 nanay?",
        'choices': ["3003", "2002", "240", "420", "924"],
        'correct': ["420"],
        'how_to_solve': "Bilangin ang lahat ng posibleng komite na may 3 nanay (2 tatay): C(6,3)*C(7,2) = 20*21 = 420."
    },
    {
        'question': "Ilang 5-digit na numero ng plaka ng tricycle ang maaaring mabuo gamit ang mga digit na 1,2,3,4,5,6,7 kung walang digit na mauulit at ang huling digit ay dapat even?",
        'choices': ["1080", "1440", "2160", "2520", "2880"],
        'correct': ["1080"],
        'how_to_solve': "Ang huling digit ay dapat even (2,4,6). Para sa bawat isa, pumili ng 4 pang digit mula sa natitira, tapos ayusin. 3 pagpipilian para sa huli × P(6,4) = 3×360=1080."
    },
    {
        'question': "Ilang paraan puwedeng ayusin ang mga letra ng salitang 'PANSIT' kung ang mga patinig ay laging magkasama?",
        'choices': ["720", "240", "2880", "4320", "5040"],
        'correct': ["240"],
        'how_to_solve': "Ituring ang mga patinig (A, I) bilang isang bloke. Kaya 5 na bloke ang aayusin: 5! = 120. Ang patinig ay pwedeng ayusin sa 2! = 2 paraan. Kabuuan: 120×2=240. (Kung may inuulit na letra, hatiin sa bilang ng pag-uulit.)"
    },
    {
        'question': "Ang isang youth club sa barangay ay may 8 kabataan. Ilang paraan puwedeng pumili ng pangulo, bise, at kalihim kung sina Ana at Jose ay hindi puwedeng magsama bilang opisyal?",
        'choices': ["336", "288", "240", "192", "300"],
        'correct': ["300"],
        'how_to_solve': "Kabuuang paraan nang walang restriction: P(8,3)=336. Ibawas ang kaso na magkasama si Ana at Jose bilang opisyal: pumili ng posisyon para kay Ana at Jose (3×2=6), pumili ng isa pa mula sa 6 na natira: P(3,2)×6=3x2x6=36. Kaya, 336-36=300."
    }
    # IB AA HL-style combinatorics and permutation problems
    ,{
        'question': "May 6 na opisyal ng barangay na uupo sa isang mesang parihaba. Ilang paraan puwedeng paupuin sila kung hindi puwedeng magkatabi ang Kapitan at ang Ingat-Yaman?",
        'choices': ["480", "4800", "1440", "720", "3600"],
        'correct': ["480"],
        'how_to_solve': "Ayusin muna lahat: 6! = 720. Bilang ng arrangement na magkatabi si Kapitan at Ingat-Yaman: 5! × 2 = 240 (5! para sa natitirang opisyal, ×2 para sa posisyon ng Kapitan at Ingat-Yaman). Sagot: 720 - 240 = 480."
    },
    {
        'question': "May 8 na guro. Ilang paraan puwedeng pumili ng 4 na miyembro ng komite kung hindi puwedeng magsama si Ma'am Cruz at Sir Reyes?",
        'choices': ["65", "70", "56", "55", "50"],
        'correct': ["55"],
        'how_to_solve': "Total: C(8,4)=70. Cases na magkasama si Cruz at Reyes: C(6,2)=15. Sagot: 70-15=55."
    },
    {
        'question': "May 5 na subject at 5 na guro. Ilang paraan puwedeng i-assign ang bawat subject sa guro kung si Ma'am Santos ay hindi puwedeng magturo ng Math?",
        'choices': ["24", "120", "96", "48", "100"],
        'correct': ["96"],
        'how_to_solve': "Total: 5! = 120. Cases na si Santos ay Math: 4! = 24. Sagot: 120-24=96."
    },
    {
        'question': "Ilang 4-digit na password ang maaaring mabuo mula 1-6 kung ang nabuong numero ay dapat odd, puwedeng ulitin ang mga digits?",
        'choices': ["360", "648", "120", "96", "256"],
        'correct': ["648"],
        'how_to_solve': "Dapat odd ang huling digit (1,3,5). Ang bawat isa sa unang 3 digit ay pwedeng 1-6 (6 choices). Kaya, 6×6×6×3=648."
    },
    {
        'question': "May 10 kabataan (5 lalaki, 5 babae). Ilang paraan pwedeng pumili ng 3 na kasali sa paligsahan kung dapat ay may hindi bababa sa 1 babae?",
        'choices': ["110", "120", "80", "90", "60"],
        'correct': ["110"],
        'how_to_solve': "Total: C(10,3)=120. All boys: C(5,3)=10. Sagot: 120-10=110."
    },
    {
        'question': "May 7 na estudyante. Ilang paraan pwedeng pumili ng grupo na 4 na miyembro at isang pinuno mula sa grupo?",
        'choices': ["840", "210", "35", "140", "420"],
        'correct': ["140"],
        'how_to_solve': "Pumili ng 4: C(7,4)=35. Pumili ng pinuno sa 4: 4. Sagot: 35×4=140."
    }
]



# Only first question is fixed, the rest are random (3 random)
quiz_fixed_question = quiz_fixed[:1]
quiz_pool = quiz_fixed[1:]
if 'random_3' not in st.session_state:
    st.session_state['random_3'] = random.sample(quiz_pool, k=3) if len(quiz_pool) >= 3 else random.choices(quiz_pool, k=3)
quiz_data = quiz_fixed_question + st.session_state['random_3']

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



# Update score display to be out of 4
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
