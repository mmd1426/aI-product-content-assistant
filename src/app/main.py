from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import base64
import json
from vlm_caption import product_description
from llm_generation import generate_marketing_content

app = FastAPI()

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return JSONResponse({"Error": "File must be an image"}, status_code=400)
    
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
        
        # Convert string to JSON if needed
        try:
            if isinstance(llm_result, str):
                # Remove markdown formatting if present
                cleaned_result = llm_result.strip()
                if cleaned_result.startswith("```json"):
                    cleaned_result = cleaned_result[7:]  # Remove ```json
                if cleaned_result.endswith("```"):
                    cleaned_result = cleaned_result[:-3]  # Remove ```
                cleaned_result = cleaned_result.strip()
                
                result = json.loads(cleaned_result)
            else:
                result = llm_result
            return JSONResponse(content=result)
        except json.JSONDecodeError:
            return JSONResponse(content={"raw_result": llm_result})
        
    except Exception as e:
        return JSONResponse(
            {"Error": f"Error in image analysis: {str(e)}"}, 
            status_code=500
        )
    
@app.get("/")
async def root():
    return {"message": "Use POST /upload to upload and analyze an image"}