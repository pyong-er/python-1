my_list = ['Spring', 'Summer', 'Fall', 'Winter']
enu = enumerate(my_list)
print(enu)
new_list = list(enu)
print(new_list)


# a=2
# print(id(a))
# a=3
# print(id(a))


# dic = {'Name': 'Jack', 'Age': 7, 'Class': 'First'}
#
# # 1 直接遍历字典获取键，根据键取值
# for key in dic:
#     print(key, dic[key])
#
# # 2 利用items方法获取键值对
# for key, value in dic.items():
#     print(key, value)
#
# # 3 利用keys方法获取键
# for key in dic.keys():
#     print(key, dic[key])
#
# # 4 利用values方法获取值，但无法获取对应的键
# for value in dic.values():
#     print(value)




# def saySomething(name, word):
#     print(name + ' say: ' + word)
# saySomething(word="I love Python", name="ZhangSan")  # 关键字参数

# def saySomething(name, word):
#     print(name + ' say: ' + word)
# saySomething("ZhangSan", "I love Python")  # 位置参数

# print((lambda x,y,z:x+y+z)(3,4,5))


#翻转字符串
# my_string=input()
# my_list=list(my_string)
# my_list.reverse()
# my_string=''.join(my_list)
# print(my_string)

# print(input().upper()#小写转大写函数

# m=input("")
# a,b=m.split(" ")
# print(int(a)+int(b))

#同时输入a和b，以空格隔开
# a,b=map(int,input().split())
# print(a+b)

