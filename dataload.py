import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go

st.title('가위바위보 게임')

# 사용자와 컴퓨터가 선택할 수 있는 옵션
choices = ['가위', '바위', '보']

# 게임 결과 저장을 위한 데이터프레임 초기화
if 'results' not in st.session_state:
    st.session_state['results'] = pd.DataFrame(columns=['user', 'computer', 'result'])

# 승패 결정 함수
def determine_winner(player, computer):
    if player == computer:
        return '비김'
    elif (player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위'):
        return '사용자 승리'
    else:
        return '컴퓨터 승리'

st.subheader('가위바위보 게임을 시작해보세요!')

# 사용자가 선택할 수 있는 버튼 추가
player_choice = st.radio("당신의 선택은?", choices)

# 컴퓨터의 선택은 무작위로 결정
if st.button('결과 확인'):
    computer_choice = random.choice(choices)
    st.write(f'컴퓨터의 선택: {computer_choice}')
    result = determine_winner(player_choice, computer_choice)
    st.write(f'결과: {result}')

    # 결과를 데이터프레임에 저장
    new_result = pd.DataFrame([[player_choice, computer_choice, result]], columns=['user', 'computer', 'result'])
    st.session_state['results'] = pd.concat([st.session_state['results'], new_result], ignore_index=True)

# 게임 결과 시각화
if not st.session_state['results'].empty:
    st.subheader('게임 결과 통계')

    # 전체 결과 데이터프레임 출력
    st.write(st.session_state['results'])

    # 결과 통계 시각화
    result_counts = st.session_state['results']['result'].value_counts().reset_index()
    user_choice_counts = st.session_state['results']['user'].value_counts().reset_index()
    computer_choice_counts = st.session_state['results']['computer'].value_counts().reset_index()

    result_counts.columns = ['result', 'count']
    user_choice_counts.columns = ['user', 'count']
    computer_choice_counts.columns = ['computer', 'count']

    def plot_pie(data, names, values, title):
        fig = go.Figure(data=[go.Pie(labels=data[names], values=data[values])])
        fig.update_layout(title=title, margin=dict(l=20, r=20, t=40, b=20))
        return fig

    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(plot_pie(result_counts, 'result', 'count', '게임 결과'), use_container_width=True)

    with col2:
        st.plotly_chart(plot_pie(user_choice_counts, 'user', 'count', '사용자 선택 통계'), use_container_width=True)

    with col3:
        st.plotly_chart(plot_pie(computer_choice_counts, 'computer', 'count', '컴퓨터 선택 통계'), use_container_width=True)
