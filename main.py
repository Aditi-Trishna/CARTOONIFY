from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from core_logic import Cartoonifier

app = FastAPI(title="Cartoonify OOP API")

# Instantiate our processor object
# If we had a heavy AI model, it would load into memory right here, ONCE.

processor = Cartoonifier(blur_value=5, edge_block_size=9)

@app.post("/cartoonify")
async def cartoonify_endpoint(file: UploadFile = File(...)):
    contents = await file.read()
    
    try:
        # Call the public method on our instantiated object
        processed_bytes = processor.process(contents)
        return Response(content=processed_bytes, media_type="image/jpeg")
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/") 
def health_check():
    return {"status": "Active", "message": "Cartoonify OOP API is running."}