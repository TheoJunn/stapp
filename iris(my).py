import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 헤더 설정
_, col, _ = st.columns([2,6,2])
col.header('Streamlit 시각화')


'' #한칸 띄우기

# iris 데이터 불러오기
dfIris = sns.load_dataset('iris')
colors = {'setosa':'red', 'virginica' : 'green', 'versicolor':'blue'}


# 사이드바의 타이틀을 지정해주기
cherry_blossom_emoji = "\U0001F338"

st.sidebar.title(f"Iris Species {cherry_blossom_emoji}")

# 사이드 바 만들기
with st.sidebar:
    selectX = st.selectbox("X 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectY = st.selectbox("Y 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectSpecies = st.multiselect('붓꽃 유형 선택 (:blue[다중]):', ['setosa', 'versicolor', 'virginica'])
    ''
    #투명도 선택 가능
    selectAlpha = st.slider('alpha 설정:', 0.1, 1.0, 0.5)

# 유형별 산점도 시각화 표현
if selectSpecies:
    fig = plt.figure(figsize = (7,5))
    for aSpecies in selectSpecies:
        df = dfIris[dfIris.species == aSpecies]
        plt.scatter(df[selectX], df[selectY],
                    color = colors[aSpecies], alpha=selectAlpha, label=aSpecies)
    plt.legend(loc='lower right')
    plt.xlabel(selectX) 
    plt.ylabel(selectY)
    plt.title('Iris Scatter Plot')
    st.pyplot(fig)
else:
    st.warning('붓꽃의 유형을 선택해 주세요!!!:pig2:')

