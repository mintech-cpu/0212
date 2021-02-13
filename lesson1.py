print("Good evening")
print("Good morning")
print("Good afternoon")

num = 1
print(num)

#数値型
num01 = 123
num02 = 1.23

print(type(num01))
print(type(num02))

string_a = "Hello, World!"

print(string_a)
print(type(string_a))

a = 10
b = 1

bool01 = (a > b)

print(bool01)
print(type(bool01))

a = ["sato", "suzuki", "takahashi"]

a[1] = "tanaka"

print(a[0])
print(a[1])
print(a[2])

a = [["sato", "suzuki", "takahashi"],["wakahashi"]]
print(a[0][0])
print(a[1][0])

x = 8
y = 3
print(x >= 5 and x <= 10)
print(y >=5 or y <=10)

# 複合代入演算子
x = 8
y = 12
z  = 20

x += 10
z += y

print(x)
print(z)

print('#################')

#if文
age = 0

if age >= 20:
    print("adult")
elif age == 0:
    print('baby')
else:
    print('child')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#for文
for a in range(5):
    a += 1
    print(a)


for i in range(5):
    if i == 3:
        break
    print(i)

#for文のネスト
for i in range(3):
    for r in range(3):
        print(i, r, sep="-")

class Student:
    def __init__(self, name):
        self.name = name

    def calculate_avg(self, data):
        sum = 0
    
    for num in data:
        sum += num
    avg = sum/len(data)
    return avg

# judgeメソッド
    def judge(self, avg):
        if avg >= 60:
            print('passed')
        else:
            print(failed)
        return result

a001 = Student('sato')
data = [70, 65, 50, 90, 30]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name + ' ' + result)

def say_hello(greeting):
    print(greeting)
say_hello('Hello World')

def num(a, b, c):
    return(a + b + c)/3
print(num(9, 4, 2))

def num(a, b, c):
    print((a + b + c)/3)
num(9, 4, 2)

class Student:
    def avg(self):
        print((80 + 70)/2)
a001= Student()
a001.avg()

class Student:
    def __init__(self, name):
        self.name = name

    def avg(self, math, english):
        print((math + english)/2)

a001= Student('sato')
print(a001.name)
a002= Student('to')
print(a002.name)

a001.avg(80, 70)
a001.avg(30, 70)

print('#################')

class Student:
    def __init__(self, name):
        self.name = name
    
    def calculate_avg(self, data):
        sum = 0

        for num in data:
            sum +=  num
        
        avg = sum/len(data)
        return avg
    
    def judge(self, avg):
        if avg >= 60:
            result = 'passed'
        else:
            result = 'failed'
        return result

a001 = Student('sato')
data = [70, 65, 50, 90, 30]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name,result)

class Student:
    def __init__(self, name):
        self.name = name
    
    def calculate_avg(self, data):
        sum = 0

        for num in data:
            sum += num
        
        avg = sum/len(data)
        return avg
    
    def judge(self, avg):
        if avg >= 60:
            result = 'passed'
        else:
            result = 'failed'
        return result

a001 = Student("watanabe")
data = [70,60,50,60,77]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg)
print(a001.name, result)
    