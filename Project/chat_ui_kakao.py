###### 기본 정보 설정 단계 #######
from fastapi import Request, FastAPI
import threading
import time
import queue as q
from llm import get_ai_message


###### 기능 구현 단계 #######

# 메세지 전송 : 모델 값을 카카오톡 json 포멧 맞게 하기
def textResponseFormat(bot_response):
    response = {'version': '2.0', 'template': {
    'outputs': [{"simpleText": {"text": bot_response}}], 'quickReplies': []}}
    return response

# 응답 초과시 답변
def timeover():
    response = {"version":"2.0","template":{
      "outputs":[
         {
            "simpleText":{
               "text":"🕵️제가 스토킹하며 기록한 문서 좀 둘러보겠습니다.\n 👇 조금 있다 호출해주세요."
            }
         }
      ],
      "quickReplies":[
         {
            "action":"message",
            "label":"문서 다 보셨나요?🙋",
            "messageText":"문서 다 보셨나요?🙋"
         }]}}
    return response

######## 서버 생성 #########
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "kakaoTest"}

@app.post("/chat/")
async def chat(request: Request):
    kakaorequest = await request.json() # 카카오톡 서버가 보낸 리퀘스트 메세지를 JSON으로
    return mainChat(kakaorequest)

######## 메인 함수 #########

response = []

# 메인 함수
def mainChat(kakaorequest):

    global response
    
    start_time = time.time()   

    # 답변 생성 함수 실행
    request_respond = threading.Thread(target=responseModel,
                                        args=( kakaorequest, ))
    
    request_respond.start()

    # 답변 생성 시간 체크
    while (time.time() - start_time < 4 ):
        if response :
            # 4 초 안에 답변이 완성되면 바로 값 리턴
            temp = response[0]
            response.clear()
            return temp
        # 안정적인 구동을 위한 딜레이 타임 설정
        time.sleep(0.01)

    # 4 초 내 답변이 생성되지 않을 경우
    if not response:     
        return timeover()


# 답변 생성 함수
def responseModel( request ):
    global response
    if not response:
        prompt = request["userRequest"]["utterance"]
        bot_res = get_ai_message(prompt)
        response.append(textResponseFormat(bot_res))
        print(bot_res)

    