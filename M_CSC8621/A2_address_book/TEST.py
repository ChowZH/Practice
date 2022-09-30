import os
import time

def clrscn ():
    time.sleep (1)
    os.system ("cls")

def dob_format (dob):
    dob_dig = dob[0] + dob[1] + dob[3] + dob[4] + dob[6] + dob[7] + dob[8] + dob[9]
    return dob_dig

# run = True

# while run == True:
#     user_in = input ("Try numbers 1, 2: ")
#     if user_in == "1":
#         run = True
#         print ("User entered 1")
#     elif user_in == "2":
#         run = True
#         print ("User entered 1")
#     else:
#         print ("Invalid")
#         run = False

# num_check = True # Checks for valid phone number
# while num_check == True:
#     new_num = input ("Please enter your phone number (44XXXXXXXXXX):\n")
#     if new_num.isdigit() == True and len(new_num) == 12:
#         new_num = int (new_num)
#         print (new_num)
#         num_check = False
#     else:
#         print (new_num)
#         print (len(new_num))
#         new_num = input ("Please enter a valid number (44XXXXXXXXXX):\n")

# def dob_format (dob):
#     dob_format = dob[0] + dob[1] + dob[3] + dob[4] + dob[6] + dob[7] + dob[8] + dob[9]
#     return dob_format

# dob = "05-07-1995"

# dob_check = True
# while dob_check == True:
#     formatted_dob = dob_format (dob)
#     if formatted_dob.isdigit() == True and len(formatted_dob) == 8 and dob[2] == "/" and dob[5] == "/":
#         print (formatted_dob)
#         dob_check = False
#     else:
#         print ("Invalid")
#         break

# __get_input = True
# while __get_input == True:
#     __user_input = input ("Select options 1, 2, 3:\n")
#     # Create new entry
#     if __user_input == "1":
#         entry_check = True
#         while entry_check == True:
#             clrscn()
#             # Get entry details
#             new_name = input ("Please enter your name:\n")
#             new_add = input ("Please enter your address:\n")
#             num_check = True # Checks for valid phone number
#             while num_check == True:
#                 new_num = input ("Please enter your phone number (44XXXXXXXXXX):\n")
#                 if new_num.isdigit() == True and len(new_num) == 12:
#                     new_num = int (new_num)
#                     num_check = False
#                 else:
#                     new_num = input ("Please enter a valid number (44XXXXXXXXXX):\n")
#             dob_check = True # Checks for valid dob
#             while dob_check == True:
#                 new_dob = input ("Please enter your birthday (dd/mm/yyyy):\n")
#                 dob_dig = dob_format (new_dob)
#                 if dob_dig.isdigit() == True and len(dob_dig) == 8 and new_dob[2] == "/" and new_dob[5] == "/":
#                     dob_check = False
#                 else:
#                     new_dob = input ("Please enter your birthday in the advised format (dd/mm/yyyy):\n")
#             clrscn()
#             print("Please check the entered details:\nName:\t{}\nAddress:\t{}\nPhone Num:\t{}\nBirthday:\t{}\n" .format(new_name, new_add, new_num, new_dob))
#             check_query_validity = True
#             while check_query_validity == True:
#                 check_query = input ("Are the details correct? (y/n)\t")
#                 if check_query.upper() == "Y":
#                     check_query_validity = False
#                     entry_check = False
#                 elif check_query.upper() == "N":
#                     check_query_validity = False
#                     entry_check = True
#                 else:
#                     check_query_validity = True
#                     check_query = input ("Please enter a valid response.\nAre the details correct? (y/n)\t")

f = open("DATABASE.in", "r")

# print ("1")
# count = 0
# for _ in f.readlines():
#     if "ID:" in _:
#         count += 1
#     print (count)

# f.close()

# for _ in f.readlines ():
#     if "Name:" in _:
#         for word in _.split():
#             print ("{}\t" .format(word), end = "")
#         print ("\r")

#     elif "ID:" in _:
#         for word in _.split():
#             print ("{}\t" .format(word), end = "")
#         print ("\r")

# keyword = "John"

# for _ in f.readlines():
#     if keyword in _:
#         print (_)

