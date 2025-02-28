from ctransformers import AutoModelForCausalLM
import chainlit as cl

#variable to store the Orca Model
llm = AutoModelForCausalLM.from_pretrained("zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")

# orca

def get_prompt(instruction: str, history: list[str]) -> str:
    system = "give me helpful answers. you answer in a short and concise way."
    prompt = f"### System:\n{system}\n\n### User:\n"
    if len(history) > 0:
        prompt += f"this is the conversation history: {''.join(history)}. Now answer the question: "
    prompt += f"{instruction}\n\n### Response:\n"
    return prompt


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    prompt = get_prompt(message.content)
    response = ""
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)
        response += word
    
    await msg.update()


@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")

