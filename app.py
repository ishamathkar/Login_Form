import streamlit as st

st.title("Login Form")

my_dict={"divyashelke@gmail.com":"123","shamikakadam@gmail.com":"456","ishamathkar@gmail.com":"789"}
email=st.text_input("Enter Email")
password=st.text_input("Enter Password")


btn=st.button("Login")

if btn:
    if email in my_dict:
        if password==my_dict[email]:
          st.balloons()
          st.success('SUCCESSFULLY LOGGED IN!', icon="✅")
        else:
          st.success('Incorrect Password', icon="❌")
    else:
          st.success('Your email is incorrect', icon="❌")