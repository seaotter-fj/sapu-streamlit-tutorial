import streamlit as st 

st.title('さぷーアプリ')
st.caption('This is a test app in the sapu tutorial.')

st.subheader('self-introduction')
st.text('Pythonに関する情報をYouTubeで発信している、Python VTuber さぷーです。\n'
        'ぜひ、チャンネル登録してね🎵')

code = '''
import streamlit as st
st.title('Sapu app')
# こんな感じで書いていくよ。
'''

st.code(code, language='python')
