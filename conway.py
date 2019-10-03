from time import sleep
from os import system,name
alive=[complex(2,5),complex(3,4),complex(1,1),complex(5,2),complex(3,3),complex(6,2),complex(1,0),complex(0,1),complex(2,4)]
gridsize=10
total=[complex(i,j) for i in range(gridsize) for j in range(gridsize)]
def execute():
        clear()
        draw()
        check()
def clear():
    if globals()['name']=='nt':
        _ = system('cls')
    else:
        _ = system('clear')
def draw():
    for i,j in enumerate(total):
        if j in alive:
            print ('■',end=' ')
        else:
            print ('□',end=' ')
        if not (i+1) % gridsize:
            print()
def sort():
    pass
def succeed(sustain,reprod):
    global alive
    alive=sustain+reprod
    sort()
    sleep(2)
    execute()
def check():
    death=[]
    sustain=[]
    reprod=[]
    #for live cells
    for i in alive:
        count=0
        for j in alive:
            if abs(j-i)<1.5:
                count+=1
        if count<2 or count>3:
            death.append(i)
        else:
            sustain.append(i)
    #for dead cells
    for i in set(total)-set(alive):
        dcount=0
        for j in alive:
            if abs(j-i)<1.5:
                dcount+=1
        if dcount==3:
            reprod.append(i)
    succeed(sustain,reprod)
    
execute()