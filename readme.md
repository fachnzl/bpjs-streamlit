pip install streamlit
save and run (click on icon run in vscode)
streamlit run main.py
ctrl+C for stop

How To Remove Humburger menu and footer
st.markdown("""
    <style>
        .css-eh5xgm.e1ewe7hr3 #found it from inspect element
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
