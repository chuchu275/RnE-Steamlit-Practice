import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')

col1, col2, col3 = st.columns(3)
col1.metric("대학수", "70 °F", "1.2 °F")
col2.metric("국", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.title('대학 기숙사 분석')

st.dataframe(data)
st.write('기숙사현황')