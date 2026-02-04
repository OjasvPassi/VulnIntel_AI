from app.core.db import SessionLocal
from app.models.cve_orm import CVEModel
from sqlalchemy.dialects.postgresql import insert

cves_to_seed = [
    {
        "id": "CVE-2024-12345",
        "description": "Example privilege escalation vulnerability.",
        "severity": "High",
        "cvss_score": 8.8,
        "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-12345"],
    },
    {
        "id": "CVE-2024-67890",
        "description": "XSS in vulnerable web module.",
        "severity": "Medium",
        "cvss_score": 6.4,
        "references": ["https://nvd.nist.gov/vuln/detail/CVE-2024-67890"],
    },
]

db = SessionLocal()

for cve in cves_to_seed:
    stmt = insert(CVEModel).values(**cve)
    stmt = stmt.on_conflict_do_nothing(index_elements=["id"])  # the primary key column
    db.execute(stmt)  # this is correct: session.execute(Core stmt)

db.commit()
db.close()
print("Seed completed (duplicates ignored).")
