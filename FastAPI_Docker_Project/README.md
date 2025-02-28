# Build an AI app with FastAPI and Docker  

<details open>
 <summary> :books:General Notes - Click Here</summary>

### What is FastAPI?

FastAPI is a popular web framework for building APIs with Python, based on standard Python type hints. It is intuitive and easy to use, and it can provide a production-ready application in a short period of time. It is fully compatible with OpenAPI and JSON Schema.
https://fastapi.tiangolo.com/

### What is HuggingFace?

Hugging Face is a company that develops tools for natural language processing (NLP) and machine learning. It’s known for its open-source libraries, which provides pre-trained models for tasks like text classification, translation, and question answering. For this example we will be using: "dandelin/vilt-b32-finetuned-vqa" 

"dandelin/vilt-b32-finetuned-vqa" is a Vision-and-Language Transformer (ViLT) fine-tuned on the VQAv2 dataset for Visual Question Answering (VQA). It processes both images and text to answer questions about the content of images

This example makes use of 
https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

### What is Docker?

Docker is a tool that packages an app and everything it needs (like code, libraries, and settings) into a container. This container can run anywhere, making it easier to move the app between computers without worrying about compatibility issues.
https://www.docker.com/

</details>

## :books: Overview

This application builds a Visual Questioning Model API using ```FastAPI``` and the ```VILT``` model. It processes image inputs to generate answers using a pre-trained transformer model. The example in this case is having an image with various fruit and the question is to ask how many fruits there are the model will count objects on the image and returns an answer.

Docker was used to containerize and deploy the application for consistent and scalable deployment.

## :checkered_flag: Installations

### Docker
1. If docker is not installed - use this link
https://docs.docker.com/desktop/setup/install/mac-install/#install-interactively

2. Open http://localhost:8088/ to make sure that docker was correctly installed

### Dependencies

   PyTorch - https://pytorch.org/get-started/locally/

   FastAPI - https://fastapi.tiangolo.com/
   
   ```bash

   pip install transformers

   ```

## :computer: Code

1. Create a file called ```main.py```

2. Add the following code:
   
```python

from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Test"}
```
## :rocket: **Test**

In the terminal run ```fastapi dev main.app```

Open your browser and go to ```http://127.0.0.1:8000/``` and you should be able to see the output in this case
{"Hello”:”World”}


## :computer: Code a model

1. Create a file called ```model.py```

2. Add the following code:

```python
rom transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image

# 470MB
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def model_pipeline(text: str, image: Image):

    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]
    

```
3. Update ```main.py```

```python
from model import model_pipeline
from fastapi import FastAPI, UploadFile
from typing import Union
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()

    image = Image.open(io.BytesIO(content))
    
    result = model_pipeline(text, image)
    return {"answer": result}
```

## :rocket: Testing the model!

1. Open your browser and go to ``` http://127.0.0.1:8000/docs``` and click on ```Try it out```

2. <img width="400" alt="Screenshot 2025-02-28 at 9 46 50 AM" src="https://github.com/user-attachments/assets/2696256f-7808-4922-aec8-2c3a5d5fcccf" /> <img width="400" alt="Screenshot 2025-02-28 at 9 47 03 AM" src="https://github.com/user-attachments/assets/cf30dcff-4926-422f-8993-377a1bd80f2a" />


## :hammer_and_wrench: Using Docker

1. In the terminal run ```docker init```

2. If successful you should have:

  Start your application by running → docker compose up --build
  Your application will be available at http://localhost:8000

3. Open the DockerFile and add the RustCompiler, to be able to run the Transformers module

```
#### Install Rust compiler
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
```
4. Ready to create an image on Docker

In the terminal run ```docker compose up --build```

5. Open your browser and go to ```localhost:8000/docs```

## :link: References



