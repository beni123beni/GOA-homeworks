# Easy:
# 1. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები.
for i in range(0,11):
    print(i)
# 2. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები.
for i in range(0,21):
    print(i)
# 3. for loop-ის გამოყენებით დაპრინტეთ 'GOA Best' 10-ჯერ.
for i in range(0,10):
    print("GOA BEST")

# Medium:
# 4. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ "hello (მომხმარებლის სახელი)" 5 ჯერ.
input1 = input("enter your name ")
for i in range(0,5):
    print("hello",input1)
# 5. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები, თითოეული გაყოფილი 2-ზე.

for i in range(0,21):
    i/=2
    print(i)
# 6. for loop-ის გამოყენებით დაპრინტეთ 15-მდე რიცხვები, თითოეული გამრავლებული 2-ზე.
sum1=0
for i in range(0,16):
    z=sum1+i
    print(z)

# Extreme:
# 7. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები, თითოეულის კვადრატი.
for i in range(0,11):
    print(i*i)
# 8. for loop-ის გამოყენებით დაპრინტეთ 10-მდე არსებული ყველა რიცხვის ჯამი, ეს ჯამი უნდა შეინახოს for loop-ის გარეთ შექმნილ ცვლად sum-ში.
sum=0
for i in range(0,11):
    sum+=i
print(sum)
    