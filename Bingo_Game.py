import random
import sys
import time
class playerone:
    def __init__(self):
        ranges = range(1, 26)
        self.player1 = random.sample(ranges, 25)
        #print(self.player1)

class Computer(playerone):
    def __init__(self):
        super().__init__()
        ranges = range(1, 26)
        self.playerc = random.sample(ranges, 25)
        #print(self.playerc)

class bingo(Computer):

    def __init__(self,b1,c1):
        self.b1=b1
        self.c1=c1
        super().__init__()
    def funcut(self):
        if self.inp in self.player1:
            index = self.player1.index(self.inp)
            self.player1[index] = 0
        if self.inp in self.playerc:
            index = self.playerc.index(self.inp)
            self.playerc[index] = 0
    def printbingo(self):
        if len(self.b1)>4:
            print("Player one you got bingo")
            print("congrats")
            sys.exit()
            return
        elif len(self.b1)==4:
            print("player you got 'bing'")
        elif len(self.b1)==3:
            print("player you got 'bin'")
        elif len(self.b1)==2:
            print("player you got 'bi'")
        elif len(self.b1)==1:
            print("player you got 'b'")
        if len(self.c1)>4:
            print("Computer you got bingo")
            print("congrats")
            sys.exit()
            return
        elif len(self.c1)==4:
            print("Computer you got 'bing'")
        elif len(self.c1)==3:
            print("Computer you got 'bin'")
        elif len(self.c1)==2:
            print("Computer you got 'bi'")
        elif len(self.c1)==1:
            print("Computer you got 'b'")
        

        
    def funwin(self):
        self.b1=[]
        if self.player1[0]==0 and self.player1[1]==0 and self.player1[2]==0 and self.player1[3]==0 and self.player1[4]==0:
            self.b1.append(1)
        if self.player1[5]==0 and self.player1[6]==0 and self.player1[7]==0 and self.player1[8]==0 and self.player1[9]==0:
            self.b1.append(2)
        if self.player1[10]==0 and self.player1[11]==0 and self.player1[12]==0 and self.player1[13]==0 and self.player1[14]==0:
            self.b1.append(3)
        if self.player1[15]==0 and self.player1[16]==0 and self.player1[17]==0 and self.player1[18]==0 and self.player1[19]==0:
            self.b1.append(4)
        if self.player1[20]==0 and self.player1[21]==0 and self.player1[22]==0 and self.player1[23]==0 and self.player1[24]==0:
            self.b1.append(5)
        if self.player1[0]==0 and self.player1[5]==0 and self.player1[10]==0 and self.player1[15]==0 and self.player1[20]==0:
            self.b1.append(6)
        if self.player1[1]==0 and self.player1[6]==0 and self.player1[11]==0 and self.player1[16]==0 and self.player1[21]==0:
            self.b1.append(7)
        if self.player1[2]==0 and self.player1[7]==0 and self.player1[12]==0 and self.player1[17]==0 and self.player1[22]==0:
            self.b1.append(8)
        if self.player1[3]==0 and self.player1[8]==0 and self.player1[13]==0 and self.player1[18]==0 and self.player1[23]==0:
            self.b1.append(9)
        if self.player1[4]==0 and self.player1[9]==0 and self.player1[14]==0 and self.player1[19]==0 and self.player1[24]==0:
            self.b1.append(10)
        if self.player1[0]==0 and self.player1[6]==0 and self.player1[12]==0 and self.player1[18]==0 and self.player1[24]==0:
            self.b1.append(11)
        if self.player1[4]==0 and self.player1[8]==0 and self.player1[12]==0 and self.player1[16]==0 and self.player1[20]==0:
            self.b1.append(12)
        
        self.c1=[]
        if self.playerc[0]==0 and self.playerc[1]==0 and self.playerc[2]==0 and self.playerc[3]==0 and self.playerc[4]==0:
            self.c1.append(1)
        if self.playerc[5]==0 and self.playerc[6]==0 and self.playerc[7]==0 and self.playerc[8]==0 and self.playerc[9]==0:
            self.c1.append(2)
        if self.playerc[10]==0 and self.playerc[11]==0 and self.playerc[12]==0 and self.playerc[13]==0 and self.playerc[14]==0:
            self.c1.append(3)
        if self.playerc[15]==0 and self.playerc[16]==0 and self.playerc[17]==0 and self.playerc[18]==0 and self.playerc[19]==0:
            self.c1.append(4)
        if self.playerc[20]==0 and self.playerc[21]==0 and self.playerc[22]==0 and self.playerc[23]==0 and self.playerc[24]==0:
            self.c1.append(5)
        if self.playerc[0]==0 and self.playerc[5]==0 and self.playerc[10]==0 and self.playerc[15]==0 and self.playerc[20]==0:
            self.c1.append(6)
        if self.playerc[1]==0 and self.playerc[6]==0 and self.playerc[11]==0 and self.playerc[16]==0 and self.playerc[21]==0:
            self.c1.append(7)
        if self.playerc[2]==0 and self.playerc[7]==0 and self.playerc[12]==0 and self.playerc[17]==0 and self.playerc[22]==0:
            self.c1.append(8)
        if self.playerc[3]==0 and self.playerc[8]==0 and self.playerc[13]==0 and self.playerc[18]==0 and self.playerc[23]==0:
            self.c1.append(9)
        if self.playerc[4]==0 and self.playerc[9]==0 and self.playerc[14]==0 and self.playerc[19]==0 and self.playerc[24]==0:
            self.c1.append(10)
        if self.playerc[0]==0 and self.playerc[6]==0 and self.playerc[12]==0 and self.playerc[18]==0 and self.playerc[24]==0:
            self.c1.append(11)
        if self.playerc[4]==0 and self.playerc[8]==0 and self.playerc[12]==0 and self.playerc[16]==0 and self.playerc[20]==0:
            self.c1.append(12)  
           
        self.printbingo()
        self.display()

    
    def Turn(self, inp):
        self.inp = inp
        for i in range(1, 26):
            self.funwin()
            if i % 2 == 0:
                a=0
                while a<100:
                    self.choose = random.randint(1,26)
                    if self.choose in self.playerc:
                        self.inp = self.choose
                        self.funcut()
                        print("Loading....")
                        time.sleep(2)
                        print("computer choose: ",self.choose)
                        #print(self.player1)
                        #print(self.playerc)
                        a=100   
                    else:
                        a=a+1
                    
            else:
                a=0
                while a<10:
                    self.inp = int(input("player 1 please choose one number: "))
                    if self.inp<26:
                        self.funcut()
                        #print(self.player1)
                        #print(self.playerc)
                        a=11
                    else:
                        a=a+1
    def display(self):
        count=0
        for i in self.player1:
            count=count+1
            print(i,end=" ")
            if(count%5==0):
                print()

def main():
    a2=[]
    a1 = bingo(a2,a2)
    a1.Turn(0)

    
main()
