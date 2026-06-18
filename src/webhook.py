import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 用來測試伺服器是否活著的路由
@app.get("/")
async def root():
    return {"message": "Server is running!"}

# 這是真正接收訊息的 Webhook
@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print(f"收到訊息: {data}")
    return {"status": "success"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)