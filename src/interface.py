import streamlit as st
import time

test_val = st.slider("try me", 0, 100)

while True:
    st.write(test_val)
    time.sleep(1)