from langgraph.graph import StateGraph, state
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, List, Literal
from datetime import datetime
import requests


# =====================
# 1. State definition
# =====================

class ChatState(TypedDict):
    messages: List


# =====================
# 2. LLM setup
# =====================

llm = ChatOllama(model="mistral")


# =====================
# 3. Internet tools
# =====================

def get_current_time() -> str:
    now = datetime.now()
    return f"Sekarang jam {now.strftime('%H:%M:%S')} pada tanggal {now.strftime('%A, %d %B %Y')}."

def get_weather(city: str = "Jakarta") -> str:
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Cuaca di {city}: {response.text}"
        else:
            return f"Tidak bisa mengambil data cuaca untuk {city}. Coba lagi nanti."
    except Exception as e:
        return f"Gagal mengambil data cuaca: {str(e)}"


# =====================
# 4. LangGraph node
# =====================

def call_llm(state: ChatState) -> ChatState:
    user_input = state["messages"][-1].content.lower()

    # Deteksi waktu
    if any(kw in user_input for kw in ["jam berapa", "sekarang hari apa", "tanggal berapa"]):
        response = get_current_time()
        return {"messages": state["messages"] + [AIMessage(content=response)]}

    # Deteksi cuaca
    if "cuaca" in user_input:
        response = get_weather()
        return {"messages": state["messages"] + [AIMessage(content=response)]}

    # Jawaban biasa dari LLM lokal
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}


# =====================
# 5. LangGraph structure
# =====================

def should_end(_: ChatState) -> Literal["end"]:
    return "end"

graph_builder = StateGraph(ChatState)
graph_builder.add_node("llm_node", call_llm)
graph_builder.add_node("end", lambda state: state)
graph_builder.set_entry_point("llm_node")
graph_builder.set_finish_point("end")
graph_builder.add_conditional_edges("llm_node", should_end)

chat_graph = graph_builder.compile()


# =====================
# 6. CLI Chat
# =====================

print("🤖 Chatbot LangGraph + Ollama aktif. Ketik 'exit' untuk keluar.\n")

messages = []

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        break

    messages.append(HumanMessage(content=user_input))
    state = {"messages": messages}
    result = chat_graph.invoke(state)
    messages = result["messages"]
    print(f"Bot: {messages[-1].content}\n")
