val=int(input("Enter the temperature value\n"))
val_unit=input("Enter the unit of the input value: C for celcius and F for farenheit\n")
if val_unit=='C':
    value=((9/5)*val)+32
    print(val,"is equal to",value)
elif val_unit=='F':
    value=(val-32)*(5/9)
    print(val,"is equal to",value)
else:
    print("Invalid unit. Please choose C for celcius or F for Farenheit\n")