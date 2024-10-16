stack=[]
top=0


    
    
def push(num):
    global top
    global stack
    stack[top]=num
    top=top+1


def pop():
    global top
    global stack
    num=stack[top]
    top=top-1
    return num 


push(50)
push(40)
push(30)
push(20)

print(pop())
print(pop())
print(pop())



    
