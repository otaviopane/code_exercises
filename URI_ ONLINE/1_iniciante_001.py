# 1010
pcas1 = input().split()
pcas2 = input().split()
valor = (float(pcas1[1])*float(pcas1[2]))+(float(pcas2[1])*float(pcas2[2]))
print(f'VALOR A PAGAR: R$ {valor:.2f}')

# 1011
R = float(input())
pi = 3.14159
vol = (4/3) * pi * R**3
print(f'VOLUME = {vol:.3f}')

# 1012
val = input().split()
A = float(val[0])
B = float(val[1])
C = float(val[2])
pi = 3.14159
tri = (A*C)/2
cir = pi * C**2
tra = (A+B)/2*C
qua = B**2
ret = A*B

print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')

# 1013
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
val = sorted([a, b, c])
print(f'{val[-1]} eh o maior')

# 1014
X = int(input())
Y = float(input())
cons = X / Y
print(f'{cons:.3f} km/l')

# 1015
p1 = input().split()
p2 = input().split()
x1, y1, x2, y2 = float(p1[0]), float(p1[1]), float(p2[0]), float(p2[1])
dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f'{dist:.4f}')

# 1016
