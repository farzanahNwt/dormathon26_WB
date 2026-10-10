"""
LAICIs - WorkBuddy Library Store
Implements the 3 core databases required by LAICIs:
1. Scans DB (22 fields)
2. Scammers DB (16 fields)
3. Financial Overview DB (9 fields)
"""

import json
import os
import time
from typing import Dict, List, Any, Optional


DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))
os.makedirs(DATA_DIR, exist_ok=True)

SCANS_FILE = os.path.join(DATA_DIR, "scans_db.json")
SCAMMERS_FILE = os.path.join(DATA_DIR, "scammers_db.json")
FINANCIAL_FILE = os.path.join(DATA_DIR, "financial_overview_db.json")
AUDIT_FILE = os.path.join(DATA_DIR, "audit_trail.json")


# Initial seed data for Malaysian fraud registry
INITIAL_SCAMMERS = [
    {
        "scammer_id": "SCAM-MY-001",
        "identifier_type": "domain",
        "identifier_value": "fake-petronas-job.com",
        "scam_category": "job_recruitment",
        "associated_bank": "Maybank",
        "reports_count": 15,
        "threat_level": "HIGH",
        "first_detected": "2025-01-15T10:00:00Z",
        "last_active": "2026-03-23T14:30:00Z",
        "pdrm_case_ref": "JSJK/KL/2025/0892",
        "mcmc_status": "BLOCKLIST_REQUESTED",
        "financial_loss_reported_rm": 52500.0,
        "notes": "Impersonates PETRONAS Talent Acquisition asking for registration fees via mule account.",
        "verified_by": "PDRM CCID / LAICIs Engine",
        "status": "ACTIVE_THREAT",
        "audit_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
        "scammer_id": "SCAM-MY-002",
        "identifier_type": "phone",
        "identifier_value": "0128888901",
        "scam_category": "crypto_investment",
        "associated_bank": "CIMB Bank",
        "reports_count": 42,
        "threat_level": "CRITICAL",
        "first_detected": "2024-12-25T08:00:00Z",
        "last_active": "2026-04-10T09:15:00Z",
        "pdrm_case_ref": "JSJK/SEL/2024/4412",
        "mcmc_status": "SUSPENDED",
        "financial_loss_reported_rm": 1176000.0,
        "notes": "Promotes fraudulent high-yield Telegram crypto scheme using deepfake VIP endorsements.",
        "verified_by": "Bank Negara Malaysia / PDRM CCID",
        "status": "FLAGGED_SYNDICATE",
        "audit_hash": "a1b2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0"
    },
    {
        "scammer_id": "SCAM-MY-003",
        "identifier_type": "bank",
        "identifier_value": "1234567890",
        "scam_category": "phishing",
        "associated_bank": "Maybank",
        "reports_count": 18,
        "threat_level": "HIGH",
        "first_detected": "2025-02-01T12:00:00Z",
        "last_active": "2026-04-08T17:45:00Z",
        "pdrm_case_ref": "JSJK/JHR/2025/1109",
        "mcmc_status": "FROZEN_NSRC",
        "financial_loss_reported_rm": 63000.0,
        "notes": "Mule account used in SMS Touch 'n Go e-wallet phishing scheme.",
        "verified_by": "NSRC Hotline 997",
        "status": "FROZEN_UNDER_SECT_420",
        "audit_hash": "c7d8e9f0123456789abcdef0123456789abcdef0123456789abcdef012345678"
    }
]


class LibraryStore:
    """
    Central storage manager for LAICIs library collections.
    """

    def __init__(self):
        self._init_files()

    def _init_files(self):
        if not os.path.exists(SCAMMERS_FILE):
            self._save_json(SCAMMERS_FILE, INITIAL_SCAMMERS)
        if not os.path.exists(SCANS_FILE):
            self._save_json(SCANS_FILE, [])
        if not os.path.exists(AUDIT_FILE):
            self._save_json(AUDIT_FILE, [])
        if not os.path.exists(FINANCIAL_FILE):
            initial_fin = {
                "record_id": "FIN-MY-2026",
                "period": "2026-YTD",
                "total_scans_evaluated": 128,
                "scams_intercepted_count": 84,
                "total_exposure_rm": 4820000.0,
                "total_prevention_value_rm": 1205000.0,
                "average_case_loss_rm": 38500.0,
                "high_risk_percentage": 65.6,
                "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            self._save_json(FINANCIAL_FILE, initial_fin)

    def _read_json(self, path: str, default: Any) -> Any:
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return default

    def _save_json(self, path: str, data: Any):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"[LibraryStore] Failed saving {path}: {e}")

    # --- Scans DB (22 fields) ---
    def record_scan(self, record: Dict[str, Any]) -> str:
        scans: List[dict] = self._read_json(SCANS_FILE, [])
        scans.insert(0, record)
        # Keep last 500 scans
        scans = scans[:500]
        self._save_json(SCANS_FILE, scans)
        self._update_financial_stats(record)
        return record.get("scan_id", "")

    def get_recent_scans(self, limit: int = 20) -> List[dict]:
        scans: List[dict] = self._read_json(SCANS_FILE, [])
        return scans[:limit]

    def get_scan_by_id(self, scan_id: str) -> Optional[dict]:
        scans: List[dict] = self._read_json(SCANS_FILE, [])
        for s in scans:
            if s.get("scan_id") == scan_id:
                return s
        return None

    # --- Scammers DB (16 fields) ---
    def get_scammers(self) -> List[dict]:
        return self._read_json(SCAMMERS_FILE, INITIAL_SCAMMERS)

    def add_scammer(self, scammer_data: dict):
        scammers: List[dict] = self.get_scammers()
        scammers.append(scammer_data)
        self._save_json(SCAMMERS_FILE, scammers)

    def search_scammer(self, query: str) -> List[dict]:
        query = query.strip().lower()
        scammers = self.get_scammers()
        results = []
        for s in scammers:
            if (
                query in s.get("identifier_value", "").lower() or
                query in s.get("scam_category", "").lower() or
                query in s.get("associated_bank", "").lower() or
                query in s.get("notes", "").lower()
            ):
                results.append(s)
        return results

    # --- Audit Trail ---
    def log_audit(self, audit_entry: dict):
        audits: List[dict] = self._read_json(AUDIT_FILE, [])
        audits.insert(0, audit_entry)
        audits = audits[:1000]
        self._save_json(AUDIT_FILE, audits)

    def get_audits(self, limit: int = 50) -> List[dict]:
        audits: List[dict] = self._read_json(AUDIT_FILE, [])
        return audits[:limit]

    # --- Financial Overview (9 fields) ---
    def get_financial_overview(self) -> dict:
        return self._read_json(FINANCIAL_FILE, {})

    def _update_financial_stats(self, new_scan: dict):
        fin = self.get_financial_overview()
        fin["total_scans_evaluated"] = fin.get("total_scans_evaluated", 0) + 1
        exposure = float(new_scan.get("exposure_rm", 0.0))
        prev_val = float(new_scan.get("prevention_value_rm", 0.0))

        if exposure > 0:
            fin["scams_intercepted_count"] = fin.get("scams_intercepted_count", 0) + 1
            fin["total_exposure_rm"] = round(fin.get("total_exposure_rm", 0.0) + exposure, 2)
            fin["total_prevention_value_rm"] = round(fin.get("total_prevention_value_rm", 0.0) + prev_val, 2)

        fin["last_updated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self._save_json(FINANCIAL_FILE, fin)
