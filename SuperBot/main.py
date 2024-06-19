import telebot
from Reader import reader
import random
from bottons import BOTTONS
token=''
bot = telebot.TeleBot(token)
global score
score = 0
send=[]
name='aaa'
num_que=0
n=4

score=0
def Score():
    global score
    score+=1


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello!!\n"+"Let`s start",reply_markup=False)
    svo(message)


def svo(message):
    if score>=n:
        bot.send_message(message.chat.id,"Your done!!!11!1!",reply_markup=False)
    global num_que
    num_que,q,a,ca,btn=randomm(n)
    send=bot.send_message(message.chat.id,"Question №"+str(num_que)+'\n\n'+q+'\n'+"Your answ?",reply_markup=btn)
    bot.register_next_step_handler(send, qwe)
    
    

def qwe(message):
    txt=message.text
    q,a,ca = reader(name,num_que)
    #print(ca)
    #print(txt)
    if txt==ca:
        bot.send_message(message.chat.id, "You right")
        Score()
        bot.send_message(message.chat.id, "Next que")
        svo(message)

    else:
        bot.send_message(message.chat.id, "Nan")
        
        bot.send_message(message.chat.id, "Next que")
        svo(message)

def randomm(n):
    num_que=random.randint(1,n)
    q,a,ca = reader(name,num_que)
    btn=BOTTONS(a)
    #print(num_que)
    return num_que,q,a,ca,btn

bot.polling()
print(".|.")

