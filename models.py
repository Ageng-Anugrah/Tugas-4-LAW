from sqlalchemy import Column, String

from database import Base


class Mahasiswa(Base):
    __tablename__ = "Mahasiswas"

    npm = Column(String, primary_key=True, index=True)
    nama = Column(String)