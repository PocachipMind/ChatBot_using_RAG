import streamlit as st
from llm import get_ai_response


st.set_page_config(page_title="이성규 스토커", page_icon="🥷")

st.title("🥷 이성규 스토커")
st.caption("매일 관찰한다고 하네요!")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_question := st.chat_input(placeholder="궁금한게 있으면 물어보세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("🕵️스토커가 자료를 찾아보는 중.."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})