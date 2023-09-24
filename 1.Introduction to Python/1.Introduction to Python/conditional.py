# in , not , not in , is , is not
# > < , >=, <=  ,== ,!= 
# python don't have the ++,-- operator 
# +=, -= , *=, /= 
# and or
a = 2
if a>10:
    print('Good luck')
elif a>5:
    print('Middle luck') 

elif a==2:
    print('khape khap')

else:
    print('Bad luck')


boss = False
if boss : 
    print("tal nia aitacii")
elif boss is not True:
    print('mar lathi ')

# Nested Condition 
if 2<3:
    print('sob thik ase ')
    if boss is True and a==2:
        print('i will do what i want')
        # same as nested loon the difference || == or and && just use english word instead of that symbol 
        
else:
    print('jibon tai vul')