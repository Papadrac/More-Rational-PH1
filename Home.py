
import streamlit as st
import streamlit.components.v1 as components

import streamlit as st
import base64
from pathlib import Path



# --- Set new background image from Imgur with light overlay ---
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://imgur.com/VQVT9bo.jpg');
    background-size: cover;
    background-position: center;
    position: relative;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.8); /* 80% white overlay */
    z-index: 0;
    pointer-events: none;
}}
[data-testid="stHeader"] {{
    background-color: #FFFFFF;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_page_config(
    page_title="More Rational PH",
    initial_sidebar_state="expanded",
    layout="wide"
)


# --- Background and Style ---
st.markdown("""
<style>
[data-testid="stSidebar"] {
  background: #0d2346 !important;
}
[data-testid="stSidebar"] * {
  color: #fff !important;
}
[data-testid="stHeader"] {
  background: rgba(255,255,255,0.7);
}
/* Make main content wide */
[data-testid="stAppViewContainer"] {
  max-width: 100vw !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
}
[data-testid="stBlockContainer"] {
  max-width: 1800px !important;
  width: 100% !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-left: 24px !important;
  padding-right: 24px !important;
}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div style="
  text-align:center;
  margin-top:0;
  padding: 10vw 0 10vw 0;
  max-width:100vw;
  width:100vw;
  margin-left:calc(-50vw + 50%);
  margin-right:calc(-50vw + 50%);
  background-image: url('https://imgur.com/RKcrFnj.jpg');
  background-size: cover;
  background-position: center;
  border-radius: 0 0 48px 48px;
  box-shadow: 0 8px 32px 0 rgba(13,35,70,0.15);
">
  <h1 style='font-size:8vw; font-weight:bold; color:#0d2346; text-shadow:2px 2px 8px #e0e0e0;'>
    More Rational PH
  </h1>
  <br>
  <a href="https://morerationalph.streamlit.app/Panuntunan" style='display:inline-block; margin-top:2em; background:#ffd700; color:#0d2346; font-size:1.5vw; font-weight:bold; padding:24px 64px; border-radius:20px; text-decoration:none; box-shadow:0 6px 24px 0 rgba(200,200,200,0.30);'>
    Pagandahin ang Iyong Pag-iisip
  </a>
</div>
""", unsafe_allow_html=True)

# --- BENEFITS SECTION ---
st.markdown("""
<div style='display:flex; flex-wrap:wrap; justify-content:center; gap:32px; margin-top:3em;'>
  <a href="https://morerationalph.streamlit.app/About_Us" style='text-decoration:none;'>
    <div style='background:#fffbe7; border-radius:18px; padding:32px 24px; min-width:260px; max-width:320px; box-shadow:0 2px 16px rgba(13,35,70,0.10); transition: box-shadow 0.2s; cursor:pointer;'>
      <img src='https://img.icons8.com/ios-filled/100/1976d2/user-group-man-man.png' width='60' style='margin-bottom:12px;'/>
      <h3 style='color:#1976d2;'>About Us</h3>
      <p style='color:#222;'>Tingnan kung ano ang layunin ng grupo.</p>
    </div>
  </a>
  <a href="https://morerationalph.streamlit.app/Bakit_Rationality" style='text-decoration:none;'>
    <div style='background:#fffbe7; border-radius:18px; padding:32px 24px; min-width:260px; max-width:320px; box-shadow:0 2px 16px rgba(13,35,70,0.10); transition: box-shadow 0.2s; cursor:pointer;'>
      <img src='https://img.icons8.com/ios-filled/100/1976d2/brain.png' width='60' style='margin-bottom:12px;'/>
      <h3 style='color:#1976d2;'>Bakit Rationality</h3>
      <p style='color:#222;'>Gaano kahalaga ang pagiging rasyonal sa ating pang-araw-araw na buhay?</p>
    </div>
  </a>
  <a href="https://morerationalph.streamlit.app/Panuntunan" style='text-decoration:none;'>
    <div style='background:#fffbe7; border-radius:18px; padding:32px 24px; min-width:260px; max-width:320px; box-shadow:0 2px 16px rgba(13,35,70,0.10); transition: box-shadow 0.2s; cursor:pointer;'>
      <img src='https://img.icons8.com/ios-filled/100/1976d2/light-on.png' width='60' style='margin-bottom:12px;'/>
      <h3 style='color:#1976d2;'>Improve Your Thinking</h3>
      <p style='color:#222;'>Pagandahin ang iyong pag-iisip.</p>
    </div>
  </a>
</div>
""", unsafe_allow_html=True)

# --- YOUTUBE VIDEO (MAXIMUM WIDTH, CENTERED) ---
st.markdown("""
<div style='width:100vw; max-width:100vw; position:relative; left:50%; transform:translateX(-50%); margin:3em 0 2em 0; padding:0; overflow-x:hidden;'>
  <div style='position:relative; padding-bottom:56.25%; height:0; overflow:hidden; width:100vw; max-width:100vw; background:#000; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.10);'>
    <iframe src="https://www.youtube.com/embed/ONzfroQlVmY?start=1" frameborder="0" allowfullscreen style='position:absolute; top:0; left:0; width:100vw; max-width:100vw; height:100%; border-radius:18px;'></iframe>
  </div>
</div>
""", unsafe_allow_html=True)

# --- TESTIMONIALS ---
st.markdown("""
<div style='text-align:center; margin:2em 0;'>
  <h2 style='color:#1976d2;'>ANO ANG SABI NG MGA ESTUDYANTE?</h2>
  <blockquote style='font-size:1.1vw; color:#333; background:#f5f5f5; border-left:6px solid #1976d2; margin:2em auto; padding:1.5em 2em; max-width:700px;'>
    "Dahil sa kursong ito, mas naunawaan ko ang mga ideya sa matematika at lohika dahil dito napaganda ang aking pag-iisip."<br><br>
    <span style='font-weight:bold;'>– Bryan, Estudyante</span>
  </blockquote>
</div>
""", unsafe_allow_html=True)

# --- COURSE DESCRIPTION ---
st.markdown("""
<div style='margin:2em 0 2em 10em;'>
  <h2 style='color:#0d2346; margin-bottom:2em;'>ANO ANG MATUTUTUNAN MO?</h2>
  <div style='display:flex; flex-wrap:wrap; gap:48px; justify-content:flex-start;'>
    <!-- Set Theory Course -->
    <a href="https://morerationalph.streamlit.app/Set_Theory-Panimula" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/ZJd7di6.png' alt='Set Theory' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Set Theory</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang set? Bakit ito mahalaga?</li>
          <li><b>Uri ng Set:</b> Finite, Infinite, Null, Universal, Subset</li>
          <li><b>Operations:</b> Union, Intersection, Difference, Complement</li>
          <li><b>Notation:</b> Roster, Rule Method</li>
          <li><b>Word Problems:</b> Pagsasanay at aplikasyon</li>
        </ul>
      </div>
    </a>
    <!-- Venn Diagram Course -->
    <a href="https://morerationalph.streamlit.app/Venn_Diagram-Unang_Antas" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/ov17u4z.png' alt='Venn Diagram' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Venn Diagram</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang Venn Diagram? Paano ito ginagamit?</li>
          <li><b>Pagbuo ng Venn Diagram:</b> Dalawa o higit pang sets</li>
          <li><b>Paglutas ng Problema:</b> Word problems gamit ang Venn Diagram</li>
          <li><b>Interpretasyon:</b> Pag-unawa sa mga bahagi ng diagram</li>
          <li><b>Hamon na Tanong:</b> Mas malalim na pagsasanay</li>
        </ul>
      </div>
    </a>
    <!-- Counting and Combinatorics Course -->
    <a href="https://morerationalph.streamlit.app/" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/4AtDRsO.png' alt='Counting and Combinatorics' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Counting and Combinatorics</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang counting at combinatorics? Bakit ito mahalaga?</li>
          <li><b>Mga Pangunahing Konsepto:</b> Permutation, Combination, Fundamental Principle of Counting</li>
          <li><b>Paglutas ng Problema:</b> Word problems gamit ang counting at combinatorics</li>
          <li><b>Applications:</b> Paggamit sa totoong buhay</li>
          <li><b>Hamon na Tanong:</b> Mas malalim na pagsasanay</li>
        </ul>
      </div>
    </a>
    <!-- Probability Course -->
    <a href="https://morerationalph.streamlit.app/" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/uCnGeIV.png' alt='Probability' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Probability</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang probability? Bakit ito mahalaga?</li>
          <li><b>Mga Pangunahing Konsepto:</b> Experiment, Outcome, Sample Space, Event</li>
          <li><b>Uri ng Probability:</b> Theoretical, Experimental</li>
          <li><b>Pagkwenta ng Probability:</b> Formula at halimbawa</li>
          <li><b>Word Problems:</b> Pagsasanay at aplikasyon</li>
        </ul>
      </div>
    </a>
    <!-- Number Theory Course -->
    <a href="https://morerationalph.streamlit.app/" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/CgUw6qt.png' alt='Number Theory' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Number Theory</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang number theory? Bakit ito mahalaga?</li>
          <li><b>Mga Pangunahing Konsepto:</b> Prime numbers, Divisibility, GCD, LCM</li>
          <li><b>Paglutas ng Problema:</b> Word problems gamit ang number theory</li>
          <li><b>Applications:</b> Paggamit sa totoong buhay</li>
          <li><b>Hamon na Tanong:</b> Mas malalim na pagsasanay</li>
        </ul>
      </div>
    </a>
    <!-- Lohika Course -->
    <a href="https://morerationalph.streamlit.app/" style="text-decoration:none; flex:1; min-width:320px; max-width:400px;">
      <div style='background:#0d2346; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.18); padding:32px 24px; height:100%; transition:box-shadow 0.2s; cursor:pointer;'>
        <img src='https://imgur.com/fmNqgwL.png' alt='Lohika' style='width:100%; max-width:220px; display:block; margin:auto; margin-bottom:18px; border-radius:12px; box-shadow:0 2px 8px rgba(13,35,70,0.20);'/>
        <h3 style='color:#fff; text-align:center;'>Lohika</h3>
        <ul style='font-size:1.1vw; color:#e3eaf7; margin-top:1em;'>
          <li><b>Panimula:</b> Ano ang lohika? Bakit ito mahalaga?</li>
          <li><b>Mga Pangunahing Konsepto:</b> Propositions, Logical Connectives, Truth Tables</li>
          <li><b>Paglutas ng Problema:</b> Word problems gamit ang lohika</li>
          <li><b>Applications:</b> Paggamit sa pang-araw-araw na buhay</li>
          <li><b>Hamon na Tanong:</b> Mas malalim na pagsasanay</li>
        </ul>
      </div>
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# --- WHAT YOU GET ---
st.markdown("""
<div style='margin:2em 0 2em 10em;'>
  <h2 style='color:#1976d2;'>LAHAT NG ITO AY MAKUKUHA MO:</h2>
  <ul style='font-size:1.1vw; color:#222; max-width:800px; margin:auto;'>
    <li>Mga leksyon sa Filipino para madaling maintindihan ang mga konsepto</li>
    <li>Libreng mga pahina na magpapaganda ng iyong isipan</li>
    <li>Benepisyo ng pagkakaroon ng lohikal na pag-iisip</li>
    <li>Direktang suporta mula sa komunidad</li>
    <li>Mga pahina na pwedi mong balikan kahit kailan</li>
    <li>Komunidad ng mga mag-aaral at mga rasyonalista gaya mo</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# --- ABOUT THE INSTRUCTOR ---
st.markdown("""
<div style='margin:2em 0 2em 10em; display:flex; align-items:center; gap:32px; max-width:800px;'>
  <img src='https://imgur.com/DwddfU6.png' alt='Profile Picture' style='width:300px; height:300px; object-fit:cover; border-radius:50%; box-shadow:0 2px 12px rgba(13,35,70,0.10); background:#fff;'/>
  <div style='background:#f5f5f5; border-radius:18px; padding:32px 24px; flex:1;'>
    <h2 style='color:#0d2346;'>KILALANIN ANG ORGANISADOR</h2>
    <p style='font-size:1.1vw; color:#222;'>
      Si <b>Lowie A. Tambis</b> ay dating third officer ng isang Japanese shipping industry. Tinalikuran niya ang maaaring ikayaman niya kapalit ng pagtahak sa hindi tiyak na daan sa matematika at lohika na sa kalaunan ay nagbigay sa kaniya ng kahulugan at katuturan.
    </p>
    <p style='font-size:1.1vw; color:#222;'>
      Ninais niyang ibahagi ang kahalagahan ng pagkakaroon ng rasyonal at lohikal na pag-iisip sa mga kapwa niya Pilipino. Sa kaniyang mga leksyon, makikita mo ang kaniyang pagkahilig at dedikasyon sa pagtuturo ng mga mahahalagang konsepto, lahat ay nasa wikang Filipino para mas madaling maintindihan.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)


# --- RISK-FREE GUARANTEE ---
st.markdown("""
<a href="https://morerationalph.streamlit.app/Panuntunan" style="text-decoration:none;">
  <div style='background:#b3e0ff; color:#0d2346; text-align:center; border-radius:18px; margin:3em 0 2em 0; padding:32px 10px; box-shadow:0 2px 16px rgba(13,35,70,0.10); transition:box-shadow 0.2s; cursor:pointer;'>
    <h2 style='font-size:2vw; font-weight:bold;'>SUBUKAN NG WALANG PANGAMBA! SIMULAN ANG PAG-AARAL</h2>
    <p style='font-size:1.2vw;'>Ang mga pahina ay libre at maaari mong subukan nang walang panganib.</p>
  </div>
</a>
""", unsafe_allow_html=True)

# --- ENROLL/CTA BUTTON ---

# --- ENROLL & EVENTS BUTTONS SIDE BY SIDE ---
st.markdown("""
<div id="enroll-events" style='text-align:center; margin:3em 0;'>
  <div style='display:inline-flex; gap:32px; flex-wrap:wrap; justify-content:center;'>
    <a href="https://chat.whatsapp.com/JlWpprYtqNBEzmwpu0wqJb" target="_blank" style='display:inline-block; background:#25D366; color:#fff; font-size:1.3vw; font-weight:bold; padding:18px 48px; border-radius:16px; text-decoration:none; box-shadow:0 4px 18px 0 rgba(13,35,70,0.25);'>
      SUMALI SA KOMUNIDAD NGAYON
    </a>
    <a href="https://www.meetup.com/more-rational-ph/" target="_blank" style='display:inline-block; background:#ff7043; color:#fff; font-size:1.2vw; font-weight:bold; padding:16px 44px; border-radius:16px; text-decoration:none; box-shadow:0 4px 18px 0 rgba(13,35,70,0.18);'>
      ATTEND EVENTS (MEETUP)
    </a>
  </div>
</div>
""", unsafe_allow_html=True)



