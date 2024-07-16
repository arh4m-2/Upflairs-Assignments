def total_sum(num1, num2):
    sum = num1+num2
    return sum

def multiply(n1, n2):
    return n1*n2

ls = [25,1,45,8,5,96,36,45]

def avg_finder(lst):
    # sum=0
    # for item in lst:
    #     sum += item
    sum1 = sum(lst) 
    length = len(lst)
    avg = sum1/length
    return avg

if __name__ == '__main__':
    print('Hello world')


