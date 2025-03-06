import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph,MessagesState,START
from langgraph.checkpoint.memory import MemorySaver

#load the mistral ai API key
load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("LANG_MISTRAL_API_START")

#get the model related info from https://python.langchain.com/docs/integrations/chat/
model = init_chat_model("mistral-large-latest", model_provider="mistralai")

#create a graph
workflow = StateGraph(MessagesState)


def call_model(state : MessagesState):
    # print("***********************************************")
    # print(type(state));print(state);print(state['messages'])
    ai_mesg = model.invoke(state['messages'])
    # print("OUTPUT")
    # print(type(ai_mesg));print(ai_mesg)
    # print("*************************************************")
    return {'messages':ai_mesg}

workflow.add_node("model_run",call_model) #add node to the graph
workflow.add_edge(START,"model_run") #add an edge

memoery = MemorySaver() #to persit information from one state to next

app = workflow.compile(memoery)


#to run the chatbot
def chatbot(chat_id : int):
    print("the chat id is ",chat_id)
    chat = {
        'configurable':
        {
        'thread_id':chat_id
        }
    }

    while True:
        user_input = input("User : ")
        
        if user_input in ["quit","exit"] :
            print("AI : Goodbye!!!")
            break
        else:
            
            output  = app.invoke({'messages':user_input},chat)
            print("AI : ",output['messages'][-1].content)

chatbot(1)


#Credits
#This is the working notes from the course  "https://courses.dataschool.io/view/courses/build-an-ai-chatbot-with-python"
