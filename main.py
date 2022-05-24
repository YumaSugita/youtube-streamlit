import streamlit as st
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i + 1)
	time.sleep(0.01)

'Done!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('発射！')
if button:
	st.balloons()
	

text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの調子は？', 1, 5, 3)

'あなたの趣味：', text
'コンディション：', condition

if condition == 5:
	food = st.radio(
		"いま食べたいのは？",
		('肉','魚','ラーメン')
	)

	if food == '肉':
		'今日は焼肉！'
	elif food == '魚':
		'寿司行こう'
	elif food == 'ラーメン':
		'もちろんとんこつだよね？'
	

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')