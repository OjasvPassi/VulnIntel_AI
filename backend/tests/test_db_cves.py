import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.db import SessionLocal
from app.models.cve_orm import CVEModel


def test_db_insert_and_fetch():
    db = SessionLocal()
    cve = CVEModel(
        id="CVE-TEST-0001",
        description="Testing insert",
        severity="Low",
        cvss_score=3.5,
        references=["https://test.example.com"],
    )
    db.add(cve)
    db.commit()
    result = db.query(CVEModel).filter(CVEModel.id == "CVE-TEST-0001").first()
    assert result is not None
    assert result.severity == "Low"
    db.delete(result)
    db.commit()
    db.close()
