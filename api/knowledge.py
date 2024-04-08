from fastapi import APIRouter, UploadFile, File, HTTPException
from functions.update_knowledge import update_knowledge

router = APIRouter()

# api for post knowledge
@router.post("/knowledge")
async def add_knowledge(file: UploadFile = File(...)):
    try:
        # calling update_knowledge function
        update_knowledge(file.file)
        print("knowledge added!")

        return{
            "message" : "Knowledge successfully added!"
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])
