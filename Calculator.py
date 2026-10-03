import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Advanced Scientific Calculator")

# Choice for Interaction Method
input_method = st.radio("Select Input Mode:", ["On-Screen Scientific Keyboard", "Direct Text Input"], horizontal=True)

if input_method == "Direct Text Input":
    st.subheader("⌨️ Keyboard Mode")
    st.caption("Type any mathematical expression directly using your laptop keyboard:")
    
    expr = st.text_input("Enter expression:", placeholder="e.g. sin(30) + sqrt(16) * 5")
    
    if st.button("Calculate Result", type="primary", use_container_width=True):
        try:
            allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            res = eval(expr, {"__builtins__": None}, allowed)
            st.success(f"**Result:** {res}")
        except Exception:
            st.error("Invalid Math Syntax! Please check your expression.")

else:
    st.subheader("🖥️ Interactive Scientific Layout")
    
    if "calc_input" not in st.session_state:
        st.session_state.calc_input = ""

    # Live Display Bar (Read-only representation)
    st.text_input("Display Bar:", value=st.session_state.calc_input, key="display_bar", disabled=True)

    # Helper function to append text
    def add_to_input(val):
        st.session_state.calc_input += str(val)

    def clear_input():
        st.session_state.calc_input = ""

    def backspace():
        st.session_state.calc_input = st.session_state.calc_input[:-1]

    # Row 1: Scientific Functions
    r1_col1, r1_col2, r1_col3, r1_col4, r1_col5 = st.columns(5)
    with r1_col1: st.button("sin", on_click=add_to_input, args=("sin(",), use_container_width=True)
    with r1_col2: st.button("cos", on_click=add_to_input, args=("cos(",), use_container_width=True)
    with r1_col3: st.button("tan", on_click=add_to_input, args=("tan(",), use_container_width=True)
    with r1_col4: st.button("log", on_click=add_to_input, args=("log10(",), use_container_width=True)
    with r1_col5: st.button("ln", on_click=add_to_input, args=("log(",), use_container_width=True)

    # Row 2: Advanced Math
    r2_col1, r2_col2, r2_col3, r2_col4, r2_col5 = st.columns(5)
    with r2_col1: st.button("√ (sqrt)", on_click=add_to_input, args=("sqrt(",), use_container_width=True)
    with r2_col2: st.button("π (pi)", on_click=add_to_input, args=("pi",), use_container_width=True)
    with r2_col3: st.button("e", on_click=add_to_input, args=("e",), use_container_width=True)
    with r2_col4: st.button("^ (pow)", on_click=add_to_input, args=("**",), use_container_width=True)
    with r2_col5: st.button("abs", on_click=add_to_input, args=("abs(",), use_container_width=True)

    # Row 3: Standard Numbers & Controls
    r3_col1, r3_col2, r3_col3, r3_col4, r3_col5 = st.columns(5)
    with r3_col1: st.button("7", on_click=add_to_input, args=("7",), use_container_width=True)
    with r3_col2: st.button("8", on_click=add_to_input, args=("8",), use_container_width=True)
    with r3_col3: st.button("9", on_click=add_to_input, args=("9",), use_container_width=True)
    with r3_col4: st.button("DEL", on_click=backspace, use_container_width=True)
    with r3_col5: st.button("CLR", on_click=clear_input, use_container_width=True)

    # Row 4: Numbers & Operators
    r4_col1, r4_col2, r4_col3, r4_col4, r4_col5 = st.columns(5)
    with r4_col1: st.button("4", on_click=add_to_input, args=("4",), use_container_width=True)
    with r4_col2: st.button("5", on_click=add_to_input, args=("5",), use_container_width=True)
    with r4_col3: st.button("6", on_click=add_to_input, args=("6",), use_container_width=True)
    with r4_col4: st.button("×", on_click=add_to_input, args=("*",), use_container_width=True)
    with r4_col5: st.button("÷", on_click=add_to_input, args=("/",), use_container_width=True)

    # Row 5: Numbers, Brackets & Operators
    r5_col1, r5_col2, r5_col3, r5_col4, r5_col5 = st.columns(5)
    with r5_col1: st.button("1", on_click=add_to_input, args=("1",), use_container_width=True)
    with r5_col2: st.button("2", on_click=add_to_input, args=("2",), use_container_width=True)
    with r5_col3: st.button("3", on_click=add_to_input, args=("3",), use_container_width=True)
    with r5_col4: st.button("+", on_click=add_to_input, args=("+",), use_container_width=True)
    with r5_col5: st.button("-", on_click=add_to_input, args=("-",), use_container_width=True)

    # Row 6: Zero, Decimals & Brackets
    r6_col1, r6_col2, r6_col3, r6_col4, r6_col5 = st.columns(5)
    with r6_col1: st.button("0", on_click=add_to_input, args=("0",), use_container_width=True)
    with r6_col2: st.button(".", on_click=add_to_input, args=(".",), use_container_width=True)
    with r6_col3: st.button("(", on_click=add_to_input, args=("(",), use_container_width=True)
    with r6_col4: st.button(")", on_click=add_to_input, args=(")",), use_container_width=True)
    with r6_col5: st.button("%", on_click=add_to_input, args=("/100",), use_container_width=True)

    # Calculate Equal Button
    if st.button("=", type="primary", use_container_width=True):
        try:
            allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(st.session_state.calc_input, {"__builtins__": None}, allowed)
            st.session_state.calc_input = str(result)
            st.rerun()
        except Exception:
            st.error("Syntax Error!")
