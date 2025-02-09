import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from config import setup_page

# 페이지 설정
setup_page()

st.title("🎯 마이크로바이옴 점수")

# 컨테이너로 내용 감싸기
with st.container():
    # 게이지 차트 컨테이너
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    score = 68
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "마이크로바이옴 건강 점수", 'font': {'size': 24}},
        delta = {'reference': 43, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#ff9999'},
                {'range': [30, 70], 'color': '#99ff99'},
                {'range': [70, 100], 'color': '#9999ff'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 메트릭 컨테이너
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("현재 점수", f"{score}", "+25%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("연령대 평균", "43", "-5%")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("전체 평균", "50", "+18%")
        st.markdown('</div>', unsafe_allow_html=True)

    # 상세 정보 컨테이너
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("마이크로바이옴 상태 분석")
    
    status_color = "🟢" if score > 60 else "🟡" if score > 30 else "🔴"
    st.markdown(f"""
        ### {status_color} 현재 상태: {'양호' if score > 60 else '주의' if score > 30 else '위험'}
        
        #### 주요 지표
        - 장내 미생물 다양성: {score}점
        - 유익균 비율: {round(score * 0.8, 1)}%
        - 면역 관련 지표: {round(score * 0.9, 1)}점
        
        #### 개선 권장사항
        1. 식이섬유가 풍부한 식단 섭취
        2. 발효식품 섭취 증가
        3. 규칙적인 운동 습관
    """)
    st.markdown('</div>', unsafe_allow_html=True)