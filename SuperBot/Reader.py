def reader(name,num_que):
    q=''
    a=''
    ca=''
    with open(str(name)+".txt", "r") as f:
        ar = [row.strip() for row in f]
    #print(ar)
    for x in range(len(ar)):
        if ar[x]==str(num_que):
            q=ar[x+1]
            a=ar[x+2]
            ca=ar[x+3]
    
    

    x1,x2=search(q)
    x3,x4=search(a)
    x5,x6=search(ca)
    return q[x1:x2],a[x3:x4],ca[x5:x6]

        
def search(ar):
    x1=0
    x2=0
    for i in range(len(ar)):
        if ar[i]=='[':
            x1=i+1
        if ar[i]==']':
            x2=i
    return x1,x2




