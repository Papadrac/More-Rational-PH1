
import streamlit as st


QUESTION = {
    "statement": "Kapag umuulan, mababasa ang mga halaman sa labas.",
    "symbol": "p → q",
    "p": "umuuulan",
    "q": "mababasa ang mga halaman sa labas",
    "converse": "Kapag nababasa ang mga halaman sa labas, umuulan.",
    "inverse": "Kapag hindi umuulan, hindi mababasa ang mga halaman sa labas.",
    "contrapositive": "Kapag hindi nababasa ang mga halaman sa labas, hindi umuulan.",
}


CHOICES = [
    "Kapag umuulan, mababasa ang mga halaman sa labas.",
    "Kapag nababasa ang mga halaman sa labas, umuulan.",
    "Kapag hindi umuulan, hindi mababasa ang mga halaman sa labas.",
    "Kapag hindi nababasa ang mga halaman sa labas, hindi umuulan.",
]

ROWS = [
    {
        "label": "Converse",
        "symbol": "q → p",
        "answer": QUESTION["converse"],
        "key": "conditional_converse",
        "placeholder": "Piliin ang converse",
    },
    {
        "label": "Inverse",
        "symbol": "¬p → ¬q",
        "answer": QUESTION["inverse"],
        "key": "conditional_inverse",
        "placeholder": "Piliin ang inverse",
    },
    {
        "label": "Contrapositive",
        "symbol": "¬q → ¬p",
        "answer": QUESTION["contrapositive"],
        "key": "conditional_contrapositive",
        "placeholder": "Piliin ang contrapositive",
    },
]


col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Tutorial: Converse, Inverse, at Contrapositive")
    st.write(
        "Basahin ang conditional statement at tingnan ang tamang converse, inverse, at contrapositive sa talahanayan sa ibaba."
    )

st.write("--------")
st.subheader("Halimbawa:")
st.markdown(
    f"<div style='font-size:24px; margin-bottom:18px'><b>Conditional Statement:</b> {QUESTION['statement']}</div>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<div style='font-size:18px; margin-bottom:16px'><b>Symbol:</b> {QUESTION['symbol']}<br><b>p:</b> {QUESTION['p']}<br><b>q:</b> {QUESTION['q']}</div>",
    unsafe_allow_html=True,
)

header_cols = st.columns([1, 1.2, 4])
header_cols[0].markdown("**Logic Symbol**")
header_cols[1].markdown("**Uri**")
header_cols[2].markdown("**Sagot**")

for row in ROWS:
    col_symbol, col_label, col_answer = st.columns([1, 1.2, 4])
    col_symbol.markdown(f"<div style='padding-top:8px; font-size:20px; font-weight:bold'>{row['symbol']}</div>", unsafe_allow_html=True)
    col_label.markdown(f"<div style='padding-top:8px'>{row['label']}</div>", unsafe_allow_html=True)
    col_answer.markdown(
        f"<div style='padding-top:8px'>{row['answer']}</div>",
        unsafe_allow_html=True,
    )

st.write("--------")
st.subheader("Tanong 2")
st.write("Subukan natin kung naalala mo ang mga konsepto ng converse, inverse at contrapostive")
st.markdown(
    f"<div style='font-size:24px; margin-bottom:18px'><b>Conditional Statement:</b> {QUESTION['statement']}</div>",
    unsafe_allow_html=True,
)

practice_header_cols = st.columns([1, 1.2, 4])
practice_header_cols[0].markdown("**Logic Symbol**")
practice_header_cols[1].markdown("**Uri**")
practice_header_cols[2].markdown("**Sagot**")

practice_answers = {}
for row in ROWS:
    col_symbol, col_label, col_dropdown = st.columns([1, 1.2, 4])
    col_symbol.markdown(
        f"<div style='padding-top:8px; font-size:20px; font-weight:bold'>{row['symbol']}</div>",
        unsafe_allow_html=True,
    )
    col_label.markdown(
        f"<div style='padding-top:8px'>{row['label']}</div>",
        unsafe_allow_html=True,
    )
    practice_answers[row["label"]] = col_dropdown.selectbox(
        "",
        CHOICES,
        index=None,
        placeholder=row["placeholder"],
        key=f"practice_{row['key']}",
        label_visibility="collapsed",
    )

if st.button("I-check ang sagot sa Tanong 2"):
    if not all(practice_answers.values()):
        st.warning("Pumili muna ng sagot sa lahat ng tatlong dropdown.")
    else:
        score = 0
        for row in ROWS:
            selected_answer = practice_answers[row["label"]]
            if selected_answer == row["answer"]:
                score += 1
                st.success(f"Tama ang {row['label'].lower()}.")
            else:
                st.error(
                    f"Mali ang {row['label'].lower()}. Tamang sagot: {row['answer']}"
                )

        st.markdown(
            f"<div style='font-size:20px; font-weight:bold; margin-top:16px'>Iskor: {score} / 3</div>",
            unsafe_allow_html=True,
        )

        if score == 3:
            st.balloons()
