import numpy as np
from uncertainties import ufloat
from uncertainties import sqrt

L = ufloat(32.351 * 10**(-3), 0 )
C = ufloat(0.851 * 10**(-9), 0)
Csp = ufloat(0.037 * 10**(-9), 0)

fp = 1 / (2 * np.pi * sqrt(L * C))
print("fp ohne Csp:")
print(fp)

Ck = ufloat(9.99 * 10**(-9),(9.99 * 10**(-9)) * 0.03)
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 12
#abw = (nexp/nth * 100) - 100
#print("abw:")
#print(abw)

Ck = ufloat(8.00 * 10**(-9),(8.00 * 10**(-9)) * 0.03)
#fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2*(fn - fp))
#print("nth:")
#print(nth)
#nexp = 11
#abw = nexp/nth * 100 - 100
#print("abw:")
#print(abw)

Ck = ufloat(6.47 * 10**(-9),((6.47 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 9
#abw = nexp/nth * 100 - 100
#print("abw:")
#print(abw)

Ck = ufloat(5.02 * 10**(-9),((5.02 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 7
#abw = nexp/nth * 100 - 100
#print("abw:")
#print(abw)

Ck = ufloat(4.00 * 10**(-9),((4.00 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 6
#abw = nexp/nth * 100 - 100
#print("abw:")
#print(abw)

Ck = ufloat(3.00 * 10**(-9),((3.00 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 5
#abw = nexp/nth * 100 - 100
#print("abw:")
#print(abw)

Ck = ufloat(2.03 * 10**(-9),((2.03 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 4
#abw = nexp/nth * 100 -100
#print("abw:")
#print(abw)

Ck = ufloat(1.01 * 10**(-9),((1.01 * 10**(-9)) * 0.03))
fp = 1 / (2 * np.pi * sqrt(L * (C + Csp)))
#fn = 1 / (2 * np.pi * sqrt((L/((1/C)+(2/Ck)) + L * Csp))
#print("fp:")
#print(fp)
#print("fn:")
#print(fn)
#nth = (fn + fp) / (2 * (fn - fp))
#print("nth:")
#print(nth)
#nexp = 2
#abw = nexp/nth * 100 -100
#print("abw:")
#print(abw)
