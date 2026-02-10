import streamlit as st
import base64
from pathlib import Path

 # --- Set meet1.JPG as background image ---
st.markdown("""
<style>
[data-testid="stSidebar"] {
  background: #0d2346 !important;
}
[data-testid="stSidebar"] * {
  color: #fff !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style='text-align:center; font-size:1.4vw; font-weight:bold; margin-top:0.0em; margin-bottom:0.0em; margin-left:0; margin-right:0; color:#0d2346; white-space:nowrap; letter-spacing:-1px; padding:0; '>
Mabuhay!
</h1>
""", unsafe_allow_html=True)

# --- Set new background image from Imgur ---
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
  background-image: url('https://imgur.com/FIdMR75.jpg');
  background-size: cover;
  background-position: center;
}}
[data-testid="stHeader"] {{
  background: rgba(255,255,255,0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# --- Custom Title: Bold, Bigger, Centered ---

st.markdown("""
<h1 style='text-align:center; font-size:6vw; font-weight:bold; margin-top:0.0em; margin-bottom:0.5em; margin-left:0; margin-right:0; color:#0d2346; white-space:nowrap; letter-spacing:-1px; padding:0; text-shadow:2px 2px 8px #e0e0e0;'>
More Rational PH
</h1>
""", unsafe_allow_html=True)

st.write("")


# --- Rectangular Links ---
st.markdown('''
<style>
/* No rotation animation, static border */
.circle-border {
  padding: 3px;
  border-radius: 18px;
  background: conic-gradient(from 0deg, #e0e0e0 0%, #b3e5fc 25%, #fffde7 50%, #b3e5fc 75%, #e0e0e0 100%);
  display: inline-block;
}
.circle-border .rect-link {
  background-clip: padding-box;
  background-origin: padding-box;
  background-color: inherit;
}
.rect-link {
  display: flex; align-items: center; justify-content: center;
  min-width: 220px; padding: 28px 0;
  border-radius: 15px;
  color: #fff !important;
  font-size: 18px; text-align: center; text-decoration: none !important; font-weight: bold;
  box-shadow: 0 4px 18px 0 rgba(200,200,200,0.25), 0 1.5px 4px 0 rgba(180,180,180,0.13);
  position: relative; height: 100%;
  background: #fff;
  border: 3px solid transparent;
  background-clip: padding-box;
  z-index: 1;
}

/* Glitter border animation */
.rect-link::before {
  content: "";
  position: absolute;
  top: -3px; left: -3px; right: -3px; bottom: -3px;
  border-radius: 18px;
  padding: 0;
  z-index: -1;
  background: linear-gradient(120deg, #fffbe7, #ffd700, #fffbe7, #b3e5fc, #fffbe7);
  background-size: 200% 200%;
  animation: glitter 2.5s linear infinite;
}

@keyframes glitter {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
  z-index: 1;
}
.rect-link.purple { background: #4b145a !important; color: #0d2346 !important; }
.rect-link.yellow { background: #ffd700 !important; color: #000 !important; }
.rect-link.blue { background: #1976d2 !important; color: #000 !important; }
.event-fixed-align {
  position: fixed !important;
  right: 80px;
  bottom: 20px;
  z-index: 1000;
}
</style>
<div style="width:100%; display:flex; justify-content:center; gap:32px; margin-top:40px;">
  <span class="circle-border"><a href="https://more-rational-ph1-jqfq2eed47wdgf6c79n2as.streamlit.app/About_Us" class="rect-link yellow">About Us</a></span>
    <span class="circle-border"><a href="https://more-rational-ph1-jqfq2eed47wdgf6c79n2as.streamlit.app/Bakit_Rationality" class="rect-link yellow">Bakit Rationality</a></span>
  <span class="circle-border"><a href="https://more-rational-ph1-jqfq2eed47wdgf6c79n2as.streamlit.app/Panuntunan" class="rect-link blue">Improve Your Thinking</a></span>
</div>
''', unsafe_allow_html=True)

# --- Event Section (lower right) ---
st.markdown('''
<div class="event-fixed-align">
  <div style="background:#fff; border-radius:18px; box-shadow:0 2px 16px rgba(13,35,70,0.12); padding:20px 20px; min-width:220px; max-width:280px; border:2px solid #1976d2;">
    <h3 style="margin-top:0; margin-bottom:10px; color:#1976d2; font-size:1.15em; font-weight:bold; text-align:left;">Events:</h3>
    <ul style="padding-left:14px; font-size:0.95em; color:#222;">
    <li><b>Meetup:</b> <a href="https://www.meetup.com/more-rational-ph/events/313155066/?eventOrigin=home_next_event_you_are_hosting" target="_blank" style="font-size:0.95em; color:#111; text-decoration:underline; font-weight:bold;">More Rational PH Meetup</a><br>
        <span style="font-size:0.85em; color:#1976d2;">Feb 21, 2026</span>
      </li>
      <li><b>Meetup:</b> More Rational PH Meetup<br><span style="font-size:0.85em; color:#1976d2;">TBA</span></li>
    </ul>
  </div>
</div>
''', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.markdown('''
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
  <a href="https://imgur.com/1wnMW4l" target="_blank" style="display:inline-block;">
    <img src="https://pngmark.com/wp-content/uploads/2023/01/Whatsapp-1024x1000.png" alt="WhatsApp Icon" style="width:34px; height:34px; object-fit:contain; vertical-align:middle;"/>
  </a>
  <a href="https://chat.whatsapp.com/JlWpprYtqNBEzmwpu0wqJb" target="_blank" style="
      display: inline-block;
      background: #25D366;
      color: #fff;
      font-size: 15px;
      font-weight: bold;
      padding: 10px 20px;
      border-radius: 12px;
      text-decoration: none;
      box-shadow: 0 2px 8px rgba(13,35,70,0.10);
      border: none;
      vertical-align: middle;
  ">Join our WhatsApp Group</a>
</div>
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
  <a href="https://imgur.com/kc4rJmO" target="_blank" style="display:inline-block;">
    <img src="https://static.vecteezy.com/system/resources/previews/018/930/698/non_2x/facebook-logo-facebook-icon-transparent-free-png.png" alt="Facebook Icon" style="width:34px; height:34px; object-fit:contain; vertical-align:middle;"/>
  </a>
  <a href="https://www.facebook.com/groups/1663328047944433" target="_blank" style="
      display: inline-block;
      background: #1877f3;
      color: #fff;
      font-size: 15px;
      font-weight: bold;
      padding: 10px 20px;
      border-radius: 12px;
      text-decoration: none;
      box-shadow: 0 2px 8px rgba(13,35,70,0.10);
      border: none;
      vertical-align: middle;
  ">Join our Facebook Group</a>
</div>
''', unsafe_allow_html=True)







