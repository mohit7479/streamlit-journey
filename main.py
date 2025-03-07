import streamlit as st
import os

st.write("Hello Mohit")
st.title("This tag is used for title")
st.header("This is a header")
st.subheader("This is used for subheading")
st.markdown("This is _Markdown_")
st.caption("small text")

code_example="""
            def greet(name):
                print("Hello",name)
            """
st.code(code_example,language='python')

st.divider() #display a horizontal line

st.image(os.path.join(os.getcwd(),"static","image.jpg"),width=300,caption="This is an image")