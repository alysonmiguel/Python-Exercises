#
#for i in range(0, 11):
#    for j in range(1, 11):
#        print(i, 'X', j,  ' = ', (i*j))
#
#    print('*'*10)
#
#
#p = [1, 1, 2, 3, 3, 5, 1]
#v = []
#pi = int(input())
#pf = int(input())

#for i in range(pi-1, pf):
#        v.append(p[i])
#
#
#print(v)
 #    p.append(v[i])

#print(p.count(1))
#
#N = int(input('Tamanho da barra = '))
#M = int(input('Numero de sequência = '))
#
#vb = []
#vp = []
#vs = []
#for i in range(N):
#    vb.append(int(input('Barra {} '. format(i+1))))
#
#for i in range(M):
#    vp.append(int(input('Posição {} '. format(i+1))))
#
#for i in range(M+1):
#    pi = vp[i]
#    pf = vp[i+1]
#    for j in range(pi, pf):
#        vs.append(vb[j])
movimento = []
for i in range(1, 5):
    movimento.append(int(input('M {}'.format(i))))

print(movimento)
for i in range(5):
    pI = movimento[i]
    pF = movimento[i+1]
    print(pI, '---', pF)
