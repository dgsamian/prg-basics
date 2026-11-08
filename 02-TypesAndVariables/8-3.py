###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

stopnie_celcjusza = float(input('Wpisz temperature w stopniach Celcjusza: '))
kelviny = stopnie_celcjusza + 273.15
farenheity = (stopnie_celcjusza * (9/5)) + 32

print(f'Celcjusza: {stopnie_celcjusza} C, Kelviny: {kelviny} K, Farenheita: {farenheity} F')