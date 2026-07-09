import os

from dotenv import load_dotenv
from llama_index.llms.openai_like import OpenAILike

load_dotenv()

llm = OpenAILike(
    model=os.getenv("TOKENLAB_MODEL", "gpt-5.4"),
    api_base="https://api.tokenlab.sh/v1",
    api_key=os.environ["TOKENLAB_API_KEY"],
    is_chat_model=True,
)

response = llm.complete("Explain TokenLab in one sentence.")
print(response)
