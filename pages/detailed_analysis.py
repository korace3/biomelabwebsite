import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def create_trend_chart():
    # 가상의 시계열 데이터 생성
    dates = pd.date_range(start='2023-01-01', periods=6, freq='M')
    ages = [55 + np.random.randint(-2, 3) for _ in range(6)]
    
    df = pd.DataFrame({
        '측정일': dates,
        '마이크로바이옴 나이': ages
    })
    
    fig = px.line(df, x='측정일', y='마이크로바이옴 나이',
                  title='마이크로바이옴 나이 변화 추이')
    return fig

def detailed_analysis():
    st.title("🔍 상세 분석")
    
    # 트렌드 분석
    st.header("시계열 분석")
    st.plotly_chart(create_trend_chart(), use_container_width=True)
    
    # 박테리아 상세 분석
    st.header("박테리아 상세 분석")
    selected_bacteria = st.selectbox(
        "분석할 박테리아 선택",
        [
            "Prevotella copri", 
            "Streptococcus parasanguinis", 
            "Clostridium phoceensis",
            "Akkermansia muciniphila",
            "Fusobacterium nucleatum",
            "Bifidobacterium bifidum",
            "E. coli",
            "Faecalibacterium prausnitzii"
        ]
    )
    
    # 선택된 박테리아에 대한 상세 정보 표시
    if selected_bacteria:
        col1, col2 = st.columns([2,1])
        
        with col1:
            # 가상의 비교 데이터 생성
            comparison_data = pd.DataFrame({
                '그룹': ['본인', '연령대 평균', '건강군 평균'],
                '수치': [0.8, 0.6, 0.5]
            })
            
            fig = px.bar(comparison_data, x='그룹', y='수치',
                        title=f"{selected_bacteria} 비교 분석")
            st.plotly_chart(fig)
            
        with col2:
            st.info(f"""
            ### 분석 결과
            - 현재 수준: 높음
            - 연령대 평균 대비: +30%
            - 건강군 대비: +60%
            """)
    
    # 맞춤형 가이드
    st.header("맞춤형 개선 가이드")
    with st.expander("영양소 섭취 가이드"):
        st.write("""
        1. 식이섬유: 하루 25-30g
        2. 오메가-3: 하루 1-2g
        3. 폴리페놀: 베리류 섭취
        """)
        
    with st.expander("생활습관 개선"):
        st.write("""
        1. 유산소 운동: 주 3회 이상
        2. 수면: 하루 7-8시간
        3. 스트레스 관리: 명상, 요가 등
        """)

if __name__ == "__main__":
    detailed_analysis() 