# WA
MOD = 1000000007
D6 = 1000000

fat = [0] * (D6+2)
fat[0] = 1
fat[1] = 1

def preFat():
    for i in xrange(2,D6+2):
        fat[i] = (fat[i-1] * i) % MOD


preFat()

a, b, n = map(int, raw_input().split())


def calc(a, b, n):
    i = n
    f = 0
    soma = 0
    while i >= 0 and f <= n:
        numero = a*i + b*f
        print a, i, b, f, numero
        if isB(str(a), str(b), str(numero)):
            #print "haha"
            soma = (soma + qntd(i, f)) % MOD
            print soma, i, f, qntd(i, f)
        i -= 1
        f += 1
    if i == f: soma = soma / 2.0
    return soma


def qntd(i, f):
    #print fat[i+f], (fat[i]), fat[f]
    return fat[i+f] / ( ((fat[i] * fat[f]) % MOD) + 0.0)

def isB(a, b, n):
    
    setn = set(n)
    print n, setn, a, b
    return (len(setn) == 2 and (a in setn and b in setn)) or (len(setn) == 1 and (a in setn or b in setn ))
    
print int(calc(a, b, n))