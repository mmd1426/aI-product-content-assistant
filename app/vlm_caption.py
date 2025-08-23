import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

IMAGE_PATH = ""

VLM_MODEL_API_KEY = os.getenv("VLM_MODEL_API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=VLM_MODEL_API_KEY,
)

PRODUCT_ANALYSIS_PROMPT = """
Please carefully analyze this product image and write a comprehensive and detailed description (description) for it that includes the following:

**Product Physical Specifications:**
- Product type and category
- Color, shape and size
- Material and raw materials
- Design details and appearance

**Technical and Functional Features:**
- Application and how to use
- Special advantages and capabilities
- Build quality and durability

**Target Audience:**
- Who is it suitable for
- In what conditions it is used

**Important Points:**
- Product strengths
- Precautions in use
- Comparison with similar products

Please write the descriptions in a coherent, attractive and understandable way for customers. Use descriptive and attractive sentences.

IMPORTANT: Please respond in Persian (Farsi) language.
"""



def product_description(base64_image):
  completion = client.chat.completions.create(
    model="qwen/qwen-2.5-vl-7b-instruct",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": PRODUCT_ANALYSIS_PROMPT
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],temperature=0.3
  )

  return completion.choices[0].message.content