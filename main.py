#
#
#
# Pharmacy Management System
# @author : SONU
# Language : Python (VERSION 3.7.2)
# Dated : 01-08-2019, 02-08-2019
# Special Thanks to : Michael Dawson, who has unknowingly helped me a lot by writing his book ! :-)
# User Interface : Character User Interface [CUI]
#
#
#






import sys
import random
from os import system #REQUIRED FOR CLEARING THE SCREEN (OS SENSITIVE !!!! : IT'S FOR WINDOWS)


def clear():
        
	_ = system('cls')



def display_menu():
        
        
	print("""
	\n\n
	____MENU____

	1 - Buy a medicine
	2 - Add Stock
	3 - Add medicine to an existing stock
	4 - Set Up File
	5 - Exit
		""")







def get_choice():
        #GETS THE USER CHOICE
	try:
		choice = int(input("Enter your choice : "))
		return choice
	except:
		print("Invalid input !! The Program will close now !")
		input("Press the ENTER key to continue...")
		sys.exit()






def open_file(file_name, mode):
        #OPENS A FILE
	try:
		the_file = open(file_name, mode)
	except IOError as e:
		print("The Required file is not found in the root directory ! Try choosing the File-Setup.")
		input("The Program will close now....Press any key to continue...")
		sys.exit()
	return the_file










def add_stock():
       #ADDS A NEW MEDICINE STOCK
       print("ADD A NEW MEDICINE STOCK :-")
       main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "r")
       pre_data = main_file.readlines()
       main_file.close()
       
       m_name = input("Enter the medicine stock name : ")
       m_name += "\n"

       while m_name in pre_data:
            #ALREADY EXISTING MEDICINES IN THE LIST
            print("That Stock already exists !")
            m_name = input("Enter the medicine stock name : ")
            m_name += "\n"

       try:
            m_stock = int(input("Enter currently available stock : "))
            m_price = int(input("Enter the price of each medicine : "))
       except:
            print("Unexpected input !!")
            input("The Program will close now...Press any key to continue...")
            sys.exit()


        #THE PRICE AND STOCK ARE ACCESSED VIA THE MEDICINE NAME INDEX
        #FOR STOCK IT IS 1+ MEDICINE_NAM INDEX, WHILE FOR PRICE IT IS 2+
	
       m_stock = str(m_stock)
       m_price = str(m_price)
       m_stock += "\n"
       m_price += "\n"
       #STRING CONVERSION IS IMPORTANT AS writelines() CAN'T WRITE INTEGER TO A TEXT FILE

       new_data = [m_name, m_stock, m_price]
       main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "a")
       main_file.writelines(new_data)
       main_file.close()
       print("OPERATION SUCCESSFULL !, stock added !!")
       input("Press the ENTER key to continue...")


def add_medicine():
       print("ADD MEDICINE:-")
       main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "r+")
       pre_data = main_file.readlines()
       
       main_file.close()
       
       m_name = input("Enter a stock name to add medicine : ")
       m_name += "\n"

       while m_name not in pre_data:
               print("The entered stock does not exist !, Try Again !")
               m_name = input("Enter a stock name to add medicine : ")
               m_name += "\n"

       try:
                print("MEDICINE FOUND SUCCESSFULLY !!")
                increment = int(input("Enter the number of medicines to be added :"))
       except:
                print("Unexpected input !! The Program will close now !")
                input("Press the ENTER key to continue...")
                sys.exit()
               
       m_index = pre_data.index(m_name)
       current = pre_data[m_index+1]
       current = current[0:len(current)-1] #OMITTING THE NEWLINE CHARACTER
       current = int(current)

        #HERE ONLY THE CURRENT STOCK IS NEEDED TO CONVERT TO (int) NOT THE PRICE
        #INT CONVERSION IS IMPORTANT TO DO CALCULATIONS
       
       current += increment

       current = str(current)
       current += "\n" #ADDING THE NEWLINE CHARACTER
       #STRING CONVERSION IS IMPORTANT AS writelines() CAN'T WRITE INTEGER TO A TEXT FILE

       pre_data[m_index+1] = current

       main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "w")
       #CAUTION ::: THIS FILE IS OPENED FOR THE SECOND TIME, THIS TIME ONLY FOR WRITING THE WHOLE DATA
       #CAUTION ::: writelines() erases the whole file, and then writes the content, 	access mode is set to "w"
       #PREVIOUSLY IT WAS OPENED TO CREATE THE pre_data LIST
       main_file.writelines(pre_data)
       main_file.close()
       print("OPERATION SUCCESSFULL, medicine added !!")
       input("Press the ENTER key to continue...")







def buy():
       print("BUY MEDICINE:-")
       main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "r+")
       pre_data = main_file.readlines()
       main_file.close()

       customer_name = input("Enter customer name : ")
       
       while not customer_name:
               customer_name = input("Please enter customer name : ")
               
       medicine = input("Enter the medicine to be bought :")

       
       while not medicine:
               medicine = input("Please enter the medicine to be bought :")
               
       medicine += "\n"

       if medicine not in pre_data:
               print("That medicine is currently not in stock ! :-( SORRY ")



       else:
                       
                       m_index = pre_data.index(medicine)
                       
                       m_stock = pre_data[m_index+1]
                       m_price = pre_data[m_index+2]
                       
                       m_stock = str(m_stock)
                       m_price = str(m_price)
                       m_price = m_price[0:len(m_price)-1]
                       m_stock = m_stock[0:len(m_stock)-1]

                       m_stock = int(m_stock)
                       m_price = int(m_price)

                       

                       if m_stock <= 0:
                               print("That medicine stock has no medicine left ! SORRY :-(")
                

                       else:
                               
                               try:
                                       no = int(input("Enter the No. of medicines to be bought : [Ex:- No. of bottles, etc] :"))
                               except:
                                       print("Unexpected input !! The Program will close now !")
                                       input("Press the ENTER key to continue...")
                                       sys.exit()

                               total_bill = m_price * no
                               m_stock = m_stock - no
                               
                               m_stock = str(m_stock)
                               m_price = str(m_price)
                               m_stock += "\n"
                               m_price += "\n"

                               pre_data[m_index+1] = m_stock
                               pre_data[m_index+2] = m_price
			
      				#CAUTION ::: THIS FILE IS OPENED FOR THE SECOND TIME, THIS TIME ONLY FOR WRITING THE WHOLE DATA
       				#CAUTION ::: writelines() erases the whole file, and then writes the content, 	access mode is set to "w"
				
                               main_file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "w")
                               main_file.writelines(pre_data)
                               main_file.close()
                               
                               print("OPERATION SUCCESSULL ! Here's the Bill...\n")
                               print("Customer name : ",customer_name)
                               print("Medicine bought : ",medicine)
                               print("Total price : Rs.",total_bill)
                               input("Press the ENTER key to continue...")
 





def setup():
        """SETS UP THE MAIN FILE"""
        print("WELCOME TO FILE SETUP....YOU ARE HERE PROBABLY YOU ARE USING THE APP FIRST TIME")
        print("A File named 'data.txt' will be created this folder...")
        input("Press the ENTER key to create the file :")
        file = open_file("C:/Users/NSAM/Desktop/Pharmacy_managment_system/data.txt", "a+")
        print("The file has been successfully created !! Please mind that if you modify that file",
              "then it will hamper your Pharmacy !! Please Please DON'T OPEN THAT FILE !! ")
        print("CONGRATS !!File Setup is Successfull ! Now you can manage your pharmacy via here !!")

        
        
def main():
        """THE PROGRAM STARTS HERE"""
        display_menu()
        choice = get_choice()
        while choice not in [1, 2, 3, 4, 5]:
                choice = get_choice()
        while choice < 5:
                if choice == 1:
                        clear()
                        buy()
                elif choice == 2:
                        clear()
                        add_stock()
                elif choice == 3:
                        clear()
                        add_medicine()
                elif choice == 4:
                        clear()
                        setup()

                clear()
                display_menu()
                choice = get_choice()
                while choice not in [1, 2, 3, 4, 5]:
                        choice = get_choice()
        if choice == 5: #EXIT PROGRAM
                clear()
                input("Press the ENTER key to exit....")


#PROGRAM STARTS HERE
########
main() #  
########
