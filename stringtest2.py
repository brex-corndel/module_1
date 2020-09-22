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

# print('output : ' + str(calc_sum))
 return(calc_sum)

with open('step3.txt', 'r') as f:
    lines = f.readlines()
    x = lines[0]
#    print(x)
    counter = 1
    end_loop = False
    while end_loop != True:
      with open("trail_file.txt","r") as t:
        trail_lines = t.readlines()
        if x in trail_lines:
          print ('Line Exists... Exit!')
          end_loop = True
      my_line = x.split()
      with open("trail_file.txt","a+") as t:
        t.write(x)
      print ('Current line : ' + str(my_line))
      next_line = (my_line[1])
      if str(next_line) != 'calc':
#        print('Goto... ' + str(next_line))
        x = lines[int(next_line)]
        print('Next line : ' + str(x))
        counter = counter + 1
      else:
        calc_op = my_line[2]
        num1 = float(my_line[3])
        num2 = float(my_line[4])
        next_line = int((calc_item(num1, num2, calc_op)))
        print('Calc...' + str(next_line))
        x = lines[int(next_line)]
        print('Next line : ' + str(x))
        counter = counter + 1
        if counter > 30:
          print ('30 Iterations...Exit!')
          end_loop = True
