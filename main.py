def main():
    try:
        # initialize books list
        booksList = []
        infile = open("Booklist.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <Booklist.txt> file is not found ")
        print("Starting a new list of books!")
        booksList = []

    choice = 0
    while choice != 4:
        print("*** Bookstore Manager ***")
        print("1) Want to add a book")
        print("2) Want to lookup a book")
        print("3) Want to Display all books")
        print("4) I Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>>")
            nAuthor = input("Enter the name of the author >>>")
            rBefore = input("Is it a good read ? >>>")
            nPages = input("How many pages are there >>>")
            booksList.append([nBook, nAuthor, rBefore, nPages])

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])

        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")

    # Saving to external TXT file
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()