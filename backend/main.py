from http.client import HTTPException
from fastapi import FastAPI
from psycopg2 import connect
from hashlib import sha256
from dotenv import load_dotenv
from pydantic import BaseModel
from os import getenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        dbname=getenv('DB_NAME'),
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        port=getenv('DB_PORT')
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


@app.post("/api/users")
async def get_users():
    pass

@app.post("/api/register")
async def register(data: LoginRequest):
    db = connect(
        dbname=getenv('DB_NAME'),
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        port=getenv('DB_PORT')
                 )
    cursor = db.cursor()

    cursor.execute(f'''
        insert into users (user_name, "password")
         Values ('{data.username}', '{password_hash(data.password)}')
        ''')
    db.commit()

    cursor.close()
    db.close()
    return {"success": True}
