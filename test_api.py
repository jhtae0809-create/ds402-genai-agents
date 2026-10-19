from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print(OpenAI().responses.create(model="gpt-4o-mini", input="Say hello in one sentence.").output_text)
