# Comma Separated value CSV
# .text for text file 

# with open('massage.txt','w') as file:
#     file.write('i love python \n')
# with open('massage.txt','a') as file:
#     file.write('i love python \n')
with open('massage.txt','r') as file:
    # file.write('i love python \n')
    text =file.read()
    # print(text)

num = lambda a:a*a
print(num(2**2))