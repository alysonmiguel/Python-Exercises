N = int(input())
M = int(input())
barra = []
movimentos = []
freq = [0,0,0,0,0,0,0,0,0,0]

for i in range(1, N+1):
    barra.append(int(input('B {}'.format(i))))
for i in range(1, M+1):
    movimentos.append(int(input('P {}'.format(i))))

for i in range(M+2):
    pI = movimentos[i]
    pF = movimentos[i+1]

    if (i > 1 and pF > pI): pI + 1
    if (i > 1 and pF < pI): pI - 1

    if(pF > pI):
        for j in range(pI, pF):
            freq[barra[j]] += 1
    elif (pF < pI):
        for j in range(pI, pF, -1):
            freq[barra[j]] += 1

for i in range(9):
    print(freq[i])




