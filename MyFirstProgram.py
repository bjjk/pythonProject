# name, surname, age = input("Please enter your name, surname, age ").split(", ")
#
# print(name)
# print(surname)
# print(age)

# a = 100
# b = 2.8
# c = True
# d = None
# e = "Hello world"
# print(str(a) + str(b) + str(c) + str(d) + e)

# a, b, c = input("Please enter sides A, B and C. Split with space. ").split()
# a, b, c = float(a), float(b), float(c)
# half_perimetr = (a + b + c) / 2
# triangle_area = (half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c)) ** 0.5
#
#
#
# print(triangle_area)

# a, b, c, d = input("Enter your name, surname, city, and birth year. Split with space. ").split()
# print("Hello, " + a + " " + b + ". You live in " + c + ". You are " + str(2021 - int(d)))


#22.06

# string_sample = "Hello world world world"
# string_sample2 = "first letteR is lowERCASE"
# string_sample3 = " extra whitespace string "
# some_string = "Hello"
# count = 2

# print(string_sample[0:5])
# print(len(some_string))
# print(type(len(some_string)))
# print(some_string in "Hello world")
# print('Hello world'.upper())
# print(string_sample.lower())
# print(string_sample2.strip("f"))                 #обрезает пробелы или знаки(ввести аргумент)по краям
# print(string_sample.replace(string_sample[6:], "planet"))                 #заменить слово(тип данных - строка)
# print(string_sample.replace(string_sample[6:], string_sample2[0:5]))
# print(string_sample.replace("world", "planet", count))                       #кол-во раз заменить
# print(string_sample.count("world"))
# count_number = string_sample.count("world", 0, 12)                         #кол-во слов
#
# found_index = (string_sample.find("world", 4, 12))
# print(string_sample[found_index:])

# string_slice = string_sample[0:5]
# print(string_slice)
# print(type(string_slice))

# a = "Your salary is"
# b = "1000"
# c = "2000"
# d = "3000"
# new_string = a + " " + str(b)
# formated_string = "Your slary is {2}, or {1}, or {0}"   #подставить индексы в скобках
# formated_string2 = "Your slary is {2}, or {2}, or {2}"   #подставить индексы в скобках
#
# print(new_string)
# print(formated_string.format(c, d, b))   #метод, при котором к скобках подставляется аргумент
# print(formated_string2.format(c, d, b))

# formatted_string = "This is {product:}. It costs {price:.2f}"                        #.2f дает два нуля после запятой
# print(formatted_string.format(product = "computer", price = 350.00))

# emp_name = "John"
# emp_age = 30
# emp_salary = 1500
# emp_string = f"Hello, my nam is {emp_name}. I am {emp_age} years old. My salary is {emp_salary}"
# print(emp_string)

#  byte_string = b'\xcf\x84o\xcf\...'
# print(byte_string.decode('utf-16'))

# same_string = 'Roman that\'s my name'
# print(same_string)


# id_code = input("Please enter your id: ")
# if len(id_code) == 11:
#     if id_code[0] != "3" and id_code[0] != "4":
#         print("Your ID is wrong")
#     else:
#         print("Your ID is " + id_code)
# elif len(id_code) > 11:
#     print("Your ID is too long")
# else:
#     print("Your ID is too short")


some_number = int(input("Please enter any number "))
if some_number % 2 == 0:
    print ("Even")
else:
    print("Odd")
number_square =  str(some_number ** 2)
print ("Square: " + number_square)
print(len(number_square))
