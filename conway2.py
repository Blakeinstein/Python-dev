from os import system,name
from time import sleep
def clear(func):
    def wrapper(*args, **kwargs):
        if globals()['name']=='nt':
            _ = system('cls')
        else:
            _ = system('clear')
        return func(*args, **kwargs)
    return wrapper 
class board():
    dead=[]
    def __init__(self,a):
        self.alive=list(a)
        self.dead=[]
        self.finddead()
    def finddead(self):
        for i in self.alive:
            for j in [1,0,-1]:
                for k in [1,0,-1]:
                    if i.real-j <= 0 or i.imag-k <=0 or complex(i.real-j,i.imag-k) in self.alive:
                        continue
                    else:
                        self.dead.append(complex(i.real-j,i.imag-k))
        self.dead=sort(list(set(self.dead)))
    def trim(self):
        temp=[]
        for i in self.dead:
            for j in self.alive:
                if abs(j-i)<1.5:
                    break
            else:
                temp.append(i)
        self.dead=list(set(self.dead)-set(temp))
        self.dead=sort(self.dead)
        m=min(self.dead,key=lambda x: abs(x))
        self.alive=[i-m for i in self.alive]
        self.dead=[i-m for i in self.dead]
    @clear
    def draw(self):
        self.trim()
        n,m=max(self.alive,key=lambda x: abs(x)),min(self.alive,key=lambda x: abs(x))
        for i in range(int(m.real)-2,int(n.real)+1):
            for j in range(int(m.imag)-2,int(n.imag)+1):
                    if complex(i+1,j+1) in self.alive:
                            print('■',end=' ')
                    else:
                            print('░',end=' ')
            print()
    def check(self):
        death=[]
        sustain=[]
        reprod=[]
        for i in self.alive:
            count=0
            for j in self.alive:
                if i==j:
                    continue
                if abs(j-i)<1.5:
                    count+=1
            if count<2 or count>3:
                death.append(i)
            else:
                sustain.append(i)
        for i in self.dead:
            dcount=0
            for j in self.alive:
                if abs(j-i)<1.5:
                    dcount+=1
            if dcount==3:
                reprod.append(i)
        sustain=set(sustain)
        reprod=set(reprod)
        death=set(death)
        self.alive=sort(list(sustain.union(reprod)))
        self.dead=sort(list(set(self.dead).union(death)))
def sort(a):
    a.sort(key=lambda x: (x.real,x.imag))
    return a
@clear
def custom():
    alive=[]
    print(' Choose input method. \n      (1).Index \n      (2).Seed')
    try:
        if int(input())-1:
            print('Seed is of the format XXXXXXXXX.... where the X are numbers of half of the length denotes number of alive cells')
            print('For ex. A seed of 222324 with gridsize < 10 denotes 3 alive cells at 2,2 , 2,3 and 2,4')
            print('If 9 < gridsize < 100 then 12222324 would denote alive cells at 12,22 and 23,24 provided provided the parameters dont exceed gridsize')
            try:
                print(' The play area is a square grid, putting 10 here would produce a 10x10 square grid for the cells ')
                print(' This is used to determine seed format, with a seed more than 9 the input would be abcdefgh such that ab,cd and ef,gh are the two alive cells ')
                gridsize=int(input('Input gridsize:- '))
                if gridsize <= 0:
                    raise Exception('Grid size can\'t be negative!')
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
                return board(sort(alive))
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
                return board(sort(alive))
    except ValueError:
        print('Invalid Input, input should be an integer!')
@clear
def setup():
    print('   Welcome to Conway\'s game of life  ')
    print(' Would you like to provide a custom seed? or proceed with the default values? 1/2 ')
    try:
        if int(input())-1:
            new=board([complex(2,1),complex(2,2),complex(2,3)])
        else:
            new=custom()
    except ValueError:
        print ('Invalid Input oh fek')
    else:
        while True:
            new.check()
            new.draw()
            sleep(1)

setup()