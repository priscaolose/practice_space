import openai

openai.api_key = "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"

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "system", "content": message})
    respnse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = respnse["choices"][0]["messages"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")