#this is a calculator

num_list = []
while True:
    num = int(input("Enter a number: "))
    num_list.append(num)
    x = input("Do you want to continue? (yes/no): ")
    if x.lower() == "no":
        break
    elif x.lower() == "yes":
        continue
    else:
        print("Enter a valid command")
print("Final list:", num_list)
print("1. Adiition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
a = str(input("select the operator: "))
if a == "1":
    print("sum of the numbers is: ", sum(num_list))
elif a=="2":
    result = num_list[0]
    for i in range(1, len(num_list)):
        result -= num_list[i]
    print("Subtraction of the numbers is: ", result)
if a=="3":
    result1 = num_list[0]
    for i in range(1, len(num_list)):
        result1 *= num_list[i]
    print("multiplication of the numbers is: ", result1)
if a=="4":
    result2 = num_list[0]
    for i in range(1, len(num_list)):
        result2 /= num_list[i]
    print("Division of the numbers is: ", result2)

