#for i in range(1,6):
#    print(str(i)*i)

# for i in range(1,6):
#     for j in range(i):
#         print(j+1,end="")
#     print()

# 1
# 01
# 010
# 1010
# 10101




# for i in range(0,2):
#      for j in range(i):
#           print(j+1)

# x=1
# for i in range(1,6):
#      for j in range(i):
#         if x%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#         x=x+1
#      print()



# *****
# *   *
# *****
# *   *
# *   *


#*****
#*****
#*****
#*****
#*****

x=1
for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i==3 or j==1 or j==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 9341167556