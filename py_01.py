# python_base# Python 变量类型
#   存储整数，小数或字符
#   Python 中的变量赋值不需要类型声明。
#   每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
#   多个变量赋值
#   Python允许你同时为多个变量赋值。例如：
#    a = b = c = 1
#   可以为多个对象指定多个变量。例如：
#   a, b, c = 1, 2, "john"
#   标准数据类型:
#   Python有五个标准的数据类型：
# Numbers（数字）number 数字
#         Python支持四种不同的数字类型：
#
#         int（有符号整型）
#         long（长整型[也可以代表八进制和十六进制]）
#         float（浮点型）
#         complex（复数）
#               复数由实数部分和虚数部分构成，可以用 a + bj,或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
# String（字符串）string 字符串
# List（列表）list 列表
""""
lists = ['john', 786, 2.23, 'john', 70.2]
lists2 = [123, 'john']
print(lists)  # 输出完整列表
print(lists[0])  # 输出列表的第一个元素
print(lists[1:3])  # 输出第二个至第三个元素
print(lists[:3])
print(lists[2:])  # 输出从第三个开始至列表末尾的所有元素
print(lists2 * 2)  # 输出列表两次
print('lists + lists2')  # 打印组合的列表
"""
# Tuple（元组）tuple 元组 元组是不允许更新的。而列表是允许更新的：
# Dictionary（字典）dictionary字典
# 逻辑运算符：and、 or、 not
# 比较运算符：==、！=、>、<、<=、>
# e = 10
# r = 20
# print(e>r)
# 逻辑运算符：and、 or、 not
q = 10
t = 10
print(q and t)
print(q or t)
print(not q)
# 算术运算符：+、-、*、/、//、%、**
# 赋值运算符：=、+=、-=、*=、/=、//=、%=、**=
# 1 **           幂最高级
# 2 * / \  % //  乘除
# 3 + -          加法减法
# 4  ><>=<=      比较运算符
# 5  <>  ==  !=  等于
# 6  =  %=  /=  //=  -=  +=  *=  **= 赋值
# 7  not and or 逻辑
# if语句
#  if 条件：
#      语句块
#   else:
#       语句块
#     print('优秀')
# 等值判断


# 小练习
money = int(input('请输入存款：(万)'))
if money >= 500:
    print('买路虎')
elif money >= 100:
    print('买宝马')
elif money >= 50:
    print('买迈腾')
elif money >= 10:
    print('买福特')
else:
    print("买比‘亚'迪")

record = int(input('请输入小明考试成绩：'))
if record == 100:
    print('爸爸给他买辆车')
elif record >= 90:
    print('妈妈给他买MP4')
elif 60 <= record < 90:
    print('妈妈给他买本参考书')
else:
    print('什么都没有')
