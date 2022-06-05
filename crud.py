from sqlalchemy.orm import Session

import models, schemas


def get_mahasiswa(db: Session, npm: str):
    return db.query(models.Mahasiswa).filter(models.Mahasiswa.npm == npm).first()

def create_mahasiswa(db: Session, mahasiswa: schemas.MahasiswaRequest):
    db_mahasiswa = models.Mahasiswa(npm=mahasiswa.npm, nama=mahasiswa.nama)
    db.add(db_mahasiswa)
    db.commit()
    db.refresh(db_mahasiswa)
    return db_mahasiswa