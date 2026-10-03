import streamlit as st
import math
import re

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

# ---------------- FUNCTIONS ----------------

def sin(x, mode):
    return math.sin(math.radians(x)) if mode == "DEG" else math.sin(x)

def cos(x, mode):
    return math.cos(math.radians(x)) if mode == "DEG" else math.cos(x)

def tan(x, mode):
    return math.tan(math.radians(x)) if mode == "DEG" else math.tan(x)

def cot(x, mode):
    value = tan(x, mode)
    if abs(value) < 1e-12:
        raise ValueError("Cotangent is undefined")
    return 1 / value

def sec(x, mode):
    value = cos(x, mode)
    if abs(value) < 1e-12:
        raise ValueError("Secant is undefined")
    return 1 / value

def csc(x, mode):
    value = sin(x, mode)
    if abs(value) < 1e-12:
        raise ValueError("Cosecant is undefined")
    return 1 / value

def asin(x, mode):
    result = math.asin(x)
    return math.degrees(result) if mode == "DEG" else result

def acos(x, mode):
    result = math.acos(x)
    return math.degrees(result) if mode == "DEG" else result

def atan(x, mode):
    result = math.atan(x)
    return math.degrees(result) if mode == "DEG" else result


# ---------------- SESSION STATE ----------------

if "expression" not in st.session_state:
    st.session_state.expression = ""

if "answer" not in st.session_state:
    st.session_state.answer = "0"

if "mode" not in st.session_state:
    st.session_state.mode = "DEG"


# ---------------- CALCULATOR ----------------

st.title("🧮 Scientific Calculator")
st.caption("Python + Streamlit")

# DEG/RAD
mode = st.radio(
    "Angle Mode",
    ["DEG", "RAD"],
    horizontal=True,
    index=0 if st.session_state.mode == "DEG" else 1
)

st.session_state.mode = mode


# ---------------- KEYBOARD INPUT ----------------

keyboard_input = st.text_input(
    "⌨️ Enter expression using keyboard:",
    value=st.session_state.expression,
    placeholder="Example: sin(30)+5^2"
)

st.session_state.expression = keyboard_input


# ---------------- DISPLAY ----------------

st.text_input(
    "Display",
    value=st.session_state.expression,
    disabled=True
)


# ---------------- CALCULATE FUNCTION ----------------

def calculate():

    expression = st.session_state.expression

    if not expression:
        return

    try:
        expression = expression.replace("^", "**")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        # Factorial
        expression = re.sub(
            r"(\d+(?:\.\d+)?)!",
            r"factorial(\1)",
            expression
        )

        functions = {
            "sin": lambda x: sin(x, mode),
            "cos": lambda x: cos(x, mode),
            "tan": lambda x: tan(x, mode),
            "cot": lambda x: cot(x, mode),
            "sec": lambda x: sec(x, mode),
            "csc": lambda x: csc(x, mode),

            "asin": lambda x: asin(x, mode),
            "acos": lambda x: acos(x, mode),
            "atan": lambda x: atan(x, mode),

            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,

            "factorial": lambda x: math.factorial(int(x)),

            "pi": math.pi,
            "e": math.e
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            functions
        )

        if isinstance(result, float):
            if abs(result) < 1e-12:
                result = 0
            result = round(result, 12)

        st.session_state.answer = str(result)
        st.session_state.expression = str(result)

    except ZeroDivisionError:
        st.error("Cannot divide by zero.")

    except ValueError:
        st.error("Invalid mathematical value.")

    except Exception:
        st.error("Invalid expression. Please check your input.")


# ---------------- BUTTON FUNCTION ----------------

def add_text(value):
    st.session_state.expression += value


# ---------------- SCIENTIFIC BUTTONS ----------------

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("sin", use_container_width=True):
        add_text("sin(")

with col2:
    if st.button("cos", use_container_width=True):
        add_text("cos(")

with col3:
    if st.button("tan", use_container_width=True):
        add_text("tan(")

with col4:
    if st.button("cot", use_container_width=True):
        add_text("cot(")

with col5:
    if st.button("C", use_container_width=True):
        st.session_state.expression = ""


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("asin", use_container_width=True):
        add_text("asin(")

with col2:
    if st.button("acos", use_container_width=True):
        add_text("acos(")

with col3:
    if st.button("atan", use_container_width=True):
        add_text("atan(")

with col4:
    if st.button("sec", use_container_width=True):
        add_text("sec(")

with col5:
    if st.button("⌫", use_container_width=True):
        st.session_state.expression = st.session_state.expression[:-1]


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("csc", use_container_width=True):
        add_text("csc(")

with col2:
    if st.button("log", use_container_width=True):
        add_text("log(")

with col3:
    if st.button("ln", use_container_width=True):
        add_text("ln(")

with col4:
    if st.button("√", use_container_width=True):
        add_text("sqrt(")

with col5:
    if st.button("(", use_container_width=True):
        add_text("(")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button(")", use_container_width=True):
        add_text(")")

with col2:
    if st.button("π", use_container_width=True):
        add_text("pi")

with col3:
    if st.button("e", use_container_width=True):
        add_text("e")

with col4:
    if st.button("x²", use_container_width=True):
        add_text("**2")

with col5:
    if st.button("xʸ", use_container_width=True):
        add_text("**")


# ---------------- NUMERIC BUTTONS ----------------

st.markdown("### Numeric Keypad")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("7", use_container_width=True):
        add_text("7")

with col2:
    if st.button("8", use_container_width=True):
        add_text("8")

with col3:
    if st.button("9", use_container_width=True):
        add_text("9")

with col4:
    if st.button("÷", use_container_width=True):
        add_text("/")

with col5:
    if st.button("%", use_container_width=True):
        add_text("/100")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("4", use_container_width=True):
        add_text("4")

with col2:
    if st.button("5", use_container_width=True):
        add_text("5")

with col3:
    if st.button("6", use_container_width=True):
        add_text("6")

with col4:
    if st.button("×", use_container_width=True):
        add_text("*")

with col5:
    if st.button("!", use_container_width=True):
        add_text("!")


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("1", use_container_width=True):
        add_text("1")

with col2:
    if st.button("2", use_container_width=True):
        add_text("2")

with col3:
    if st.button("3", use_container_width=True):
        add_text("3")

with col4:
    if st.button("-", use_container_width=True):
        add_text("-")

with col5:
    if st.button("=", use_container_width=True):
        calculate()


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("0", use_container_width=True):
        add_text("0")

with col2:
    if st.button(".", use_container_width=True):
        add_text(".")

with col3:
    if st.button("00", use_container_width=True):
        add_text("00")

with col4:
    if st.button("+", use_container_width=True):
        add_text("+")

with col5:
    if st.button("Ans", use_container_width=True):
        add_text(st.session_state.answer)


# ---------------- CALCULATE FROM KEYBOARD ----------------

if st.button("🔢 Calculate", type="primary", use_container_width=True):
    calculate()


# ---------------- INFORMATION ----------------

st.divider()

st.info(
    "Keyboard input is supported through the expression box. "
    "You can also use the mouse to press calculator buttons."
)

st.caption(
    "Scientific Calculator | Python | Streamlit"
)