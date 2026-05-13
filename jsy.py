import streamlit as st

# 페이지 설정
st.set_page_config(page_title="기분 맞춤 노래 추천", page_icon="🎵")

# 앱 제목 및 설명
st.title("🎵 오늘 당신의 기분은 어떤가요?")
st.write("현재 기분을 선택하시면 딱 맞는 노래를 추천해 드릴게요!")

# 기분별 노래 데이터 (원하는 노래로 수정 가능)
songs = {
    "신나요! (Energetic)": [
        {"title": "Dynamite - BTS", "url": "https://www.youtube.com/watch?v=gdZLi9hzHmM"},
        {"title": "Shake It Off - Taylor Swift", "url": "https://www.youtube.com/watch?v=nfWlot6h_JM"}
    ],
    "우울해요... (Gloomy)": [
        {"title": "밤편지 - 아이유", "url": "https://www.youtube.com/watch?v=BzYnNdJh5TQ"},
        {"title": "Someone Like You - Adele", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"}
    ],
    "차분해지고 싶어요 (Calm)": [
        {"title": "Weightless - Marconi Union", "url": "https://www.youtube.com/watch?v=UfcAVejslrU"},
        {"title": "Lofi Hip Hop Radio", "url": "https://www.youtube.com/watch?v=jfKfPfyJRdk"}
    ],
    "자신감이 필요해요 (Confident)": [
        {"title": "Roar - Katy Perry", "url": "https://www.youtube.com/watch?v=CevxZvSJLk8"},
        {"title": "Believer - Imagine Dragons", "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc"}
    ]
}

# 사이드바 또는 메인 화면에서 기분 선택
mood = st.selectbox("당신의 기분을 알려주세요:", list(songs.keys()))

st.divider()

# 추천 결과 출력
if mood:
    st.subheader(f"✨ '{mood}' 기분에 추천하는 노래")
    
    for song in songs[mood]:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{song['title']}**")
        with col2:
            st.link_button("듣기", song['url'])

# 응원 문구 추가
st.info("음악은 마음의 약이라고 하죠. 오늘 하루도 고생 많으셨어요! ❤️")
