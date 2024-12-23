numbers = [2, 4, 6, 8, 10]
product = numbers[0] * numbers[3]
print(product)  # 16

strings = ["ერთი", "ორი", "სამი", "ოთხი", "ხუთი", "ექვსი", "შვიდი"]
middle_string = strings[len(strings) // 2]
print(middle_string)  # ოთხი

string_var = "გამარჯობა"
second_char = string_var[1]
print(second_char)  # ა

products = ["ჩიფსები", "შოკოლადი", "სოდა", "ნაჭრები", "ჩაი"]
print("გთხოვთ აირჩიოთ პროდუქტი (1-5):")
print("1: ჩიფსები")
print("2: შოკოლადი")
print("3: სოდა")
print("4: ნაჭრები")
print("5: ჩაი")
choice = int(input("შეიყვანეთ თქვენი არჩევანი: "))
if 1 <= choice <= 5:
    print("თქვენი არჩეული პროდუქტი არის:", products[choice - 1])
else:
    print("არასწორი არჩევანი.")

