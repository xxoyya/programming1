book_list = [
    {"Book Number": 1, "Book Title": "축구의 역사", "Publisher": "굿스포츠", "Price": 17000},
    {"Book Number": 2, "Book Title": "축구 아는 여자", "Publisher": "나무수", "Price": 13000},
    {"Book Number": 3, "Book Title": "축구의 이해", "Publisher": "대한미디어", "Price": 22000},
    {"Book Number": 4, "Book Title": "골프 바이블", "Publisher": "대한미디어", "Price": 35000},
    {"Book Number": 5, "Book Title": "피겨 교본", "Publisher": "굿스포츠", "Price": 8000}
]

for book in book_list:
    print("도서번호:", book["Book Number"], ", 도서이름:", book["Book Title"], ", 출판사:", book["Publisher"], ", 가격:", book["Price"])
