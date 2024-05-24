import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header('The Best Company')
st.title('this is a bunch of random text')
st.subheader("Our Team")



df = pandas.read_csv('files/data.csv')


col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:].iterrows():
        if index % 3 == 0:
            st.title(row['first name'].title()+" "+row['last name'].title())
            st.write(row['role'])
            st.image(f"files/images/{row['image']}")
with col2:
    for index, row in df[:].iterrows():
        if index % 3 == 1:
            st.title(row['first name'].title()+" "+row['last name'].title())
            st.write(row['role'])
            st.image(f"files/images/{row['image']}")
with col3:
    for index, row in df[:].iterrows():
        if index % 3 == 2:
            st.title(row['first name'].title()+" "+row['last name'].title())
            st.write(row['role'])
            st.image(f"files/images/{row['image']}")






