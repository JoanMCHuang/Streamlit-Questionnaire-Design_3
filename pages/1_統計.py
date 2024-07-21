import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from os import path
from sqlalchemy import create_engine



st.markdown("# 統計 🎉")
st.sidebar.markdown("# 統計 🎉")

# 將資料由資料庫取出  
#@st.cache 
def read_data(engine=None):
    if path.exists('data.sqlite'):
        if engine is None:
            engine = create_engine('sqlite:///data.sqlite', echo=False)
        df = pd.read_sql('select * from dinner', engine)
    else:
        df = pd.DataFrame()
    return df


def draw_chart(df):
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 要改為正楷體,否則中文出不來
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.unicode_minus'] = False
    # ax = sns.countplot(x=df['晚餐'], data=df)  # Seaborn 繪圖,要 import seaborn as sns
    # print(df[晚餐].unique(), list(range(df[晚餐].nunique())))
    # ax.set_xticklabels(df[晚餐].unique()) 
    # ax.set_ylim([0, 10])
    # st.pyplot(ax.figure)
    
    # Seaborn & Matplotlib 繪圖參考來源: https://aipin.io/2021/12/09/streamlit-essential-tools-for-data-science/
    st.title('晚餐樣式統計人數')
    st.subheader('Matploblib Chart')
    fig_mp, ax_mpl = plt.subplots()  # 利用 Matplotlib 繪圖 
    ax_mp = plt.hist(df['晚餐'])
    # fig_mp, ax_mpl = plt.subplots()   # 利用 Seaborn 繪圖
    # ax_sb = sns.histplot(df['晚餐'])
    plt.xlabel('Dinner type')
    plt.ylabel('Count')
    st.pyplot(fig_mp)



engine = create_engine('sqlite:///data.sqlite', echo=False)
df2 = read_data(engine)  
engine.dispose()
st.table(df2) #前面先定義 read_data,後面再輸出
draw_chart(df2) #前面先定義 draw_chart,後面再輸出


    