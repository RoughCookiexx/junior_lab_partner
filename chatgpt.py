from openai import OpenAI
from secrets import CHAT_GPT_API_KEY

PERSONA = ('You are modifying python code that will directly go onto my Twitch stream.'
           'This stream is a challenge to battle an ai to complete a game.'
           'Every five minutes, the code from a particular file and you have to introduce bugs into the code.'
           'Limit the bugs from 5 to 10. Make some of the bugs subtle, and others in my face.'
           'Write bugs that are more than simple typos. Make sure some of them are bugs veterans will miss.'
           'Have fun. My viewers expect shenanigans and goofing around.'
           'Input will be the current code. Output code with bugs introduced.'
           'DO NOT write comments.'
           'Also, you\'re a jerk. Like a big major stinkin\' jerk. Be mean.')


def send_message_to_chatgpt(message, client):
    messages = []
    messages.append(
        {"role": "system", "content": PERSONA}
    )
    messages.append(
        {"role": "user", "content": message}
    )

    response = client.chat.completions.create(model='gpt-4o',
                                        messages=messages,
                                        max_tokens=500)

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    client = OpenAI(api_key=CHAT_GPT_API_KEY)
    user_message = input("Enter your message for ChatGPT: ")
    reply = send_message_to_chatgpt(user_message, client)
    print("ChatGPT's reply:", reply)

