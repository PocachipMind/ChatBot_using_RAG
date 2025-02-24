# 프로젝트 코드들

- chat_ui.py : Streamlit 관련 실행 코드
- chat_ui_kakao.py : 카카오 관련 실행 코드

# 실행 방법
### chat_ui.py : Streamlit
1. ``.env`` 파일을 만들고 GPT API 와 Pinecone API 환경 변수를 정의합니다.
    ```
    OPENAI_API_KEY = ~~~
    PINECONE_API_KEY = ~~~
    ```
3. ``ChatBot_using_RAG/DB/`` 폴더에 있는 코드와 자료를 통해 Pinecone 에 임베딩을 진행합니다. 
4. ``streamlit run chat_ui.py``를 터미널에 입력하여 실행합니다.
### chat_ui_kakao.py : 카카오톡
해당 코드를 통해 카카오톡 챗봇을 구현하려면 **카카오톡 채널관리자** API와 채널 등록등 복잡합니다.

1. ``카카오톡 채널관리자``에 회원가입을 하고 비즈니스 관리자 센터에 들어가 채널을 생성합니다.
2. 채널을 만들고 나면 채널 공개와 검색 허용을 On으로 해줍니다.

   ![image](https://github.com/user-attachments/assets/13703700-f33e-4d93-a19b-2adfa81e8136)

3. 채널 URL을 복사하고 기록해 둡니다.

   ![image](https://github.com/user-attachments/assets/5d0a9b6e-00ec-4925-8425-d0b3515fc771)

4. 챗봇 관리자 채널에 가서 챗봇을 만듭니다.

   ![image](https://github.com/user-attachments/assets/7da842d9-7163-40c8-a181-6b65abfd27bf)

5. 

1. ``ngrok`` 에 가입하고 설치를 합니다.
2. ngrok API 토큰을 발급 받고 ngrok터미널을 연 뒤 ``ngrok authtoken <Your token>``을 통해 토큰 설정을 완료합니다.
3. ``uvicorn chat_ui_kakao:app --reload`` 명령어를 통해 
4. ``ngrok http 8000``
