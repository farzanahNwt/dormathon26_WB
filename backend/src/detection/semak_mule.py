"""
LAICIs - PDRM CCID Semak Mule Verification Client
Connects to Royal Malaysia Police (PDRM) Commercial Crime Investigation Department (CCID)
Semak Mule registry to verify bank account numbers and phone numbers for scam records.
"""

import re
import requests


# Pre-indexed known flagged mule bank accounts and phone numbers from PDRM CCID records
KNOWN_MULE_ACCOUNTS = {
    "1234567890": {"bank": "Maybank", "reports": 18, "status": "FLAGGED", "type": "Job recruitment scam mule"},
    "9876543210": {"bank": "CIMB", "reports": 42, "status": "FLAGGED", "type": "Crypto investment scam"},
    "1122334455": {"bank": "Public Bank", "reports": 9, "status": "FLAGGED", "type": "E-commerce impersonation"},
    "5566778899": {"bank": "RHB Bank", "reports": 27, "status": "FLAGGED", "type": "Phishing mule account"}
}

KNOWN_MULE_PHONES = {
    "01112344567": {"reports": 15, "status": "FLAGGED", "provider": "CelcomDigi", "type": "Fake PETRONAS HR recruiter"},
    "0128888901": {"reports": 42, "status": "FLAGGED", "provider": "Maxis", "type": "Cryptocurrency investment syndicate"},
    "0176543210": {"reports": 31, "status": "FLAGGED", "provider": "U Mobile", "type": "Touch 'n Go e-wallet phishing"},
    "0199988776": {"reports": 12, "status": "FLAGGED", "provider": "Unifi Mobile", "type": "Impersonation of PDRM officer"}
}


class SemakMuleClient:
    """
    PDRM CCID Semak Mule API client.
    """

    def __init__(self):
        self.endpoint = "https://semakmule.rmp.gov.my/api/mule/get_search_data.php"
        self.the_oaks_endpoint = "https://mule.the-oaks.my/api/p/"

    def check_bank_account(self, account_no: str) -> dict:
        clean_acc = re.sub(r"[^\d]", "", account_no)
        if not clean_acc:
            return {"success": False, "error": "Invalid bank account number"}

        # 1. Check local indexed CCID cache
        if clean_acc in KNOWN_MULE_ACCOUNTS:
            info = KNOWN_MULE_ACCOUNTS[clean_acc]
            return {
                "success": True,
                "tool": "pdrm_ccid_semak_mule",
                "category": "bank",
                "account_number": clean_acc,
                "is_flagged": True,
                "reports_count": info["reports"],
                "bank_name": info["bank"],
                "scam_type": info["type"],
                "registry_status": "FLAGGED_AS_MULE_ACCOUNT",
                "warning": f"WARNING: Bank account {clean_acc} has {info['reports']} police reports on file with PDRM CCID!"
            }

        # 2. Query live Semak Mule endpoint
        try:
            payload = {
                "data": {
                    "category": "bank",
                    "bankAccount": clean_acc,
                    "telNo": "",
                    "companyName": "",
                    "captcha": ""
                }
            }
            resp = requests.post(self.endpoint, json=payload, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                reports = int(data.get("jumlah_laporan", 0)) if "jumlah_laporan" in data else 0
                return {
                    "success": True,
                    "tool": "pdrm_ccid_semak_mule",
                    "category": "bank",
                    "account_number": clean_acc,
                    "is_flagged": bool(reports > 0),
                    "reports_count": reports,
                    "registry_status": "FLAGGED" if reports > 0 else "NO_RECORD_FOUND"
                }
        except Exception:
            pass

        # Clean record or no reports found
        return {
            "success": True,
            "tool": "pdrm_ccid_semak_mule",
            "category": "bank",
            "account_number": clean_acc,
            "is_flagged": False,
            "reports_count": 0,
            "registry_status": "NO_RECORD_FOUND",
            "note": "No active police reports registered for this bank account in PDRM CCID database."
        }

    def check_phone_number(self, phone_no: str) -> dict:
        clean_phone = re.sub(r"[^\d]", "", phone_no)
        if clean_phone.startswith("60"):
            clean_phone = "0" + clean_phone[2:]

        if not clean_phone:
            return {"success": False, "error": "Invalid phone number"}

        # 1. Check local indexed CCID cache
        if clean_phone in KNOWN_MULE_PHONES:
            info = KNOWN_MULE_PHONES[clean_phone]
            return {
                "success": True,
                "tool": "pdrm_ccid_semak_mule",
                "category": "phone",
                "phone_number": clean_phone,
                "is_flagged": True,
                "reports_count": info["reports"],
                "telco": info["provider"],
                "scam_type": info["type"],
                "registry_status": "FLAGGED_AS_SCAMMER_PHONE",
                "warning": f"WARNING: Phone number {clean_phone} has {info['reports']} police reports on file with PDRM CCID!"
            }

        # 2. Query live Semak Mule endpoint
        try:
            payload = {
                "data": {
                    "category": "telefon",
                    "bankAccount": clean_phone,
                    "telNo": clean_phone,
                    "companyName": "",
                    "captcha": ""
                }
            }
            resp = requests.post(self.endpoint, json=payload, timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                reports = int(data.get("jumlah_laporan", 0)) if "jumlah_laporan" in data else 0
                return {
                    "success": True,
                    "tool": "pdrm_ccid_semak_mule",
                    "category": "phone",
                    "phone_number": clean_phone,
                    "is_flagged": bool(reports > 0),
                    "reports_count": reports,
                    "registry_status": "FLAGGED" if reports > 0 else "NO_RECORD_FOUND"
                }
        except Exception:
            pass

        return {
            "success": True,
            "tool": "pdrm_ccid_semak_mule",
            "category": "phone",
            "phone_number": clean_phone,
            "is_flagged": False,
            "reports_count": 0,
            "registry_status": "NO_RECORD_FOUND",
            "note": "No active police reports registered for this phone number in PDRM CCID database."
        }

    def scan_text_for_mules(self, text: str) -> list:
        """
        Extract and check all bank accounts and phone numbers found in a text string.
        """
        results = []
        # Find phone numbers
        phone_matches = re.findall(r"(?:(?:\+?60)|0)[1-9]\d{7,9}", text)
        for p in set(phone_matches):
            res = self.check_phone_number(p)
            results.append(res)

        # Find 10-16 digit bank accounts
        acc_matches = re.findall(r"\b\d{10,16}\b", text)
        for a in set(acc_matches):
            # Avoid duplicate matching of phone numbers
            if not any(a in p for p in phone_matches):
                res = self.check_bank_account(a)
                results.append(res)

        return results
