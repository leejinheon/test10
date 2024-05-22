# app.py
import streamlit as st
import random

# 함수 정의
def get_computer_choice(choices):
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "가위" and computer == "보") or \
       (player == "바위" and computer == "가위") or \
       (player == "보" and computer == "바위"):
        return "player"
    return "computer"

# Streamlit 앱 설정
st.title("묵찌빠 게임")
st.write("가위바위보로 선공을 결정합니다.")

# 초기 상태 설정
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
if 'turn' not in st.session_state:
    st.session_state.turn = None
if 'game_result' not in st.session_state:
    st.session_state.game_result = None
if 'player_choice' not in st.session_state:
    st.session_state.player_choice = None
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = None

# 가위바위보 단계
if st.session_state.stage == 'start':
    st.write("가위바위보를 선택하세요.")
    player_choice = st.selectbox("가위, 바위, 보 중 하나를 선택하세요", ["가위", "바위", "보"])
    if st.button("결과 확인"):
        computer_choice = get_computer_choice(["가위", "바위", "보"])
        winner = determine_winner(player_choice, computer_choice)
        
        st.session_state.player_choice = player_choice
        st.session_state.computer_choice = computer_choice
        
        if winner == "draw":
            st.write("비겼습니다. 다시 선택하세요.")
        else:
            st.session_state.turn = winner
            st.session_state.stage = 'muk_jji_bba'
            st.write(f"가위바위보 결과: {'당신이 이겼습니다!' if winner == 'player' else '컴퓨터가 이겼습니다!'}")
            st.write(f"당신의 선택: {player_choice}, 컴퓨터의 선택: {computer_choice}")

# 묵찌빠 단계
if st.session_state.stage == 'muk_jji_bba':
    st.write(f"{'당신의 턴입니다.' if st.session_state.turn == 'player' else '컴퓨터의 턴입니다.'} 묵찌빠 중 하나를 선택하세요.")
    choices = ["묵", "찌", "빠"]
    if st.session_state.turn == 'player':
        player_choice = st.selectbox("묵, 찌, 빠 중 하나를 선택하세요", choices)
        if st.button("묵찌빠 결과 확인"):
            computer_choice = get_computer_choice(choices)
            st.session_state.player_choice = player_choice
            st.session_state.computer_choice = computer_choice
            st.write(f"당신의 선택: {player_choice}, 컴퓨터의 선택: {computer_choice}")
            if player_choice == computer_choice:
                st.session_state.game_result = 'player'
            else:
                st.session_state.turn = 'computer'
    else:
        computer_choice = get_computer_choice(choices)
        st.write(f"컴퓨터의 선택: {computer_choice}")
        player_choice = st.selectbox("묵, 찌, 빠 중 하나를 선택하세요", choices)
        if st.button("묵찌빠 결과 확인"):
            st.session_state.player_choice = player_choice
            st.session_state.computer_choice = computer_choice
            st.write(f"당신의 선택: {player_choice}, 컴퓨터의 선택: {computer_choice}")
            if player_choice == computer_choice:
                st.session_state.game_result = 'computer'
            else:
                st.session_state.turn = 'player'

# 게임 결과 출력
if st.session_state.game_result:
    if st.session_state.game_result == 'player':
        st.write("축하합니다! 당신이 이겼습니다!")
    else:
        st.write("아쉽지만, 컴퓨터가 이겼습니다.")
    if st.button("게임 다시 시작"):
        st.session_state.stage = 'start'
        st.session_state.turn = None
        st.session_state.game_result = None
        st.session_state.player_choice = None
        st.session_state.computer_choice = None

# Streamlit 앱 실행
if __name__ == "__main__":
    st.run()
