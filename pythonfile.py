

# user input
# 1.code data
# 2.code validation
# 3exit
while True:
    try:
        user_code = input("Please enter your ID ")

        if len(user_code) != 11:
            raise UserWarning
            raise ValueError
            user_code = int(user_code)

    except ValueError:
        print("ID code you entered is not numeric")
        continue

    except UserWarning:
        print("ID you entered is wrong")
        continue

    else:
        user_choice = input("Please choose: \n"
                            "1. ID data \n"
                            "2. Validate \n"
                            "3. Exit ")

        if user_choice =="1":
            if int(user_code[0]) % 2 ==0:
                gender ="Female"
            else:
                gender = "Male"
            if user_code[0] == "1" or user_code[0] =="2":
                birth_cent = "18"
            elif user_code[0] == "3" or user_code[0] == "4":
                birth_cent = "19"

            date_birth = (user_code[5:7] + "." + user_code[3:5] + "." + birth_cent + user_code[1:3])
            print("You are " + gender)
            state_num = int(user_code[7:10])

            born = "You were born " + date_birth + " in "
            if state_num <= 10:
                print(born + "Kuresaare haigla")
            elif state_num >= 11 and state_num <= 19:
                print(born + "Tartu Ülikooli Naistekliinik")
            elif state_num >= 21 and state_num <= 150:
                print(born + "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)")
            elif state_num >= 151 and state_num <= 160:
                print(born + "Keila haigla")
            elif state_num >= 161 and state_num <= 220:
                print(born + "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla")
            elif state_num >= 221 and state_num <=270:
                print(born + "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)")
            elif state_num >= 271 and state_num <= 270:
                print(born + "Maarjamõisa kliinikum (Tartu), Jõgeva haigla")
            elif state_num >= 371 and state_num <= 420:
                print(born + "Narva haigla")
            elif state_num >= 421 and state_num <= 470:
                print( born + " Pärnu haigla")
            elif state_num >= 471 and state_num <= 490:
                print(born + "Haapsalu haigla")
            elif state_num >= 491 and state_num <= 520:
                print(born + "Järvamaa haigla (Paide)")
            elif state_num >= 521 and state_num <= 570:
                print(born + "Rakvere haigla, Tapa haigla")
            elif state_num >= 571 and state_num <= 600:
                print(born + "Valga haigla")
            elif state_num >= 601 and state_num <= 650:
                print(born + "Viljandi haigla")
            elif state_num >= 651 and state_num <= 700:
                print(born + "Lõuna-Eesti haigla (Võru), Põlva haigla")

            continue

        elif user_choice =="2":

            control_num = int(user_code[0]) * 1 + int(user_code[1]) * 2 + int(user_code[2]) * 3 + int(user_code[3]) * 4 \
                + int(user_code[4]) * 5 + int(user_code[5]) * 6 + int(user_code[6]) * 7 + int(user_code[7]) * 8 \
                + int(user_code[8]) * 9 + int(user_code[9]) * 1

            if control_num % 11 == int(user_code[10]) :
                print("Your ID is correct")
            elif control_num % 11 > 10:
                y = int(user_code[0]) * 3 + int(user_code[1]) * 4 + int(user_code[2]) * 5 + int(user_code[3]) * 6 \
                + int(user_code[4]) * 7 + int(user_code[5]) * 8 + int(user_code[6]) * 9 + int(user_code[7]) * 1 \
                + int(user_code[8]) * 2 + int(user_code[9]) * 3

                print("Your ID is correct")
            else:
                print("Id you entered is not correct")

            continue

        elif user_choice =="3":
            print("Good bye")
            break





