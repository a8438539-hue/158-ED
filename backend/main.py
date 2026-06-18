from fastapi import FastAPI, Request
import httpx

app = FastAPI()

@app.post("/webhook")
async def handle_message(request: Request):
    data = await request.json()
    msg = data.get("message")
    
    # 這裡加入你的派單邏輯 (例如：解析「叫車」關鍵字)
    if "叫車" in msg:
        print(f"收到訂單: {msg}")
        # 在這裡呼叫 Google Sheets API 或進行派單邏輯
    return {"status": "ok"}