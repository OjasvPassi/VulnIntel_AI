from app.models.cve_model import CVE
from app.models.cve_orm import CVEModel
from sqlalchemy.orm import Session


def get_all_cves(db: Session):
    return db.query(CVEModel).limit(100).all()


def get_cve_by_id(db: Session, cve_id: str):
    return db.query(CVEModel).filter(CVEModel.id == cve_id).first()


def create_cve(db: Session, cve: CVE):
    db_cve = CVEModel(
        id=cve.id,
        description=cve.description,
        severity=cve.severity,
        cvss_score=cve.cvss_score,
        references=cve.references,
    )
    db.add(db_cve)
    db.commit()
    db.refresh(db_cve)
    return db_cve
