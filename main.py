from fastapi import FastAPI

app = FastAPI()


@app.get("/chat/{user_id}")
async def chat(
    user_id: int,
    message: str,
    chat_id: int | None = None,
):
    return {
        "user_id": user_id,
        "message": message,
        "chat_id": chat_id,
    }


@app.get("/chat/history/{user_id}")
async def chat_history(user_id: int):
    return {
        "user_id": user_id,
        "message": "Chat history",
    }


@app.get("/login")
async def login():
    return {
        "message": "Login",
    }


@app.get("/logout")
async def logout():
    return {
        "message": "Logout",
    }


@app.get("/register")
async def register():
    return {
        "message": "Register",
    }


if __name__ == "__main__":
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=int, default=8000, help="Port to run the server on")
    args = parser.parse_args()
    port = args.p

    uvicorn.run(app, host="127.0.0.1", port=port)
