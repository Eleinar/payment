import bcrypt
import os
from modules import Users, create_connection
from sqlalchemy import update

def hash_password():
    db = create_connection()
    
    users = db.query(Users).all() # Собирает всех пользователей
    file = open("passwords.txt", "w")
    for user in users: # Проходится по списку
        salt = bcrypt.gensalt() # Генерация "соли"
        hashed_password = bcrypt.hashpw(user.password.encode(), salt) # Хешируемый пароль
        user.password = hashed_password.decode()
        file.write(hashed_password.decode() + '\n')
    db.commit()
    file.close()
    
    
    # Функция для хеширования паролей.
hash_password()