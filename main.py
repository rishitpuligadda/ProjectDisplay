import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])
name = "cat.jpg"

with col1:
    st.image("images/cat.jpg", width=400)

with col2:
    st.title("Rishit")
    content = """I really hope I have something
    to write here in the future.
    For now let's leave it as it is"""
    st.info(content)

st.write("Below you can find some of the apps I have built in python. Would be building many more in the future ;)")

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

print(df)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
