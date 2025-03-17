


from fastapi import FastAPI,Body

app = FastAPI()


BOOKS = [
    {'id':1,'title':'Introduction to Python','author':'Rony','published_year':2021,'rating':5},
    {'id':2,'title':'Introduction to TensorFlow','author':'Geoffrey','published_year':2016,'rating':4},
    {'id':3,'title':'Regular Expressions Expert','author':'Experia','published_year':2019,'rating':3},
    {'id':4,'title':'Adavanced Python','author':'Pycharm','published_year':2021,'rating':5},
    {'id':5,'title':'Start with Statistics','author':'Statistica','published_year':2022,'rating':2}
]

def find_id():
    return 1 if len(BOOKS) == 0 else BOOKS[-1]['id'] + 1


@app.get("/get_books")
def get_book_data():
    return BOOKS

@app.get("/get book by author")
def get_book_by_rating(author:str):
    rating_books = []
    for book in BOOKS:
        if book['author'].casefold() == author.casefold():
            rating_books.append(book)
    return rating_books

@app.get("/get_book_by_id/{id}")
def get_book_by_id(id:int):
    for book in BOOKS:
        for book in BOOKS:
            if book['id'] == id:
                return book
            
@app.post("/add_new_book")
def add_new_book(new_book = Body()):
    id_data = find_id()
    new_book['id'] = id_data
    BOOKS.append(new_book)

@app.put("/update_book")
def update_book(new_body = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['id'] == new_body['id']:
            BOOKS[i] = new_body
            
@app.delete("/delete_book/{id}")
def remove_book(id : int):
    for i in range(len(BOOKS)):
        if BOOKS[i]['id'] == id:
            BOOKS.pop(i)
            break
    



#Refremces

#https://stackoverflow.com/questions/76804344/why-fastapi-swagger-interface-doesnt-update-after-updating-the-backend-code   