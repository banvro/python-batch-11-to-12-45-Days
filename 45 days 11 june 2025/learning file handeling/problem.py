# adding two numbers

# x = ?  ------> x.txt 
# y = ? -------> y.txt

# zx = read (x.txt)
# pq = read(y.txt)

# qq = zx + pq

# ---> store ---> ouput.txt

f1 = open("x.txt", "w")
num1 = input("Enter first number : ")
f1.write(num1)
f1.close()

f2 = open("y.txt", "w")
num2 = input("Enter second number : ")
f2.write(num2)
f2.close()

zx = open("x.txt", "r")
get_num1 = zx.read()
zx.close()

pq = open("y.txt", "r")
get_num2 = pq.read()
pq.close()

qq = int(get_num1) + int(get_num2)

str_qq = str(qq)

f3 = open("output.txt", "a")
f3.write(f"\n History : The sum of {get_num1} and {get_num2} is : {str_qq}")
f3.close()