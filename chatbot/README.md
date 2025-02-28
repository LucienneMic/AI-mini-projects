# :robot: AI Chatbot using Orca Model & Chainlit :robot: 

## :books: Overview
This chatbot uses ```ctransformers``` to load the Orca Mini 3B language model and ``` chainlit``` to create a chatbot UI. It streams AI responses in real time.

```ctransformers``` is used to load and interact with the Orca language model.
```chainlit``` is a lightweight Python library for building chatbot UIs.

Model built with 

## :checkered_flag: Installation

1. Install dependencies

   ```bash

   pip install ctransformers chainlit

   ```

2. Create a file called ```chatbot.py```


## :computer: Code

```python

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

```
## :gear: **Code Explanation** 
<details>
<summary>  Click to expand **Code Explanation**</summary>


*Loading the AI Model*
```python
llm = AutoModelForCausalLM.from_pretrained(
    "zoltanctoth/orca_mini_3B-GGUF", 
    model_file="orca-mini-3b.q4_0.gguf"
)
```

```AutoModelForCausalLM.from_pretrained(...)```: Loads the Orca Mini 3B model from Hugging Face.

```"zoltanctoth/orca_mini_3B-GGUF"```: Refers to the model repository.

```model_file="orca-mini-3b.q4_0.gguf"```: Specifies the exact model file for inference.

----
*Generating a Prompt for the AI*

```python
def get_prompt(instruction: str, history: list[str]) -> str:
    system = "give me helpful answers. you answer in a short and concise way."
    prompt = f"### System:\n{system}\n\n### User:\n"
```
The function formats a prompt to provide better AI responses.
system: Defines AI behavior, instructing it to be concise.

```python

    if len(history) > 0:
        prompt += f"this is the conversation history: {''.join(history)}. Now answer the question: "
```

If there is chat history, it is included in the prompt for better contextual understanding.

```python

    prompt += f"{instruction}\n\n### Response:\n"
    return prompt
```
The user's question (instruction) is added to the prompt.
The function returns the final prompt to be sent to the model.

----
*Handling User Messages*

```python
@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()
```

@cl.on_message: This function is triggered when a user sends a message.
msg = cl.Message(content=""): Initializes an empty message.
await msg.send(): Sends the message to update the UI.

---

*Generating and Streaming AI Response*

```python
    prompt = get_prompt(message.content)
    response = ""
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)
        response += word
```
Calls get_prompt(message.content) to format the prompt.
llm(prompt, stream=True): Sends the prompt to the Orca model and streams the response word-by-word.
await msg.stream_token(word): Streams each word to the UI in real-time.
response += word: Builds the response as words arrive.

---
*Final UI Update*

```python
    await msg.update()
```
Finalizes and updates the UI with the complete response.

---
*Handling Chat Session Start*
```python
@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")
```

@cl.on_chat_start: Runs when a new chat session begins.
Prints "A new chat session has started!" to indicate a fresh conversation.

---
</details>

## :rocket: Run the chatbot!

In the terminal run:
```bash
chainlit run chatbot.py
```

Open your browser and go to ```http://localhost:8000```
Start chatting! 🚀

## :hammer_and_wrench: Customizations

Modify the AI instructions in ```get_prompt()``` for different behaviors.

Change ```stream=True to False``` if you want instant responses instead of streaming.

## :link: References

Chainlit Docs: https://docs.chainlit.io

Orca Model: https://huggingface.co/TheBloke/orca_mini_3B-GGUF

