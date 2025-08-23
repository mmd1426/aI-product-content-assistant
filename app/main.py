from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import base64
from vlm_caption import product_description
from llm_generation import generate_marketing_content

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return JSONResponse({"error": "فایل باید تصویر باشد"}, status_code=400)
    
    # Save image to uploads folder
    os.makedirs("src/uploads", exist_ok=True)
    file_path = f"src/uploads/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Convert image to base64 for VLM
    with open(file_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
    
    try:
        # Get product description from VLM
        vlm_result = product_description(img_base64)
        
        # Generate marketing content with LLM
        llm_result = generate_marketing_content(vlm_result)
        
        return {
            llm_result
        }
        
    except Exception as e:
        return JSONResponse(
            {"error": f"خطا در تحلیل تصویر: {str(e)}"}, 
            status_code=500
        )

@app.get("/")
async def root():
    return {"message": "برای آپلود و تحلیل تصویر از POST /upload استفاده کنید"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
