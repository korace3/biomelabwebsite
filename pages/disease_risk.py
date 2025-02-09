import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 회사 테마 색상 정의
THEME_COLOR = "#0066CC"  # 진한 파란색
BACKGROUND_COLOR = "#1E1E1E"
SECONDARY_COLOR = "#333333"

def create_health_metric(icon, title, value, max_value=100):
    # 현대적인 선형 프로그레스 차트
    fig = go.Figure()
    
    # 배경 라인 (더 두꺼운 선)
    fig.add_shape(
        type="line",
        x0=0, x1=100,
        y0=0, y1=0,
        line=dict(color="#333333", width=12),  # 더 두꺼운 선
        layer="below"
    )
    
    # 값 표시 라인 (더 두꺼운 선)
    fig.add_shape(
        type="line",
        x0=0, x1=value,
        y0=0, y1=0,
        line=dict(color=THEME_COLOR, width=12),  # 테마 색상 적용
        layer="above"
    )
    
    # 마커 (더 큰 크기)
    fig.add_trace(go.Scatter(
        x=[value],
        y=[0],
        mode="markers",
        marker=dict(size=24, color=THEME_COLOR, symbol="circle"),  # 더 큰 마커
        showlegend=False
    ))
    
    fig.update_layout(
        height=100,  # 높이 증가
        margin=dict(l=0, r=0, t=20, b=20),  # 여백 조정
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(range=[-5, 105], showgrid=False, zeroline=False, showline=False, showticklabels=False),
        yaxis=dict(range=[-1, 1], showgrid=False, zeroline=False, showline=False, showticklabels=False),
    )
    
    return fig

def show_disease_risk():
    # 스타일 정의
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
    
    .health-metric {
        background: #1E1E1E;
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        border: 2px solid #333;
        transition: all 0.3s ease;
    }
    
    .health-metric:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0, 102, 204, 0.2);
        border-color: #0066CC;
    }
    
    .metric-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .metric-icon {
        width: 48px;
        height: 48px;
        margin-right: 20px;
        filter: invert(1);
    }
    
    .metric-title {
        color: #FFFFFF;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.4em;
        font-weight: 700;
    }
    
    .metric-value {
        color: #0066CC;
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 15px;
    }
    
    .status-optimal {
        color: #0066CC;
    }
    
    .status-good {
        color: #4D94FF;
    }
    
    .status-warning {
        color: #FFA500;
    }
    
    .divider {
        height: 2px;
        background: #333;
        margin: 40px 0;
    }
    
    .expander-content {
        background: #262626;
        border-radius: 10px;
        padding: 20px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("건강 위험도 분석")

    # 건강 지표 정의
    health_metrics = {
        "digestive": {
            "icon": "🫁",  # 실제로는 SVG 아이콘을 사용
            "title": "소화기 건강",
            "value": 85,
            "status": "optimal",
            "description": "장내 미생물 다양성과 소화 효율성을 나타냅니다."
        },
        "immunity": {
            "icon": "🛡️",
            "title": "면역력",
            "value": 72,
            "status": "good",
            "description": "면역 체계의 강건성과 반응성을 측정합니다."
        },
        "mental": {
            "icon": "🧠",
            "title": "정신 건강",
            "value": 68,
            "status": "warning",
            "description": "뇌-장 축을 통한 정신 건강 상태를 평가합니다."
        },
        "metabolic": {
            "icon": "⚡",
            "title": "대사 건강",
            "value": 91,
            "status": "optimal",
            "description": "에너지 대사와 영양소 흡수 효율을 나타냅니다."
        },
        "cardiovascular": {
            "icon": "❤️",
            "title": "심혈관 건강",
            "value": 78,
            "status": "good",
            "description": "심혈관 시스템의 건강 상태를 평가합니다."
        },
        "sleep": {
            "icon": "😴",
            "title": "수면 건강",
            "value": 65,
            "status": "warning",
            "description": "수면의 질과 관련된 마이크로바이옴 지표를 분석합니다."
        }
    }

    # 2열 레이아웃으로 지표 표시
    col1, col2 = st.columns(2)
    metrics_iter = iter(health_metrics.items())

    for i, (metric_id, metric) in enumerate(metrics_iter):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="health-metric">
                <div class="metric-header">
                    <span class="metric-icon">{metric['icon']}</span>
                    <span class="metric-title">{metric['title']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            fig = create_health_metric(metric['icon'], metric['title'], metric['value'])
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("자세히 보기"):
                st.markdown(f"""
                <div class="expander-content">
                    <p>{metric['description']}</p>
                    <p><strong>현재 상태:</strong> {metric['status'].title()}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if metric['value'] < 70:
                    st.warning("개선이 필요한 영역입니다")
                    st.markdown("""
                    #### 권장 사항
                    • 맞춤형 영양 보충
                    • 생활습관 개선
                    • 정기적 모니터링
                    """)

    # 종합 분석 섹션
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("💡 맞춤형 개선 방안")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 단기 실천 방안
        • 프로바이오틱스 섭취
        • 식이섬유 섭취 증가
        • 스트레스 관리
        """)
    
    with col2:
        st.markdown("""
        #### 장기 관리 계획
        • 정기적인 마이크로바이옴 검사
        • 식단 다양성 확보
        • 운동 습관 형성
        """)

if __name__ == "__main__":
    show_disease_risk() 