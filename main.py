# from dotenv import load_dotenv

# load_dotenv()

from langchain.llms import OpenAI, CTransformers
from langchain.chat_models import ChatOpenAI
import streamlit as st


# llm = OpenAI()
# result = llm.predict('모니터 아웃소싱을 하는데 있어서 가장 핵심적인 일')

# chat_model = ChatOpenAI()
llm = CTransformers(
    model='llama-2-7b-chat.ggmlv3.q2_K.bin',
    model_type='llama'
)

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = llm.predict('Write a poem about ' + content)
        st.write(result)