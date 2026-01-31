from typing import List, Optional

from pydantic import BaseModel


class CVE(BaseModel):
    id: str
    description: str
    severity: str
    cvss_score: float
    references: Optional[List[str]] = []
