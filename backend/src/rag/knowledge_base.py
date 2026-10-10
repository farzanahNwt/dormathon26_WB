"""
LAICIs - WorkBuddy RAG Knowledge Base
Retrieves context from Bank Negara Malaysia (BNM) RMiT regulations,
MCMC directives, and PDRM CCID scam investigation playbooks.
"""

import math
import re
from typing import List, Dict, Any


KNOWLEDGE_CHUNKS = [
    {
        "id": "BNM-RMIT-01",
        "title": "Bank Negara Malaysia (BNM) RMiT - Multi-Factor & Fraud Kill Switch",
        "category": "Regulatory_BNM",
        "content": (
            "Under BNM Risk Management in Technology (RMiT) requirements, all licensed financial institutions "
            "must provide a customer-activated Emergency Kill Switch to immediately freeze internet banking accounts "
            "and e-wallet credentials upon suspicion of fraud. Additionally, SMS OTPs must be phased out in favor of "
            "secure two-factor authenticators (e.g., Secure2u) with mandatory transaction cooling-off periods for new device registrations."
        ),
        "tags": ["bnm", "rmit", "kill switch", "otp", "cooling-off", "banking", "fraud"]
    },
    {
        "id": "BNM-FRAUD-02",
        "title": "National Scam Response Centre (NSRC) 997 Fund Interception Protocol",
        "category": "Intervention_Protocol",
        "content": (
            "Victims who transferred funds to a scammer must contact NSRC Hotline 997 immediately. "
            "NSRC operates a joint operations command comprising BNM, PDRM CCID, MCMC, and commercial banks. "
            "Within the critical 24-hour golden window, participating banks can initiate rapid inter-bank fund holds "
            "under Section 435 of the Criminal Procedure Code to prevent withdrawal through mule account networks."
        ),
        "tags": ["nsrc", "997", "fund freeze", "mule account", "pdrm", "bnm", "recovery"]
    },
    {
        "id": "PDRM-CCID-03",
        "title": "PDRM CCID Semak Mule Verification Standard",
        "category": "Law_Enforcement",
        "content": (
            "The Royal Malaysia Police Commercial Crime Investigation Department (CCID) maintains the Semak Mule "
            "portal (semakmule.rmp.gov.my). Any bank account number, phone number, or company identity registered with "
            "prior police reports is classified as a high-risk compromised entity. Fraudulent operators utilize rented mule "
            "accounts (akaun keldai) to layer proceeds of crime under Section 424 and 420 of the Penal Code."
        ),
        "tags": ["semak mule", "pdrm", "ccid", "akaun keldai", "penal code", "police report"]
    },
    {
        "id": "AI-DEEPFAKE-04",
        "title": "Forensic Indicators of Generative AI & Deepfake Media",
        "category": "Forensic_Standards",
        "content": (
            "AI-synthesized faces and voices exhibit detectable forensic anomalies: (1) Incongruent Error Level Analysis (ELA) "
            "compression variance across facial boundaries; (2) Spatial-frequency artifacts in high-frequency texture regions (hair, teeth, iris); "
            "(3) Deepfake audio exhibiting unnatural vocal spectral continuity and absence of micro-breath acoustics; "
            "(4) Lip-sync temporal delay exceeding 120ms against synthesized acoustic phonemes."
        ),
        "tags": ["deepfake", "ela", "forensics", "voice clone", "synthetic media", "efficientnet", "lip sync"]
    },
    {
        "id": "MCMC-TAKEDOWN-05",
        "title": "MCMC Domain & Telecom Enforcement Guidelines",
        "category": "Telecom_Regulation",
        "content": (
            "Under the Communications and Multimedia Act 1998 (CMA 1998) Section 211 and 233, creating or transmitting "
            "fraudulent websites, malicious hyperlinks, or fake SMS headers is prohibited. The Malaysian Communications and "
            "Multimedia Commission (MCMC) executes emergency DNS blocklists and telco line suspensions upon receipt of verified "
            "phishing telemetry from certified SOC/CERT incident response teams."
        ),
        "tags": ["mcmc", "takedown", "phishing", "sms header", "dns blocklist", "cma 1998"]
    }
]


class RAGKnowledgeBase:
    """
    Retrieval-Augmented Generation (RAG) knowledge engine for Malaysian compliance and fraud prevention.
    """

    def __init__(self):
        self.chunks = KNOWLEDGE_CHUNKS

    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Rank knowledge chunks using BM25-style term-frequency keyword matching.
        """
        query_words = set(re.findall(r"\w+", query.lower()))
        if not query_words:
            return self.chunks[:top_k]

        scored_chunks = []
        for chunk in self.chunks:
            chunk_text = (chunk["title"] + " " + chunk["content"] + " " + " ".join(chunk["tags"])).lower()
            chunk_words = re.findall(r"\w+", chunk_text)

            score = 0.0
            for qw in query_words:
                tf = chunk_words.count(qw)
                if tf > 0:
                    idf = math.log((len(self.chunks) + 1) / (1 + sum(1 for c in self.chunks if qw in (c["title"] + " " + c["content"]).lower())))
                    score += tf * idf

            scored_chunks.append((score, chunk))

        # Sort descending by score
        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        return [c for _, c in scored_chunks[:top_k]]

    def answer_query(self, query: str) -> Dict[str, Any]:
        """
        Synthesize answer from retrieved regulatory knowledge chunks.
        """
        docs = self.retrieve(query, top_k=2)
        doc_titles = [d["title"] for d in docs]
        
        # Grounded LLM synthesis using Gemini
        gemini_summary = None
        try:
            from ..detection.gemini_client import GeminiScamAnalyzer
            analyzer = GeminiScamAnalyzer()
            grounding_text = "\n\n".join([f"[{d['id']}] {d['title']}:\n{d['content']}" for d in docs])
            rag_prompt = (
                "You are LAICIs, a Malaysian regulatory compliance and cyber-forensic AI advisor.\n"
                f"Using the following verified regulatory context:\n{grounding_text}\n\n"
                f"Answer the user query: \"{query}\"\n"
                "Guidelines:\n"
                "- Provide an authoritative, clear, and actionable explanation.\n"
                "- Explicitly cite the regulatory codes (e.g. [BNM-RMIT-01], [BNM-FRAUD-02], [PDRM-CCID-03]).\n"
                "- Keep the response concise, professional, and well-structured."
            )
            payload = {
                "contents": [{"parts": [{"text": rag_prompt}]}],
                "generationConfig": {"temperature": 0.2}
            }
            res = analyzer._call_gemini(payload)
            if res and res.get("text"):
                gemini_summary = res["text"].strip()
        except Exception:
            gemini_summary = None

        if not gemini_summary:
            summary_points = []
            for d in docs:
                summary_points.append(f"• **{d['title']}**: {d['content']}")
            gemini_summary = "\n\n".join(summary_points)

        return {
            "query": query,
            "matched_regulations": doc_titles,
            "regulatory_summary": gemini_summary,
            "citations": [d["id"] for d in docs],
            "framework": "Bank Negara Malaysia RMiT & PDRM CCID Reference Standards"
        }
