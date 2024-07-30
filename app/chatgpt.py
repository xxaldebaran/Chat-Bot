from openai import AsyncOpenAI
from app.config import AI_TOKEN

client =  AsyncOpenAI(api_key = AI_TOKEN)

async def chat(req):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": req,
            }
        ],
        model="gpt-4o-mini",
    )

    return chat_completion.choices[0].message.content

