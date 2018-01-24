import random
import string
try:
        bull=0
        N=int(input("enter size of the random string:\n"))
        cow=0
        guess=0
        #num=[1,2,3,4,5,6,7,8,9]
        #bnumber=random.sample(num,3)
        bnumber=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
        bnumber=list(bnumber)
        print(bnumber)
        while guess<10:
                guess+=1
                print("Guess no:"+str(guess))
                pnumber=input("\nenter number:\n")[:N]
                for i in range(len(pnumber)):
                        if pnumber[i] in bnumber and pnumber[i]==bnumber[i]:
                                bull+=1
                        if pnumber[i] in bnumber and pnumber[i]!=bnumber[i]:
                                cow+=1
                        if pnumber[i] not in bnumber:
                                pass
                if bull==N:
                        print("YOU WIN")
                        break
                if bull==0 and cow==0:
                        print("no bull no cow")
                else:
                        print(str(bull)+" bull ,"+str(cow)+" cow")
                bull=0
                cow=0
        if guess>=10:
                print("YOU LOST")
except:
        print("exception")
