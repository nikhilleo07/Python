print('Exercise values in Celsius and Fahrenheit')
temp=[1200,2400,3700,4300,5500,6800,7200,8400,9700,10000]
for item in temp:
    cel=item-273.15
    far=1.8*(cel)+32
    print (f'The Kelvin temperature {item} converted into Celsius is {cel:.2f} and Fahrenheit is {far:.2f}'.format(cel,far))