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

    system_prompt = """You are an expert Persian (Farsi) marketing content creator specializing in creating compelling, sales-driven product content that converts browsers into buyers. Your mission is to craft irresistible marketing copy that makes customers want to purchase products immediately.

Key requirements:
1. Output must be in Persian (Farsi) language
2. Response must be valid JSON format
3. Include all required fields: product_name, description, category, hashtags
4. Product names should be compelling, benefit-focused, and create urgency in Persian
5. Descriptions should be persuasive, emotionally appealing, and highlight:
   - Key benefits and solutions to customer problems
   - Social proof and exclusivity
   - Limited time offers or scarcity
   - Call-to-action elements
6. Categories should be strategic and marketable
7. Hashtags should be trending, conversion-focused, and include Persian sales hashtags
Always create content that drives sales and customer engagement."""

    user_prompt = f"""Based on the following product description, create compelling, sales-driven marketing content in Persian that will make customers want to buy immediately:

Product Description: {product_description}

Create irresistible marketing copy that includes:
- Emotional triggers and benefits-focused language
- Urgency and scarcity elements
- Social proof and trust signals
- Clear call-to-action
- Problem-solution messaging

Please provide the output in the following JSON format with persuasive Persian content:

{{
  "product_name": "نام جذاب و فوری محصول که مشتری را ترغیب به خرید کند",
  "description": "توضیحات متقاعدکننده و فروش‌محور که مزایا، حل مشکلات، و فوریت خرید را برجسته کند",
  "category": "دسته‌بندی استراتژیک و قابل فروش",
  "hashtags": ["#خرید_فوری","#پیشنهاد_ویژه","#محدود_زمان","#هشتگ_فروش","#هشتگ_تبلیغات"],
}}

Focus on creating content that drives immediate sales and customer conversion. Make it impossible for customers to resist!"""

    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
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
        temperature=0.6,
        max_tokens=1000
    )

    return completion.choices[0].message.content

