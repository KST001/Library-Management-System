import Return
import ListSplit
import DateTime
import Borrow


def Main_Menu():
    while(True):
        print(" _______________________________________________________")
        print("|\t\tLibrary Management System\t\t|")
        print("|-------------------------------------------------------|")
        print("| PRESS 1: Display all the Books                        |")
        print("| PRESS 2: Borrow a book                                |")
        print("| PRESS 3: Return a book                                |")
        print("| PRESS 4: Exit                                         |")
        print("|_______________________________________________________|\n")
        try:
            num = int(input("Select a choice from 1 to 4: "))
            print()
            if(num == 1):
                with open("Stock.txt", "r") as f:
                    lines = f.read()
                    print("*** Display all the Books ***")
                    print(lines)
                    
            elif(num == 2):
                ListSplit.List_Split()
                Borrow.Borrow_Book()

            elif(num == 3):
                ListSplit.List_Split()
                Return.Return_Book()

            elif(num == 4):
                print("*** Thank you for using Library Management System. ***")
                break

            else:
                print("Please enter a valid choice from 1 to 4: ")

        except ValueError:
            print("Please input as suggested number only.")


Main_Menu()
