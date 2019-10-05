from time import sleep
from os import system,name
from math import log10
# alive=[complex(2,5),complex(3,4),complex(1,1),complex(5,2),complex(3,3),complex(6,2),complex(1,0),complex(0,1),complex(2,4)]
# gridsize=0
# alive=[]
# total=[] 
def clear(func):
    def wrapper(*args, **kwargs):
        if globals()['name']=='nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return func(*args, **kwargs)
    return wrapper 
@clear
def execute(alive,gridsize):
        total=[complex(i,j) for i in range(gridsize) for j in range(gridsize)]
        draw(alive,gridsize,total)
        check(alive,gridsize,total)
@clear
def draw(alive,gridsize,total):
    for i,j in enumerate(total):
        if j in alive:
            print ('■',end=' ')
        else:
            print ('░',end=' ')
        if not (i+1) % gridsize:
            print()
def sort(alive,gridsize):
    alive.sort(key=lambda x: (x.real+1)*gridsize + x.imag)
    return alive
def succeed(sustain,reprod,alive,gridsize,total):
    alive=sustain+reprod
    alive=sort(alive,gridsize)
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
@clear
def default():
    gridsize=5
    alive=[complex(2,1),complex(2,2),complex(2,3)]
    execute(alive,gridsize)
@clear
def custom():
    try:
        print(' The play area is a square grid, putting 10 here would produce a 10x10 square grid for the cells ')
        gridsize=int(input('Input gridsize:- '))
        if gridsize <= 0:
            raise ValueError
    except ValueError:
        print('Invalid Input, input should be an integer!')
    else:
        alive=[]
    print(' Choose input method. \n      (1).Index \n      (2).Seed')
    try:
        if int(input())-1:
            print('Seed is of the format XXXXXXXXX.... where the X are numbers of half of the length denotes number of alive cells')
            print('For ex. A seed of 222324 with gridsize < 10 denotes 3 alive cells at 2,2 , 2,3 and 2,4')
            print('If 9 < gridsize < 100 then 12222324 would denote alive cells at 12,22 and 23,24 provided provided the parameters dont exceed gridsize')
            try:
                seed=int(input('Enter seed:- '))
                n=1
                while n <= gridsize:
                    n*=10
                while seed%(n**2)!=0:
                    a,b=(seed%(n**2))//n,(seed%(n**2))%n
                    if a>gridsize or b>gridsize:
                        raise Exception(f'Seed input exceeded grid with values {a},{b}')
                    elif not a or not b:
                        raise Exception(f'There is no row/column with index 0, seed specifies 0 location as {a},{b}')
                    else:
                        alive.append(complex(b-1,a-1))
                        seed//=(n**2)
            except ValueError:
                print('Invalid Input, input should be an integer!')
            else:
                alive=sort(alive,gridsize)
                execute(alive,gridsize)    
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
        print('Invalid Input, input should be an integer!')
@clear
def setup():
    print('   Welcome to Conway\'s game of life  ')
    print(' Would you like to provide a custom seed? or proceed with the default values? 1/2 ')
    try:
        if int(input())-1:
            default()
        else:
            custom()
    except ValueError:
        print ('Invalid Input')         
setup()