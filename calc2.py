def calc_item(num1, num2, calc_op):
# print (str(num1))
# print (str(num2))
# print (str(calc_op))

 global calc_sum

 if calc_op == '+':
  calc_sum = num1 +  num2
 elif calc_op == '-':
  calc_sum = num1 - num2
 elif calc_op == '/':
  calc_sum = num1 / num2
 elif calc_op == '*':
  calc_sum = num1 * num2

 print('output : ' + str(calc_sum))
 return(calc_sum)


with open('step2.txt', 'r') as f:
    data = f.readlines()
    tot_count = 0
    for x in data:
      print('input  : ' + str(x))
      l = x.split()
#      print(l[0])
#      print(l[1])
#      print(l[2])
#      print(l[3])
      calc_op = l[1]
      num1 = float(l[2])
      num2 = float(l[3])
#      print(calc_op)
      tot_count = tot_count + (calc_item(num1, num2, calc_op))
print('TOTAL : ' + str(tot_count))
