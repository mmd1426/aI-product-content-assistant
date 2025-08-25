import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL_API_KEY = os.getenv("LLM_MODEL_API_KEY")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=LLM_MODEL_API_KEY,
)


def generate_marketing_content(product_description):

    system_prompt = """
You are a marketing assistant for an Iranian online marketplace. Given the product details in JSON, generate the following in **Persian (Farsi) only**:

- product_name: Write a 1-sentence engaging product name in Persian.  
- description: Write a 3–4 sentence engaging, storytelling-style product description in **Persian (Farsi) only**. Make it natural, smooth, and appealing. Highlight the product’s unique taste, aroma, color, or texture first, then mention its health benefits or practical uses. Use sensory words so the reader can imagine the experience of using the product. The tone should be warm, flowing, and persuasive, similar to high-quality honey marketing texts.  
- category: Suggest the two most suitable categories for the product.  
- hashtags: Provide 1-3 relevant Persian hashtags. Each hashtag should represent a **single concept** (e.g., #عسل_طبیعی, #سلامتی, #تقویت_سیستم_ایمنی). Use underscore `_` instead of spaces and avoid combining چند مفهوم در یک هشتگ.
    """

    user_prompt = f"""

Input Text:

Product Description: {product_description}

Output Format (JSON only):
{{
  "product_name": "...",
  "description": "...",
  "category": ["...", "..."],
  "hashtags": ["...", "..."]
}}

    """



    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct:nebius",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                'role': 'user',
                'content': user_prompt
            }
        ],
        temperature=0.5,
        max_tokens=1000
    )

    return completion.choices[0].message.content