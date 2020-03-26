#0316
#P6練習
# r=4
# pi=3.14
# print(r**2*pi)

#平均取整數
# scores=[10,30,40,90,100,61]
# average=sum(scores)/len(scores)
# average1=round(average)
# print(average1)
#
# #ifelse
# scores=60
# if scores >= 60:
#     print('及格')
#     if scores >=90:
#         print('你最棒')
#     else:
#         print('還可以更好')
# elif 40<= scores and scores< 60:
#     print('不及格')
# else:
#     print('要被死當了QQ')
#
# #print各種用法
# print("Hello", "world", "!")
# print('Hellp\nworld \n!')
# print('123', end="")

#35
# family = {
#     'dad':'Homer',
#     'mom':'Marge',
#     'som':'Bart',
#     'daughter':'Lisa'
# }
# for member in family.items():
#     print(member)
# for role, name in family.items():
#     print(f'my {role} is {name}')
# for key, value in family.items():
#     print(f"my {key} is {value}")

#36練習
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# for score in mathScores:
#     print(math.sqrt(score)*10)
#
#for i in range(10):
#print(i)

#[print(i) for i in range(10)]

# improt math
# mathScore = [60, 70, 10, 20, 81, 63, 4]
# for item in mathScore:
#     print(math.sqrt(item)*10)
# [print(math.sqrt(item)*10) for item in mathScores]

#41
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print('lood end')

#42break正個for迴圈跳掉
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# for score in mathScores:
#     if score >80:
#         break
#     print(score)

#43continue跳過一圈for迴圈
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# for score in mathScores:
#     if score >80:
#         continue
#     print(score)
#

# import random
# i = random.randint(1,3)
# row = input('how many rows')


#eval string轉int

#99乘法
# for i in range(1, 10):
# for j in range(1, 10):
# ans = i * j
# print (f'{i} * {j} = {i*j}')
#
# #使⽤ while 迴圈顯⽰ 50 個你好，並在顯⽰第 100 個後，使⽤ print 顯⽰「我說完了啦」並停⽌
# k=0
# while k <=50:
#     print('你好', end='')
#     k+=1
#     print('我說完了啦')


# #輸入⼀個數值，輸出從1到這個數的所有奇數
# num = eval(input('enter a number'))
# for i in range (1, num+1):
#     if i % 2 == 1:
#         print(i)


# 輸入rows及columns，隨機亂數(0-100)
# 產⽣⼀個rows * columns的⼆維串列，並印出(參照範例)
