import string

def recognize (index, word):
    if word.isalpha() == True:
        if word.isupper() == True and all(True if i in romannum_dict else False for i in word) == True:
            return 0
    if word.isdigit() == True and len(words_source) > index+1 and words_source[index+1] != "-" and words_source[index+1] != "–":
            return 2
    if word.count(":") == 1 and 4 <= len(word) <= 5 :
        return 4
    if word.count("/") == 2 or word.count(".") == 2 or word.count("-") == 2 or word.count("–") == 2:
        if word[:1].isdigit() == True and word[-1:].isdigit() == True:
            return 5
        else:
            return -1
    if word.count("-") == 1 or word.count("–") == 1:
        if index > 0  and len(words_source) > index+1 and word[0].isdigit() == False:
            if words_source[index-1].isdigit() == words_source[index+1].isdigit() == True :
                return 6
        if word[0].isdigit() == word[-1].isdigit() == True:
            return 7
        if len(words_source) > index+1 and words_source[index+1].isdigit() == True == word[0].isdigit() :
            return 8
    for i in word:
        if i.isdigit() == True:
            return 9
    else:
        return -1

def num2words (num):
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
    # Checking inflection
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

def read_number (word):
    number_name=""
    for digit in word:
        if digit == "0":
            if number_name == "":
                number_name = "zero "
            else:
                number_name = number_name + "zero "
        else:
            break
    if int(word) > 0:
        number_name = number_name + num2words(int(word))
    return number_name.strip()

def read_time (word):
    mid_position = word.find(":")
    hour_name=""
    if mid_position == 1 :
        word = "0"+ word
    # Czytanie godzin -------- jest słownik a nie potrzeba
    if int(word[0:2]) <= 20:
        hour_name = "godzina " + hours_dict[int(word[0:2])]
    elif int(word[0:2]) <= 24:
        hour_name = "godzina " + hours_dict[20] + " " + hours_dict[int(word[0:2])%10]
    # Czytanie minut
    if int(word[3:]) == 0:
        return hour_name
    else:
        hour_name = hour_name + " " + read_number(word[3:])
    return hour_name

def read_date (word):
    date_name=""
    #separate_char = ""
    numbers = ["", "", ""]
    temp = 0
    for i in str(word):
        if i.isdigit() == True:
            numbers[temp] = numbers[temp] + i
        else:
            #separate_char = i
            temp += 1
    temp = 0
    for i in range(3):
        numbers[i] = int(numbers[i])
    if numbers[0] > numbers[2]:
        temp = numbers[0]
        numbers[0] = numbers[2]
        numbers[2] = temp
    if numbers[0]>31 or numbers[1]>12:
        return "OUT OF RANGE"

    # czytanie dni
    if numbers[0] <= 20:
        date_name = dates_dict[numbers[0]-1] + " "
    else:
        date_name = dates_dict[int(numbers[0]/10)+17] + " "
        if numbers[0]%10 != 0:
            date_name = date_name + dates_dict[numbers[0]%10] + " "
    
    # czytanie miesięcy
    date_name += dates_dict[numbers[1]+20] + " "

    # czytanie lat
    if numbers[2]%100 == 0:
        if numbers[2]%1000 == 0:
            date_name += dates_dict[int(numbers[2]/1000)+68] + " "
        elif numbers[2]%100 == 0 and numbers[2]>1000: 
            date_name += num2words(int(numbers[2]/1000)*1000) + " " + dates_dict[int(numbers[2]%1000/100)+59] + " "
        else:
            date_name += dates_dict[int(numbers[2]/100)+59] + " "
    elif numbers[2]>100:
        date_name += num2words(int(numbers[2]/100)*100) + " "
        if numbers[2]%100 < 20:
            date_name += dates_dict[int(numbers[2]%100)+32] + " "
        else:
            date_name += dates_dict[int(numbers[2]%100/10)+50] + " " + dates_dict[int(numbers[2]%10)+32] + " "
    else:
        if numbers[2]%100 < 20:
            date_name += dates_dict[numbers[2]+32] + " "
        else:
            date_name += dates_dict[int(numbers[2]/10)+50] + " " + dates_dict[numbers[2]%10+32] + " "
    return date_name + "roku"

def roman2arabic(roman):
    arabic = [romannum_dict[i] for i in roman if i in romannum_dict]
    return sum(i if i>=arabic[min(j+1, len(arabic)-1)] else -i for j,i in enumerate(arabic))

def read_ranges(index, typ_range):
    if typ_range == 6 :
        result = "od " + num2words(int(words_source[index-1])) + " do " + num2words(int(words_source[index+1]))
        nrl_result[index-1] = ""
        words_source[index+1] = ""
        return result
    if typ_range == 7:
        numbers_range = ["", ""]
        temp=0
        for i in str(words_source[index]):
            if i.isdigit() == True:
                numbers_range[temp] = numbers_range[temp] + i
            else:
                temp += 1
        result = "od " + num2words(int(numbers_range[0])) + " do " + num2words(int(numbers_range[1]))
        return result
    if typ_range == 8:
        words_source[index] = words_source[index].strip("-")
        words_source[index] = words_source[index].strip("–")
        result = "od " + num2words(int(words_source[index])) + " do " + num2words(int(words_source[index+1]))
        words_source[index+1] = ""
        return result        

def text_num_read(word):
    split_text = []
    temp=[-1,2]
    for i in word:
        if i.isdigit() == True:
            if temp[1]==0:
                split_text[temp[0]] +=  i
            else:
                temp[0] += 1
                temp[1] = 0
                split_text.append(i)
        else:
            if temp[1] == 1:
                split_text[temp[0]] +=  i
            else:
                temp[0] += 1
                temp[1] = 1
                split_text.append(i)
    #sprawdzanie wymowy
    for i,j in enumerate(split_text):
        if j.isdigit()==True:
            split_text[i] = read_number(j)
        elif j.lower() in shorts_dict :
            split_text[i] = shorts_dict[j.lower()]
    return split_text
    
###############################################
# Wprowadzenie tekstu
text_source = input("Wprowadź tekst: ")
# split into words by white space
words_source = text_source.split()

words_source = [words_source[i].strip() for i in range(len(words_source))]
words_source = [words_source[i].strip(",") for i in range(len(words_source))]

# Dictionary
mapping_dict = "dictionary.txt"
mapping_lines = [l.strip() for l in open(mapping_dict, encoding='utf-8')] 
# Digits Dictionary
digits_dict = mapping_lines[:(mapping_lines.index("##$$**HOURS**$$##"))]
# Hours Dictionary
hours_dict = mapping_lines[(mapping_lines.index("##$$**HOURS**$$##")+1):(mapping_lines.index("##$$**DATES**$$##"))]
# Dates Dictionary
dates_dict = mapping_lines[(mapping_lines.index("##$$**DATES**$$##")+1):(mapping_lines.index("##$$**ROMANNUM**$$##"))]
# Roman numbers Dictionary
romannum_dict = {k: int(v) for k, v in (l.split() for l in mapping_lines[(mapping_lines.index("##$$**ROMANNUM**$$##")+1):(mapping_lines.index("##$$**SHORTSDOT**$$##"))])}
# Dictionary shorts with dot
shorts_dot_dict = {k: v.replace("_", " ") for k, v in (l.split() for l in mapping_lines[(mapping_lines.index("##$$**SHORTSDOT**$$##")+1):(mapping_lines.index("##$$**SHORTS**$$##"))])}
# Dictionary shorts
shorts_dict = {k: v.replace("_", " ") for k, v in (l.split() for l in mapping_lines[(mapping_lines.index("##$$**SHORTS**$$##")+1):(mapping_lines.index("##$$**END**$$##"))])}

nrl_result = []

# Przetwarzanie textu
for i, j in enumerate(words_source):
    temp_skip = False
    if len(j) > 0 and j[-1]=="." :
        if j.lower() in shorts_dot_dict:
            nrl_result.append(shorts_dot_dict[j.lower()])
            temp_skip = True
        else:
            j=j.strip(".")
            j=j.lower()
            words_source[i]=j
    if temp_skip == False and len(j) > 0: 
        re_option = recognize(i, j)
        if re_option == 0 :
            j= roman2arabic(j)
            nrl_result.append(num2words(j))
        elif re_option == 2 :
            nrl_result.append(read_number(j))
        elif re_option == 4 :
            nrl_result.append(read_time(j))
        elif re_option == 5 :
            nrl_result.append(read_date(j))
        elif 6 <= re_option <= 8 :
            nrl_result.append(read_ranges(i, re_option))
        elif re_option == 9 :
            nrl_result.extend(text_num_read(j))
        elif j in shorts_dict :
            nrl_result.append(shorts_dict[j])
        elif j.lower() in shorts_dict :
            nrl_result.append(shorts_dict[j.lower()])
        else :
            nrl_result.append(j.lower())

final_string = ""
for i in range(len(nrl_result)):
        final_string += " " + nrl_result[i]

final_string = final_string.translate(str.maketrans('', '', string.punctuation))
final_string = final_string.strip()

# Tekst wynikowy
print("FINISH")
print(final_string)
input()