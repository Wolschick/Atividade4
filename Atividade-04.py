def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fact(n):
    if(n == 0 or n == 1): return 1
    val = 1
    for i in range(1, n+1):
        val = val*i
     
    return val


with open('arquivo.txt', 'r') as arquivo:
    archive = arquivo.read()

arquivo.close()

cont = 0
var = ''
[fib, fat, calc_fib, calc_fat] = [[], [], [], []]
for i in archive:
    if(i == ' '): 
        cont = 1
        for j in fib:
            var = var + j    
        calc_fib.append(fibo(int(var))+1)
        fib = []
        var = ''

    if(i == '\n'): 
        cont = 0
        for j in fat:
            var = var + j    
        calc_fat.append(fact(int(var)))
        fat = []
        var = ''

    if(cont == 0): fib.append(i)
    if(cont == 1): fat.append(i)

f = open("output.dat", "a")
  
for i in range(len(calc_fib)):

    f.write(str(calc_fib[i]) + ' ' + str(calc_fat[i]) + '\n')

f.close()
