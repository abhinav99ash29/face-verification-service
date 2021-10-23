from fastapi import FastAPI, File, UploadFile, Header
from typing import Optional
from imageHelper import img2encoding, isRegistered
from dbHelper import write, search

app = FastAPI()

@app.post("/face/v1")
async def register(type: str = Header(None), id: str = Header(None), file: UploadFile = File(...)):

    if type == 'register':
        encoding = await img2encoding(file)

        result = write(identityId, encoding)

        return {
            "success": result
        }
    elif type == 'lookup':
        encoding = await img2encoding(file)
        knownEnc = search(identityId)

        result = isRegistered(encoding, knownEnc)

        return {
            "success": result
        }


