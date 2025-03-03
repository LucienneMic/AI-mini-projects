# Using Google Gemini AI to analyze an image and suggest home decor

<details open>
 <summary> :books:General Notes - Click Here</summary>

### How Gemini LLM Works
The Gemini models are powerful AI systems designed to work with both text and images. They excel at tasks that require understanding both kinds of information, like describing images or answering questions based on visual content. The models aim to improve performance across a variety of applications, providing more accurate and efficient solutions compared to earlier AI systems.
For more details, you can check out the full paper here.

### Getting Google Gemini API Access
  https://ai.google.dev/aistudio?pli=1

  Scroll to Get a Gemini API Key - Do not expose publicly

</details>

## :books: Overview

This application processes an image of an empty living room and generates suggestions to improve the home decor. It also suggest pricing range.

## :checkered_flag: Installations

   ```bash

   pip install google-generativeai

   ```

## :computer: Code

1. Create a file called ```imgVision.py```

2. Add the following code:
   
```python

from PIL import Image
import google.generativeai as genai
#import openai

# Configure the API key for gemini AI
genai.configure(api_key="<<INSERT API KEY>>")

# Initialize the model (Make sure the correct model supports image generation)
model = genai.GenerativeModel("gemini-1.5-pro")

#Load image of living room
img = Image.open('livingRoom.jpg')
img.show()
#Generate content with a prompt (describe an image)
response = model.generate_content(["Explain what you see in this room"])
#response = model.generate_content(img)
#print(response.text)
room = response.text

# Generate home decor recommendations based on this image
recommendation_prompt = f"Based on what you see in this: {room}, suggest home decor and explain why and provide and idea of pricing"
recommendation_response = model.generate_content(recommendation_prompt)

# Print the suggested book
print("### Home Decor Recommendation ###")
print(recommendation_response.text)

```
## :rocket: **Test**

In the terminal run ```python3 imgVision.py```


## :link: References

