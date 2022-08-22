import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')
st.dataframe(data)

st.title('대학 기숙사 분석')
st.write('기숙사현황')