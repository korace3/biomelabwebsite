import streamlit as st
from pathlib import Path

def setup_page():
    # 페이지 기본 설정
    st.set_page_config(
        page_title="BiomeLab - 마이크로바이옴 분석",
        page_icon="🧬",
        layout="wide"
    )
    
    # 로고 이미지 경로
    logo_path = Path(__file__).parent / "assets" / "FullLogo_NoBuffer.png"
    
    # 커스텀 CSS 추가
    st.markdown("""
        <style>
        .main {
            padding: 0rem 1rem;
        }
        .stApp {
            background-color: #f8f9fa;
        }
        .st-emotion-cache-16txtl3 {
            padding: 1rem;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .company-logo {
            width: 150px;
            margin-bottom: 2rem;
        }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # 로고 이미지 표시
    if logo_path.exists():
        st.image(str(logo_path), width=150)