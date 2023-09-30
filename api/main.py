from fastapi import FastAPI

# FastAPI のインスタンス
app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
