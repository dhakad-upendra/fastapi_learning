import fastapi
from fastapi.responses import JSONResponse
from test import mock_response
from chat_input import Chat_Input

app = fastapi.FastAPI()

@app.get("/")
def home():
    return JSONResponse(content={"message": "welcome to OverLLM"})



@app.post('/chat')
def chat(chat_input: Chat_Input):

    
    #we should process the chat and generate a response here, but for now we will just return the input
    return JSONResponse(content={"response": mock_response(chat_input.model)})


