import string as s
import random as rd
sequence1=s.ascii_letters+s.digits
sequence2=sequence1+"!#$%^&*_.(){}[]:;,"
def key(n): #获取n位数的密码
    key_list=[]
    for i in range(n):
        factor=rd.choice(sequence)
        key_list.append(factor)
    key="".join(key_list)
    print(key)
def get_key(m): #获取多少个密码
    for i in range(m):
        key(16)
k1=int(input("输入1为有特殊字符，0则没有："))
if k1==0:
    sequence=sequence1
else:
    sequence=sequence2
m=int(input("请输入想要的16位密码个数："))
get_key(m)
a=input("输入q则退出")
if a=="q":
    exit()
