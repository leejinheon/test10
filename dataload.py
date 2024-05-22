# app.py
import streamlit as st
import random

# 함수 정의
def get_computer_choice():
    return random.choice(["묵", "찌", "빠"])

def determine_winner(player, computer, turn):
    if player == computer:
        return "승리" if turn == "player" else "패배"
    if (player == "묵" and computer == "빠") or (player == "찌" and computer == "묵") or (player == "빠" and computer == "찌"):
        return "승리" if turn == "player" else "패배"
    return "패배" if turn == "player" else "승리"

# Streamlit 앱 설정
st.title("묵찌빠 게임")
st.write("묵찌빠 게임을 시작합니다!")

# 사용자의 선택
user_choice = st.selectbox("묵찌빠 중 하나를 선택하세요", ["묵", "찌", "빠"])

# 상태 초기화
if 'turn' not in st.session_state:
    st.session_state.turn = 'player'
if 'result' not in st.session_state:
    st.session_state.result = None

# 게임 로직
if st.button("결과 확인"):
    computer_choice = get_computer_choice()
    st.write(f"컴퓨터의 선택: {computer_choice}")
    
    if st.session_state.turn == 'player':
        result = determine_winner(user_choice, computer_choice, st.session_state.turn)
        st.write(f"결과: {result}")
        if result == "승리":
            st.write("당신이 이겼습니다!")
            st.session_state.turn = 'computer'
        else:
            st.write("당신이 졌습니다. 컴퓨터가 다음 턴을 가져갑니다.")
            st.session_state.turn = 'computer'
    else:
        result = determine_winner(computer_choice, user_choice, st.session_state.turn)
        st.write(f"결과: {result}")
        if result == "승리":
            st.write("컴퓨터가 이겼습니다!")
            st.session_state.turn = 'player'
        else:
            st.write("컴퓨터가 졌습니다. 당신이 다음 턴을 가져갑니다.")
            st.session_state.turn = 'player'

    st.session_state.result = result

# 상태 리셋 버튼
if st.button("게임 리셋"):
    st.session_state.turn = 'player'
    st.session_state.result = None
    st.write("게임이 리셋되었습니다.")

# Streamlit 앱 실행
if __name__ == "__main__":
    st.run()
