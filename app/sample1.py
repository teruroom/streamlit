# https://share.streamlit.io/
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def 折れ線グラフを表示する():
    st.title('折れ線グラフ')
    # データフレームを作成
    df = pd.DataFrame(
        np.random.randn(30, 2),
        columns=['a', 'b']
    )

    # 折れ線グラフを表示
    st.line_chart(df)

    # データフレームを表示
    st.write(df)

def 棒グラフを表示する():
    st.title('棒グラフ')
    # データフレームを作成
    df = pd.DataFrame(
        np.random.randn(30, 2),
        columns=['a', 'b']
    )

    # 棒グラフを表示
    st.bar_chart(df)

def ヒストグラムを表示する():
    st.title('ヒストグラム')
    # 生成数を設定
    n = 500

    # データフレームを作成
    df = pd.DataFrame(
        np.random.randn(int(n), 3),
        columns=['a', 'b', 'c']
    )

    # ヒストグラムを作成
    fig, ax = plt.subplots()
    ax.hist(df)
    ax.set_facecolor("black")
    st.pyplot(fig)

def main():
    折れ線グラフを表示する()
    棒グラフを表示する()
    ヒストグラムを表示する()

main()
