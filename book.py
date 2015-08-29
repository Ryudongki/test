def loadData(newfiletxt):
    f = open("newfile.txt",'r')
    book_data = {}
    lines = f.readlines()
    f.close()

    for line in lines :
        line = line.strip()
        book_list = line.split()
        book_name = book_list[0]

        book_list.remove(book_name)
        book_data[book_name] = book_list

    return book_data

def addbook(book_data) :
    print("add name, author, price.")
    book_name = (input("name : "))
    if book_name in book_data:
        print("It's already in the list")
        return
    book_author = (input("author : "))
    book_price = (input("price : "))
    book_list = [book_author, book_price]
    book_data[book_name] = book_list
    f=open("newfile.txt",'w')
    new_list = list(book_data.keys())
    for key in new_list:
        f.write(key)
        f.write(" ")
        f.write(book_data[key][0])
        f.write(" ")
        f.write(book_data[key][1])
        f.write("\n")

    f.close()

def removeBook(book_data):
    print("delete book name")
    remove_name = (input("name  : "))
    if remove_name in book_data:
        del book_data[remove_name]
        print("yes")
    else :
        print("sorry")
    f=open("newfile.txt",'w')
    new_list = list(book_data.keys())
    for key in new_list:
        f.write(key)
        f.write(" ")
        f.write(book_data[key][0])
        f.write(" ")
        f.write(book_data[key][1])
        f.write("\n")

    f.close()

def printname(book_data):
    dic_list = list(book_data.keys())
    dic_list.sort()

    print("name"," author"," price")
    for key in dic_list :
        print(key, '  ',book_data[key][0],'   ',book_data[key][1])

book_data = loadData("newfile.txt")

while 1:
    print("-------menu-------")
    print("1.add")
    print("2.del")
    print("3.print")
    print("4.quit")
    choice = int(input("number"))

    if choice == 1:
        addbook(book_data)
    elif choice == 2:
        removeBook(book_data)
    elif choice == 3:
        printname(book_data)
    else :
        print("quit.")
        break
