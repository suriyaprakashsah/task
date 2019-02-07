# 1
def Palindrome(x):
 value = x.casefold()
 y = reversed(value)
 if list(value) == list(y):
    print("It is palindrome")
 else:
    print(x +" is not palindrome")
value = input("Enter the word: ")
Palindrome(value)




# 2
class cricket:
    single = 1
    wicket = 'w'
    value = ['Overs','Maiden','Wicket','Runs']

    def batsmans(self,x):
        self.batsman1 = []
        self.batsman2 = []
        self.balls = len(x)
        for i in range(0, len(x)):
           if Input[i] == self.single:
             if 1 in self.batsman1:
               self.batsman2.append(Input[i])
             else:
               self.batsman1.append(Input[i])
           else:
            self.batsman2.append(Input[i])

           if Input[i] == 3:
               self.batsman2.remove(Input[i])
               self.batsman1.append(Input[i])
        print("Batsman1 {1}({0})".format(len(self.batsman1),sum(self.batsman1)))
        print("Batsman2 {1}({0})".format(len(self.batsman2),sum(self.batsman2)))

    def Bolers(self):
        self.boler1 = dict.fromkeys(self.value)
        self.boler2 = dict.fromkeys(self.value)
        self.total_score = sum(Input)
        self.overs = []
        self.ballspover = 6
        self.lst = []

        for j in range(self.ballspover):
               self.lst.append(Input[j])
        a = sum(self.lst)
        self.boler1['Runs'] = a
        self.boler1['Overs'] = 1
        self.boler1['Maiden'] = 0
        self.boler1['Wicket'] = 0
        b = sum(Input[6:])
        self.boler2['Runs'] = b
        self.boler2['Overs'] = 0.4
        self.boler2['Maiden'] = 0
        self.boler2['Wicket'] = 0
        get = self.boler1['Overs']
        get1 = self.boler2['Overs']
        ans = get + get1
        self.overs.append(ans)
        print(self.boler1)# boler1 statics
        print(self.boler2)# boler2 statics
        print("total: {1} for {0} in {2} overs".format(0, self.total_score, self.overs))

Input = [1, 2, 0, 0, 4, 1, 6, 2, 1, 3]
obj = cricket()
obj.batsmans(Input)
obj.Bolers()
