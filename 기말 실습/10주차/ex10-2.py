# (1)
booknums = [1,2,3,4,5]
booknames = ['축구의 역사', '축구 아는 여자', '축구의 이해', '골프 바이블', '피겨 교본']
pubs = ['굿스포츠', '나무수', '대한미디어', '대한미디어', '굿스포츠']
prices = [7000, 13000, 22000, 35000, 8000]

# 리스트의 리스트를 표처럼 포장해서 출력하는 함수
def print_table(t):
    for item in t:
        print(item)
    print()


# (2)
book_catalog = list(zip(booknums, booknames, pubs, prices))

for index, item in enumerate(book_catalog):
    book_catalog[index] = list(item)
print_table(book_catalog)


# (3)
def f(x):
    return x >= 10000

# filter 함수 사용 예
prices_ge10000 = list(filter(f, prices))

books_ge10000 = []
for j in range(0, len(prices_ge10000)):
    for item in book_catalog:
        if item[3] == prices_ge10000[j]:
            books_ge10000.append(item)
            break

# 대체 표현: 리스트 컴프리헨션
#books_ge10000 = [x for x in book_catalog if f(x[3]) == True]
#print_table(books_ge10000)


# (4)
def convert(p):
    return round(p / 1300, 2)

prices_usd = list(map(convert, prices))
book_catalog_usd = list(zip(booknums, booknames, pubs, prices_usd))
for index, item in enumerate(book_catalog_usd):
    book_catalog_usd[index] = list(item)
print_table(book_catalog_usd)


# (5)
        
# 책의 이름 순서로 booknames 리스트를 정렬해서 booknames2 에 저장하고
# 이 순서대로 새로운 도서 목록 book_catalog_sorted 생성
booknames2 = list(sorted(booknames))
book_catalog_sorted = []
for j in range(0, len(booknames2)):
    for item in book_catalog:
        if item[1] == booknames2[j]:
            book_catalog_sorted.append(item)
print_table(book_catalog_sorted)

# 축약 표현: 각 서브리스트의 1번 인덱스가 도서 이름이므로 이를 기준으로 정렬
#book_catalog_sorted = list(sorted(book_catalog, key=lambda x: x[1]))
#print_table(book_catalog_sorted)


# (6)
print(f"도서 가격의 총 합: {sum(prices)}")
