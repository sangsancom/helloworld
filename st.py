import streamlit as st
import datetime
from PIL import Image
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="상산고등학교 정보과 안내",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일 적용
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stHeader {
        color: #2E4053;
    }
    </style>
    """, unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.title("📚 메뉴")
    page = st.radio("이동할 섹션", ["홈", "프로그래밍 학습", "SW 동행프로젝트", "전북 SW 캠프"])
    
    st.markdown("---")
    st.markdown("### 📞 문의하기")
    st.info("문의사항이 있으시면 담당 선생님께 연락주세요!")

# 메인 컨텐츠
if page == "홈":
    st.title("🎓 상산고등학교 정보과 안내")
    st.markdown("### 안녕하세요! 상산고등학교 정보과에 오신 것을 환영합니다.")
    
    # 현재 날짜 표시
    today = datetime.datetime.now()
    st.info(f"📅 오늘 날짜: {today.strftime('%Y년 %m월 %d일')}")

elif page == "프로그래밍 학습":
    st.header("1. 프로그래밍 학습 법 사이트")
    
    # 프로그래밍 학습 사이트 카드
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 📖 점프 투 파이썬
        - **링크**: [바로가기](https://wikidocs.net/book/1)
        - **난이도**: ⭐⭐⭐
        - **추천 대상**: 파이썬 입문자
        """)
    with col2:
        st.markdown("""
        ### 💡 학습 가이드
        - 파이썬 기초부터 심화까지 단계별 학습
        - 실습 예제와 함께하는 체계적인 커리큘럼
        - 무료로 제공되는 풍부한 학습 자료
        """)

elif page == "SW 동행프로젝트":
    st.header("2. SW 동행프로젝트 일정")
    
    # 프로젝트 일정 데이터프레임
    projects = pd.DataFrame({
        '프로젝트명': ['AI와 함께하는 우리 동네 교통신호 최적화', '양평 블룸비스타 호텔 해커톤', 
                  '서울대 글로벌 공학교육센터 컨벤션 캠프', '로보틱스 과제 수행'],
        '기간': ['5월 19일~5월 22일', '7월 30일~7월 31일', '8월 12일', '9월 15일부터'],
        '위치': ['온라인', '양평 블룸비스타 호텔', '서울대 글로벌 공학교육센터', '온라인']
    })
    
    st.dataframe(projects, use_container_width=True)
    
    # 프로젝트 선택
    selected_project = st.selectbox("자세히 알아보기", projects['프로젝트명'])
    if selected_project:
        st.info(f"선택한 프로젝트: {selected_project}")
        st.markdown(f"**기간**: {projects[projects['프로젝트명'] == selected_project]['기간'].iloc[0]}")
        st.markdown(f"**위치**: {projects[projects['프로젝트명'] == selected_project]['위치'].iloc[0]}")

elif page == "전북 SW 캠프":
    st.header("3. 전북 SW 캠프 일정")
    
    # 캠프 일정 타임라인
    st.markdown("""
    ### 📅 캠프 일정 타임라인
    """)
    
    timeline = pd.DataFrame({
        '단계': ['온라인 사전교육', '코딩캠프', '사후 교육'],
        '날짜': ['7월 6일 14:00~18:00', '7월 19일 토요일', '8월, 9월 (추후 공지)'],
        '상태': ['예정', '예정', '예정']
    })
    
    st.dataframe(timeline, use_container_width=True)
    
    # 캠프 참가 신청 버튼
    if st.button("캠프 참가 신청하기"):
        st.success("신청이 완료되었습니다! 담당 선생님께서 확인 후 연락드리겠습니다.")
