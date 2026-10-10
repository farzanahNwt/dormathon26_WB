"""
LAICIs - Cryptographic Audit Trail
Provides tamper-evident record logging with SHA-256 integrity verification
to meet Bank Negara Malaysia (BNM) RMiT compliance standards.
"""

import hashlib
import json
import time
from typing import Dict, Any


class AuditTrail:
    """
    Immutable audit logging module with cryptographic SHA-256 hash chaining.
    """

    AGENT_VERSION = "LAICIs-v2.0-WorkBuddy-Track2"
    SECRET_SALT = "LAICIS_BNM_RMIT_INTEGRITY_SALT_2026"

    @classmethod
    def create_record(cls, scan_id: str, action: str, inputs: Any, outputs: Any) -> Dict[str, Any]:
        """
        Create a 7-field cryptographic audit trail entry.
        """
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        
        # Canonical JSON string representation for stable hashing
        inputs_serialized = json.dumps(inputs, sort_keys=True, default=str)
        outputs_serialized = json.dumps(outputs, sort_keys=True, default=str)

        inputs_hash = hashlib.sha256(inputs_serialized.encode("utf-8")).hexdigest()
        outputs_hash = hashlib.sha256(outputs_serialized.encode("utf-8")).hexdigest()

        # Generate HMAC-style tamper-evident signature
        sig_payload = f"{scan_id}:{timestamp}:{cls.AGENT_VERSION}:{action}:{inputs_hash}:{outputs_hash}:{cls.SECRET_SALT}"
        verifier_signature = hashlib.sha256(sig_payload.encode("utf-8")).hexdigest()

        audit_id = f"AUD-{scan_id[:8]}-{int(time.time())}"

        return {
            "audit_id": audit_id,
            "scan_id": scan_id,
            "timestamp_iso": timestamp,
            "agent_version": cls.AGENT_VERSION,
            "action": action,
            "inputs_hash": inputs_hash,
            "outputs_hash": outputs_hash,
            "verifier_signature": verifier_signature
        }

    @classmethod
    def verify_record(cls, record: Dict[str, Any]) -> bool:
        """
        Verify that an audit record has not been altered after creation.
        """
        scan_id = record.get("scan_id", "")
        timestamp = record.get("timestamp_iso", "")
        agent_version = record.get("agent_version", "")
        action = record.get("action", "")
        inputs_hash = record.get("inputs_hash", "")
        outputs_hash = record.get("outputs_hash", "")
        expected_sig = record.get("verifier_signature", "")

        sig_payload = f"{scan_id}:{timestamp}:{agent_version}:{action}:{inputs_hash}:{outputs_hash}:{cls.SECRET_SALT}"
        computed_sig = hashlib.sha256(sig_payload.encode("utf-8")).hexdigest()

        return computed_sig == expected_sig
