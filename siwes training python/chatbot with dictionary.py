# Chatbot
bot_dict = {
    "good morning": "morning :) how was your night?",
    "weather": "Its raining today :(please try to stay indoor",
    "where are you": "Am at apata with mum : (wait for me pls",
    "hope you are not feeling cold": "The weather is cool : (stay indor",
    "are you at home bby": "Nope :( Am at Apata to meet mum",
    "kiss": "chop kiss :( I love you bby bby",
}

print("Welcome to my chatbot!\nPressn {q} to quit")
print("Bot: Hello Friend!")
while True:
    u_input = input("You:").lower()
    if u_input =='q':
        break

#for i in bot_dict:
   # if i in u_input:
        #print(f'Bot: {bot_dict[i]}')
    bot_reply = [ bot_dict[i] for i in bot_dict if i in u_input ]

    if len(bot_reply) > 0:
        print(f'Bot: {bot_reply[0]}')
        continue

    print("Bot: Sorry :( I have no reply for this")


        
print("Thank you for chatting with me :)")
