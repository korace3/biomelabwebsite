import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from pathlib import Path

# 페이지 기본 설정
st.set_page_config(
    page_title="마이크로바이옴 에이지 분석",
    page_icon="🧬",
    layout="wide"
)

# CSS 스타일 적용
def load_css():
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Noto Sans KR', sans-serif;
        }
        
        .main-gauge {
            text-align: center;
            padding: 2rem;
        }
        
        .status-card {
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .guide-card {
            background: #ffffff;
            padding: 1rem;
            border-radius: 8px;
            margin: 0.5rem 0;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 게이지 차트 생성 함수
def create_age_gauge(microbiome_age, real_age):
    delta = microbiome_age - real_age
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = microbiome_age,
        delta = {"reference": real_age, "valueformat": ".0f"},
        title = {"text": "마이크로바이옴 나이"},
        gauge = {
            "axis": {"range": [None, 100]},
            "bar": {"color": "#4A90E2"},
            "steps": [
                {"range": [0, 40], "color": "#7ED321"},
                {"range": [40, 70], "color": "#F5A623"},
                {"range": [70, 100], "color": "#D0021B"}
            ]
        }
    ))
    
    return fig

def main():
    load_css()
    
    # 사이드바 - 사용자 정보 입력
    with st.sidebar:
        st.header("👤 사용자 정보")
        name = st.text_input("이름", "홍길동")
        real_age = st.slider("실제 나이", 20, 80, 50)
        gender = st.selectbox("성별", ["남성", "여성"])
        
    # 메인 페이지
    st.title("🧬 마이크로바이옴 에이지 분석")
    
    # 시뮬레이션을 위한 가상의 마이크로바이옴 나이
    microbiome_age = real_age + np.random.randint(-5, 15)
    
    # 게이지 차트
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.plotly_chart(create_age_gauge(microbiome_age, real_age), use_container_width=True)
    
    # 상태 표시
    delta_age = microbiome_age - real_age
    if delta_age > 10:
        st.error("⚠️ 위험: 마이크로바이옴 나이가 실제 나이보다 10세 이상 높습니다.")
    elif delta_age > 5:
        st.warning("⚠️ 주의: 마이크로바이옴 나이가 실제 나이보다 다소 높습니다.")
    else:
        st.success("✅ 정상: 마이크로바이옴 나이가 양호한 상태입니다.")
    
    # 박테리아 분석
    st.header("주요 박테리아 분석")
    bacteria_col1, bacteria_col2 = st.columns(2)
    
    with bacteria_col1:
        # 박테리아 비교 차트
        bacteria_data = pd.DataFrame({
            "박테리아": ["Prevotella copri", "Streptococcus para.", "Clostridium pho."],
            "검출량": [np.random.rand(), np.random.rand(), np.random.rand()],
            "기준치": [0.5, 0.6, 0.4]
        })
        
        fig = px.bar(bacteria_data, x="박테리아", y=["검출량", "기준치"],
                    barmode="group",
                    title="주요 박테리아 검출량 비교")
        st.plotly_chart(fig)
    
    # 개선 가이드
    st.header("💡 맞춤형 개선 가이드")
    guide_col1, guide_col2, guide_col3 = st.columns(3)
    
    with guide_col1:
        with st.expander("식단 가이드"):
            st.write("""
            - 식이섬유 섭취 증가 (하루 25g 이상)
            - 프리바이오틱스가 풍부한 식품 섭취
            - 가공식품 섭취 제한
            """)
            
    with guide_col2:
        with st.expander("프로바이오틱스 추천"):
            st.write("""
            - Lactobacillus rhamnosus
            - Bifidobacterium longum
            - 하루 1회 복용 권장
            """)
            
    with guide_col3:
        with st.expander("생활습관 개선"):
            st.write("""
            - 규칙적인 운동 (주 3회 이상)
            - 충분한 수면 (7-8시간)
            - 스트레스 관리
            """)

if __name__ == "__main__":
    main() 