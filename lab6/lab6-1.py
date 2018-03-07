def celsius_temp(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius
def main():
  fahrenheit=float(input("Enter temperature in Fahrenheit: "))
  print("The temperature in Celsius is: ",celsius_temp(fahrenheit))
main()