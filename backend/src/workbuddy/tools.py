"""
LAICIs - WorkBuddy Tool Registry
Defines and executes the forensic tools available to the WorkBuddy Agent.
"""

from typing import Dict, Any, List
from ..detection.ela_analyzer import ELAAnalyzer
from ..detection.pytorch_detector import PyTorchDetector
from ..detection.sightengine_client import SightengineClient
from ..detection.gemini_client import GeminiScamAnalyzer
from ..detection.semak_mule import SemakMuleClient
from ..detection.domain_inspector import DomainInspector
from ..financial.risk_assessor import FinancialRiskAssessor
from ..financial.recovery_playbook import RecoveryPlaybook
from ..rag.knowledge_base import RAGKnowledgeBase


class WorkBuddyToolRegistry:
    """
    Central dispatcher of WorkBuddy agent tools.
    """

    def __init__(self):
        self.ela = ELAAnalyzer()
        self.pytorch = PyTorchDetector()
        self.sightengine = SightengineClient()
        self.gemini = GeminiScamAnalyzer()
        self.semak_mule = SemakMuleClient()
        self.domain_inspector = DomainInspector()
        self.rag = RAGKnowledgeBase()

    def get_registered_tools(self) -> List[Dict[str, str]]:
        return [
            {"id": "local_pytorch_efficientnetv2", "category": "forensics", "name": "PyTorch EfficientNetV2-S AI Classifier"},
            {"id": "local_ela_analyzer", "category": "forensics", "name": "Local Error Level Analysis (ELA)"},
            {"id": "sightengine_api", "category": "forensics", "name": "Sightengine Deepfake & GenAI API"},
            {"id": "gemini_scam_analyzer", "category": "threat_intel", "name": "Gemini 2.0 Flash Multimodal Scam Inspector"},
            {"id": "pdrm_ccid_semak_mule", "category": "law_enforcement", "name": "PDRM CCID Semak Mule Registry Client"},
            {"id": "domain_inspector", "category": "network_security", "name": "SSRF-Safe Domain & Phishing Inspector"},
            {"id": "financial_risk_assessor", "category": "financial", "name": "Malaysian RM Exposure & Loss Prevention Calculator"},
            {"id": "rag_knowledge_base", "category": "compliance", "name": "BNM RMiT & MCMC Regulatory RAG Engine"}
        ]

    def run_ela(self, image_path: str) -> dict:
        return self.ela.analyze(image_path)

    def run_pytorch(self, image_path: str) -> dict:
        return self.pytorch.predict(image_path)

    def run_sightengine(self, image_path: str) -> dict:
        return self.sightengine.analyze_image(image_path)

    def run_gemini(self, text: str, goal: str = "") -> dict:
        return self.gemini.analyze_text_or_context(text, goal)

    def run_gemini_multimodal(self, image_path: str, goal: str = "") -> dict:
        return self.gemini.analyze_image_multimodal(image_path, goal)

    def run_semak_mule_text(self, text: str) -> list:
        return self.semak_mule.scan_text_for_mules(text)

    def run_semak_mule_account(self, account_no: str) -> dict:
        return self.semak_mule.check_bank_account(account_no)

    def run_semak_mule_phone(self, phone_no: str) -> dict:
        return self.semak_mule.check_phone_number(phone_no)

    def run_domain_check(self, url: str) -> dict:
        return self.domain_inspector.inspect_url(url)

    def run_financial_assessment(self, confidence: float, scam_type: str = "default", segment: str = "individual", has_transactional_context: bool = False) -> dict:
        return FinancialRiskAssessor.assess_exposure(confidence, scam_type, segment, has_transactional_context)

    def run_recovery_plan(self, risk_tier: str, threat_type: str = "") -> dict:
        return RecoveryPlaybook.get_action_plan(risk_tier, threat_type)

    def run_rag_query(self, query: str) -> dict:
        return self.rag.answer_query(query)
