import streamlit as st
import math

st.title("🧮 Scientific Calculator")

# Option to input via keyboard or buttons
input_method = st.radio("Choose Input Method:", ["Keyboard Input", "On-Screen Buttons"])

if input_method == "Keyboard Input":
    expression = st.text_input("Enter expression (e.g., 5 + 3, sin(30), sqrt(16)):", "")
    if st.button("Calculate"):
        try:
            # Safe evaluation with math functions
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expression, {"__builtins__": None}, allowed_names)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error("Invalid Expression! Please check your math syntax.")

else:
    # On-screen buttons layout
    if "calc_input" not in st.session_state:
        st.session_state.calc_input = ""

    st.text_input("Display:", st.session_state.calc_input, key="display", disabled=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("7"): st.session_state.calc_input += "7"
        if st.button("4"): st.session_state.calc_input += "4"
        if st.button("1"): st.session_state.calc_input += "1"
        if st.button("C"): st.session_state.calc_input = ""
    with col2:
        if st.button("8"): st.session_state.calc_input += "8"
        if st.button("5"): st.session_state.calc_input += "5"
        if st.button("2"): st.session_state.calc_input += "2"
        if st.button("0"): st.session_state.calc_input += "0"
    with col3:
        if st.button("9"): st.session_state.calc_input += "9"
        if st.button("6"): st.session_state.calc_input += "6"
        if st.button("3"): st.session_state.calc_input += "3"
        if st.button("."): st.session_state.calc_input += "."
    with col4:
        if st.button("+"): st.session_state.calc_input += "+"
        if st.button("-"): st.session_state.calc_input += "-"
        if st.button("*"): st.session_state.calc_input += "*"
        if st.button("/"): st.session_state.calc_input += "/"

    if st.button("=", use_container_width=True):
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(st.session_state.calc_input, {"__builtins__": None}, allowed_names)
            st.session_state.calc_input = str(result)
            st.rerun()
        except Exception:
            st.error("Invalid Expression")
