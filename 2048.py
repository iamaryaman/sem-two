import random
maindict = {}

def main_dict_call():
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
    count = 0
    exe = False
    for i in range(len(l)): 
        if i == None:
            continue
        for j in range(count,len(l)):
            if i == j or l[j] == None:
                continue
            if l[i] != l[j]:
                break
            if l[i] == l[j]:
                if LEFTORRIGHT == "L":
                    l[i] = l[j]*2
                    l[j] = None
                elif LEFTORRIGHT == "R":
                    l[j] = l[i]*2
                    l[i] = None
                exe = True
        count +=1
    if exe == False:
        return "Nothing"
    else:
        return l 

