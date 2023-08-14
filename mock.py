import random

def counter(string):
    chars = list(string)
    count = {}

    for i in chars:
        count[i] = count.get(i,0) + 1

    print(count)

counter('aaabbccd[5]')

def passgen(num_al,num_n,num_spl):
    al = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n = list('0123456789')
    spl = list('!@#$%^&*()_+{-=}[]:;<?>/')
    s = []
    
    for i in range(num_al):
        v = random.choice(al)
        s.append(v)
        al.remove(v)

    for i in range(num_n):
        v = random.choice(n)
        s.append(v)
        n.remove(v)

    for i in range(num_spl):
        v = random.choice(spl)
        s.append(v)
        spl.remove(v)

    
    random.shuffle(s)
    s = ''.join(s)
    print(s)


passgen(6,5,4)