import random
def cointoss():
    out=["heads","tails"]
    r=random.randint(0,1)
    return out[r]
t=1

while(t==1):
    print("do you want to do toss? (enter 'yes' or 'no') ")
    st=input()
    if (st=="yes"):
        print("enter your choice: ('heads' or 'tails') ")
        ch=input()
        result=cointoss()
        if(ch=='heads' and result=="heads"):
            print("you won the toss it is",result)
            print("\n")
        elif (ch=='tails' and result=="tails"):
            print("you won the toss it is",result)
            print("\n")
        else:
            print("you lost the toss")
            print("you choose",ch,"but you got",result)
            print("\n")
    elif (st=="no"):
        print("bye!")
        t=0
    else:
        print("plese re-enter the input 'yes' or 'no': ")
            


