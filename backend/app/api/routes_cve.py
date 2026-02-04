from typing import List

from app.api import crud_cve
from app.core.db import get_db
from app.models.cve_model import CVE
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/cves", response_model=List[CVE])
def list_cves(db: Session = Depends(get_db)):
    return crud_cve.get_all_cves(db)


@router.get("/cve/{cve_id}", response_model=CVE)
def get_cve(cve_id: str, db: Session = Depends(get_db)):
    cve = crud_cve.get_cve_by_id(db, cve_id)
    if not cve:
        raise HTTPException(status_code=404, detail="CVE not found")
    return cve
