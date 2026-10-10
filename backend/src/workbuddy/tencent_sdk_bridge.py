"""
LAICIs - Official Tencent WorkBuddy / CodeBuddy Agent SDK Integration
Natively integrates with Tencent's official agent framework:
- Uses @tool decorator from codebuddy_agent_sdk
- Exports official Tencent MCP (Model Context Protocol) server via create_sdk_mcp_server
- Registers AgentDefinition for the Tencent WorkBuddy runtime
"""

import os
from typing import Dict, Any, List
from codebuddy_agent_sdk import (
    tool,
    create_sdk_mcp_server,
    AgentDefinition,
    CallToolResult
)

from ..detection.ela_analyzer import ELAAnalyzer
from ..detection.pytorch_detector import PyTorchDetector
from ..detection.semak_mule import SemakMuleClient
from ..detection.domain_inspector import DomainInspector
from ..financial.risk_assessor import FinancialRiskAssessor
from ..rag.knowledge_base import RAGKnowledgeBase

# Shared singletons
_ela = ELAAnalyzer()
_pytorch = PyTorchDetector()
_mule = SemakMuleClient()
_domain = DomainInspector()
_rag = RAGKnowledgeBase()


# --------------------------------------------------------------------------
# 1. OFFICIAL TENCENT WORKBUDDY TOOLS (Decorated via codebuddy_agent_sdk)
# --------------------------------------------------------------------------

@tool(
    name="local_pytorch_deepfake_detector",
    description="Analyzes images using local fine-tuned EfficientNetV2-S model to classify AI-generated vs human-captured media.",
    input_schema={
        "type": "object",
        "properties": {
            "image_path": {"type": "string", "description": "Absolute path to the image file to evaluate"}
        },
        "required": ["image_path"]
    }
)
def tencent_pytorch_tool(args: dict) -> CallToolResult:
    path = args.get("image_path", "")
    res = _pytorch.predict(path)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="local_error_level_analyzer",
    description="Performs forensic Error Level Analysis (ELA) on JPEG images to detect localized tampering and splicing.",
    input_schema={
        "type": "object",
        "properties": {
            "image_path": {"type": "string", "description": "Path to the image file"}
        },
        "required": ["image_path"]
    }
)
def tencent_ela_tool(args: dict) -> CallToolResult:
    path = args.get("image_path", "")
    res = _ela.analyze(path)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="pdrm_ccid_semak_mule_checker",
    description="Queries the Royal Malaysia Police (PDRM) CCID Semak Mule database for reported bank accounts and phone numbers.",
    input_schema={
        "type": "object",
        "properties": {
            "query_type": {"type": "string", "enum": ["bank", "phone", "text"]},
            "value": {"type": "string", "description": "The bank account number, phone number, or text message"}
        },
        "required": ["query_type", "value"]
    }
)
def tencent_semak_mule_tool(args: dict) -> CallToolResult:
    q_type = args.get("query_type", "text")
    val = args.get("value", "")

    if q_type == "bank":
        res = _mule.check_bank_account(val)
    elif q_type == "phone":
        res = _mule.check_phone_number(val)
    else:
        res = _mule.scan_text_for_mules(val)

    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="ssrf_safe_domain_inspector",
    description="Inspects URLs for brand impersonation and phishing risks while enforcing SSRF protection against internal IPs.",
    input_schema={
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "The target website URL"}
        },
        "required": ["url"]
    }
)
def tencent_domain_tool(args: dict) -> CallToolResult:
    url = args.get("url", "")
    res = _domain.inspect_url(url)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="bnm_financial_risk_actuary",
    description="Calculates quantifiable Malaysian Ringgit (RM) exposure and 25% loss prevention value under BNM RMiT standards.",
    input_schema={
        "type": "object",
        "properties": {
            "confidence": {"type": "number", "description": "Forensic confidence score between 0.0 and 1.0"},
            "scam_type": {"type": "string", "description": "Category of threat"},
            "segment": {"type": "string", "enum": ["individual", "sme", "enterprise"]}
        },
        "required": ["confidence"]
    }
)
def tencent_financial_tool(args: dict) -> CallToolResult:
    conf = float(args.get("confidence", 0.5))
    scam_type = args.get("scam_type", "default")
    segment = args.get("segment", "individual")
    res = FinancialRiskAssessor.assess_exposure(conf, scam_type, segment)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="regulatory_rag_compliance_retriever",
    description="Retrieves Bank Negara Malaysia (BNM) RMiT, NSRC 997, and MCMC regulatory requirements for fraud response.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Natural language compliance query"}
        },
        "required": ["query"]
    }
)
def tencent_rag_tool(args: dict) -> CallToolResult:
    q = args.get("query", "")
    res = _rag.answer_query(q)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


@tool(
    name="gemini_multimodal_fraud_reasoner",
    description="Multimodal LLM inspector using Gemini to identify social engineering narratives and visual synthetic deepfake artifacts.",
    input_schema={
        "type": "object",
        "properties": {
            "content": {"type": "string", "description": "Text content or message to analyze"},
            "goal": {"type": "string", "description": "Context or investigation goal"}
        },
        "required": ["content"]
    }
)
def tencent_gemini_tool(args: dict) -> CallToolResult:
    from ..detection.gemini_client import GeminiScamAnalyzer
    gm = GeminiScamAnalyzer()
    val = args.get("content", "")
    g = args.get("goal", "")
    res = gm.analyze_text_or_context(val, g)
    return {
        "content": [{
            "type": "text",
            "text": str(res)
        }]
    }


# --------------------------------------------------------------------------
# 2. OFFICIAL TENCENT WORKBUDDY MCP SERVER
# --------------------------------------------------------------------------

TENCENT_CREDENTIALS = {
    "secret_id": os.environ.get("TENCENTCLOUD_SECRET_ID", ""),
    "secret_key": os.environ.get("TENCENTCLOUD_SECRET_KEY", "")
}

ALL_TENCENT_TOOLS = [
    tencent_pytorch_tool,
    tencent_ela_tool,
    tencent_gemini_tool,
    tencent_semak_mule_tool,
    tencent_domain_tool,
    tencent_financial_tool,
    tencent_rag_tool
]

def build_tencent_mcp_server():
    """
    Builds the official Tencent WorkBuddy MCP (Model Context Protocol) Server config.
    """
    return create_sdk_mcp_server(
        name="laici-forensics-mcp",
        version="2.0.0",
        tools=ALL_TENCENT_TOOLS
    )


# --------------------------------------------------------------------------
# 3. OFFICIAL TENCENT AGENT DEFINITION
# --------------------------------------------------------------------------

LAICI_AGENT_DEFINITION = AgentDefinition(
    description="LAICIs Autonomous Deepfake Forensic & Malaysian Financial Risk Agent",
    prompt=(
        "You are LAICIs, an autonomous fraud forensic investigation agent operating under "
        "the Tencent WorkBuddy execution runtime. Your mission is to protect Malaysian citizens, SMEs, "
        "and financial institutions from deepfakes and syndicates under Bank Negara Malaysia (BNM) RMiT guidelines.\n"
        "1. Understand the user goal and examine input evidence.\n"
        "2. Dynamically plan and call relevant forensic tools (local PyTorch, ELA, Semak Mule, SSRF domain inspector, Gemini Multimodal).\n"
        "3. Cross-validate findings to prevent false alarms.\n"
        "4. Calculate quantifiable, justified exposure in Malaysian Ringgit (RM) and loss prevention value.\n"
        "5. Deliver an actionable evidence dossier with official emergency hotlines (NSRC 997, BNM, PDRM CCID)."
    ),
    tools=[
        "local_pytorch_deepfake_detector",
        "local_error_level_analyzer",
        "gemini_multimodal_fraud_reasoner",
        "pdrm_ccid_semak_mule_checker",
        "ssrf_safe_domain_inspector",
        "bnm_financial_risk_actuary",
        "regulatory_rag_compliance_retriever"
    ]
)

