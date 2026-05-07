# --- ARRANGEMENT TUTORIAL ---
import streamlit as st

# TUTORIAL NAVIGATION STATE
if 'tutorial_page' not in st.session_state:
	st.session_state['tutorial_page'] = 1  # 1 = first, 2 = second

# FIRST TUTORIAL: 5 people in a line
##############
# Tutorial state
if 'arrange_tutorial_step' not in st.session_state:
	st.session_state['arrange_tutorial_step'] = 1
if 'arrange_tutorial_answers' not in st.session_state:
	st.session_state['arrange_tutorial_answers'] = [None]*5

# --- Show the correct tutorial page based on navigation state ---
if st.session_state['tutorial_page'] == 1:
	# FIRST TUTORIAL
	pos_names = ["unang", "ikalawang", "ikatlong", "ikaapat", "ikalimang"]
	step = st.session_state['arrange_tutorial_step']
	blank_vals = st.session_state['arrange_tutorial_answers']
	corrects = ["5", "4", "3", "2", "1"]
	dropdown_options = [
		["", "5", "4", "3", "2", "1"],
		["", "4", "3", "2", "1"],
		["", "3", "2", "1"],
		["", "2", "1"],
		["", "1"]
	]
	col_logo, col_header = st.columns([1, 5])
	with col_logo:
		st.image("https://imgur.com/wuASFCz.jpg", width=150)
	with col_header:
		st.subheader("*Permutations*: Bilang ng Posibleng Ayos")
		st.write("Bilangin ang bilang ng posibleng ayos o pagkakasunod-sunod ng mga bagay.")
	st.write("---")
	st.subheader("Tutorial: Bilang ng Posibleng Ayos ng 5 Tao")
	st.markdown("<div style='font-size:1.1em; font-weight:500; margin-bottom:16px'>May limang tao sa isang palarong pampamilya: nanay, tatay, kuya, ate, at bunso. Ilan ang posibleng ayos kung sila ay nakaupo sa isang linya? Sagutan ang bawat pwesto, isa-isa.</div>", unsafe_allow_html=True)
	cols = st.columns(5)
	dropdown_feedback = [st.empty() for _ in range(5)]
	for i in range(5):
		disabled = i > st.session_state['arrange_tutorial_step'] - 1
		with cols[i]:
			val = blank_vals[i] if blank_vals[i] is not None else ""
			selected = st.selectbox(
				f"", dropdown_options[i],
				index=dropdown_options[i].index(val) if val in dropdown_options[i] else 0,
				key=f"arrange_dropdown_{i}",
				disabled=disabled
			)
			if not disabled:
				blank_vals[i] = selected
				# Show feedback if wrong and not blank
				if val not in (None, "") and val != corrects[i]:
					remaining = corrects[i]
					dropdown_feedback[i].info(f"Dapat {remaining} ang natitira sa pwesto na ito dahil {remaining} tao pa ang hindi nauupo.")
				else:
					dropdown_feedback[i].empty()
	st.markdown(f"**Step {step}**: Ilang tao ang pwedeng ilagay sa {pos_names[step-1]} pwesto?")
	feedback = st.empty()
	can_submit = blank_vals[step-1] not in (None, "")
	submit = st.button("Ipadala", key=f"arrange_submit_{step}", disabled=not can_submit)
	if submit:
		user_ans = blank_vals[step-1]
		st.session_state['arrange_tutorial_answers'][step-1] = user_ans
		if user_ans == corrects[step-1]:
			feedback.success("Tama!")
			if step < 5:
				st.session_state['arrange_tutorial_step'] += 1
				st.rerun()
		else:
			feedback.error(f"Mali. Dapat {corrects[step-1]} ang sagot dito.")
	if step > 1:
		if st.button("Nakaraan", key="arrange_prev"):
			st.session_state['arrange_tutorial_step'] -= 1
			st.rerun()
	if all(blank_vals[i] == corrects[i] for i in range(5)):
		st.info("Lahat ng pwesto ay nasagutan! Upang makuha ang kabuuang bilang ng ayos, imultiply ang mga sagot: 5 × 4 × 3 × 2 × 1 = ?")
		final_ans = st.text_input("I-type ang kabuuang bilang ng ayos:", key="arrange_final_ans")
		if final_ans:
			if final_ans.strip() == "120":
				st.balloons()
				st.success("Tama! May 120 posibleng ayos ng limang tao sa isang linya.")
				if st.button("Susunod", key="arrange_tutorial_next"):
					st.session_state['tutorial_page'] = 2
					st.session_state['arrange2_tutorial_step'] = 1
					st.session_state['arrange2_tutorial_answers'] = [None]*3
					st.rerun()
			else:
				st.error("Mali. Subukang muli. Sagot ay 120.")
	st.stop()

elif st.session_state['tutorial_page'] == 2:
	# SECOND TUTORIAL
	pos_names2 = ["unang", "ikalawang", "ikatlong"]
	step2 = st.session_state['arrange2_tutorial_step']
	blank_vals2 = st.session_state['arrange2_tutorial_answers']
	corrects2 = ["7", "6", "5"]
	dropdown_options2 = [
		["", "7", "6", "5", "4", "3", "2", "1"],
		["", "6", "5", "4", "3", "2", "1"],
		["", "5", "4", "3", "2", "1"]
	]
	col_logo, col_header = st.columns([1, 5])
	with col_logo:
		st.image("https://imgur.com/wuASFCz.jpg", width=150)
	with col_header:
		st.subheader("*Permutations*: Bilang ng Posibleng Ayos")
		st.write("Bilangin ang bilang ng posibleng ayos o pagkakasunod-sunod ng mga bagay.")
    
	st.write("---")
	st.subheader("Tutorial: Bilang ng Posibleng Ayos ng 3 Tao mula sa 7")
	st.markdown("<div style='font-size:1.1em; font-weight:500; margin-bottom:16px'>May 7 na tao: Ana, Ben, Carlo, Dina, Ella, Faye, at Greg. Ilan ang posibleng ayos kung pipili ng 3 at isasaayos sila sa isang linya? Sagutan ang bawat pwesto, isa-isa.</div>", unsafe_allow_html=True)
	cols2 = st.columns(3)
	dropdown_feedback2 = [st.empty() for _ in range(3)]
	for i in range(3):
		disabled = i > st.session_state['arrange2_tutorial_step'] - 1
		with cols2[i]:
			val = blank_vals2[i] if blank_vals2[i] is not None else ""
			selected = st.selectbox(
				f"", dropdown_options2[i],
				index=dropdown_options2[i].index(val) if val in dropdown_options2[i] else 0,
				key=f"arrange2_dropdown_{i}",
				disabled=disabled
			)
			if not disabled:
				blank_vals2[i] = selected
				# Show feedback if wrong and not blank
				if val not in (None, "") and val != corrects2[i]:
					remaining = corrects2[i]
					dropdown_feedback2[i].info(f"Dapat {remaining} ang natitira sa pwesto na ito dahil {remaining} tao pa ang hindi nauupo.")
				else:
					dropdown_feedback2[i].empty()
	st.markdown(f"**Step {step2}**: Ilang tao ang pwedeng ilagay sa {pos_names2[step2-1]} pwesto?")
	feedback2 = st.empty()
	can_submit2 = blank_vals2[step2-1] not in (None, "")
	submit2 = st.button("Ipadala", key=f"arrange2_submit_{step2}", disabled=not can_submit2)
	if submit2:
		user_ans2 = blank_vals2[step2-1]
		st.session_state['arrange2_tutorial_answers'][step2-1] = user_ans2
		for i in range(3):
			if blank_vals2[i] not in (None, ""):
				if blank_vals2[i] == corrects2[i]:
					cols2[i].success("Tama!")
				else:
					cols2[i].error(f"Mali. Dapat {corrects2[i]} ang sagot dito.")
		if user_ans2 == corrects2[step2-1]:
			feedback2.success("Tama!")
			if step2 < 3:
				st.session_state['arrange2_tutorial_step'] += 1
				st.rerun()
		else:
			feedback2.error(f"Mali. Dapat {corrects2[step2-1]} ang sagot dito.")
	if step2 > 1:
		if st.button("Nakaraan", key="arrange2_prev"):
			st.session_state['arrange2_tutorial_step'] -= 1
			st.rerun()
	if all(blank_vals2[i] == corrects2[i] for i in range(3)):
		st.info("Lahat ng pwesto ay nasagutan! Upang makuha ang kabuuang bilang ng ayos, imultiply ang mga sagot: 7 × 6 × 5 = ?")
		final_ans2 = st.text_input("I-type ang kabuuang bilang ng ayos:", key="arrange2_final_ans")
		if final_ans2:
			if final_ans2.strip() == "210":
				st.balloons()
				st.success("Tama! May 210 posibleng ayos ng tatlong tao mula sa 7.")
				# Add link to next file with comment
				st.markdown("""
<div style='margin-top:24px; font-size:1.1em; color:#2E8B57; font-weight:500;'>
Ngayon alam mo na pano sagutan, <b>Subukan ang susunod na mga tanong</b>:
</div>
<a href="https://morerationalph.streamlit.app/" target="_self">
<button style='font-size:1em; padding:8px 16px; background:#4CAF50; color:white; border:none; border-radius:4px; cursor:pointer; margin-top:8px;'>Pumunta sa Susunod na Seksyon &#8594;</button>
</a>
""", unsafe_allow_html=True)
			else:
				st.error("Mali. Subukang muli. Sagot ay 210.")
		st.stop()


# NAVIGATION BUTTONS AT THE BOTTOM (always show)
nav_col1, nav_col2 = st.columns([1, 1])
with nav_col1:
	st.button("Nakaraan", on_click=lambda: st.session_state.update({'tutorial_page': max(1, st.session_state['tutorial_page']-1)}), disabled=(st.session_state['tutorial_page'] == 1), key="tutorial_prev")
with nav_col2:
	# Always enable 'Susunod' if on first tutorial, or if on second and not finished
	show_next = (st.session_state['tutorial_page'] == 1) or (st.session_state['tutorial_page'] == 2)
	st.button("Susunod", on_click=lambda: st.session_state.update({'tutorial_page': min(2, st.session_state['tutorial_page']+1)}), disabled=not show_next, key="tutorial_next")
