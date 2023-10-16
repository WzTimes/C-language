#variable(变量)，每个变量指向一个值————与该变量相关联的信息
message="hello python world!"
print(message)

#变量的命名和使用
#1.变量名只能包含数字(0~9)、字母(Aa~Zz)和下划线(_)。变量可以使用字母和下划线作为开头，但不能以数字作为开头
# example：message_1(√)，1_message_2(×)
#2.变量名不能包含空格，但是可以使用下划线来分割其中的单词。
#example：hello_world(√), hello world(×)
#3.不要将python的关键字和函数名用作变量名。
#example：print不能作为变量名
#4.变量名应既简短又具有描述性。
#example: student_name比s_n具备更好的描述性
#5.慎用小写字母l和大写字母O，容易被认为数字1和0


#变量是标签（变量是可以被赋值的标签，或者说变量指向特定的值）



#字符串
#字符串是一系列字符。example："this is a string","this is also a string"

#修改字符串的大小写
#name.title()中，name后面的点(.)让python对name变量执行title()方法指定的操作
name="romeo"
print(name.title())

#全部大写/小写
name="Remeo"
print(name.upper())
print(name.lower())


#在字符串中使用变量
#这种字符串称为f字符串。f是format（设置格式）的简写
first_name="Romeo"
second_name="Juliet"
book_name=f"{first_name} and {second_name}"
print(book_name)
print(f"Hello, the book is {book_name}")
#也可以插入字符串的大小写规则
print(f"Hello, the book is {book_name.title()}")



#使用制表符或换行符添加空白
#\t
print("Python")
print("\tPython")
#\n
print("编程语言：\nR\nPython\nC#\C++\nJava")


#删除空白
#strip(剥除)函数
#在编写程序中，额外的空白字符可能会使人看了困惑。就好比"Python"和"Python "是两个不同的字符串
#1.找出能够找出字符串左端的和右端多余的空白
message="Did you study today?  "
message
print(message)
#rstrip和lstrip这种删除只是暂时的，如果再次访问message的值，这个字符串的内容与输入的时候是保持一致的
message.rstrip()
message
message="  Did you study today?"
message.lstrip()
message

#2.永久删除字符串中的空白，必须将删除操作的结果关联到变量
message="Did you study today?  "
message=message.rstrip()
message


#删除前缀
#假设有一个URL包含常见的前缀https://,你想删除这个前缀，只关注用户需要输入的地址栏部分
new_url='https://abc.com'
new_url=new_url.removeprefix('https://')

#一般部分浏览器的地址栏看不到包含https://部分的URL,可能是浏览器在幕后使用了类似于removeprefix()方法。

#数据类型
#数
#1.整数
#可以对整数执行加(+)减(-)乘(*)除(/),乘方(**)
#2.浮点数(带有小数点的数)
#3.整数和浮点数的运算，如果包含浮点数，默认得到的结果为浮点数
#4.数中的下划线
#打印这种下划线定义的数字时，python不会打印其中的下划线
number=123_456_789
print(number)
#5.同时给多个变量赋值
x,y,z=1,2,3
print(x,y,z)
#6.常量:在程序的整个生命周期内保持不变的变量。