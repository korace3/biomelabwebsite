import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from config import setup_page

# 페이지 설정
setup_page()

st.title("🔬 마이크로바이옴 다양성 분석")

with st.container():
    # 다양성 비교 차트
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    diversity_data = pd.DataFrame({
        '분류': ['건강군', '당신', '위험군'],
        '다양성 지수': [211, 127, 82],
        '상태': ['양호', '주의', '위험']
    })

    fig = px.bar(diversity_data, 
                 x='분류', 
                 y='다양성 지수',
                 color='분류',
                 color_discrete_map={
                     '건강군': '#2ecc71',
                     '당신': '#3498db',
                     '위험군': '#e74c3c'
                 },
                 title='마이크로바이옴 다양성 비교')

    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 상세 분석 결과
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📊 다양성 분석 결과")
        st.markdown("""
            #### 현재 상태: 중간 수준의 다양성
            - 건강군 대비: -84종
            - 연령대 평균 대비: +15종
            - 전년 대비: +5종
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("💡 개선 방안")
        st.markdown("""
            #### 권장 사항
            1. 식이섬유가 풍부한 식품 섭취
            2. 발효식품 섭취 증가
            3. 프리바이오틱스 섭취
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # 시계열 트렌드
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("📈 다양성 변화 추이")
    
    # 시계열 데이터 생성
    dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
    trend_data = pd.DataFrame({
        '날짜': dates,
        '다양성 지수': np.random.normal(127, 10, 12)
    })

    trend_fig = px.line(trend_data, 
                       x='날짜', 
                       y='다양성 지수',
                       title='최근 12개월 다양성 변화')
    
    trend_fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(trend_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)