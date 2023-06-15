from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()


class TextData(BaseModel):
    filename: str
    content: str


@app.post("/upload")
async def upload_file(file: UploadFile = None):
    if file is None:
        return {"error": "No file provided"}

    # Read the contents of the file
    contents = await file.read()

    # Create an instance of the TextData model
    text_data = TextData(filename=file.filename, content=contents.decode())

    # Process or store the text data as needed
    # You can perform any necessary data processing or ingestion here

    return {"filename": file.filename, "content": text_data.content}
