from datetime import datetime
from cryptography.fernet import Fernet

class Account:
    '''Class holding all the information about an account'''
    __next_id = 1

    def __init__(self, name, domain, username, password, id_=None, date=None):
        self.name = name
        self.hidden_password = self.hide_password(password)
        self.shown_password = password
        self.domain = domain
        self.username = username
        self.logo = 'assets/logos/default_big.png'
        if id_ == None:
            self.id = self.__next_id
        else:
            self.id = id_
        
        Account.__next_id += 1

        if date == None:
            self.date = datetime.strftime(datetime.now(), '%d %b, %Y; %H:%M:%S')
        else:
            self.date = date

        self.hidden = True

    # def encrypt_password(self, string):
    #     key = self.__load_secret_key()
    #     f = Fernet(key)
    #     return f.encrypt(string.encode())

    # def decrypt_password(self, string):
    #     key = self.__load_secret_key()
    #     f = Fernet(key)
    #     return f.decrypt(string.encode())

    def hide_password(self, password):
        '''Hides a password'''
        hidden_password = ''
        for _ in password:
            hidden_password += '\u25cf'
        return hidden_password

    # def __load_secret_key(self):
    #     return open('secret.key', 'rb').read()


    def __str__(self):
        return f'{self.id},{self.name.lower()},{self.domain},{self.username},{self.shown_password},{self.date},{self.logo}'