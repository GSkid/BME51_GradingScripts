#@author: Grant Skidmore
#get the inputs
Ru = input("Ru: ") #first get the values of all the variables from the input values
Rd = input("Rd: ") 
Cu = input("Cu: ")
Cd = input("Cd: ")

#calculate and print the outputs
f_lo = (1/(2*3.14159265)) * (1/((float(Rd)*float(Cu) + float(Rd)*float(Cd) + float(Ru)*float(Cu))))
print("f_lo = ")
print(f_lo)
f_hi = (1/(2*3.14159265)) * ((1/(float(Ru)*float(Cd))) + (1/(float(Ru)*float(Cu))) + (1/(float(Rd)*float(Cd))))
print("f_hi = ")
print(f_hi)
gain = (float(Rd)*float(Cu) / ((float(Rd)*float(Cu)) + (float(Ru)*float(Cu)) + (float(Rd)*float(Cd))))
print("gain = ")
print(gain)
