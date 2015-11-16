import numpy as np
from uncertainties import ufloat
from uncertainties import sqrt

L = 32.351*10**(-3)
C = 0.851*10**(-9)
Csp = 0.037*10**(-9)


Ckf = (9.99*10**(-9))*0.03
Ck = ufloat(9.99*10**(-9),Ckf)
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 33560
print("abw+:")
print((fpexp / fp *100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ckf = (8.00 * 10**(-9)) * 0.03
Ck = ufloat(8.00 * 10**(-9),Ckf)
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 34010
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(6.47 * 10**(-9),((6.47 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 34720
print("abw+:")
print((fpexp / fp *100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(5.02 * 10**(-9),((5.02 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 35210
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(4.00 * 10**(-9),((4.00 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 36500
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(3.00 * 10**(-9),((3.00 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 37590
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(2.03 * 10**(-9),((2.03 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 40320
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)

Ck = ufloat(1.01 * 10**(-9),((1.01  *10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * np.sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi *np.sqrt((L/((1/C)+(2/Ck)) + L * Csp))
fpexp = 30300
fnexp = 47170
print("abw+:")
print((fpexp / fp * 100)-100)
#print("abw-:")
#print(fnexp/fn *100)
