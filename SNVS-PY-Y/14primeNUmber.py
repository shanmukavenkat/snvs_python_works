###
#a = int(input())
#count = 0
#flag = False
#for i in range(2,a):
#    if (a%i) == 0:
#      flag = True
#
#if flag:
#   print("not")
####

numbe = int(input())
for num in range(1,numbe+1):
    if num >1:
        for j in range(2,num):
            if(num%j)== 0:
                break
        else:
            print(num)
  


