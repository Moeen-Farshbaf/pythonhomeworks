import math
prompt = 'How many numbers are you going to work with?(max=2, for now))'
qnum= int(input(prompt))
if qnum > 2:
    print ('Sorry  we can only work with maximum two numbers.')

if qnum == 1:
    op = input("choose between sin,cos,tan,raise to sqaure. more options will be availble soon")
    num = int(input ("now choose the number:"))
    if op == 'sin':
        print ("Sinus of the choosen number is: "+str(math.sin(num)))
    # and so on...

if qnum == 2:
    op = input('choose between sum,sub,multiply,divide:')
    num1_2 = int(input ('Now enter the first number:'))
    num2_2 = int(input('Now enter the second number:'))
    if op == 'multiply' or 'x' or '*':
        print ('multiply of'+' '+str(num1_2)+' and '+str(num2_2)+' '+"is: "+str(num1_2*num2_2))
    #and so on...



