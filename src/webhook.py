import os
import uvicorn
from fastapi import FastAPI, Request
import json

app = FastAPI()

# 測試伺服器是否啟動的根目錄路徑
@app.get("/")
async def root():
    return {"status": "online", "message": "Webhook Server is running!"}

# 這是接收 Chrome 擴充功能訊息的 Webhook 核心
@app.post("/webhook")
async def receive_message(request: Request):
    try:
        # 取得擴充功能傳來的 JSON 資料
        data = await request.json()
        message = data.get("message", "")
        
        # 這裡會將訊息印在 Railway 的 Logs 裡面，方便你檢查
        print(f"收到 LINE 訊息: {message}")
        
        # --- 未來業務邏輯區 (例如呼叫 processor.py) ---
        # result = process_order(message)
        # ------------------------------------------
        
        return {"status": "success", "received": message}
    except Exception as e:
        print(f"處理訊息時發生錯誤: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # 這是部署到雲端的關鍵，一定要抓取 PORT 環境變數
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)