from pandas.core.tools import numeric
import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('기숙사수용현황분석.csv')

num1 = 108
num2 = len(df[df['설립구분'] != '사립'['학교']].unique())
num3 = len(df[df['설립구분'] != '사립']['학교'].unique())


st.title('대학 기숙사 분석')



col1, col2, col3 = st.columns(3)
col1.metric("대학수", num1, "")
col2.metric("국공립학교", num2, f'{round(num2/num1 * 100,2)}%')
col3.metric("사립학교", num3, f'{round(num3/num1) * 100,2}%')



st.dataframe(data)
#st.write('기숙사현황')