n = int(input())

ending_a = ['2', '3', '4']
ending_a_exceptions = ['12', '13', '14']

def scl(n=n):
    n = str(n)
    if n[len(n)-1] in ending_a and not n[len(n)-2:] in ending_a_exceptions:
        return print(n, 'программиста')
    if n[len(n)-1] == '1' and n[len(n)-2:] != '11':
        return print(n, 'программист')
    else:
        return print(n, 'программистов')

scl()



