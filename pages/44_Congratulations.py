import streamlit as st

col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Pagbati!")

st.write("--------")
st.markdown(
    """
    <div style='text-align:center; padding:40px 16px;'>
        <h2>Salamat sa pagtapos ng mga kurso!</h2>
        <p style='font-size:22px; font-weight:700; color:#0d47a1;'>
            Ikaw ay isang ganap na na rasyonalista.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
