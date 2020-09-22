def calc_item(num1, num2, calc_op):
 print (str(num1))
 print (str(num2))
 print (str(calc_op))

 if calc_op == '+':
  calc_sum = num1 +  num2
 elif calc_op == '-':
  calc_sum = num1 - num2
 elif calc_op == '/':
  calc_sum = num1 / num2
 elif calc_op == '*':
  calc_sum = num1 * num2
 print('output : ' + str(calc_sum))

calc_list = ['*','+','-','/']
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

while True:
 calc_type = input("Enter the operation type : ")
 print(calc_type)
 if calc_type in calc_list:
   break

print ('num1      : ' + str(num1))
print ('num2      : ' + str(num2))
print ('Operation : ' + (calc_type))

calc_item(num1, num2, calc_type)

