import streamlit as st

col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Venn Diagram: Tapos Na")

st.write("--------")

st.markdown(
    """
    <div style='text-align:center; padding:24px 12px;'>
        <h2>Natapos mo ang Venn Diagram.</h2>
        <p style='font-size:20px; font-weight:600;'>Pumunta sa Counting and Combinatorics.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='text-align:center; margin-top:8px;'><a href='https://morerationalph.streamlit.app/Counting-Unang_Antas' target='_self'><button style='font-size:16px;padding:10px 18px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Counting and Combinatorics →</button></a></div>",
    unsafe_allow_html=True,
)
