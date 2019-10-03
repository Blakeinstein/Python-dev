from math import sqrt,atan2,pi,cos,sin
from fractions import Fraction
class complex():
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
    def arg(self):
        return atan2(self.imag,self.real)
    def __add__(self,*a):
        for i in a:
            self.real+=i.real
            self.imag+=i.imag
        return self
    def __str__(self):
        if self.imag == 0: 
            return f'{self.real}'
        if self.real == 0: 
            return f'{self.imag}i'
        sign = '+' if self.imag>0 else '-'
        return f'{self.real}{sign}{abs(self.imag)}i'
    def __mul__(self,*b):
        for i in b:
            self.real,self.imag=self.real*i.real - self.imag*i.imag,self.real*i.imag + self.imag*i.real
        return self
    def __abs__(self):
        return sqrt(self.real**2+self.imag**2)
    def __invert__(self):
        t=abs(self)**2
        self.real= self.real/t
        self.imag= -self.imag/t
        return self
    def conjugate(self):
        self.imag=-self.imag
        return self
    def __repr__(self):
        return str(self)
    def __pow__(self, b):
        if isinstance(b,int): 
            if b==0:
                return 1          
            r=abs(self)**b
            t=self.arg()**b
            ret=complex(r*cos(t),r*sin(t))
            return ret
        else:
            roots=list()
            c=Fraction(b).limit_denominator()
            c,d=c.numerator,c.denominator
            tem=self**c
            r=abs(tem)**(1/d)
            t=tem.arg()
            for i in range(d):
                rangle=(t+2*pi*i)/d
                ret=complex(r*cos(rangle),r*sin(rangle))
                roots.append(ret)
            return roots
    def __truediv__(self, b):
        try:
            if isinstance(b,complex):
                return (self*(~b))/abs(b)
            else:
                self.real/=b
                self.imag/=b
                return self
        except ZeroDivisionError as a:
            print (a)
    def __floordiv__(self, b):
        try:
            if isinstance(b,complex):
                return (self*(~b))//abs(b)
            else:
                self.real//=b
                self.imag//=b
                return self
        except ZeroDivisionError as a:
            print (a)
a=complex(1,0)
b=complex(0,1)
a=a/b
print(a)