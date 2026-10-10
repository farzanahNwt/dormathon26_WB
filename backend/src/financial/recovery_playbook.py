"""
LAICIs - Malaysian Scam Recovery & Authority Playbook
Provides immediate action steps and verified contact details for Malaysian
enforcement and regulatory bodies (NSRC, BNM, PDRM CCID, MCMC, CyberSecurity Malaysia).
"""

from typing import List, Dict, Any


OFFICIAL_REGULATORY_CONTACTS = [
    {
        "agency": "NSRC (National Scam Response Centre)",
        "role": "Immediate fund interception & bank freezing (Call within 24h of transfer)",
        "hotline": "997",
        "hours": "8:00 AM - 8:00 PM Daily",
        "urgent": True
    },
    {
        "agency": "Bank Negara Malaysia (BNMTELELINK)",
        "role": "Central bank fraud and unlicensed financial operator reporting",
        "hotline": "1-300-88-5465",
        "email": "bnmtelelink@bnm.gov.my",
        "website": "https://telelink.bnm.gov.my",
        "urgent": False
    },
    {
        "agency": "PDRM CCID (Commercial Crime Investigation Dept)",
        "role": "Police report filing & Semak Mule registry verification",
        "hotline": "03-2610 1599",
        "whatsapp_infoline": "013-211 1222",
        "portal": "https://semakmule.rmp.gov.my",
        "urgent": True
    },
    {
        "agency": "MCMC (Malaysian Communications & Multimedia Commission)",
        "role": "Scam website takedown & fraudulent telecom number suspension",
        "hotline": "1800-188-030",
        "portal": "https://aduan.mcmc.gov.my",
        "urgent": False
    },
    {
        "agency": "CyberSecurity Malaysia (Cyber999)",
        "role": "Digital forensic assistance and incident response",
        "hotline": "1-300-88-2999",
        "email": "cyber999@cybersecurity.my",
        "urgent": False
    }
]


class RecoveryPlaybook:
    """
    Generates tailored remediation action plans based on scan risk tier.
    """

    @staticmethod
    def get_action_plan(risk_tier: str, threat_type: str = "") -> Dict[str, Any]:
        """
        Generate an actionable checklist for the victim or analyst.
        """
        tier = risk_tier.upper()

        if tier in ("CRITICAL", "HIGH"):
            steps = [
                "1. STOP all communication immediately. Do NOT send further funds, OTPs, or IDs.",
                "2. Call the National Scam Response Centre (NSRC) at 997 immediately if money was transferred within the last 24 hours.",
                "3. Contact your bank's 24/7 fraud emergency hotline to request a temporary freeze on your online banking account.",
                "4. Lodge a formal police report at the nearest Balai Polis for investigation under Section 420 of the Penal Code.",
                "5. Retain all evidence: screenshots of chat messages, bank slips, phone numbers, and URLs.",
                "6. Submit domain and phone details to PDRM CCID Semak Mule and MCMC Aduan."
            ]
            urgency = "IMMEDIATE_ACTION_REQUIRED"
        elif tier == "MODERATE":
            steps = [
                "1. Perform independent out-of-band verification via official phone directory or verified corporate app.",
                "2. Never use phone numbers or web links supplied inside the suspicious message itself.",
                "3. Check the sender's account number against PDRM CCID Semak Mule (semakmule.rmp.gov.my).",
                "4. If impersonating a company, contact the official corporate HR / Customer Support directly."
            ]
            urgency = "VERIFICATION_RECOMMENDED"
        else:
            steps = [
                "1. Content exhibits low technical indicators of digital synthesis or known scam moduses.",
                "2. Maintain general security hygiene: never disclose passwords or TAC/OTP numbers to any party.",
                "3. Verify website address bar SSL lock and domain spelling before entering sensitive data."
            ]
            urgency = "STANDARD_HYGIENE"

        return {
            "urgency_level": urgency,
            "checklist": steps,
            "official_contacts": OFFICIAL_REGULATORY_CONTACTS
        }
