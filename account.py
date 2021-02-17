from datetime import datetime

class Account:
    __next_id = 1

    def __init__(self, name, domain, username, password, id_=None, date=None):
        self.name = name
        self.password = password
        self.domain = domain
        self.username = username
        self.logo = 'default.png'
        if id_ == None:
            self.id = self.__next_id
        else:
            self.id = id_
        
        Account.__next_id += 1

        if date == None:
            self.date = datetime.strftime(datetime.now(), '%d %b, %Y; %H:%M:%S')
        else:
            self.date = date

    def __str__(self):
        return f'{self.id},{self.name.lower()},{self.domain},{self.username},{self.password},{self.date},{self.logo}'