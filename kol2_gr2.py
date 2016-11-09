#import student
#class obec(object):
 #   def __init__(self)
       #tu powinny byc pary data-lista lekcji 1/0 


class student(object):
    def __init__(self,name,sname):
        self.name=name
        self.sname=sname
        self.scores=[]

    def __str__(self):
        stud_str="imie: "+self.name+"\n"
	stud_str+="nazwisko: "+self.sname+"\n" 
        stud_str+="oceny: "
        stud_str+=''.join(str(e)+"," for e in self.scores)+"\n"
        stud_str+="srednia: "+str(self.ret_avr())
        return stud_str

    def add_score(self,x):
        self.scores.append(x)

    def ret_avr(self):
        avr=0    
        for x in self.scores:
            avr+=x
        avr/=len(self.scores)
#coś się popsulo


s1=student("janek","iks") 
s1.add_score(4)
s1.add_score(3)
s1.add_score(5)
s1.add_score(5)
s1.add_score(2)
s1.add_score(4)
s1.add_score(4)

print s1 
