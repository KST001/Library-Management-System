import DateTime
import ListSplit


def Borrow_Book():

    success = False
    while(True):

        FirstName = input("Enter the First Name: ")
        if FirstName.isalpha():
            break
        print("Input alphabets")

    while(True):

        LastName = input("Enter the Last Name: ")
        if LastName.isalpha():
            break
        print("Input alphabets")

    t = "Borrow_" + FirstName + ".txt"

    with open(t, "w+") as f:
        f.write("\n")
        f.write(" *****************************************\n")
        f.write(" *\tLibrary Management System\t *\n")
        f.write(" *****************************************\n")
        f.write(" *"" Date:" + DateTime.Date() + "\t" "Time:" + DateTime.Time() + "\t *\n")
        f.write(" * Borrowed By: " + FirstName + " " + LastName + "\t\t *\n")
        f.write(" *****************************************\n")
        f.write(" * S.N. * Book Name \t\t\t *\n")
        f.write(" *****************************************\n")
        print("\nPlease select a option below:\n")

    while success == False:

        print("----------------List of all the Books----------------\n")

        for i in range(len(ListSplit.BookName)):

            print("Press:", i, " ", ListSplit.BookName[i], " ,",ListSplit.AuthorName[i], " ,", "$",ListSplit.Cost[i])

        try:
            num = int(input("...> "))
            try:
                count = 1
                if(int(ListSplit.Quantity[num]) > 0):
                    with open(t, "a") as f:
                        f.write(" * " + str(count) + ".\t  " + ListSplit.BookName[num] + "\t\t *\n")
                        print("Book is available !\n")

                    ListSplit.Quantity[num] = int(ListSplit.Quantity[num]) - 1

                    with open("Stock.txt", "w+") as f:
                        for i in range(3):
                            f.write(ListSplit.BookName[i] + "," + ListSplit.AuthorName[i] + "," + str(ListSplit.Quantity[i]) + "," + "$" + ListSplit.Cost[i] + "\n")

                    loop = True
                    count = 1
                    while loop == True:
                        with open(t, "r") as f:
                            detail = f.read()
                        choice = str(input("Do you want to borrow more books?\nPress [Y] for Yes and [N] for No: "))

                        if(choice.upper() == "Y"):
                            count = count + 1
                            print("Please select an option below:\n")
                            for i in range(len(ListSplit.BookName)):
                                print("Press:", i, " ", ListSplit.BookName[i]," ,", ListSplit.AuthorName[i], " ," , "$", ListSplit.Cost[i])

                            num = int(input("...> "))

                            if(int(ListSplit.Quantity[num]) > 0):

                                if ListSplit.BookName[num] in detail:

                                    print("*** Sorry! same book cannot be borrow ***\n")

                                else:

                                    print("Book is available !\n")
                                    with open(t, "a") as f:
                                        f.write(" * " + str(count) + ".\t  " + ListSplit.BookName[num] + "\t *\n")
                                        f.write(" *****************************************\n")

                                    ListSplit.Quantity[num] = int(ListSplit.Quantity[num]) - 1

                                    with open("Stock.txt", "w+") as f:
                                        for i in range(3):
                                            f.write(ListSplit.BookName[i] + "," + ListSplit.AuthorName[i] + "," + str(ListSplit.Quantity[i]) + "," + "$" + ListSplit.Cost[i] +"\n")
                                            success = False
                            else:
                                loop = False
                                break

                        elif (choice.upper() == "N"):

                            with open(t,"r") as j:
                                read = j.read()
                                print(read)
                                print("\n*** Thank you for borrowing books from us. ***\n")
                            loop = False
                            success = True

                        else:
                            print("Please choose as instructed\n")

                else:
                    print("Book is out of stock !\n")
                    Borrow_Book()
                    success = False

            except IndexError:

                print("Please choose book acording to their number.\n")

        except ValueError:
            
            print("Please choose as suggested.\n")
    
    
