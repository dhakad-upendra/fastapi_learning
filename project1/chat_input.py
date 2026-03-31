from pydantic import BaseModel, Field , computed_field



class Chat_Input(BaseModel):
    model: str = Field(..., description="The model to use for generating the response", examples=['gpt-4o'])
    prompt: str = Field(..., description="The input prompt for the chat", examples=['What is the capital of France?'])