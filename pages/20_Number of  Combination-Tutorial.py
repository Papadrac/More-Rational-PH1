import streamlit as st
import random
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------

col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Tutorial: Number of Combination")
    st.write("Sa tutorial na ito, matututuhan mo kung paano kunin ang bilang ng posibleng grupo gamit ang kombinasyon.")
st.write("--------")

# --- COMBINATION TUTORIALS ---

# --- Combination Tutorial 1 ---
if 'comb_tutorial_page' not in st.session_state:
    st.session_state['comb_tutorial_page'] = 1

st.subheader("Tutorial 1: Pumili ng grupo ng 3 para sa Palarong Pinoy")
st.markdown("""
<div style='font-size:1.1em; font-weight:500; margin-bottom:16px'>
May 5 na bata: Jose, Maria, Lito, Inday, at Cardo. Ilan ang paraan ng pagpili ng 3 na magiging kalahok sa <b>Patintero</b>?
</div>
""", unsafe_allow_html=True)

show_next = False
# Step 1: Dropdowns for multiplication (permutation part)
st.write("**Step 1:** Piliin ang bilang ng pagpipilian sa bawat pwesto:")
cols1 = st.columns(3)
options1 = [["", "5", "4", "3", "2", "1"], ["", "4", "3", "2", "1"], ["", "3", "2", "1"]]
corrects1 = ["5", "4", "3"]
answers1 = []
for i in range(3):
    ans = cols1[i].selectbox(f"Piliin para sa pwesto {i+1}", options1[i], key=f"comb1_{i}")
    answers1.append(ans)

# Step 2: Multiply answers
if all(a in corrects1 for a in answers1) and all(a != "" for a in answers1):
    st.write("**Step 2:** Imultiply ang mga sagot sa itaas: 5 × 4 × 3 = ?")
    mult1 = st.text_input("I-type ang sagot sa multiplication:", key="comb1_mult")
    if mult1:

            if mult1.strip() == "60":
                st.success("Tama! 5 × 4 × 3 = 60.")
                st.write("**Step 3:** Dahil hindi mahalaga ang ayos, hatiin sa 3! (3 × 2 × 1 = 6)")
                div1 = st.text_input("I-type ang sagot sa 60 ÷ 6:", key="comb1_div")
                if div1:
                    if div1.strip() == "10":
                        st.success("Tama! May 10 na paraan ng pagpili ng 3 mula sa 5.")
                        
                        show_next = True
                    else:
                        st.error("Mali. Sagot ay 10.")
            else:
                st.error("Mali. Sagot ay 60.")

if show_next:
    if st.button("Susunod", key="comb_next_btn"):
        st.session_state['comb_tutorial_page'] = 2

# --- Combination Tutorial 2 ---
if st.session_state.get('comb_tutorial_page', 1) == 2:
    st.write("---")
    st.subheader("Tutorial 2: Pumili ng 2 Kakanin para sa Handaan")
    st.markdown("""
<div style='font-size:1.1em; font-weight:500; margin-bottom:16px'>
May 6 na kakanin: Puto, Kutsinta, Suman, Bibingka, Sapin-sapin, at Kalamay. Ilan ang paraan ng pagpili ng 2 na ihahain sa pista?
</div>
""", unsafe_allow_html=True)

    # Step 1: Dropdowns for multiplication (permutation part)
    st.write("**Step 1:** Piliin ang bilang ng pagpipilian sa bawat pwesto:")
    cols2 = st.columns(2)
    options2 = [["", "6", "5", "4", "3", "2", "1"], ["", "5", "4", "3", "2", "1"]]
    corrects2 = ["6", "5"]
    answers2 = []
    for i in range(2):
        ans = cols2[i].selectbox(f"Piliin para sa pwesto {i+1}", options2[i], key=f"comb2_{i}")
        answers2.append(ans)

    # Step 2: Multiply answers
    show_next2 = False
    if all(a in corrects2 for a in answers2) and all(a != "" for a in answers2):
        st.write("**Step 2:** Imultiply ang mga sagot sa itaas: 6 × 5 = ?")
        mult2 = st.text_input("I-type ang sagot sa multiplication:", key="comb2_mult")
        if mult2:

            if mult2.strip() == "30":
                st.success("Tama! 6 × 5 = 30.")
                st.write("**Step 3:** Dahil hindi mahalaga ang ayos, hatiin sa 2! (2 × 1 = 2)")
                div2 = st.text_input("I-type ang sagot sa 30 ÷ 2:", key="comb2_div")
                if div2:
                    if div2.strip() == "15":
                        st.success("Tama! May 15 na paraan ng pagpili ng 2 mula sa 6.")
                        st.balloons()
                        show_next2 = True
                    else:
                        st.error("Mali. Sagot ay 15.")
            else:
                st.error("Mali. Sagot ay 30.")

    if show_next2:
        
        st.markdown("""
<div style='margin-top:24px; font-size:1.1em; color:#2E8B57; font-weight:500;'>
Handa ka na sa susunod na bahagi!
</div>
<a href="/pages/21_Susunod_na_Tutorial.py">
<button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer; margin-top:8px;'>Susunod &rarr;</button>
</a>
""", unsafe_allow_html=True)
