
# print("hello world")
# sum = 0
# for i in range(10):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)

# sum(i for i in range(10) if i%3==0 or i%5==0)
# sum(i for i in range(100) if i % 3 == 0 or i % 5 == 0)


# def calculate():
#     sum(i for i in range(100) if i % 3 == 0 or i % 5 == 0)


# calculate()
# hw
# ispallindrome(pro)

# return true/false
# calculate(2)
# projecteullar
# def isPalindrome(num):
#     rev = ''.join(reversed(num))
#     if (num == rev):
#         return True
#     return False


# num = str(1234321)
# ans = isPalindrome(num)
# if (ans):
#     print("yes")
# else:
#     print("no")


# second class of web
# f = open('p022_names (1).txt', 'r')
# a = str(f.readlines())
# st = a.split(',')
# names = []
# names.append(st)
# size = len(st)
# print(names)
# print(size)
class Euler():
    def __init__(self):
        self.rule = self.generate_rule()

    def read_file(self):
        f = open('home.txt', 'r')
        a = f.readlines()
        # print(self.a)
        f.close()
        names = a[0].split(',')
        refineddNames = []
        for name in names:
            refineddNames.append(name.strip('"'))
        return refineddNames

    def calculate_overall_score(self):
        print("caculating score")
        names = self.read_file()
        names.sort()
        overall_score = 0
        for name in names:
            name_score = self.find_score(name)
            position = names.index(name)+1
            product = name_score*position
            overall_score = overall_score+product
        print(overall_score)

    def find_score(self, name):
        sum = 0
        for letter in name:
            sum = sum+self.rule[letter]
        return sum

    def generate_rule(self):
        st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {}
        for i in range(26):
            d[st[i]] = i+1
        return d


euler = Euler()
euler.calculate_overall_score()
