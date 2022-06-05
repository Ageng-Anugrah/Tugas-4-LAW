from typing import Optional
from sqlalchemy.orm import Session

import crud
import models
from schemas import MahasiswaRequest
from database import SessionLocal, engine

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create mahasiswa
@app.post("/update")
def create_mahasiswa(mahasiswa: MahasiswaRequest,
                     db: Session = Depends(get_db)):
    try:
        crud.create_mahasiswa(db=db, mahasiswa=mahasiswa)
        return JSONResponse(status_code=201, content={"status": "OK"})
    except:
        raise HTTPException(status_code=500,
                            detail="Failed to create mahasiswa")


# Get mahasiswa by NPM
@app.get("/read/{npm}")
def read_mahasiswa(npm: str, db: Session = Depends(get_db)):
    db_mahasiswa = crud.get_mahasiswa(db, npm=npm)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="mahasiswa not found")
    return JSONResponse(status_code=200,
                        content={
                            "status": "OK",
                            "npm": db_mahasiswa.npm,
                            "nama": db_mahasiswa.nama
                        })


# Get mahasiswa by NPM
@app.get("/read/{npm}/{trx_id}")
def read_mahasiswa_2(npm: str, db: Session = Depends(get_db)):
    db_mahasiswa = crud.get_mahasiswa(db, npm=npm)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="mahasiswa not found")
    return JSONResponse(
        status_code=200,
        content={
            "status": "OK",
            "npm": db_mahasiswa.npm,
            "nama": db_mahasiswa.nama
        },
    )
