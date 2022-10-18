import streamlit as st
import pandas as pd

st.title('ENGLISH NE high school 1 Hyun kwon Yang etc Word collection')
option = st.sidebar.selectbox(
    'Please select a unit.',
    pd.Series(["unit1", "unit2", "unit3", "unit4", "unit5", "unit6", "unit7", "unit8", ]))

'You choice : ', option

if option == "unit1":
    if st.button("View"):
        st.subheader('act on ~에 따라 행동하다')
        st.subheader('confident 자신감 있는')
        st.subheader('counsel ...에게 조언하다, 권고하다')
        st.subheader('cover up ~을 덮어 가리다, 감추다')
        st.subheader('face ~에 직면하다')
        st.subheader('feel like ~할 마음이 내키다')
        st.subheader('get along with ~와 잘 지내다, ...와 사이가 좋다')
        st.subheader('give ~ a shot ~을 한 번 시도해 보다')
        st.subheader('give ~ consideration ~을 검토하다, 숙고하다, 고려하다')
        st.subheader('involve ~을 참여시키다, 관여시키다')
        st.subheader('keep an eye out for 눈을 똑바로 뜨고 잘 살피다')
        st.subheader('make sure 분명히 ~하도록 하다')
        st.subheader('more than 매우, 정말')
        st.subheader('passion 열정, 격정')
        st.subheader('pay attention to ~에 주의를 기울이다')
        st.subheader('perspective 시각, 관점')
        st.subheader('photography (영화)촬영술')
        st.subheader('poem 시(詩)')
        st.subheader('poet 시인')
        st.subheader('psychologist 심리학자')
        st.subheader('pure 순수한')
        st.subheader('reflect on 곰곰이 생각하다, 숙고하다')
        st.subheader('remove ~을 제거하다')
        st.subheader('self-identity 자기 정체성')
        st.subheader('shoot for ~을 겨냥하다, ~을 목표로 하다')
        st.subheader('sign up for ...에 신청하다[등록하다, 가입하다]')
        st.subheader('since ~이므로, ~때문에')
        st.subheader('sooner or later 조만간, 머지않아')
        st.subheader('specialist 전문가')
        st.subheader('stick one’s toe in the water ~을 시험 삼아 해보다, 잘 하는지 알기 위해 시작하다')
        st.subheader('stick to 고수하다, 끈기 있게 하다')
        st.subheader('stretch ~을 쭉 펴다')
        st.subheader('suffer 더 나빠지다, 악화되다')
        st.subheader('take advantage of ~을 이용하다')
        st.subheader('to be honest 솔직히 말해서, 실은')
        st.subheader('try ~ing (시험 삼아) ...해보다')
        st.subheader('unfamiliar 낯선, 생소한')
        st.subheader('unique 유일한, 특유한')
        st.subheader('value ~를 중요하게 여기다, ~을 높이 평가하다, ~을 존중하다')
        st.subheader('wing 날개')
        st.subheader('yet 그런데도, 그렇지만')
if option == "unit2":
    if st.button("View"):
        st.subheader('단어2 : 단어뜻2')
if option == "unit3":
    if st.button("View"):
        st.subheader('단어3 : 단어뜻3')
if option == "unit4":
    if st.button("View"):
        st.subheader('단어4 : 단어뜻4')
if option == "unit5":
    if st.button("View"):
        st.subheader('단어5 : 단어뜻5')
if option == "unit6":
    if st.button("View"):
        st.subheader('단어6 : 단어뜻6')
if option == "unit7":
    if st.button("View"):
        st.subheader('단어7 : 단어뜻7')
if option == "unit8":
    if st.button("View"):
        st.subheader('단어8 : 단어뜻8')
