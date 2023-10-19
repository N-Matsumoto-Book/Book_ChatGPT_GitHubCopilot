class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def information(self):
        return f"{self.title} by {self.author}, contains {self.page_count} pages."


# インスタンスの生成
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 277)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 324)

# 属性へのアクセス
print(book1.title)  # The Catcher in the Rye
print(book2.title)  # To Kill a Mockingbird

# メソッドの実行
# The Catcher in the Rye by J.D. Salinger, contains 277 pages.
print(book1.information())
# To Kill a Mockingbird by Harper Lee, contains 324 pages.
print(book2.information())
