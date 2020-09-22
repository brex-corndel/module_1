def calc_item(num1, num2, calc_op):
# print (str(num1))
# print (str(calc_op))
# print (str(num2))

 global calc_sum

 if calc_op == '+':
  calc_sum = num1 +  num2
 elif calc_op == '-':
  calc_sum = num1 - num2
 elif calc_op == '/':
  calc_sum = num1 / num2
 elif calc_op == '*':
  calc_sum = num1 * num2

# print('output : ' + str(calc_sum))
 return(calc_sum)


with open('step3.txt', 'r') as f:
    data = f.readlines()
    tot_count = 0
    end_loop = False
    goto_line = 1
    x = data(int(goto_line))
    while end_loop == False:
      l = x.split()
      is_calc = l[1]
      print('input  : ' + str(x))
      if is_calc == 'calc':
        calc_type = l[1]
        calc_op   = l[2]
        num1      = float(l[3])
        num2      = float(l[4])
#       print(calc_type)
#       print(calc_op)
#       print(str(num1))
#       print(str(num2))
        goto_line = int((calc_item(num1, num2, calc_op)))
        print(goto_line)
      else:
        goto_line = l[1]
        print('go to : ' + int(goto_line))
#     next_line = data(goto_line)
#      x = data(int(goto_line))
#     print(str(next_line))
