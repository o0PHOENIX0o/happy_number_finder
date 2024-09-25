def Happy_number(num):
    sum=0
    while num>0:
        rem=num%10
        sum = sum + rem*rem
        num=num//10
    if sum!=1 and sum!=4:
        return Happy_number(sum)
    else:
        return sum
while True:
    number = input('enter a number or Type Exit/Done/Quit to Stop :\n')
    if number.lower() in ['exit','done','quit']:
        print('\n\t\tProgram Terminated\n')
        break
    else:
        try:
            number=int(number)
            ans=Happy_number(number)
            if ans == 1:
                print(f'\n\t\t{number} is a happy number\n')
            else:
                print(f'\n\t\t{number} is not a happy number\n')
        except Exception as e:
            print('\n\t\t\tinvalid input\n')
