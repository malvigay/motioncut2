val=int(input("Enter the temperature value\n"))
val_unit=input("Enter the unit of the input value: C for celcius and F for farenheit\n")
if val_unit.upper()=='C':
    value=((9/5)*val)+32
    print(val,"C is equal to",value,"F")
elif val_unit.upper()=='F':
    value=(val-32)*(5/9)
    print(val,"F is equal to",value,"C")
else:
    print("Invalid unit. Please choose C for celcius or F for Farenheit\n")