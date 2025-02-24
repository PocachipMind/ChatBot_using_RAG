# ChatBot_using_RAG

RAG를 활용한 ChatBot 구현

배포 두 가지 :
1. Streamlit
2. KakaoTalk

# 시연 영상

# 세부 구현 사항

## 1. 벡터 데이터 베이스 및 LLM

### 벡터 데이터 베이스 
Pinecone : cosine Metric 사용

![image](https://github.com/user-attachments/assets/c5594df6-0bd1-454b-a613-2afa26ecd6d3)

### LLM 

OpenAI gpt 사용 

![image](https://github.com/user-attachments/assets/109c07e9-ff8d-4549-af34-5be3ce1708b7)

토큰의 비용으로 인해 TEST 할 때는 3.5 버전을 사용하였음.

![image](https://github.com/user-attachments/assets/ba5397cc-a865-41a7-ad2f-043994617bb3)


## 2. 참고 자료

나(이성규) 에 대한 정보를 담은 문서로 작성. 이력서를 docx 형식으로 변환하고, 개인적인 취향 등 데이터를 제작함.

![image](https://github.com/user-attachments/assets/c2673781-e8c2-419b-bb29-b03a6eaabd2a)

![image](https://github.com/user-attachments/assets/a73f5b9a-6445-4476-b23e-346359508ce3)

OpenAI는 마크다운의 형식을 사용하므로 docx의 테이블을 이해하지 못하여, 마크다운 형식으로 변환

## 프롬포트

### 유사도 검색을 할 때 사용할 문장 다듬기 

RAG로 활용되는 문서에서 빈번하게 사용될만한 단어를 찾아 정리.

내 데이터의 경우 자주 등장하는 단어나 대체할만한 단어가 없어서 간략히 한 개만 넣어줌.

![image](https://github.com/user-attachments/assets/b186ed06-9d86-4106-9e70-64f712d95bee)

------------------

### 히스토리 관련 공식 문서 프롬포팅 사용.

https://python.langchain.com/v0.2/docs/how_to/qa_chat_history_how_to/#prompt

![image](https://github.com/user-attachments/assets/47c46fe8-031d-4fd3-9aeb-35301b837121)

------------------
### 역할 부여

![image](https://github.com/user-attachments/assets/f7a4e7aa-d35f-40bf-b92f-c4aa8a089ebf)

-------------------
### FewShot 적용

![스크린샷 2025-02-24 143520](https://github.com/user-attachments/assets/6d1d6884-89ba-4d33-9d46-e3dd2f308759)
![스크린샷 2025-02-24 143502](https://github.com/user-attachments/assets/17b1dd69-1727-4ed5-9d4a-c499fac9c05d)

위 이미지와 같이 문서에서 발견하지 못한 내용에도 자꾸 ``내 관찰결과에 따르면`` 아웃풋을 내놓음.

![image](https://github.com/user-attachments/assets/43ce3b14-5a5c-4b80-865a-125b4ba90d0f)

예시 프롬포트를 적용해서 모르는 것에 대해 올바르게 답하도록 조정.

# 깃 설명

- DB : 문서 및 임베딩 관련 코드 기재
- Project :
  - chat_ui.py : Streamlit 관련 실행 코드
  - chat_ui_kakao.py : 카카오 관련 실행 코드
