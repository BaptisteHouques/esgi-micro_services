from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Configurer les origines autorisées (whitelist)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a database connection
conn = sqlite3.connect("example.db")

# Define data models
class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str

class Pin(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    user_id: int

# CRUD endpoints for users
@app.post("/users/")
async def create_user(user: User):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (user.username, user.email)
    )
    conn.commit()
    return {"id": cursor.lastrowid, **user.dict()}

@app.get("/users/")
async def read_users():
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    rows = cursor.fetchall()
    return [{"id": row[0], "username": row[1], "email": row[2]} for row in rows]

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    if not row:
        return {"error": "User not found"}
    return {"id": row[0], "username": row[1], "email": row[2]}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET username = ?, email = ? WHERE id = ?",
        (user.username, user.email, user_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "User not found"}
    return {"id": user_id, **user.dict()}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "User not found"}
    return {"message": "User deleted"}


# CRUD endpoints for pins
@app.post("/pins/")
async def create_pin(pin: Pin):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pins (title, description, user_id) VALUES (?, ?, ?)",
        (pin.title, pin.description, pin.user_id)
    )
    conn.commit()
    return {"id": cursor.lastrowid, **pin.dict()}

@app.get("/pins/")
async def read_pins():
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, user_id FROM pins")
    rows = cursor.fetchall()
    return [{"id": row[0], "title": row[1], "description": row[2], "user_id": row[3]} for row in rows]

@app.get("/pins/{pin_id}")
async def read_pin(pin_id: int):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description, user_id FROM pins WHERE id = ?",
        (pin_id,)
    )
    row = cursor.fetchone()
    if not row:
        return {"error": "Pin not found"}
    return {"id": row[0], "title": row[1], "description": row[2], "user_id": row[3]}

@app.put("/pins/{pin_id}")
async def update_pin(pin_id: int, pin: Pin):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE pins SET title = ?, description = ?, user_id = ? WHERE id = ?",
        (pin.title, pin.description, pin.user_id, pin_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "Pin not found"}
    return {"id": pin_id, **pin.dict()}

@app.delete("/pins/{pin_id}")
async def delete_pin(pin_id: int):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM pins WHERE id = ?",
        (pin_id,)
    )
    conn.commit()
    if cursor.rowcount == 0:
        return {"error": "Pin not found"}
    return {"message": "Pin deleted"}

@app.get("/users/{user_id}/pins")
async def read_user_pins(user_id: int):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description, user_id FROM pins WHERE user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()
    if not rows:
        return {"error": "User has no pins"}
    return [{"id": row[0], "title": row[1], "description": row[2], "user_id": row[3]} for row in rows]