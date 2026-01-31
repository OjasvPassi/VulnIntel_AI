from typing import List

from app.models.cve_model import CVE
from fastapi import APIRouter, HTTPException

router = APIRouter()

# mock dataset
MOCK_CVES = [
    CVE(
        id="CVE-2024-0001",
        description="Example buffer overflow in sample library.",
        severity="High",
        cvss_score=8.5,
        references=["https://nvd.nist.gov/vuln/detail/CVE-2024-0001"],
    ),
    CVE(
        id="CVE-2024-0002",
        description="Cross-site scripting vulnerability in webapp.",
        severity="Medium",
        cvss_score=6.3,
        references=["https://nvd.nist.gov/vuln/detail/CVE-2024-0002"],
    ),
]


@router.get("/cves", response_model=List[CVE])
async def list_cves():
    """Return mock list of CVEs."""
    return MOCK_CVES


@router.get("/cve/{cve_id}", response_model=CVE)
async def get_cve(cve_id: str):
    """Return single CVE by ID."""
    for cve in MOCK_CVES:
        if cve.id == cve_id:
            return cve
    raise HTTPException(status_code=404, detail="CVE not found")
