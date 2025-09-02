book=eval(input("Enter the books"))
addbook=input("Enter the book name")
remBook=input("Enter the book name")

book.add(addbook)
book.remove(remBook)
print("Currents books : ",book)
print("Total Books: ",len(book))