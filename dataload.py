# app.py
import streamlit as st
import random

# 함수 정의
def get_computer_choice():
    return random.choice(["가위", "바위", "보"])

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        return "player"
    else:
        return "computer"

def update_score(winner):
    if winner == "player":
        st.session_state.player_wins += 1
    elif winner == "computer":
        st.session_state.computer_wins += 1

def calculate_win_rate():
    total_games = st.session_state.player_wins + st.session_state.computer_wins + st.session_state.draws
    if total_games == 0:
        return 0, 0
    player_win_rate = st.session_state.player_wins / total_games * 100
    computer_win_rate = st.session_state.computer_wins / total_games * 100
    return player_win_rate, computer_win_rate

# Streamlit 앱 설정
st.title("가위바위보 게임")
st.write("가위, 바위, 보 중 하나를 선택하세요.")

# 초기 상태 설정
if 'player_wins' not in st.session_state:
    st.session_state.player_wins = 0
if 'computer_wins' not in st.session_state:
    st.session_state.computer_wins = 0
if 'draws' not in st.session_state:
    st.session_state.draws = 0
if 'game_history' not in st.session_state:
    st.session_state.game_history = []

# 사용자의 선택
user_choice = st.selectbox("가위, 바위, 보 중 하나를 선택하세요", ["가위", "바위", "보"])

if st.button("결과 확인"):
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "draw":
        st.session_state.draws += 1
    else:
        update_score(winner)
    
    st.session_state.game_history.append({
        "user": user_choice,
        "computer": computer_choice,
        "result": winner
    })

    st.write(f"당신의 선택: {user_choice}")
    st.write(f"컴퓨터의 선택: {computer_choice}")
    if winner == "draw":
        st.write("비겼습니다!")
    elif winner == "player":
        st.write("당신이 이겼습니다!")
    else:
        st.write("컴퓨터가 이겼습니다!")

    player_win_rate, computer_win_rate = calculate_win_rate()
    st.write(f"사용자의 승률: {player_win_rate:.2f}%")
    st.write(f"컴퓨터의 승률: {computer_win_rate:.2f}%")

    st.write("경기 기록:")
    for idx, game in enumerate(st.session_state.game_history, 1):
        st.write(f"게임 {idx}: 당신의 선택: {game['user']}, 컴퓨터의 선택: {game['computer']}, 결과: {'비김' if game['result'] == 'draw' else ('당신이 이김' if game['result'] == 'player' else '컴퓨터가 이김')}")

# Streamlit 앱 실행
if __name__ == "__main__":
    st.run()
