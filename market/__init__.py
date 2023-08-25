import sqlalchemy.ext.declarative
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.secret_key import app_config_secret_key


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_BINDS'] = {
    "market": "sqlite:///market.db"
}
app.config['SECRET_KEY'] = app_config_secret_key

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'

connect_db = sqlite3.connect('./instance/market.db')

db_exec = connect_db.execute
db_execmany = connect_db.executemany
cursor = connect_db.cursor()

# connect_db.execute("DROP TABLE IF EXISTS")
# db_exec("DROP TABLE User")
# db_exec('''
#     CREATE TABLE User
#         (id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         email_address TEXT NOT NULL,
#         passwd_hash TEXT NOT NULL,
#         budget INT NOT NULL,
#         items TEXT REFERENCES Item);
# ''')
# user_vals = [
#     (1,'Oz','oz@iri.com','oz542',1000,'iPhone X'),
#     (2,'Ozi','coz@iri.com','ozI542',1500,'Keyboard'),
#     (3,'ziri','ziri@oz.com','ziri142',2500,'Laptop'),
# ]
# db_execmany("REPLACE INTO User VALUES (?,?,?,?,?,?)", user_vals)

# db_exec("DROP TABLE Item")
# db_exec('''
#     CREATE TABLE Item(
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         price INT NOT NULL,
#         barcode INT NOT NULL,
#         description TEXT NOT NULL,
#         owner INT REFERENCES User(id)
#     );
# ''')

# instead of INSERT, the 'REPLACE' keyword can be used to allow overwriting of pre-existing data
item_vals = [
    (1, 'iPhone X', 500, 8461541, 'desc', None),
    (2, 'Laptop', 700, 7461542, 'descr', None),
    (3, 'Keyboard', 100, 6461540, 'described', None),
    (4, 'Mouse', 30, 6461541, 'described1', None),
]
# db_execmany("REPLACE INTO Item VALUES (?,?,?,?,?,?)",item_vals)

connect_db.commit()

# cursor.execute("SELECT * FROM Item")
# data = cursor.fetchall()
# print(f"all_data from Item:\n {data}")

# search_val = 'iPhone X'
# cursor.execute("SELECT name FROM Item WHERE name = ?", (search_val,))
# item1 = cursor.fetchall()[0][0]
# print(f"Item1: {item1}")

# cursor.execute("SELECT * FROM User")
# data = cursor.fetchall()
# print(f"all_data from User:\n {data}")

connect_db.close()

from market import routes

# search_val = 'Oz'
# cursor.execute("SELECT id FROM User WHERE username = ?", (search_val,))
# item1_owner_ID = item2_owner_ID = cursor.fetchall()[0][0]
# print(f"Item_1n2 Owner ID: {item1_owner_ID}, {item2_owner_ID}")
# cursor.execute("SELECT username FROM User")
# owners = cursor.fetchall()

# item1_owner = owners[0][0]
# item2_owner = owners[1][0]
# item3_owner = item4_owner = owners[2][0]

# print(f"owners: {owners}")

# search_val = 'Ozi'
# cursor.execute("SELECT id FROM User WHERE username = ?", (search_val,))
# item3_owner_ID = item4_owner_ID = cursor.fetchall()[0][0]

# print(f"Item_3n4 Owner ID: {item3_owner_ID}, {item4_owner_ID}")

# connect_db.commit()

