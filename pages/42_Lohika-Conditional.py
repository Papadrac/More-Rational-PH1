import random
import streamlit as st
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Lohika: Conditional Statement")
    st.write(
        "Given ang isang conditional statement, piliin kung alin ang tamang converse, inverse, o contrapositive gamit ang logical symbols."
    )
st.write("--------")
# --- Session state for quiz navigation ---
if 'quiz_step' not in st.session_state:
    st.session_state['quiz_step'] = 1

def next_question():
    st.session_state['quiz_step'] += 1

quiz_fixed = [
    {
        'question': "Given ang conditional statement na <b>Kapag umuulan, nababasa ang lupa.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> umuulan<br><b>q:</b> nababasa ang lupa<br><br>Ano ang <b>converse</b> o <b>q → p</b>?",
        'choices': [
            "Kapag nababasa ang lupa, umuulan.",
            "Kapag hindi umuulan, hindi nababasa ang lupa.",
            "Kapag hindi nababasa ang lupa, hindi umuulan.",
            "Kapag umuulan, nababasa ang lupa.",
        ],
        'correct': ["Kapag nababasa ang lupa, umuulan."],
        'how_to_solve': "Ang converse ay q → p. Pinagpapalit ang hypothesis at conclusion."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nag-aral ka, matataas ang marka mo.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nag-aral ka<br><b>q:</b> matataas ang marka mo<br><br>Ano ang <b>inverse</b> o <b>¬p → ¬q</b>?",
        'choices': [
            "Kapag hindi ka nag-aral, hindi matataas ang marka mo.",
            "Kapag matataas ang marka mo, nag-aral ka.",
            "Kapag hindi matataas ang marka mo, hindi ka nag-aral.",
            "Kapag nag-aral ka, matataas ang marka mo.",
        ],
        'correct': ["Kapag hindi ka nag-aral, hindi matataas ang marka mo."],
        'how_to_solve': "Ang inverse ay ¬p → ¬q. Nilalagyan ng negation ang p at q nang hindi pinagpapalit."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag may kuryente, umiikot ang bentilador.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> may kuryente<br><b>q:</b> umiikot ang bentilador<br><br>Ano ang <b>contrapositive</b> o <b>¬q → ¬p</b>?",
        'choices': [
            "Kapag hindi umiikot ang bentilador, walang kuryente.",
            "Kapag umiikot ang bentilador, may kuryente.",
            "Kapag walang kuryente, hindi umiikot ang bentilador.",
            "Kapag may kuryente, umiikot ang bentilador.",
        ],
        'correct': ["Kapag hindi umiikot ang bentilador, walang kuryente."],
        'how_to_solve': "Ang contrapositive ay ¬q → ¬p. Pinagpapalit ang p at q at parehong nilalagyan ng negation."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag maaga kang umalis, aabot ka sa klase.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> maaga kang umalis<br><b>q:</b> aabot ka sa klase<br><br>Ano ang <b>converse</b> o <b>q → p</b>?",
        'choices': [
            "Kapag aabot ka sa klase, maaga kang umalis.",
            "Kapag hindi ka maagang umalis, hindi ka aabot sa klase.",
            "Kapag hindi ka aabot sa klase, hindi ka maagang umalis.",
            "Kapag maaga kang umalis, aabot ka sa klase.",
        ],
        'correct': ["Kapag aabot ka sa klase, maaga kang umalis."],
        'how_to_solve': "Sa converse, ang q ang mauuna at susunod ang p."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nagtanim ka, may aanihin ka.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nagtanim ka<br><b>q:</b> may aanihin ka<br><br>Ano ang <b>inverse</b> o <b>¬p → ¬q</b>?",
        'choices': [
            "Kapag hindi ka nagtanim, wala kang aanihin.",
            "Kapag may aanihin ka, nagtanim ka.",
            "Kapag wala kang aanihin, hindi ka nagtanim.",
            "Kapag nagtanim ka, may aanihin ka.",
        ],
        'correct': ["Kapag hindi ka nagtanim, wala kang aanihin."],
        'how_to_solve': "Ang inverse ay hindi nagpapalit ng ayos. Nilalagyan lang ng negation ang p at q."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nagsuot ka ng uniporme, papapasukin ka.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nagsuot ka ng uniporme<br><b>q:</b> papapasukin ka<br><br>Ano ang <b>contrapositive</b> o <b>¬q → ¬p</b>?",
        'choices': [
            "Kapag hindi ka papapasukin, hindi ka nagsuot ng uniporme.",
            "Kapag papapasukin ka, nagsuot ka ng uniporme.",
            "Kapag hindi ka nagsuot ng uniporme, hindi ka papapasukin.",
            "Kapag nagsuot ka ng uniporme, papapasukin ka.",
        ],
        'correct': ["Kapag hindi ka papapasukin, hindi ka nagsuot ng uniporme."],
        'how_to_solve': "Ang contrapositive ay q at p na pinagpalit at kapwa nilagyan ng negation."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nagpraktis ang manlalaro, gagaling siya.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nagpraktis ang manlalaro<br><b>q:</b> gagaling siya<br><br>Ano ang <b>converse</b> o <b>q → p</b>?",
        'choices': [
            "Kapag gagaling siya, nagpraktis ang manlalaro.",
            "Kapag hindi nagpraktis ang manlalaro, hindi siya gagaling.",
            "Kapag hindi siya gagaling, hindi nagpraktis ang manlalaro.",
            "Kapag nagpraktis ang manlalaro, gagaling siya.",
        ],
        'correct': ["Kapag gagaling siya, nagpraktis ang manlalaro."],
        'how_to_solve': "Ang converse ay q → p, kaya pinagpapalit lang ang dalawang bahagi."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag may pista sa barangay, masaya ang mga tao.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> may pista sa barangay<br><b>q:</b> masaya ang mga tao<br><br>Ano ang <b>inverse</b> o <b>¬p → ¬q</b>?",
        'choices': [
            "Kapag walang pista sa barangay, hindi masaya ang mga tao.",
            "Kapag masaya ang mga tao, may pista sa barangay.",
            "Kapag hindi masaya ang mga tao, walang pista sa barangay.",
            "Kapag may pista sa barangay, masaya ang mga tao.",
        ],
        'correct': ["Kapag walang pista sa barangay, hindi masaya ang mga tao."],
        'how_to_solve': "Ang inverse ay ¬p → ¬q. Nilalagyan ng negation ang p at q nang hindi pinapalit ang ayos."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nagtutulungan ang magkakapitbahay, mabilis na naililipat ang bahay-kubo.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nagtutulungan ang magkakapitbahay<br><b>q:</b> mabilis na naililipat ang bahay-kubo<br><br>Ano ang <b>contrapositive</b> o <b>¬q → ¬p</b>?",
        'choices': [
            "Kapag hindi mabilis na naililipat ang bahay-kubo, hindi nagtutulungan ang magkakapitbahay.",
            "Kapag mabilis na naililipat ang bahay-kubo, nagtutulungan ang magkakapitbahay.",
            "Kapag hindi nagtutulungan ang magkakapitbahay, hindi mabilis na naililipat ang bahay-kubo.",
            "Kapag nagtutulungan ang magkakapitbahay, mabilis na naililipat ang bahay-kubo.",
        ],
        'correct': ["Kapag hindi mabilis na naililipat ang bahay-kubo, hindi nagtutulungan ang magkakapitbahay."],
        'how_to_solve': "Ang contrapositive ay ¬q → ¬p. Pinagpapalit ang p at q at nilalagyan ng negation ang pareho."
    },
    {
        'question': "Given ang conditional statement na <b>Kapag nagsisimbang Gabi ang pamilya, maaga silang nagigising.</b><br><br><b>Logical symbols:</b> p → q<br><b>p:</b> nagsisimbang Gabi ang pamilya<br><b>q:</b> maaga silang nagigising<br><br>Ano ang <b>converse</b> o <b>q → p</b>?",
        'choices': [
            "Kapag maaga silang nagigising, nagsisimbang Gabi ang pamilya.",
            "Kapag hindi nagsisimbang Gabi ang pamilya, hindi sila maagang nagigising.",
            "Kapag hindi sila maagang nagigising, hindi nagsisimbang Gabi ang pamilya.",
            "Kapag nagsisimbang Gabi ang pamilya, maaga silang nagigising.",
        ],
        'correct': ["Kapag maaga silang nagigising, nagsisimbang Gabi ang pamilya."],
        'how_to_solve': "Ang converse ay q → p, kaya ang conclusion ang inilalagay muna bago ang hypothesis."
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

shuffled_choices = q['choices'][:]
random.shuffle(shuffled_choices)

## st.image(q['image'], width=350, caption=q['caption'])
st.markdown(f"<div style='font-size:1.2em; font-weight:400; margin-bottom:12px'>{q['question']}</div>", unsafe_allow_html=True)
feedback_placeholder = st.empty()


# All questions: normal single-choice dropdown with freshly randomized options
selected = st.selectbox("Pumili ng sagot:", shuffled_choices, index=None, key=f"single{step}", placeholder="Pumili ng sagot")
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
            st.markdown("<a href='https://morerationalph.streamlit.app/' target='_blank'><button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer;'>Pumunta sa Sunod na Seksyon &#8594;</button></a>", unsafe_allow_html=True)
