# ATM MACHINE 

# available_bal = 5000
# message = """
# Enter 1 for checking balance
# Enter 2 for depositing amount
# Enter 3 for withdrawl amount
# """
# print(message)


# task = int(input('Enter your task: '))

# if task == 1 :
#     # CHECK BALANCE
#     print('Available Balance: ', available_bal)
# elif task == 2:
#     # DEPOSITE
#     deposite_amt = int(input('Enter amount to be deposited: '))
    
#     if deposite_amt > 0:
#         available_bal += deposite_amt
#         print(f'Amount deposited successfully : {deposite_amt} ')
#         print(f'Current Available Balance : {available_bal}')
#     else:
#         print('Please enter valid amount')

# elif task ==3:
#     # WITHDRAWL
#     withdraw_amt = int(input('Enter amount you want to withdraw : '))
   
#     if withdraw_amt <= available_bal:
#         available_bal -= withdraw_amt
#         print(f'Successfully withdrew amount : {withdraw_amt}')
#         print(f'Current available balance : {available_bal}')
#     else:
#         print('Available balance is not sufficient')

# else:
#     print('Enter valid task')



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FOR LOOP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


# using for loop in range

# for i in range(10):
#     print(i)

# list1 = list(range(20))
# print(list1)

# list1 = [10,20,30,40,50]

# for item in list1:
#     print(item)

# for item in list1:
#     if item == 40:
#         print('40 is present')

# tuple1 = (10,20,30,40,50)

# for item in tuple1:
#     print(item)

# string1 = "Arham Jain"

# for char in string1:
#     print(char)

# dict1 = {
#     'Name' : 'Arham',
#     'Branch' : 'CSE',
#     'Roll_No.' : 47
# }
        

# print(dict1.keys())
# print(dict1.values())

# for char in dict1.values():
#     print(char)

# list1 = [12,4,25,1,63,58,4,5,85,96,45,74,87,12]

# target = int(input('Enter the element to be searched : '))

# for item in list1:
#     if item == target:
#         print('Is present')

# even = 0
# for num in list1:
#     if num%2 != 0:
#         even += 1

# print(f'total no. of odd numbers = {even}')


# <<<<<<<<<<<<<<<<<<<<<< WHILE LOOP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

# i = 0

# while i < 10:
#     print(i)
#     i += 1

# condition = True
# while condition:
#     print('Hello World')
#     condition = False


# break and continue keywords

# for i in range(21):
#     print(i)
#     if i == 10:
#         break

# for i in range(21):
#     if i == 10:
#         continue
#     print(i)



# <<<<<<<<<<<<<<<<  QUIZ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## QUIZ 1

num = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for item in num:
    sum += item

print(f'Average of list : {sum/len(num)}')


## QUIZ 2

num2 = [12,3,4,1,15,28,29]

max = num2[0]

for i in num2:
    if i>max:
        max = i

print(f'Maximum no. in list : {max}')
    

min = num2[0]

for i in num2:
    if i<min:
        min = i

print(f'Minimum no. in list : {min}')
    
