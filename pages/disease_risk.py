import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_health_metric(icon, title, value, max_value=100):
    # 현대적인 선형 프로그레스 차트
    fig = go.Figure()
    
    # 배경 라인 (더 두꺼운 선)
    fig.add_shape(
        type="line",
        x0=0, x1=100,
        y0=0, y1=0,
        line=dict(color="#2D3436", width=8),
        layer="below"
    )
    
    # 값 표시 라인 (더 두꺼운 선)
    fig.add_shape(
        type="line",
        x0=0, x1=value,
        y0=0, y1=0,
        line=dict(color="#00B894", width=8),
        layer="above"
    )
    
    # 마커 (더 큰 크기)
    fig.add_trace(go.Scatter(
        x=[value],
        y=[0],
        mode="markers",
        marker=dict(size=20, color="#00B894", symbol="circle"),
        showlegend=False
    ))
    
    fig.update_layout(
        height=80,
        margin=dict(l=0, r=0, t=10, b=10),
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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    
    .health-metric {
        background: #1E1E1E;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .health-metric:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .metric-header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .metric-icon {
        width: 40px;
        height: 40px;
        margin-right: 15px;
        filter: invert(1);
    }
    
    .metric-title {
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        font-size: 1.2em;
        font-weight: 500;
    }
    
    .metric-value {
        color: #00B894;
        font-size: 1.5em;
        font-weight: 600;
        margin-top: 10px;
    }
    
    .status-optimal {
        color: #00B894;
    }
    
    .status-warning {
        color: #FDCB6E;
    }
    
    .status-alert {
        color: #FF7675;
    }
    
    .divider {
        height: 1px;
        background: #333;
        margin: 30px 0;
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
                st.markdown(metric['description'])
                st.markdown(f"**현재 상태:** {metric['status'].title()}")
                
                if metric['value'] < 70:
                    st.warning("개선이 필요한 영역입니다")
                    st.markdown("#### 권장 사항")
                    st.markdown("• 맞춤형 영양 보충")
                    st.markdown("• 생활습관 개선")
                    st.markdown("• 정기적 모니터링")

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