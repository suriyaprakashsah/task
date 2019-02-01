
# 1
def variable(N):
 lst = []
 for i in range(1,int(N)+1):
  if i % 3 == 0 and i % 5 == 0:
      lst.append('FizzBuzz')
  elif i % 3 == 0:
      lst.append("Fizz")
  elif i % 5 == 0:
      lst.append('Buzz')
  else:
      lst.append(i)
 print(lst)
variable(input("Enter the Number: "))


# 2
'''def Repeat(x):
    value = dict()
    for i in x:
        if i in value:
            value[i] += 1
        else:
            value[i] = 1

    print(value)
value = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
Repeat(value)
'''

# 3
'''def Dict(x):
 ans = 0
 for i in x.values():
    ans = ans + i
 return ans
value = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
print(Dict(value))


# 4
def crikt(x):
 balls = len(Input)
 batsman1 = []
 batsman2 = []
 total_score = sum(Input)
 for i in range(0, int(balls)):
    if Input[i] == 1:
      if 1 in batsman1:
         batsman2.append(Input[i])
      else:
         batsman1.append(Input[i])
    else:
      batsman2.append(Input[i])
    if Input[i] == 3:
        batsman2.remove(Input[i])
        batsman1.append(Input[i])
 print("Total Score: {}".format(total_score))
 print("Batsman1 Score: {}".format(sum(batsman1)))
 print("Batsman2 Score: {}".format(sum(batsman2)))
Input = [1, 2, 0, 0, 4, 1, 6, 2, 1, 3]
crikt(Input)

'''
