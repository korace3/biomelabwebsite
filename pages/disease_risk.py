import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def create_slider_chart(title, value, status="Average"):
    # 현대적인 슬라이더형 차트 생성
    fig = go.Figure()
    
    # 배경 라인
    fig.add_shape(
        type="line",
        x0=0, x1=100,
        y0=0, y1=0,
        line=dict(color="#E5E5E5", width=3),
    )
    
    # 값 표시 라인
    fig.add_shape(
        type="line",
        x0=0, x1=value,
        y0=0, y1=0,
        line=dict(color="#FF6B6B", width=3),
    )
    
    # 마커 추가
    fig.add_trace(go.Scatter(
        x=[value],
        y=[0],
        mode="markers",
        marker=dict(size=15, color="#FF6B6B", symbol="line-ns"),
        showlegend=False
    ))
    
    # 레이아웃 설정
    fig.update_layout(
        height=100,
        margin=dict(l=0, r=0, t=30, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            range=[-5, 105],
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        yaxis=dict(
            range=[-1, 1],
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
    )
    
    return fig

def show_disease_risk():
    st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .metric-container {
        background: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .status-text {
        color: #666;
        font-size: 0.8em;
    }
    .metric-title {
        font-size: 1.2em;
        font-weight: 500;
        margin-bottom: 5px;
    }
    .stMarkdown {
        padding: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("건강 위험도 분석")
    
    metrics = {
        "장 건강 지수": {
            "value": 75,
            "status": "Average",
            "description": "전반적인 장 건강 상태를 나타내는 지표입니다."
        },
        "염증 활성도": {
            "value": 45,
            "status": "Not optimal",
            "description": "체내 염증 반응의 정도를 나타냅니다."
        },
        "대사 기능": {
            "value": 85,
            "status": "Optimal",
            "description": "영양소 대사와 에너지 생산 능력을 나타냅니다."
        },
        "소화 효율": {
            "value": 65,
            "status": "Average",
            "description": "음식물의 소화 및 흡수 효율을 나타냅니다."
        },
        "장벽 건강도": {
            "value": 55,
            "status": "Not optimal",
            "description": "장벽의 무결성과 보호 기능을 나타냅니다."
        }
    }
    
    for metric, data in metrics.items():
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-title">{metric}</div>
            <div class="status-text">{data['status']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig = create_slider_chart(metric, data['value'], data['status'])
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("자세히 보기"):
            st.markdown(data['description'])
            
            if data['value'] < 50:
                st.warning("⚠️ 개선이 필요한 영역입니다.")
                st.markdown("#### 개선 방안")
                st.markdown("- 식단 조절을 통한 개선")
                st.markdown("- 생활습관 개선")
                st.markdown("- 정기적인 모니터링")
            elif data['value'] < 75:
                st.info("ℹ️ 정상이지만 개선의 여지가 있습니다.")
            else:
                st.success("✅ 최적의 상태입니다.")

    # 종합 분석 및 권장사항
    st.markdown("### 💡 맞춤형 개선 방안")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 즉시 실천 가능한 조치
        - 식이섬유가 풍부한 식단
        - 발효식품 섭취 증가
        - 규칙적인 운동
        """)
    
    with col2:
        st.markdown("""
        #### 장기적 관리 방안
        - 정기적인 검사
        - 스트레스 관리
        - 수면 관리
        """)

if __name__ == "__main__":
    show_disease_risk() 