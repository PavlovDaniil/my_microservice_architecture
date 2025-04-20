from http.client import HTTPException
from fastapi import FastAPI
from psycopg2 import connect
from hashlib import sha256
from dotenv import load_dotenv
from pydantic import BaseModel
from os import getenv

app = FastAPI()
load_dotenv()

class LoginRequest(BaseModel):
    username: str
    password: str

def password_hash(input_string):
    sha256_hash = sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

@app.post("/api/login")
async def login(data: LoginRequest):
    db = connect(
        dbname=getenv("NAME"),
        host=getenv("HOST"),
        user=getenv("DB_USER"),
        password=getenv("PASSWORD"),
        port=getenv("PORT")
    )
    cursor = db.cursor()
    cursor.execute(
        'SELECT user_name, password FROM users WHERE user_name = %s',
        (data.username,)
    )
    result = cursor.fetchone()
    cursor.close()
    db.close()

    if result is None:
        return {"success": False, "message": "User not found"}

    if result[1] == password_hash(data.password):
        return {"success": True}
    else:
        return {"success": False, "message": "Incorrect password"}


@app.get("/api/users")
async def get_users():
    pass

@app.get("/api/register/{username}_{password}")
async def register(username: str, password: str):
    db = connect(dbname='db', host='127.0.0.1', user='user', password='1234', port="5432")
    cursor = db.cursor()

    cursor.execute(f'''
        insert into users (user_name, "password")
         Values ('{username}', '{password_hash(password)}')
        ''')
    db.commit()

    cursor.close()
    db.close()
    return True
