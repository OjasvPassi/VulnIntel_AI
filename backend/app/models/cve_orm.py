from app.core.db import Base
from sqlalchemy import JSON, Column, Float, String, Text


class CVEModel(Base):
    __tablename__ = "cves"

    id = Column(String, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    severity = Column(String, index=True)
    cvss_score = Column(Float)
    references = Column(JSON)
