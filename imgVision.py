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