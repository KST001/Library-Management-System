def List_Split():
    global BookName
    global AuthorName
    global Quantity
    global Cost
    BookName = []
    AuthorName = []
    Quantity = []
    Cost = []
    with open("Stock.txt", "r") as f:

        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind = 0
            for a in lines[i].split(','):
                if(ind == 0):
                    BookName.append(a)

                elif(ind == 1):
                    AuthorName.append(a)

                elif(ind == 2):
                    Quantity.append(a)

                elif(ind == 3):
                    Cost.append(a.strip("$"))
                ind += 1

