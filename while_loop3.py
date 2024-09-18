sum1=0
count1=0

while True:
    
    user_choice=input("Enter numbers to add or press 'N' to exit: ")
    if user_choice=='N':
        break
    
    sum1=sum1+int(user_choice)
    count1=count1+1
    
print('The sum of numbers is:', sum1)
print('Count of entries is:', count1)