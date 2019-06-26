def num2words(num):
    if num < 20: 
        return digits_dict[num]
    if num < 100:
        number_name = digits_dict[20+int(num/10)-2]
        if num%10 == 0:
            return number_name
        else:
            number_name = number_name + " " + digits_dict[num%10]
            return number_name
    if num < 1000:
        if num%100 == 0:
            return digits_dict[28+int(num/100)-1]
        else:
            number_name = digits_dict[28+int(num/100)-1] + " " + num2words(num%100)
            return number_name
    
    multiplier = (1000, 1000000, 1000000000, 1000000000000, 1000000000000000, 1000000000000000000, 1000000000000000000000)
    # Find the largest multiplier smaller than num
    maxmulti = max([multi for multi in multiplier if multi <= num])
    # Chcking inflection
    inflection = int(num / maxmulti) % 100
    if inflection > 10 and inflection < 20:
        eleven_19 = True
    else:
        eleven_19 = False
    inflection = int(num / maxmulti) % 10

    if int(num/maxmulti) == 1:
        number_name = str(digits_dict[37+multiplier.index(maxmulti)*3])   
    elif inflection > 1 and inflection < 5 and eleven_19 == False:
        number_name = str(num2words(int(num/maxmulti)) + " " + digits_dict[37+multiplier.index(maxmulti)*3+1])
    elif inflection < 2 or inflection > 4 or eleven_19 == True:
        number_name = str(num2words(int(num/maxmulti)) + " " + digits_dict[37+multiplier.index(maxmulti)*3+2])
    if num%maxmulti != 0:
        number_name = str(number_name + " " + num2words(num%maxmulti))
    return number_name


# wczytanie słownika
numbers = open ("numbers.txt", encoding='utf-8')
try:
    digits_dict= numbers.readlines()
finally:
    numbers.close()
# Usówanie znaków \n i spacji
i=0
while i < len(digits_dict):
    digits_dict[i]=digits_dict[i].rstrip()
    i += 1

liczba=int(input("Wprowadź liczbe: "))
print(num2words(liczba))
