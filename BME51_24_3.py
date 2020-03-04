Rf = input("Rf: ") #first get the values of all the variables from the input values
Cf = input("Cf: ") #the source that helped me with the basics http://www.wikihow.com/Create-a-Very-Simple-Program-in-Python
Ri = input("Ri: ")
Ci = input("Ci: ")

f_lo = 1/(2*3.14159265) * 1/(float(Rf)*float(Cf)+float(Ri)*float(Ci))
print("f_lo = ")
print(f_lo)
f_hi = 1/(2*3.14159265) * (1/(float(Rf)*float(Cf)) + 1/(float(Ri)*float(Ci)))
print("f_hi = ")
print(f_hi)
gain = -(float(Rf)*float(Ci)) / (float(Rf)*float(Cf) + float(Ri)*float(Ci))
print("gain = ")
print(gain)
