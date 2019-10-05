from time import sleep
from os import system,name
# alive=[complex(2,5),complex(3,4),complex(1,1),complex(5,2),complex(3,3),complex(6,2),complex(1,0),complex(0,1),complex(2,4)]
# gridsize=0
# alive=[]
# total=[]
def cleard(func):
    def wrapper(*args, **kwargs):
        clear()
        func(*args, **kwargs)
        return returned_value
    return wrapper      
def execute(alive,gridsize):
        clear()
        total=[complex(i,j) for i in range(gridsize) for j in range(gridsize)]
        draw(alive,gridsize,total)
def clear():
    if globals()['name']=='nt':
        _ = system('cls')
    else:
        _ = system('clear')
def draw(alive,gridsize,total):
    for i,j in enumerate(total):
        if j in alive:
            print ('■',end=' ')
        else:
            print ('□',end=' ')
        if not (i+1) % gridsize:
            print()
def sort():
    alive.sort(key=lambda x: (x.real+1)*gridsize + x.imag)
def succeed(sustain,reprod,alive,gridsize,total):
    alive=sustain+reprod
    sort()
    sleep(1)
    draw(alive,gridsize,total)
    check(alive,gridsize,total)
def check(alive,gridsize,total):
    death=[]
    sustain=[]
    reprod=[]
    #for live cells
    for i in alive:
        count=0
        for j in alive:
            if i==j:
                continue
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
    succeed(sustain,reprod,alive,gridsize,total)
def default():
    clear()
    gridsize=5
    alive=[complex(2,1),complex(2,2),complex(2,3)]
    execute(alive,gridsize)
def custom():
    clear()
    try:
        print(' The play area is a square grid, putting 10 here would produce a 10x10 square grid for the cells ')
        gridsize=int(input('Input gridsize:- '))
    except ValueError:
        print('Invalid Input, input should be an integer!')
    clear()
    print(' Choose input method. \n      (1).seed \n      (2).index')
    try:
        if int(input)-1:
            pass
        else:
            try:
                loop=int(input('Enter number of alive cells in seed'))
            except ValueError:
                print('Invalid Input, input should be an integer!')
            else:
                for i in range(loop):
                    for j in range(loop):
                        print (f'{i+1},{j+1}',end=' ')
                print('If you want the an alive cell at 2,1 pass 2 first and then 1 for the corresponding cell.')
                for i in range(loop):
                    alive.append(complex(int(input(f'{i+1}th value\'s row'))-1,int(input(f'{i+1}th value\'s column'))-1))
                execute(alive,gridsize)
    except ValueError:
        print('Invalid Input, input shouldbe an integer!')
def setup():
    clear()
    print('   Welcome to Conway\'s game of life  ')
    print(' Would you like to provide a custom seed? or proceed with the default values? 1/2 ')
    try:
        if int(input())-1:
            clear()
            default()
        else:
            clear()
            custom()
    except ValueError:
        print ('Invalid Input') 
        
    
setup()