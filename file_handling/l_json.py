import json

book_series = {}
book_series["HP"] = {
    "name": "Harry Potter",
    "author": "J.K. Rowling",
    "books": 7,
    "finished reading": True
}
book_series["SOIAF"] = {
    "name": "Game of Thrones",
    "author": "George R.R. Martine",
    "books": 7,
    "status": "Nopes"
}
#for i in book_series:
    #print(book_series[i]["name"], '.'*5, book_series[i])

s = json.dumps(book_series)
with open('books.json', 'w') as f:
    f.write(s)
    f.close()

f_read = open('books.json', 'r')
print("*"*10)
s=f_read.read()
print(s)
