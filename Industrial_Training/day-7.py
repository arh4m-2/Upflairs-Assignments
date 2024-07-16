import os
# print(os.getcwd())
# print(os.listdir())
# os.mkdir('JECRC')
os.makedirs('JECRC2', exist_ok = True) # If the file is already present, it does not throw an error
path = r'C:\Users\Arham\OneDrive\Desktop\Industrial Training\JECRC'  # 'r' for raw string
os.chdir(path)
print(os.getcwd())

# open('test.txt', 'x')  # 'x' is mode for exclusive creation , failing if file already exists

# file = open('test.txt', 'w')
# data = 'Hello we are from JECRC'
# data2 = 'Hello jecrc'
#  file.write(data2)

# file = open('test.txt', 'r')
# data = file.read()
# file.close()
# print(data)

file = open('test.txt', 'a')
data = 'Hello this is a test message'
file.write(data)
file.close()



