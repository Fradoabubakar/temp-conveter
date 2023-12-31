def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    f_temp = float(input("Enter temperature in Fahrenheit: "))
    c_temp = fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F is equal to {c_temp:.2f}°C")
elif choice == 2:
    c_temp = float(input("Enter temperature in Celsius: "))
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is equal to {f_temp:.2f}°F")
else:
    print("Invalid choice")
