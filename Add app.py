import streamlit as st
import math

def fatigue(t):
    return 58 * math.exp(-0.344 * t) + 5.4

st.title("사회적 피로도 계산기")
st.write("대화 시간이 길어질수록 피로도가 어떻게 변하는지 확인해보세요!")

t = st.number_input("대화 시간 t (시간 단위)", min_value=0.0)
st.write("예상 피로도:", fatigue(t))

