import streamlit as st  
import streamlit as st



col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col2:
    st.markdown("<div style='display: flex; align-items: center; height: 100%;'><div><h1 style='margin: 0; padding-left: 20px; line-height: 1;'>More Rational PH</h1><h3 style='margin: -10px 0 0 20px; padding: 0; line-height: 1;'>Para sa Pag-unlad</h3></div></div>", unsafe_allow_html=True)

st.write("---")
sidebar_css = """
<style>
[data-testid="stSidebar"] {
    background: #14532d !important;
}
[data-testid="stSidebar"] .css-1v3fvcr,
[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    color: #fff !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] span {
    color: #fff !important;
}
</style>
"""
st.markdown(sidebar_css, unsafe_allow_html=True)
st.markdown("<h2 style='font-size:27px'>Ang Malaking Tulong ng Pagkakaroon ng Rasyonal at Kritikal na Pag-iisip:</h2>", unsafe_allow_html=True)

st.markdown("<p style='font-size:19px'>Hindi ko intensyon na sabihin ito sa negatibong paraan, pero isang mahalagang obserbasyon na kung ikukumpara mo ang Pilipinas sa ibang progresibong bansa, ang mga Pilipinong mag-aaral ay halos huli sa academic performance.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ano ang gagawin? Sa kalagayan ng bansang Pilipinas ngayon, kailangan nating magkaroon ng makabago at talentadong mga Pilipinong mag-aaral. Ito ay masisimulan natin sa ating pag-iisip. Ang pagkakaroon ng rasyonal at kritikal na pag-iisip ay malaking impluwensiya sa halos lahat ng aspeto kung paano tayo mamuhay.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ang pagkakaroon ng negatibong pilosopiya ay maaaring magdulot ng malaking pinsala hindi lamang sa iyong sarili pati na rin sa iyong mga minamahal sa buhay o maging sa buong bansang Pilipinas.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ang rasyonalidad ay parang isang tagalinis ng isipan upang maalis at mapalitan ang mga idolohiyang nakakasama.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Para sa pag-unlad, inaanyayahan ko kayong magkaroon o hasain pa ang inyong magandang pag-iisip. Ang More Rational PH ay naghahandog ng mga pahinang maaaring pag-aralan upang makatulong sa iyong pag-iisip.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Para sa iyong pag-unlad!!!</p>", unsafe_allow_html=True)

st.markdown('''
<div style="width:100%; display:flex; align-items:center; justify-content:space-between;">
    <a href="https://more-rational-ph1-jqfq2eed47wdgf6c79n2as.streamlit.app/" style="display:flex;align-items:center;text-decoration:none;margin-top:24px;gap:10px;">
        <span style="font-size:28px;line-height:1;">𖠿</span>
        <span style="font-size:19px;color:#222;font-weight:bold;vertical-align:middle;text-align:left;">Home</span>
    </a>
    <a href="https://more-rational-ph1-jqfq2eed47wdgf6c79n2as.streamlit.app/Panuntunan" style="display:inline-block;margin-top:24px;padding:16px 32px;background:#222;border-radius:12px;color:white;font-size:19px;text-decoration:none;box-shadow:0 0 16px 4px #42a5f5, 0 2px 8px rgba(0,0,0,0.2);font-weight:bold;">Simulan ang Pag-aaral &#8594;</a>
</div>
''', unsafe_allow_html=True)
