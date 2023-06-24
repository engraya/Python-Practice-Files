class Post:
    def __init__(self, message, author, author_surname = ''):
        self.message = message
        self.author = author
        self.author_surname = author_surname

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")