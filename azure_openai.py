from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()

print(os.getenv("AZURE_OPENAI_ENDPOINT"))
print(os.getenv("AZURE_OPENAI_API_KEY"))


client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
    api_version="2023-12-01-preview",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)


def get_completion_from_messages(
    system_message, user_message, model="gpt-4", temperature=0, max_tokens=3000
) -> str:
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{user_message}"},
    ]

    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )

    result = response.choices[0].message.content
    print(result)

    # Hack to format the result
    result = result.replace("```json", "").replace("```", "")

    return result


if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))
