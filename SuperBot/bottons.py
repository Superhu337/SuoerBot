from telebot import types

def BOTTONS(a):

    func_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ans = search(a)
    for i in range(a.count(',')+1):
        item0 = types.KeyboardButton(ans[i])

        func_btn.add(item0)

    return func_btn


def search(A):
    x=[]
    q=[0]
    for i in range(len(A)):
        if A[i]==",":
            q.append(i)
        if i == len(A)-1:
            q.append(len(A))
    for i in range(len(q)-1):
        #print(q[i],i)
        if i==0:
            x.append(A[q[i]:q[i+1]])
        else:
            x.append(A[(q[i]+1):q[i+1]])


    return x


