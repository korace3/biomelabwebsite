import streamlit as st
import plotly.graph_objects as go

def create_progress_bar(value, color="#0066CC"):
    fig = go.Figure()
    
    # 배경 트랙
    fig.add_trace(go.Scatter(
        x=[0, 100],
        y=[0, 0],
        mode='lines',
        line=dict(
            color='#F0F3F9',
            width=10,
        ),
        hoverinfo='skip'
    ))
    
    # 진행 바
    fig.add_trace(go.Scatter(
        x=[0, value],
        y=[0, 0],
        mode='lines',
        line=dict(
            color=color,
            width=10,
        ),
        hoverinfo='skip'
    ))
    
    # 원형 마커
    fig.add_trace(go.Scatter(
        x=[value],
        y=[0],
        mode='markers',
        marker=dict(
            color='white',
            size=16,
            line=dict(
                color=color,
                width=2
            )
        ),
        hoverinfo='skip'
    ))

    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=50,
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
        )
    )
    
    return fig

def show_disease_risk():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap');
    
    .health-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        margin: 12px 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .card-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    .card-icon {
        font-size: 2em;
    }
    
    .card-title {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.2em;
        font-weight: 700;
        color: #1E1E1E;
        margin: 0;
    }
    
    .card-score {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 2.5em;
        font-weight: 700;
        color: #0066CC;
        margin: 16px 0;
    }
    
    .card-status {
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 0.9em;
        color: #666666;
        margin-bottom: 16px;
    }
    
    .details-button {
        width: 100%;
        padding: 8px;
        margin-top: 16px;
        border: 1px solid #E5E5E5;
        border-radius: 8px;
        background: white;
        color: #666666;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 0.9em;
        cursor: pointer;
    }
    
    .stExpander {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("건강 위험도 분석")

    health_metrics = {
        "respiratory": {
            "icon": "🫁",
            "title": "소화기 건강",
            "value": 85,
            "status": "최적",
            "description": "장내 미생물 다양성과 소화 효율성이 매우 양호합니다."
        },
        "immunity": {
            "icon": "🛡️",
            "title": "면역력",
            "value": 72,
            "status": "양호",
            "description": "면역 체계가 안정적으로 작동하고 있습니다."
        },
        "brain": {
            "icon": "🧠",
            "title": "정신 건강",
            "value": 68,
            "status": "주의",
            "description": "스트레스 관리가 필요할 수 있습니다."
        },
        "metabolic": {
            "icon": "⚡",
            "title": "대사 건강",
            "value": 91,
            "status": "최적",
            "description": "에너지 대사가 매우 효율적입니다."
        },
        "heart": {
            "icon": "❤️",
            "title": "심혈관 건강",
            "value": 78,
            "status": "양호",
            "description": "심혈관 건강이 안정적입니다."
        },
        "sleep": {
            "icon": "😴",
            "title": "수면 건강",
            "value": 65,
            "status": "주의",
            "description": "수면의 질 개선이 필요합니다."
        }
    }

    cols = st.columns(2)
    for idx, (key, metric) in enumerate(health_metrics.items()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="health-card">
                <div class="card-header">
                    <span class="card-icon">{metric['icon']}</span>
                    <span class="card-title">{metric['title']}</span>
                </div>
                <div class="card-score">{metric['value']}</div>
                <div class="card-status">{metric['status']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            fig = create_progress_bar(metric['value'])
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("자세히 보기"):
                st.markdown(metric['description'])
                if metric['value'] < 70:
                    st.markdown("""
                    **개선 권장사항**
                    - 생활습관 개선
                    - 정기적인 검사
                    - 전문가 상담
                    """)

if __name__ == "__main__":
    show_disease_risk()