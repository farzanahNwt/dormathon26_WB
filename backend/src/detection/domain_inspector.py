"""
LAICIs - SSRF-Safe Domain & URL Inspector
Evaluates URL safety, phishing risks, and brand impersonation without
indiscriminately fetching arbitrary URLs (SSRF protection).
"""

import ipaddress
import re
import socket
from urllib.parse import urlparse


SUSPICIOUS_TLDS = {".xyz", ".top", ".work", ".cam", ".click", ".icu", ".rest", ".online", ".buzz", ".monster", ".bar"}

HIGH_RISK_KEYWORDS = [
    "login", "secure", "verify", "update", "banking", "maybank", "cimb",
    "rhb", "publicbank", "touchngo", "tng", "petronas", "bonus", "claim",
    "subsidy", "bsh", "str", "epf", "kwsp", "lhdn", "refund", "invest"
]

KNOWN_MALICIOUS_DOMAINS = {
    "fake-petronas-job.com": "Known recruitment phishing scam",
    "quick-crypto-profits.net": "Known fraudulent crypto investment platform",
    "maybank2u-security-update.xyz": "Active banking credential harvester",
    "touchngo-ewallet-claim.top": "E-wallet phishing site targeting Malaysian OTPs",
    "pelaburan-asnb-vip.com": "Unregistered illegal investment syndicate"
}


class DomainInspector:
    """
    SSRF-safe domain forensics engine.
    """

    def is_ssrf_risk(self, hostname: str) -> bool:
        """
        Check if hostname resolves to private, loopback, link-local, or reserved IP.
        """
        if not hostname or hostname.lower() in ("localhost", "127.0.0.1", "0.0.0.0"):
            return True

        try:
            ip_str = socket.gethostbyname(hostname)
            ip = ipaddress.ip_address(ip_str)
            return (
                ip.is_private or
                ip.is_loopback or
                ip.is_link_local or
                ip.is_reserved or
                ip.is_multicast
            )
        except Exception:
            # If resolution fails, don't flag as internal SSRF, but mark unresolvable
            return False

    def inspect_url(self, raw_url: str) -> dict:
        """
        Inspect URL without fetching raw body, enforcing SSRF controls.
        """
        if not raw_url.startswith(("http://", "https://")):
            raw_url = "https://" + raw_url

        try:
            parsed = urlparse(raw_url)
            hostname = parsed.hostname or ""
            path = parsed.path or ""

            if not hostname:
                return {"success": False, "error": "Invalid URL structure"}

            # SSRF check
            if self.is_ssrf_risk(hostname):
                return {
                    "success": True,
                    "tool": "domain_inspector",
                    "hostname": hostname,
                    "is_dangerous": True,
                    "risk_tier": "CRITICAL",
                    "threat_type": "SSRF_ATTEMPT",
                    "threat_score": 1.0,
                    "reputation_score": 0.0,
                    "findings": ["URL targets private/loopback network address (SSRF blocked)"],
                    "recommendations": ["Do not route network traffic to private address ranges."]
                }

            # Known blacklist check
            if hostname.lower() in KNOWN_MALICIOUS_DOMAINS:
                reason = KNOWN_MALICIOUS_DOMAINS[hostname.lower()]
                return {
                    "success": True,
                    "tool": "domain_inspector",
                    "hostname": hostname,
                    "is_dangerous": True,
                    "risk_tier": "CRITICAL",
                    "threat_type": "KNOWN_MALICIOUS_PHISHING",
                    "threat_score": 0.95,
                    "reputation_score": 0.05,
                    "findings": [f"Domain is listed in active threat blacklist: {reason}"],
                    "recommendations": ["Immediate blocklist domain; report to MCMC and CyberSecurity Malaysia."]
                }

            # Heuristic inspection
            findings = []
            risk_score = 0.1  # baseline

            # Check scheme
            if parsed.scheme == "http":
                findings.append("Unencrypted HTTP protocol in use")
                risk_score += 0.2

            # Check TLD
            tld_match = any(hostname.endswith(tld) for tld in SUSPICIOUS_TLDS)
            if tld_match:
                findings.append("Uses high-risk, low-cost TLD frequently abused by scammers")
                risk_score += 0.3

            # Check excessive subdomains or hyphens
            if hostname.count("-") >= 2:
                findings.append("Excessive hyphens in domain, common in brand spoofing")
                risk_score += 0.25

            if hostname.count(".") >= 3:
                findings.append("Deeply nested subdomains designed to deceive mobile browser address bars")
                risk_score += 0.2

            # Check high-risk keyword combinations
            matched_keywords = [kw for kw in HIGH_RISK_KEYWORDS if kw in (hostname + path).lower()]
            if len(matched_keywords) >= 2:
                findings.append(f"Combination of high-risk financial/brand terms: {', '.join(matched_keywords)}")
                risk_score += 0.35
            elif len(matched_keywords) == 1:
                findings.append(f"Contains financial/authentication keyword: {matched_keywords[0]}")
                risk_score += 0.15

            # IP address in URL
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname):
                findings.append("Raw IP address used instead of reputable registered domain name")
                risk_score += 0.4

            risk_score = min(risk_score, 1.0)
            is_dangerous = risk_score >= 0.55

            if risk_score > 0.75:
                risk_tier = "CRITICAL"
            elif risk_score > 0.50:
                risk_tier = "HIGH"
            elif risk_score > 0.30:
                risk_tier = "MODERATE"
            else:
                risk_tier = "LOW"

            return {
                "success": True,
                "tool": "domain_inspector",
                "hostname": hostname,
                "protocol": parsed.scheme,
                "risk_tier": risk_tier,
                "is_dangerous": is_dangerous,
                "threat_score": round(risk_score, 2),
                "reputation_score": round(1.0 - risk_score, 2),
                "matched_keywords": matched_keywords,
                "findings": findings if findings else ["No obvious brand-squatting or suspicious structural patterns detected"],
                "recommendations": [
                    "Verify SSL certificate issuer before providing credentials.",
                    "Ensure full domain name matches official corporate registration."
                ]
            }

        except Exception as e:
            return {"success": False, "error": f"Domain inspection failed: {str(e)}"}
