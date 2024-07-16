# #<<<<<<<<<<<<< FUNCTIONS >>>>>>>>>>>>>>>>>>>>

# # creating a function
# def test():  
#     print('This is a function')

# # calling a function
# test()




# def test(num1, num2):
#     print(num1+num2)

# test(35,6)


# def avg_finder(lst):
#     # sum=0
#     # for item in lst:
#     #     sum += item
#     sum1 = sum(lst) 
#     length = len(lst)
#     avg = sum1/length
#     return avg
#     # print(f'Average of list : {sum1/len(lst)}')

# list1 = [25,4,5,85,96,3,6,12,52,5,74]
# list_avg = avg_finder(list1)
# print(f'Average of given list : {list_avg}')


# # QUIZ 1

# def sqr_list(lst):
#     sqr = []
#     for num in lst:
#         sqr.append(num**2)
    
#     print(sqr)

# list1 = [1,2,3,4,5,6]
# sqr_list(list1)


# LAMBDA FUNCTIONS

square = lambda x : x**2
print(square(5))


avg = lambda a : sum(a)/len(a)
list1 = [1,2,3,4,5,6]
print(avg(list1))


total_sum = lambda x,y : x+y
print(total_sum(20,20))