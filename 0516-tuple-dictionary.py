#t1 = (123, 44, 99, "abc")
#print(t1)
#print(t1[-1])

price = {'Pb95':5.42, 'Pb98':5.58, 'ON':5.36, 'LPG':1.99}
cash = float(input("Za ile zatankować?"))
for key, value in price.items():
    print(key, value, "zł, kupimy", round(cash/value,2), "l")

price['LPG'] = 2.30
price['AdBlue'] = 11.22
print(price)
