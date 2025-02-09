import streamlit as st
from config import setup_page

# 페이지 설정
setup_page()

st.title("💪 맞춤형 개선 추천")

with st.container():
    # 현재 상태 선택
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("현재 마이크로바이옴 상태")
    status = st.selectbox(
        "상태 선택",
        ["위험", "주의", "정상"],
        index=0,
    )

    # 상태별 색상 및 아이콘 매핑
    status_info = {
        "위험": {"color": "red", "icon": "🔴"},
        "주의": {"color": "orange", "icon": "🟡"},
        "정상": {"color": "green", "icon": "🟢"}
    }

    st.markdown(f"""
        ### {status_info[status]['icon']} 현재 상태: {status}
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # 주요 개선 필요 사항
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("⚡ 주요 개선 필요 사항")
    
    if status == "위험":
        st.warning("""
            1. 식단 다양성 증가
            2. 발효식품 섭취
            3. 운동량 증가
        """)
    elif status == "주의":
        st.info("""
            1. 식이섬유 섭취 증가
            2. 수분 섭취 증가
            3. 규칙적인 운동
        """)
    else:
        st.success("""
            1. 현재 상태 유지
            2. 정기적인 모니터링
            3. 건강한 생활습관 유지
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # 맞춤형 식단 추천
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("🥗 권장 식품")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            ### 🥬 발효식품
            - 김치
            - 요구르트
            - 콤부차
            - 된장/청국장
        """)
    
    with col2:
        st.markdown("""
            ### 🌾 식이섬유
            - 현미
            - 귀리
            - 견과류
            - 과일/채소
        """)
    
    with col3:
        st.markdown("""
            ### 🧄 프리바이오틱스
            - 마늘
            - 양파
            - 아스파라거스
            - 바나나
        """)
    st.markdown('</div>', unsafe_allow_html=True)

    # 생활습관 개선 방안
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader("✨ 생활습관 개선 방안")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
            ### 일상 생활
            1. 규칙적인 식사 시간 유지
            2. 충분한 수면 (7-8시간)
            3. 스트레스 관리
            4. 적절한 수분 섭취
        """)
    
    with col2:
        st.info("""
            ### 운동 관리
            1. 주 3회 이상 유산소 운동
            2. 가벼운 스트레칭
            3. 규칙적인 걷기
            4. 적절한 운동 강도 유지
        """)
    st.markdown('</div>', unsafe_allow_html=True)