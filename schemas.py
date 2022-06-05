from pydantic import BaseModel


class MahasiswaRequest(BaseModel):
    npm: str
    nama: str

    class Config:
       orm_mode = True