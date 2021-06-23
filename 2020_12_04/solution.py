# -*- coding:utf-8 -*-
"""
author: 15025
time: 2021/6/23 9:35
software: PyCharm

Description:

"""
import numpy as np


# Solution of question one:
def calculatePi():
    pi = 0
    for n in range(1, 1000):
        pi += 4 * (1 / (4 * n - 3) - 1 / (4 * n - 1))

    return pi


pi_ = calculatePi()
print(f"当n为1000时， pi的估算值为：{pi_}")

# ====================================================================================================================================================
# Solution of question two:
def calculateCosine(angle):
    Sn = angle
    for i in range(2, 100, 2):
        Cn = 1
        for j in range(1, i + 1):
            Cn *= j
        num = pow(angle, i) / Cn
        if abs(num) > 0.000001:
            Sn += pow(-1, i // 2) * num
        else:
            break

    return Sn


angle_ = np.deg2rad(float(input("请输入一个角度： ")))
value = calculateCosine(angle_)
print(f"cosx的值为：{value}")


# ====================================================================================================================================================
# Solution of question three:
def findPrimeNumber(num):
    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    num += 1

            else:
                print(num, "是质数")
                break

        # 如果输入的数字小于或等于 1，不是质数
        else:
            print("输入有误，请重新输入数字！")

    return num


num_ = int(input("请输入一个角度： "))
value = findPrimeNumber(num_)
print(f"质数为：{value}")


# ====================================================================================================================================================
# Solution of question four:
def findNumber():
    num_list = []
    for num in range(100, 1000):
        i = num // 100
        j = num // 10 - i * 10
        k = num % 10
        if num // 9 == pow(i, 2) + pow(j, 2) + pow(k, 2):
            num_list.append(num)

    return num_list


num_ = findNumber()
print(f"满足条件的数为：{num_}")


# ====================================================================================================================================================
# Solution of question five:
def invertList(list1):
    list1 = list1[::-1]

    return list1


num = int(input('请定义输入列表的长度：'))
list1_ = []
for i in range(num):
    list1_.append(input(f'请输出列表的第{i}个元素：'))

list_ = invertList(list1_)
print(f"翻转后的列表为：{list_}")


# ====================================================================================================================================================
# Solution of question six:
def invertList(list1):
    for index, num in enumerate(list1):
        if num % 2 == 0:
            list1[index] = pow(num, 2)
        else:
            pass

    return list1


num_ = int(input('请定义输入列表的长度：'))
list1_ = []
for i in range(num_):
    list1_.append(int(input(f'请输出列表的第{i}个元素：')))

list_ = invertList(list1_)
print(f"加工后的新列表为：{list_}")
