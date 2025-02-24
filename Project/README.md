# 프로젝트 코드들

- chat_ui.py : Streamlit 관련 실행 코드
- chat_ui_kakao.py : 카카오 관련 실행 코드

# 실행 방법
### chat_ui.py
1. ``.env`` 파일을 만들고 GPT API 와 Pinecone API 환경 변수를 정의한다.
    ```
    OPENAI_API_KEY = ~~~
    PINECONE_API_KEY = ~~~
    ```
3. ``ChatBot_using_RAG/DB/`` 폴더에 있는 코드와 자료를 통해 Pinecone 에 임베딩을 진행한다. 
4. ``streamlit run chat_ui.py``를 터미널에 입력하여 실행한다.
