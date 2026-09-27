def celcius_to_fahrenheit(celcius):
    fahrenheit=(celcius*(9/5))+32   
    print("Temperature is ",celcius,"in celcius and",round(fahrenheit,2),"in fahrenheit")

temp=int(input("Enter the temperature in celcius: "))
celcius_to_fahrenheit(temp)
