import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def calculate_risk_score(microbiome_data):
    # 실제로는 더 복잡한 계산 로직이 들어갈 것입니다
    return np.random.randint(0, 100)

def create_gauge_chart(score, title):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    return fig

def show_disease_risk():
    st.title("🔬 질병 위험도 분석")
    st.markdown("""
    마이크로바이옴 데이터를 기반으로 각종 질병의 위험도를 분석하고 예측합니다.
    """)

    # 전체 위험도 요약
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("주요 질병군 위험도")
        
        diseases = {
            "대사성 질환": {
                "score": calculate_risk_score(None),
                "markers": ["인슐린 저항성", "지방대사 이상", "염증 지표"],
                "description": "당뇨병, 비만 등과 관련된 위험도를 나타냅니다."
            },
            "소화기 질환": {
                "score": calculate_risk_score(None),
                "markers": ["장벽 투과성", "염증성 지표", "면역 반응"],
                "description": "IBD, IBS 등 소화기 질환의 위험도를 나타냅니다."
            },
            "면역 질환": {
                "score": calculate_risk_score(None),
                "markers": ["면역 조절", "알레르기 반응", "자가면역 지표"],
                "description": "알레르기, 자가면역질환 등의 위험도를 나타냅니다."
            },
            "정신건강": {
                "score": calculate_risk_score(None),
                "markers": ["세로토닌 생성", "스트레스 반응", "뇌-장 축"],
                "description": "우울증, 불안장애 등 정신건강 관련 위험도입니다."
            }
        }

    # 각 질병별 상세 분석
    st.subheader("질병별 상세 분석")
    
    for disease, data in diseases.items():
        with st.expander(f"{disease} - 위험도 {data['score']}"):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                fig = create_gauge_chart(data['score'], disease)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.markdown("#### 주요 마이크로바이옴 지표")
                for marker in data['markers']:
                    st.markdown(f"- {marker}")
                
                st.markdown("#### 설명")
                st.markdown(data['description'])
                
                if data['score'] > 70:
                    st.warning("⚠️ 고위험군에 속합니다. 전문의와 상담을 권장합니다.")
                elif data['score'] > 30:
                    st.info("ℹ️ 중간 위험군입니다. 생활습관 개선을 권장합니다.")
                else:
                    st.success("✅ 정상 범위입니다. 현재 상태를 유지하세요.")

    # 개선 권장사항
    st.subheader("💡 맞춤형 개선 방안")
    recommendations = {
        "식이 권장사항": [
            "식이섬유가 풍부한 음식 섭취",
            "프로바이오틱스가 풍부한 발효식품 섭취",
            "항산화 물질이 풍부한 채소와 과일 섭취"
        ],
        "생활습관 개선": [
            "규칙적인 운동",
            "충분한 수면",
            "스트레스 관리"
        ],
        "정기검진": [
            "6개월 주기로 마이크로바이옴 검사 권장",
            "연 1회 이상 건강검진 권장",
            "고위험군의 경우 3개월 주기 검사 권장"
        ]
    }

    for category, items in recommendations.items():
        with st.expander(category):
            for item in items:
                st.markdown(f"- {item}")

if __name__ == "__main__":
    show_disease_risk() 