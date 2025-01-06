import random
maindict = {}

def maindictcall():
    for i in range(1,4*4+1):
        maindict[i]=None
    return None

def setrandom():
    total = list(maindict.keys())
    left = [i for i in total if maindict[i]==None]
    new_square = random.choice(left)
    what_square = random.choice([2,2,2,4])
    
    maindict[new_square] = what_square
    return None

def clear():
    maindict.clear()
    return None


def display(mydict):
    l=[[None for _ in range(4)] for _ in range(4)]
    j=0
    while j < 4:
        for i in range(4):
            key = i+(j*4)+1
            if key in mydict:
                l[j][i] = mydict[key]
            else:
                l[j][i]=None
        j=j+1    
    return l


def check(l,LEFTORRIGHT):
    n = len(l)
    
    for i in range(n):
        for j in range(n):
            if LEFTORRIGHT == "R":
                if l[i] == l[j] and l[i] != None and (i != j):
                    l[j] = l[i]*2
                    l[i] = None
            elif LEFTORRIGHT == "L":
                if l[i] == l[j] and l[i] != None and (i != j):
                    l[i] = l[j]*2
                    l[j] = None
                    print(i,j)



        
    
    
        
        
        
    

    
# main()