a = 2
b = 10
c = 2
d = 10


for j in range(c, d+1):
    print('\t', j, end='')
print()
for i in range(a, b+1):
    print(i, end='\t')
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()



#
# for j in range(c, d+1):
#     print('\t', j, end='')
# for i in range(a, b+1):
#     print()
#     print(i, end='\t')