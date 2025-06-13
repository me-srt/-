class Gxt:

    def __init__(self, book_name, book_author, book_price, book_type):
        self.book_name = book_name
        self.book_author = book_author
        self.book_price = book_price
        self.book_type = book_type

    def to_dict(self):
        return {"书名": self.book_name, "作者": self.book_author, "价格": self.book_price, "图书类型": self.book_type}

class Register:

    def __init__(self, user_name, pass_word):
        self.username = user_name
        self.password = pass_word

    def user_to_dict(self):
        return {"账号": self.username, "密码": self.password}