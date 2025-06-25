def celsius_para_fahrenheit(celsius):
  """Converte graus Celsius para Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def celsius_para_kelvin(celsius):
  """Converte graus Celsius para Kelvin."""
  kelvin = celsius + 273.15
  return kelvin

temperatura_celsius = 25
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)

print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")
print(f"{temperatura_celsius}°C é igual a {temperatura_kelvin}K")