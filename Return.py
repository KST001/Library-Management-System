import ListSplit
import DateTime

def Return_Book():

    total = 0.0
    fine = 0.0
    name = input("Enter First Name of borrower: ")
    b = "Return_"+name+".txt"

    print("Is the book return date expired?")
    option = input("Press [Y] for Yes & [N] for No: ")

    if(option.upper() == "Y"):

        day = int(input("How many days was the book returned late: "))
        fine = 2 * day

    with open(b, "a")as f:
        f.write("\t\t\t\t\tTotal: $" + str(total))

    a = "Borrow_" + name + ".txt"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]

        with open(a, "r") as f:
            data = f.read()

    except:
        print("The borrower name is incorrect")
        Return_Book()

    with open(b, "w+") as f:
        f.write("\n")
        f.write("------------------------------------------------\n")
        f.write("|          Library Management System            |\n")
        f.write("|-----------------------------------------------|\n")
        f.write("|   Date: " + DateTime.Date() +" \t\tTime:" + DateTime.Time()+"\t|\n")
        f.write("|   Returned By: " + name +"                        |\n")
        f.write("|-----------------------------------------------|\n")
        f.write("|S.N.\tBookname\t\t\tCost\t|\n")
        f.write("|-----------------------------------------------|\n")
    count = 1
    for i in range(3):
        if ListSplit.BookName[i] in data:
            with open(b, "a") as f:
                f.write(" " + str(count)+".\t" +
                        ListSplit.BookName[i]+"\t\t$"+ListSplit.Cost[i]+"\n")
                count += 1
                ListSplit.Quantity[i] = int(ListSplit.Quantity[i]) + 1
            total += float(ListSplit.Cost[i])

    with open(b, "a")as f:
        f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
    total = total + fine

    with open(b, "a") as k:

        k.write("\t\t\t\t\tTotal:" + "$" + str(total)+ "\n")
        # k.write("\t\t\t\t\tFinal Total: " + "$" + str(total))
    

    with open("Stock.txt", "w+") as f:
        for i in range(3):
            f.write(ListSplit.BookName[i] + "," + ListSplit.AuthorName[i] + "," + str(ListSplit.Quantity[i]) + "," + "$" + ListSplit.Cost[i] + "\n")

    with open(b, "r") as g:
        read = g.read()
    print(read)
