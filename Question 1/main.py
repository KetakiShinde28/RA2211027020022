from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {
    "1": "V",
    "2": "Johnny Silverhand",
    "3": "Judy Alvarez",
    "4": "Panam Palmer",
    "5": "Takemura",
    "6": "Julian Alvarez",
    "7": "James Anderson",
    "8": "Romario Smith",
    "9": "Harry Shepherd",
    "10": "Judy Gravenbench",
}

top_users = {
    "1": "Judy Alvarez",
    "2": "V",
    "3": "Panam Palmer",
    "4": "Johnny Silverhand",
    "5": "Takemura",
    "6": "James Anderson",
}

popular_posts = [
    {"id": 1, "content": "Night City never sleeps.", "likes": 4200},
    {"id": 2, "content": "Samurai never dies!", "likes": 3800}
]

latest_posts = [
    {"id": 3, "content": "Another corpo deal gone wrong.", "timestamp": "5 min ago"},
    {"id": 4, "content": "Time to upgrade my cyberware.", "timestamp": "10 min ago"}
]

@app.get("/users")
def get_users():
    return {"users": users}

@app.get("/top_users")
def get_top_users():
    return {"top_users": top_users}

@app.get("/posts")
def get_posts(type: str):
    return {"popular_posts": popular_posts} if type == "popular" else {"latest_posts": latest_posts}

@app.get("/")
def home():
    return {"message": "Cyberpunk FastAPI Backend is Running!"}
