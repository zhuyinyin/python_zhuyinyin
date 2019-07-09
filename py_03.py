# python_baseimport random
# random.randint(a,b) #返回[a,b]之间随机数  a必须小于b

min = int(input('输入最小值：'))
max = int(input('输入最大值：'))
rand = random.randint(min,max)

num = 0
while True:
    guss = int(input('猜测数：'))
    num += 1
    if guss < rand:
        print('小了')
    elif guss > rand:
        print('小了')
    else :
        print('猜对了')
    break
print('共猜%d次'%num)

# 将字符串变为列表
strs = ("hello")
list00 = [1,2,3,4,5]
lists = [1,2,3,4,5]
liststr = list(strs)
# 删除列表命令
del liststr[0]
print(liststr)
del liststr
# 在list后面加一个元素,无返回值
lists.append(4)
print(lists)
# index -- 找出某个值的位置
# 在1的索引位置价格元素8，无返回值
lists.insert(1, 8)
print(lists)
# 在list列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
lists.extend(list00)  # 无返回值
print(lists)
# pop列表删除   返回删除位置的值，
c = lists.pop()  # 删除最后一个列表值s
d = lists.pop(1)  # 删除第二个位置列表值，（索引位置）
print('lists',lists)
# remove删除指定数据
lists.remove(1)  # 删除list中第一个元素1 没有返回值
print(lists)
# clear()清空列表
# lists.clear()
# count数组元素个数统计
e = lists.count(1)  # 累计list中1的次数
print(e)
# .index(元素)，找出list中元素首次出现的下表就是索引值
f = lists.index(1)  # 返回索引位置
print(f)
# in 判断列表中是否存在某个元素
a = 5 in lists  # 返回
print(a)
# 排序
random.shuffle(lists)  # 打乱list中元素无返回值
print(lists)
# .sort()排序，没有返回值
# list.sort(cmp=None, key=None, reverse=False)
# everse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）
lists.sort(reverse=False)  # 此处发现列表lists中不能有字符串？
print(lists)
lists.sort(reverse=True)
print(lists)

# 课后作业


#  求1！+2！+3！+4！+5！的和。
k = int(input('输入一个数'))
j = 1
sum = 0
for k in range(1,k+1):
    j = k*j
    sum = sum + j
print(sum)

# 篮球弹跳高度的计算
# 如果篮球从某一高度落下，每次落地后反弹回原来高度的一半再落下。
# 那么球在第10次落地时，共经过多少米呢? 第10次反弹多高？ （你问我这个题是不是瞎编的？当然是了，你什么时候见过书呆子打篮球？）
# 输入：输入一个整数h，单位是米，表示球的初始高度。
# 输出：输出包含两行：
# 第1行：到球第10次落地时，一共经过的距离。
# 第2行：第10次弹跳的高度。
# 例如输入：20 对应输出：第一行：59.921875 第二行：0.01953125
h1 = float(input('篮球的初始高度：(米)'))
h2 = h1
h = h1/2
h3 = 0
for n in range(1,8):
    h2 = h2/2
    h = h + h2/2
    if n == 7 :
        h3 = h2/8

h = h + h1*2
print(h)
print('第十次落地一共经过的距离：%s'%h)
print('第十次弹跳的高度：%s'%h3)



# 我国现有13亿人口，设每年增长0.8%，编写程序，计算多少年后达到26亿？
nums = 13.0
w = 0
while nums < 26:
     nums = nums + nums*(0.008)
     w = w + 1
print('%d年后达到26亿'%w)
