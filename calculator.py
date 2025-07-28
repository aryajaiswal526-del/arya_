num1=int(input("How many values you want to operate?"))
numbers=[]
for i in range(num1):
    num=float(input(f"enter number{i+1}:"))
    numbers.append(num)
print("You have entered these numbers:",numbers)

command=input("what operation would you like to perform?\n a.Addition\n b.Substraction\n c.Multiplication\n d.Division\n e.Exponential\n f.Floor division\n g.Remainder\n") 
if command=='a':
    result=sum(numbers)
    print(result)
elif command=='b':
    result=numbers[0]
    for num in numbers[1:]:
        result -= num
    print(result)
elif command=='c':
    result=1
    for num in numbers:
        result *= num
    print(result)
elif command=='d':
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            print("sorry dude but can't divide by zero otherwise I'll go berserk.")
            result="BAKA!"
            break
        result /= num
    print(result)
elif command=='e':
    result=numbers[0]
    for num in numbers[1:]:
        try:
            result = result**num
        except OverflowError:
 print("Excuse me!! you can't ask for a domain expansion. That's too big for this realm.")
            result="BAKA!"
            break
    print(result)
elif command=='f':
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            print("sorry dude but can't floor divide by zero otherwise I'll go berserk.")
            result="BAKA!"
            break
        result //= num
    print(result)
elif command=='g':
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            print("sorry dude but can't modulo by zero otherwise I'll go berserk.")
            result="BAKA!"
            break
        result = result%num
    print(result,)
else:
    print("NANDEYO!\n Kindly enter a valid letter from the list if you really wish to\n PERFORM.AN.OPERATION\n BAKA!")
   
