import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.markdown("""
    <style>
        .css-eh5xgm.e1ewe7hr3
        {
            visibility: hidden;
        }
        .css-cio0dv.e1g8pov61
        {
            visibility:hidden;
        }
    </style>
""", unsafe_allow_html=True)
# css-eh5xgm e1ewe7hr3
table1 = pd.DataFrame(
    {"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2": [8, 9, 10, 11, 12, 13, 14]})

st.title("Hi! Im Streamlit Web App")
st.subheader("Hi im your Subheader")
st.header("Hi Im Header")

st.text("Hi Im text function and programmers uses me implace of paragraph text")

st.markdown("**Hello** *World*")
st.markdown("# Header 1")  # H1
st.markdown("## Header 2")
st.markdown("> Block Code")
st.markdown("`Code Here`")
st.markdown("---")  # Horizontal rule
st.markdown(
    "[Markdown Cheat-sheet](https://www.markdownguide.org/cheat-sheet/)")

st.markdown("[Streamlit Youtube Tutorial](https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=2)")
st.caption("Hi Im Caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown("[Latex Cheat Sheet](https://katex.org/docs/supported.html)")

json = {"a": "1,2,3", "b": "4,5,6"}
st.json(json)

code = """
print("Hello World")
def funct():
    return 0;
"""
st.code(code, language="python")

st.write("## H2")

st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1,4ms⁻¹")  # \^-1 (tab)

st.table(table1)
st.dataframe(table1)
st.image("image.jpg", caption="This my image caption", width=200)
# st.audio() st.video()


def change():
    print(st.session_state.checker)


state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")

if state:
    st.write("Hi")
else:
    pass

radio_btn = st.radio("Im which country do you live",
                     options=("US", "UK", "Canada"))
# print(radio_btn)


def btn_click():
    print("button clicked")


btn = st.button("click me!", on_click=btn_click
                )

select = st.selectbox("what is your favourite car",
                      options=("Audi", "BMW", "Ferrari"))
# print(select)

multi_select = st.multiselect("What is your favourite Tech Brand", options=(
    "MIcrosoft", "Apple", "Amazon", "Oracle"))
# st.write(multi_select)

st.write("### Uploading Files")
st.write("---")

images = st.file_uploader("Please upload an image", type=["jpg", "png", "jpeg"],
                          accept_multiple_files=True)

if images is not None:
    for image in images:
        st.image(image, width=100)

val = st.slider("This is slider", min_value=50, max_value=100, value=70)

val = st.text_input("Enter your Course Title", max_chars=60)

val = st.text_area("Enter your Course Description", max_chars=1000)

val = st.date_input("enter your registration date")

val = st.time_input("Set Time", value=time(0, 0, 0))


def converter(value):
    m, s, ms = value.split(":")
    t_s = int(m)*60+int(s)+int(ms)/1000
    return(t_s)


if str(val) == "00:00:00":
    st.write("please set timer")
else:
    sec = converter(str(val))
    bar = st.progress(0)
    per = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i)+"%")
        ts.sleep(per)
# print(val)


st.markdown("<h1 style='text-align:center;'>Form User Registration</h1>",
            unsafe_allow_html=True)

form = st.form("Form 1")

form.text_input("first name")
form.form_submit_button("Submit")

with st.form('Form 2', clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    st.text_input("Email-address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("month")
    year.text_input("year")
    s_state = st.form_submit_button("Submit")

    if s_state:
        if f_name == "" and l_name == "":
            st.warning("please fill above fields")
        else:
            st.success("Submitted Succesfully")

opt = st.sidebar.radio("Select Any Graph", options=("Line", "Bar", "H-Bar"))

st.markdown("<h1 style='text-align:center;'>Chart</h1>",
            unsafe_allow_html=True)

bar_x = np.array([1, 2, 3, 4, 5])

x = np.linspace(0, 10, 100)
if opt == "Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)

elif opt == "Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align:center;'>H-Bar Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)
