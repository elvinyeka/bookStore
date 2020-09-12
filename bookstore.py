
import json

i = 1
bookList = []



while True:
    print(f"--------------------------------{i}-ci kitabın məlumatlarını daxil edin-----------------------------")
    i += 1
    _bookID = int(input("Kitabin sıra nömrəsini daxil edin: "))
    _bookName = input("Kitabın Adı: ")
    _bookAuthor = input("Müəllifi: ")
    _bookAmount = int(input("Kitabın qiyməti: "))
    _bookPage = int(input("Kitabın səhifə sayı: "))
    _bookGenre = input("Kitabın janrı: ")
    _bookNumber = int(input("Bu kitabın sayını daxil edin:"))
    book = {
        'bookID': _bookID,
        'bookName': _bookName,
        'bookAuthor': _bookAuthor,
        'bookAmount': _bookAmount,
        'bookPage': _bookPage,
        'bookGenre': _bookGenre,
        'bookNumber': _bookNumber
    }

    bookList.append(book)
    Davam = int(
        input("Novbəti kitabın məlumatlarını daxil etmek isteyirsinizse 1 yazin\nSonlamaq isteyirsizse 2 yazin :"))
    if Davam == 1:
        continue
    else:
        break

for _book in bookList:
    print(
        f" Kitabın Adı: {_book['bookName']}\n Kitabın müəllifi: {_book['bookAuthor']}\n Kitabın qiyməti: {_book['bookAmount']} AZN\n Kitabın səhifə sayı: {_book['bookPage']}\n Kitabın janrı: {_book['bookGenre']}\n Kitabın sayı: {_book['bookNumber']}")

    with open("booklist.json", "w") as connect:
        json.dump(bookList, connect)
