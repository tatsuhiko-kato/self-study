class User:
    '''User
    '''
    user_type = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""

if __name__ == '__main__':
    user1 = User("寺田学", 35, "東京都台東区")
    print(user1.name)