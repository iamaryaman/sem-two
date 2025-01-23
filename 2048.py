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


def check(sublist,LEFTORRIGHT):
    count = 0
    exe = False
    for i in range(len(sublist)): 
        if i == None:
            continue
        for j in range(count,len(l)):
            if i == j or sublist[j] == None:
                continue
            if sublist[i] != sublist[j]:
                break
            if sublist[i] == sublist[j]:
                if LEFTORRIGHT == "L":
                    sublist[i] = sublist[j]*2
                    sublist[j] = None
                elif LEFTORRIGHT == "R":
                    sublist[j] = sublist[i]*2
                    sublist[i] = None
                exe = True
        count +=1
    if exe == False:
        return "Nothing"
    else:
        return sublist

def arraypick(pick,mainlist):
    if pick.lower() == "l" or pick.lower() == "r":
        return mainlist
    else:
        mainnewlist= []
        for i in range(0,4):
            newlist = []
            for j in range(0,4):
                newlist.append(mainlist[j][i])
            mainnewlist.append(newlist)
        
        return mainnewlist
    


