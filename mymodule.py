
def stack():
    stack = []
    while(True):
        x = int(input("Enter your choice: [1]-Insert [2]-Delete [3]-Display"))
        if(x==1):
            v = int(input("Enter any integer value: "))
            stack.append(v)
            print(stack)
        elif(x==3):
            print(stack)
        elif x ==2 :
            stack.pop()
            print(stack)
