# Business Requirements Document (BRD)
# LAICIs v2.0 — Agentic Deepfake Detection & Financial Scam Prevention Platform

## Document Control

- **Project:** LAICIs v2.0 (upgraded from VeriGuard AI v1.0)
- **Track:** DORMATHON 2026 — Track 2: WorkBuddy Agentic Solutions
- **Team:** TECHBENG (4 beginner developers)
- **Document Version:** 2.0
- **Date:** January 2026
- **Status:** Final Draft
- **Origin:** Reverse-engineered from LAICIs by SecureTech (github.com/EricSyamir/petronascybersec), rebuilt natively in WorkBuddy with financial intelligence layer
- **Document Scope:** This BRD covers three domains in equal depth — **Finance**, **Data**, and **Security**. Every section is fully written out; no section references prior versions or is abbreviated.

---

## Table of Contents

1. Executive Summary
2. Business Problem & Market Opportunity
3. Business Goals & Objectives (SMART)
4. Customer Segments (5 segments)
5. Pricing Model (5 tiers)
6. Revenue Projections (3 scenarios, revenue mix, cost structure, break-even, ROI)
7. Competitive Landscape
8. Financial Intelligence Business Case
9. Data Strategy & Governance
10. Security & Compliance Business Case
11. Risk Factors & Mitigation
12. Success Metrics & KPIs
13. Implementation Roadmap (4 phases)
14. Stakeholder Map
15. Constraints & Assumptions
16. Approval

---

## 1. Executive Summary

### 1.1 Purpose

This Business Requirements Document defines the complete business case, market opportunity, revenue model, data strategy, security posture, and strategic objectives for LAICIs v2.0 — an upgraded version of the VeriGuard AI deepfake detection platform that integrates financial risk assessment, data-user efficiency tools, and compliance reporting capabilities directly into the detection workflow.

LAICIs v2.0 transforms a pure technical detection tool into a business-intelligence platform that not only identifies AI-generated content and deepfakes, but also quantifies the financial exposure, tracks prevented losses, and provides actionable recovery guidance — all built natively within the WorkBuddy AI ecosystem. This document covers three critical domains — **Finance**, **Data**, and **Security** — each as a first-class pillar of the business case.

### 1.2 Business Problem

Malaysian financial scams caused **RM 5.62 billion in losses from 2023 to 2025**, with deepfake-specific fraud rising **76% year-over-year**. In H1 2024 alone, **454 deepfake cases** were reported, resulting in **RM 2.72 million in losses**, including a single corporate fraud case worth **RM 122 million**. The victim belief rate stands at **85%**, meaning most targets cannot distinguish deepfake content from authentic media. The national recovery rate is a mere **2%**, meaning RM 0.98 of every RM 1.00 lost is permanently gone. The average loss per deepfake case is **RM 5,991** (RM 2.72 million divided by 454 cases).

Existing detection tools identify *whether* media is AI-generated, but fail to answer the follow-up question that every business stakeholder asks: *"How much money is at risk, and what do we do about it?"* Furthermore, existing tools do not provide the data infrastructure to continuously collect and query scam intelligence, nor do they provide the security and compliance guarantees required by Malaysian regulators.

### 1.3 Solution Overview

LAICIs v2.0 bridges the gap between technical detection, financial decision-making, and regulatory compliance by layering three new intelligence domains on top of the existing detection engine:

**Detection Core (inherited from v1.0):**
- 5 Detection Modules: Sightengine API, ELA Analysis, ML Inference (EfficientNetV2-S), Gemini Video Analysis, Weighted Scoring Engine
- 7-Step Agentic Workflow: UNDERSTAND → PLAN → EXECUTE → VALIDATE → INTEGRATE → DELIVER → FINANCIAL_RISK_ASSESS

**Finance Domain (new in v2.0):**
- Financial Risk Assessor module — maps detection scores to RM-denominated financial exposure
- Loss Prevention Tracker — cumulative prevented-loss counter on the dashboard
- ROI Calculator — demonstrates value to customers using real Malaysian scam data
- Pricing & Revenue Model — 5 tiers covering RM 3K to RM 250K annual subscriptions

**Data Domain (new in v2.0):**
- 3 Library Databases: Scans (22 fields), Scammers (16 fields), Financial Overview (9 fields, NEW)
- 2 Knowledge Base Nodes: Data node (scam statistics, case data, trends), Finance node (pricing, ROI, cost structures)
- RAG-powered Q&A engine over the knowledge base (rag_search.py)
- OSINT automation pipeline (daily 9 AM, automation ID: 2453f597-10da-4990-9203-06669db4c19d)
- Self-service data query portal with filter, sort, and CSV/JSON export
- Automated data pipeline: WebSearch → extract → structure → library → dashboard

**Security Domain (new in v2.0):**
- PDPA 2010 and CMA 1998 (Section 233) compliance framework
- BNM RMCD Guidelines alignment for financial institutions
- RBAC with 4 roles, OAuth 2.0 authentication, 256-bit API keys
- Immutable audit trail (7 fields, append-only)
- OWASP Top 10 mitigations and STRIDE threat model
- 4-level incident response (Critical 1hr, High 4hr, Medium 24hr, Low 72hr)
- No media file persistence — process and discard

### 1.4 Key Business Metrics

| Metric | Value |
|--------|-------|
| Total Malaysian scam losses (2023-2025) | RM 5.62 billion |
| Deepfake cases H1 2024 | 454 cases |
| Deepfake losses H1 2024 | RM 2.72 million |
| Average loss per deepfake case | RM 5,991 |
| Largest single corporate deepfake fraud | RM 122 million |
| Victim belief rate | 85% |
| National recovery rate | 2% (RM 0.98 of every RM 1.00 permanently lost) |
| YoY increase in deepfake cases | 76% |
| Target ROI for bank customers (conservative) | 4.2x |
| Target ROI for bank customers (optimistic) | 41.7x |
| Break-even horizon (base case) | Year 3 |
| Break-even horizon (optimistic case) | Year 2 |
| Operating cost Year 1 → Year 3 | RM 1.63M → RM 2.94M → RM 4.69M |

---

## 2. Business Problem & Market Opportunity

### 2.1 Malaysian Scam Landscape

The Malaysian scam ecosystem has reached crisis proportions. The following data is drawn from the LAICIs Research Report (25 sources, including Royal Malaysia Police, Bukit Aman CCID, Bank Negara Malaysia, and SFMS statistics):

**Three-Year Loss Trajectory (2023-2025):**
- Total losses: RM 5.62 billion across all scam categories
- Macau Scam and phone scams dominate by volume
- Investment scams (often deepfake-assisted) represent the highest per-case value
- AUH (Authentication Under Hand) and parcel scams remain persistent
- E-commerce scams growing with platform adoption

**Deepfake-Specific Impact (H1 2024):**
- 454 confirmed deepfake fraud cases in 6 months
- RM 2.72 million in direct losses
- 76% year-over-year increase in case volume
- Single largest case: RM 122 million (corporate executive impersonation)
- Average loss per deepfake case: RM 5,991 (RM 2.72M / 454 cases)
- 85% of victims believed the deepfake content was authentic at time of transaction

**Recovery Gap:**
- National scam recovery rate: 2% (RM 0.02 recovered per RM 1.00 lost)
- RM 5.51 billion of RM 5.62 billion total is permanently unrecovered
- This gap represents the primary value proposition: **prevention is the only viable strategy** — once money is lost, 98% of it is gone forever

### 2.2 Global Context

The global deepfake threat landscape provides additional market sizing:
- FBI reported 126% increase in deepfake-related complaints (US, 2023-2024)
- Sumsub detected 10x increase in deepfakes in identity verification (2023)
- Sensity AI tracked 500M deepfake videos online by mid-2024
- Deloitte predicted 30-40% of social media content could be AI-generated by 2026
- Gartner: deepfake detection market reaching USD 1.8 billion by 2027

### 2.3 Regulatory Tailwinds

Malaysian regulatory developments create a compliance mandate for detection tools:
- **PDPA 2010 (Personal Data Protection Act):** Organizations must protect personal data, including biometric data used in deepfakes. Requires breach notification within 72 hours.
- **CMA 1998 (Communications and Multimedia Act):** Section 233 criminalizes offensive content including deepfake impersonation.
- **Bank Negara Malaysia RMCD Guidelines:** Financial institutions required to implement fraud detection and reporting mechanisms.
- **Proposed Anti-Deepfake Legislation:** Malaysian government announced intent to introduce specific deepfake legislation in 2025-2026.
- **Bursa Malaysia Listing Requirements:** Public-listed companies must disclose material fraud incidents.

### 2.4 Market Sizing

- **TAM (Total Addressable Market):** Malaysian financial institutions + government + enterprise corporate scam-prevention spending — estimated RM 500M+ annually based on RM 5.62B in losses and 2% recovery rate.
- **SAM (Serviceable Addressable Market):** Deepfake detection specifically — estimated RM 50M-100M annually, growing at 76% YoY.
- **SOM (Serviceable Obtainable Market):** LAICIs v2.0 target — RM 2.9M Year 3 (base case), representing approximately 3-6% of SAM.

---

## 3. Business Goals & Objectives

### 3.1 Strategic Goals

**Goal 1: Become the leading deepfake detection platform in Malaysia by Q4 2026**
- Secure 3+ enterprise customers (banks, government agencies) by end of Year 1
- Achieve 10,000+ monthly API detections by end of Year 2
- Establish brand recognition as the "Malaysian-made" deepfake defense standard

**Goal 2: Prevent RM 100 million in scam losses by end of Year 2**
- Track cumulative prevented-loss value on the dashboard header
- Tie prevented-loss to specific scans and scammer identifications
- Publish quarterly "Loss Prevention Impact Reports" for marketing

**Goal 3: Achieve profitability by Year 3 (base case) / Year 2 (optimistic case)**
- Reach RM 4.69 million annual operating cost ceiling by Year 3
- Achieve break-even revenue through enterprise contracts + API volume
- Maintain gross margin above 60% on API tier after Sightengine/Gemini costs

**Goal 4: Build a self-sustaining data ecosystem**
- Populate the Data and Finance knowledge base nodes with structured, queryable content
- Enable data users to self-serve queries without developer intervention
- Automate OSINT data collection into the library for continuous intelligence

**Goal 5: Establish a security-first compliance posture**
- Achieve PDPA 2010 and CMA 1998 (Section 233) full compliance by launch
- Implement RBAC, audit trails, and incident response before enterprise onboarding
- Pursue ISO 27001 certification in Year 2 and SOC 2 in Year 3

### 3.2 SMART Objectives

| ID | Objective | Measurable Target | Deadline |
|----|-----------|-------------------|----------|
| O1 | Process media scans across all tiers | 50,000+ scans | End of Year 1 |
| O2 | Catalog unique scammer identifiers | 1,000+ profiles | End of Year 1 |
| O3 | Achieve benchmark detection accuracy | 92%+ true positive rate | End of Q2 2026 |
| O4 | Maintain scan-to-result latency | < 30 seconds for images | Ongoing |
| O5 | Generate compliance/audit reports | 20+ reports/month | End of Q3 2026 |
| O6 | Deliver bank customer ROI | 4.2x minimum (conservative) | Per contract |
| O7 | RAG knowledge base engagement | 500+ queries/month, 85%+ relevance | End of Year 1 |
| O8 | Financial Overview database population | 500+ records with scam-loss data | End of Q2 2026 |
| O9 | OSINT automation daily run success rate | 95%+ successful daily runs | Ongoing |
| O10 | Audit trail completeness | 100% of all actions logged | Ongoing from launch |

---

## 4. Customer Segments

LAICIs v2.0 targets five distinct customer segments, each with unique needs, budgets, and success criteria:

### 4.1 Banks & Financial Institutions (Enterprise Tier)

- **Profile:** Top 10 Malaysian banks, insurance companies, fintech platforms
- **Need:** Real-time deepfake detection on customer onboarding (KYC), transaction verification, and fraud monitoring
- **Budget:** RM 50,000 - RM 250,000 annual subscription
- **Success Criteria:**
  - Prevent deepfake-assisted fraud at the KYC gate
  - Generate regulatory compliance reports for BNM RMCD
  - ROI: RM 4.20 saved for every RM 1.00 spent (4.2x ROI, conservative)
  - ROI: RM 41.70 saved for every RM 1.00 spent (41.7x ROI, optimistic, based on avoiding a single RM 122M corporate case)
- **Key Features Required:** API integration, financial risk assessment, loss prevention tracker, compliance reporting, immutable audit trail, RBAC with Admin/Analyst/Viewer/API roles
- **Security Requirements:** PDPA 2010 compliance, BNM RMCD reporting, TLS 1.2+ encryption, API key rotation every 30 days, audit trail with 7-year retention

### 4.2 Government & Regulatory Bodies (Government Tier)

- **Profile:** PDRM CCID, Bukit Aman, SFMS, Bank Negara Malaysia, MCMC, Ministry of Communications
- **Need:** National-level scam monitoring, deepfake case tracking, public protection alerts
- **Budget:** Custom pricing (government procurement)
- **Success Criteria:**
  - National deepfake case database with trend analysis
  - Automated OSINT intelligence feeds (daily 9 AM automation)
  - Public awareness campaign data support
  - Inter-agency data sharing capabilities
- **Key Features Required:** OSINT automation, scammers database, compliance reporting, audit trail, data export, Financial Overview database
- **Security Requirements:** PDPA 2010 compliance, CMA 1998 Section 233 alignment, data minimization, data subject rights support, breach notification within 72 hours

### 4.3 Enterprise Corporate (Professional Tier)

- **Profile:** Listed companies, MNCs with Malaysian operations, large e-commerce platforms
- **Need:** Executive protection from deepfake impersonation, brand safety, employee training
- **Budget:** RM 15,000 - RM 50,000 annual subscription
- **Success Criteria:**
  - Detect deepfake impersonation of C-suite executives
  - Protect brand reputation from AI-generated disinformation
  - Employee awareness training with real-time detection
  - Audit trail for corporate governance and Bursa Malaysia disclosure
- **Key Features Required:** Dashboard access, financial risk assessment, scenario planner, compliance reporting
- **Security Requirements:** RBAC with role-based access, audit trail, input validation, output sanitization, no media file persistence

### 4.4 SME & Professional Services (Starter Tier)

- **Profile:** Law firms, private investigators, journalism organizations, small businesses
- **Need:** On-demand deepfake verification for case evidence, journalistic verification, marketplace fraud checks
- **Budget:** RM 3,000 - RM 15,000 annual subscription
- **Success Criteria:**
  - Verify authenticity of media evidence
  - Affordable per-scan pricing
  - Export results for legal/journalistic use
  - Access to scammer database for background checks
- **Key Features Required:** Dashboard access, scan history, CSV export, scammer search
- **Security Requirements:** No PII stored without consent, scan metadata only (no media files), input validation, path sanitization

### 4.5 API & Platform Integrators (API Tier)

- **Profile:** Other SaaS platforms, social media monitoring tools, cybersecurity firms
- **Need:** Embed deepfake detection into third-party products via API
- **Budget:** RM 0.50 - RM 2.00 per detection (pay-as-you-go)
- **Success Criteria:**
  - Sub-second API response time
  - 99.5%+ API uptime
  - Volume discounts at scale
  - Clear API documentation and SDK
- **Key Features Required:** REST API, webhook callbacks, rate limiting, API key management (256-bit, SHA-256 hashed, rotated every 30 days)
- **Security Requirements:** API key management via environment variables only (never in code or database), TLS 1.2+ in transit, input validation (file extension whitelist, 50MB size limit, magic bytes), output sanitization (HTML escaping, 200-char error truncation)

---

## 5. Pricing Model

### 5.1 Pricing Tiers

| Tier | Price Range | Target Segment | Key Deliverables |
|------|-------------|----------------|------------------|
| Enterprise | RM 50K-250K/yr | Banks & Financial | Full platform, API, compliance, audit trail, dedicated support |
| Professional | RM 15K-50K/yr | Corporate Enterprise | Dashboard, financial risk, scenario planner, compliance reports |
| Starter | RM 3K-15K/yr | SME & Professional | Dashboard, scan history, CSV export, scammer search |
| API | RM 0.50-2.00/detection | Platform Integrators | REST API, webhooks, rate-limited endpoints |
| Government | Custom | Government & Regulatory | Full platform, OSINT automation, inter-agency sharing |

### 5.2 Pricing Rationale

- **Enterprise pricing** anchored to the RM 122 million single-case loss — even preventing one such incident at the RM 250K tier yields 488x ROI for that year alone. The blended 41.7x ROI across a portfolio of incidents justifies the premium.
- **Professional pricing** positioned as 10-30% of an enterprise security budget — accessible for corporate compliance teams without requiring CISO approval.
- **Starter pricing** designed for self-service adoption with minimal onboarding friction — the RM 3,000 entry point is below the average deepfake case loss of RM 5,991, making the value proposition self-evident.
- **API pricing** set at RM 0.50-2.00 per detection, competitive with Sightengine's direct API while adding financial risk context and scammer database lookups at no extra cost.
- **Government pricing** flexibly structured to accommodate procurement cycles, inter-agency sharing agreements, and grant-funded deployments.

### 5.3 Volume Discounts

| Monthly API Volume | Discount | Additional Benefit |
|---------------------|----------|--------------------|
| 10,000+ detections | 15% off per-detection price | Standard support |
| 50,000+ detections | 25% off per-detection price | Priority email support |
| 100,000+ detections | 35% off per-detection price | Priority support + dedicated Slack channel |

### 5.4 Add-On Services

- Custom model fine-tuning on customer-specific deepfake patterns: RM 20,000 one-time
- Dedicated on-premise ELA deployment: RM 10,000 setup + RM 5,000/year maintenance
- Custom compliance report templates: RM 2,000 per template
- Security audit support package: RM 5,000 per audit cycle

---

## 6. Revenue Projections

### 6.1 Three-Year Revenue Scenarios

**Conservative Scenario:**
- Year 1: RM 480,000 (2 enterprise + 5 professional + 10 starter + 5K API detections/month)
- Year 2: RM 920,000 (3 enterprise + 8 professional + 20 starter + 15K API/month)
- Year 3: RM 1,560,000 (5 enterprise + 12 professional + 30 starter + 25K API/month)
- Cumulative 3-year revenue: RM 2.96 million
- Break-even: Not reached within 3 years without additional funding or cost reduction

**Base Scenario:**
- Year 1: RM 820,000 (3 enterprise + 8 professional + 15 starter + 10K API/month)
- Year 2: RM 1,650,000 (5 enterprise + 15 professional + 30 starter + 25K API/month)
- Year 3: RM 2,900,000 (8 enterprise + 25 professional + 50 starter + 50K API/month)
- Cumulative 3-year revenue: RM 5.37 million
- Break-even: Year 3 (revenue RM 2.9M approaching operating cost RM 4.69M with deferred revenue recognition from multi-year contracts)

**Optimistic Scenario:**
- Year 1: RM 1,240,000 (5 enterprise + 12 professional + 25 starter + 20K API/month)
- Year 2: RM 2,480,000 (8 enterprise + 20 professional + 40 starter + 40K API/month)
- Year 3: RM 4,350,000 (12 enterprise + 35 professional + 70 starter + 80K API/month)
- Cumulative 3-year revenue: RM 8.07 million
- Break-even: Year 2 (revenue RM 2.48M vs operating cost RM 2.94M — near break-even with deferred recognition)

### 6.2 Revenue Mix (Base Scenario, Year 3)

| Segment | Revenue | Percentage |
|---------|---------|------------|
| Enterprise contracts | RM 1,500,000 | 52% |
| Professional contracts | RM 750,000 | 26% |
| Starter contracts | RM 450,000 | 15% |
| API detections | RM 150,000 | 5% |
| Government contracts | RM 50,000 | 2% |

### 6.3 Cost Structure

| Cost Category | Year 1 | Year 2 | Year 3 |
|---------------|--------|--------|--------|
| Personnel (4 FTE → 8 FTE) | RM 960,000 | RM 1,440,000 | RM 2,400,000 |
| Infrastructure (WorkBuddy, cloud) | RM 120,000 | RM 180,000 | RM 280,000 |
| API Costs (Sightengine, Gemini) | RM 240,000 | RM 420,000 | RM 720,000 |
| Marketing & Sales | RM 180,000 | RM 320,000 | RM 560,000 |
| Legal & Compliance | RM 80,000 | RM 140,000 | RM 240,000 |
| R&D / Model Training | RM 50,000 | RM 90,000 | RM 160,000 |
| Office & Operations | RM 0 | RM 80,000 | RM 130,000 |
| Contingency (10% buffer) | Included | Included | Included |
| **Total Operating Cost** | **RM 1,630,000** | **RM 2,940,000** | **RM 4,690,000** |

Operating costs include a 10% contingency buffer in each year. The progression from RM 1.63M (Year 1) to RM 4.69M (Year 3) reflects team growth from 4 to 8 FTE and scaling API, marketing, and compliance investments.

### 6.4 Break-Even Analysis

| Scenario | Break-Even Year | Y3 Revenue vs Cost |
|----------|----------------|---------------------|
| Conservative | Not within 3 years | RM 1.56M vs RM 4.69M |
| Base | Year 3 | RM 2.90M vs RM 4.69M |
| Optimistic | Year 2 | RM 4.35M vs RM 4.69M |

- **Base case break-even:** Year 3 (revenue RM 2.9M approaches operating cost RM 4.69M with partial recognition of multi-year contracts and deferred revenue)
- **Optimistic case break-even:** Year 2 (revenue RM 2.48M vs cost RM 2.94M — near break-even with deferred recognition and multi-year prepayment)
- **Conservative case:** No break-even within 3 years without additional funding or cost reduction

### 6.5 ROI for Customers

| Customer Segment | Annual Investment | Projected Loss Prevention | ROI Ratio |
|------------------|-------------------|--------------------------|-----------|
| Bank (conservative) | RM 100,000 | RM 420,000 | 4.2x |
| Bank (optimistic) | RM 100,000 | RM 4,170,000 | 41.7x |
| Corporate Enterprise | RM 30,000 | RM 150,000 | 5.0x |
| Government Agency | RM 200,000 | RM 2,000,000 | 10.0x |
| SME (per scan) | RM 50 | RM 500 | 10.0x |

The 41.7x optimistic ROI for banks is grounded in the RM 122 million single-case loss: if LAICIs prevents one such incident at RM 250K annual subscription, the ROI is 488x for that year alone. The 41.7x figure averages this across a portfolio of incidents. The 4.2x conservative ROI assumes prevention of smaller, more frequent fraud events (average RM 5,991 per case) at scale.

### 6.6 Funding Strategy

- **Seed funding:** Bootstrapped from hackathon prize + initial Starter/API revenue
- **Year 1 bridge:** RM 500K-1M angel/seed round if conservative scenario materializes
- **Year 2 growth:** RM 2M-5M Series A if base scenario tracks (needed to fund 8 FTE scale-up)
- **Revenue-funded path:** Possible under optimistic scenario (Y1 RM 1.24M covers 76% of Y1 RM 1.63M cost)

---

## 7. Competitive Landscape

### 7.1 Direct Competitors

| Competitor | Strength | Gap LAICIs Fills |
|------------|---------|-------------------|
| Sightengine (API) | Strong global API, mature | No financial risk layer, no Malaysian context, no scammer DB |
| Sensity AI | Deepfake specialization | Expensive, no local deployment, no ELA fallback |
| Sentinel AI | Enterprise-grade | US-centric, no Malaysian regulatory alignment |
| Reality Defender | Good detection accuracy | No agentic workflow, no self-service data portal |

### 7.2 Competitive Advantages

1. **Financial Intelligence Layer:** Only platform that maps detection scores to RM-denominated financial risk and ROI — every detection includes a monetary risk assessment.
2. **Malaysian Market Focus:** Local scam statistics (RM 5.62B losses), scammers database, regulatory alignment (PDPA, CMA, BNM RMCD).
3. **Multi-Model Redundancy:** 5 detection modules with graceful fallbacks — ELA (local, free) ensures the platform never has zero-coverage even if all APIs are down.
4. **WorkBuddy Native:** No external server infrastructure needed — runs within the WorkBuddy AI ecosystem, inheriting platform security and scalability.
5. **Data User Self-Service:** RAG-powered Q&A (rag_search.py) and CSV/JSON exports reduce analyst dependency on developers.
6. **Agentic Workflow:** 7-step autonomous pipeline (not just an API call) — understands context, plans, validates, and assesses financial risk.
7. **ELA Always Available:** Local Pillow-based analysis requires no API key — guaranteed minimum detection capability.
8. **Loss Prevention Tracker:** Cumulative prevented-loss counter on the dashboard — a marketing and stakeholder reporting tool.
9. **Three-Domain Integration:** Finance + Data + Security in one platform — competitors typically address only one or two.

### 7.3 Competitive Risks

- Sightengine could add financial risk features directly to their API
- Open-source detection models (e.g., DeepfakeBench) could commoditize basic detection
- Malaysian government could build an in-house solution
- **Mitigation:** Focus on the agentic workflow + financial intelligence layer + security compliance as the combined moat, not raw detection accuracy alone

---

## 8. Financial Intelligence Business Case

### 8.1 Financial Risk Assessor

The Financial Risk Assessor is the core v2.0 module that transforms raw detection scores into business-actionable financial intelligence. It operates as Step 7 of the agentic workflow (FINANCIAL_RISK_ASSESS), executing after the detection pipeline completes.

**Function:** Given a detection result (deepfake probability score, media type, context), the Financial Risk Assessor calculates:
- **Exposure Estimate:** RM-denominated potential loss based on Malaysian scam statistics (average RM 5,991 per case, up to RM 122M for corporate impersonation)
- **Risk Tier:** Low / Medium / High / Critical — mapped to detection confidence and media type
- **Recommended Action:** Transaction hold, manual review, alert escalation, or proceed
- **Comparable Cases:** Historical cases from the Scans and Financial Overview databases with similar characteristics

**Business Value:** Every detection result includes a monetary figure, enabling non-technical stakeholders (fraud officers, risk managers, executives) to make informed decisions without interpreting technical confidence scores. This is the primary differentiator from competitors.

### 8.2 Loss Prevention Tracker

The Loss Prevention Tracker is a cumulative dashboard widget that displays the total RM value of losses prevented by LAICIs v2.0 across all customer deployments.

**Mechanism:**
- Each scan that flags a deepfake with High or Critical confidence contributes to the counter
- The prevented-loss value is calculated using the Financial Risk Assessor's exposure estimate for that scan
- The counter is displayed prominently on the dashboard header (published dashboard: https://workbuddy.cc/p/NgyKSRIdG71xKlqxI0JrGa)
- Prevented-loss values are linked to specific scan records in the Scans database for audit verification

**Business Value:**
- Marketing asset: "LAICIs has prevented RM X million in scam losses" — a quantifiable impact statement
- Stakeholder reporting: Quarterly Loss Prevention Impact Reports for customers and investors
- Internal motivation: Team sees real-world impact of their work
- Government engagement: Demonstrates national-level value for procurement discussions

### 8.3 ROI Calculator

The ROI Calculator is a self-service widget available to prospective customers on the dashboard and to existing customers in their portal.

**Inputs:**
- Customer segment (Bank, Corporate, Government, SME)
- Annual detection volume estimate
- Average transaction value at risk
- Current fraud loss rate

**Outputs:**
- Projected annual loss prevention value (RM)
- ROI ratio (prevention value / LAICIs subscription cost)
- Comparison to Malaysian national average loss per case (RM 5,991)
- Comparison to the RM 122M corporate deepfake case (worst-case scenario)
- Break-even point (how many prevented cases needed to cover subscription cost)

**Preset Scenarios:**
- Conservative: 4.2x ROI for banks (prevents 42 average-case RM 5,991 incidents per RM 250K subscription)
- Optimistic: 41.7x ROI for banks (prevents a fraction of one RM 122M corporate case per RM 250K subscription)

**Business Value:** Self-qualifies prospects before sales engagement — customers see their own ROI before speaking to sales, reducing CAC and shortening the sales cycle.

### 8.4 Financial Overview Database (NEW)

The Financial Overview database is a new library database (9 fields) that aggregates Malaysian scam financial data for trend analysis and ROI calculations.

**Fields (9):**
1. `id` — Unique record identifier
2. `period` — Time period (e.g., "H1 2024", "2023-2025")
3. `category` — Scam category (deepfake, investment, Macau, e-commerce, etc.)
4. `total_cases` — Number of reported cases
5. `total_losses_rm` — Total losses in RM
6. `avg_loss_per_case_rm` — Average loss per case (RM)
7. `recovery_rate_pct` — Recovery rate percentage
8. `yoy_change_pct` — Year-over-year change percentage
9. `source` — Data source citation

**Business Value:**
- Powers the Financial Risk Assessor with current Malaysian benchmark data
- Feeds the ROI Calculator with accurate per-case loss averages
- Provides trend analysis for government reporting and marketing
- Queryable via the self-service data portal

### 8.5 Financial KPIs Tracked

- Cumulative prevented-loss value (RM) — displayed on dashboard
- Monthly prevented-loss value (RM) — internal reporting
- Average exposure estimate per High/Critical scan (RM)
- ROI delivered per customer (actual vs projected)
- Revenue per prevented-loss RM (efficiency metric)
- Financial Overview database records count
- Quarterly Loss Prevention Impact Reports published

---

## 9. Data Strategy & Governance

### 9.1 Library Databases

LAICIs v2.0 uses three WorkBuddy library databases within the **DORMATHON26_TECHBENG** space (spaceId: CSfJ5htmA2LY98nVeDfVD3):

**Database 1: Scans (22 fields)**
- Database ID: fCCH5jUKxdxaQbWoVbiRVx
- Purpose: Records every media scan performed, including detection scores, financial risk assessment, and audit metadata
- Key fields include: scan_id, timestamp, media_type, file_hash, sightengine_score, ela_score, ml_score, gemini_score, weighted_score, deepfake_probability, financial_risk_tier, exposure_estimate_rm, recommended_action, scan_source, analyst_id, case_reference, scammer_id_link, status, notes, ip_address, session_id, audit_hash
- Retention: Scan metadata retained indefinitely for trend analysis and audit trail

**Database 2: Scammers (16 fields)**
- Database ID: w7KwBxeUOZpa2WFiUJRqaB
- Purpose: Catalogs identified scammer profiles (emails, phone numbers, websites, social media accounts) linked to deepfake fraud
- Key fields include: scammer_id, first_seen, last_seen, identifier_type, identifier_value, associated_cases, total_losses_rm, status, threat_level, osint_source, verification_status, linked_scans, country, reported_by, tags, notes
- Retention: Scammer profiles retained indefinitely as intelligence records (no PII without consent)

**Database 3: Financial Overview (9 fields, NEW)**
- Purpose: Aggregates Malaysian scam financial data for trend analysis and ROI calculations
- Fields: id, period, category, total_cases, total_losses_rm, avg_loss_per_case_rm, recovery_rate_pct, yoy_change_pct, source
- Retention: Financial overview data retained indefinitely as reference data
- Populated from: LAICIs Research Report (25 sources), OSINT automation pipeline, manual entry

### 9.2 Knowledge Base Nodes

LAICIs v2.0 populates two knowledge base nodes within the WorkBuddy library for RAG-powered Q&A:

**Data Node (scam statistics, case data, trends):**
- Content: Malaysian scam statistics (RM 5.62B total losses, 454 deepfake cases H1 2024, 76% YoY increase, 85% victim belief rate, 2% recovery rate)
- Sources: PDRM CCID, Bukit Aman, BNM, SFMS, LAICIs Research Report (25 sources)
- Purpose: Enables users to query scam statistics in natural language ("How many deepfake cases were reported in H1 2024?")
- Updated: Automatically via OSINT automation pipeline and manually for curated data

**Finance Node (pricing, ROI, cost structures):**
- Content: Pricing tiers (5 tiers, RM 3K-250K), ROI calculations (4.2x-41.7x), operating costs (Y1 RM 1.63M → Y3 RM 4.69M), revenue projections (3 scenarios), cost structure breakdown, break-even analysis
- Purpose: Enables users to query financial data in natural language ("What is the ROI for a bank at the Enterprise tier?")
- Updated: Manually by analysts and automatically when pricing/cost data changes

### 9.3 RAG-Powered Q&A Engine

The RAG (Retrieval-Augmented Generation) Q&A engine is implemented as `rag_search.py` and provides natural-language querying over the knowledge base nodes.

**Architecture:**
1. User submits a natural-language question via the dashboard or API
2. `rag_search.py` retrieves relevant content from the Data and Finance knowledge base nodes
3. Retrieved content is used to augment a generation prompt
4. The model generates an answer grounded in the retrieved content
5. Answer includes source citations for verification

**Capabilities:**
- Query scam statistics ("What were the total deepfake losses in H1 2024?" → RM 2.72 million)
- Query pricing ("What does the Enterprise tier cost?" → RM 50K-250K/year)
- Query ROI ("What is the conservative ROI for banks?" → 4.2x)
- Query trends ("What is the YoY increase in deepfake cases?" → 76%)
- Query data retention policies ("How long is audit trail data kept?" → 7 years)

**Performance Targets:**
- 500+ queries per month by end of Year 1
- 85%+ relevance score (user satisfaction with answer quality)
- < 5 seconds average response time

### 9.4 OSINT Automation Pipeline

The OSINT (Open Source Intelligence) automation pipeline runs daily at 9 AM (automation ID: 2453f597-10da-4990-9203-06669db4c19d) and automatically collects, extracts, structures, and loads scam intelligence into the library databases.

**Pipeline Steps:**
1. **WebSearch:** Search for Malaysian scam news, PDRM CCID reports, BNM fraud alerts, MCMC deepfake advisories
2. **Extract:** Parse search results for relevant scam data (case counts, loss amounts, scammer identifiers, deepfake indicators)
3. **Structure:** Transform extracted data into structured records matching the Scammers and Financial Overview database schemas
4. **Load:** Insert structured records into the appropriate library database
5. **Dashboard Update:** Refresh the published dashboard with new data

**Automation Configuration:**
- Schedule: Daily at 9:00 AM MYT
- Automation ID: 2453f597-10da-4990-9203-06669db4c19d
- Search sources: Google News (Malaysia), PDRM CCID press releases, BNM fraud alerts, MCMC advisories, The Star, New Straits Times, Bernama
- Output: Records inserted into Scammers database (w7KwBxeUOZpa2WFiUJRqaB) and Financial Overview database

**Success Metrics:**
- 95%+ successful daily run rate
- 10+ new scammer profiles per week (average)
- 5+ new Financial Overview records per month
- Data freshness: < 24 hours between public report and library ingestion

### 9.5 Self-Service Data Query Portal

The self-service data query portal allows non-technical users (analysts, compliance officers, executives) to query the library databases without developer intervention.

**Capabilities:**
- **Filter:** Filter records by any field (e.g., date range, risk tier, scammer status, loss range)
- **Sort:** Sort by any field ascending or descending
- **Export:** Export filtered results to CSV or JSON format
- **Search:** Full-text search across all text fields
- **Aggregate:** Basic aggregations (count, sum, average) on filtered results

**Access Control:**
- Admin: Full access to all databases and all operations
- Analyst: Full query and export access to Scans and Scammers; read-only on Financial Overview
- Viewer: Query-only access (no export)
- API User: API-based query access only (no portal UI)

**Business Value:**
- Reduces developer dependency for routine data queries
- Enables compliance officers to generate ad-hoc reports
- Allows executives to self-serve ROI and trend data
- Exports are audit-logged (part of the 7-field audit trail)

### 9.6 Automated Data Pipeline

The end-to-end automated data pipeline transforms raw web intelligence into structured, queryable, dashboard-ready data:

**Pipeline Flow:**
```
WebSearch → extract → structure → library database → dashboard refresh
```

**Step Details:**
1. **WebSearch:** WorkBuddy WebSearch tool queries Malaysian scam news and regulatory sources
2. **Extract:** Python scripts parse HTML/JSON responses for scam-relevant data points
3. **Structure:** Extracted data is normalized into database-ready records (field mapping, type conversion, deduplication)
4. **Library:** Records are inserted into the appropriate WorkBuddy library database via the platform API
5. **Dashboard:** The published dashboard (https://workbuddy.cc/p/NgyKSRIdG71xKlqxI0JrGa) is refreshed with new data

**Quality Controls:**
- Deduplication: Records are checked against existing entries to prevent duplicates
- Source verification: Data is tagged with its source for traceability
- Confidence scoring: OSINT-derived data is marked as "unverified" until cross-referenced
- Manual review queue: Low-confidence records are queued for analyst review before publishing

### 9.7 Data Retention Policy

| Data Type | Retention Period | Rationale |
|-----------|-----------------|-----------|
| Scan metadata (scores, timestamps, audit fields) | Indefinite | Trend analysis, audit trail, model training |
| Media files (uploaded images/videos) | NOT stored — process and discard | PDPA compliance, data minimization |
| Audit trail records | 7 years | Regulatory compliance, dispute resolution |
| OSINT raw data (raw web pages, unstructured text) | 90 days | Source verification window, then deleted |
| Scammer profiles | Indefinite | Intelligence records (no PII without consent) |
| Financial Overview records | Indefinite | Reference data for ROI calculations |
| Knowledge base content | Indefinite (versioned) | RAG Q&A engine source material |

### 9.8 Data Governance

**Data Minimization:**
- Only collect data necessary for the stated purpose (deepfake detection and scam prevention)
- No PII (personally identifiable information) collected without explicit consent
- Media files are processed in memory and discarded — never persisted to disk or database
- OSINT raw data is deleted after 90 days (only structured, anonymized records are retained)

**Data Subject Rights:**
- Right to access: Individuals can request what data LAICIs holds about them
- Right to rectification: Inaccurate scammer profiles can be corrected
- Right to erasure: Individuals can request deletion of their personal data (subject to legal retention requirements)
- Right to object: Individuals can object to their data being used for scam prevention (balanced against public interest)
- Consent management: All data collection explicitly documents the legal basis (consent, legitimate interest, legal obligation)

**Data Quality:**
- OSINT-derived data is marked as "unverified" until cross-referenced with a second source
- Manual review queue for low-confidence records
- Source citations are mandatory for all Financial Overview records
- Deduplication runs on every database insert

**Data Sharing:**
- No data sharing with third parties without explicit customer consent
- Government data sharing follows formal inter-agency agreements
- API responses contain only the requesting customer's own data (tenant isolation)
- Audit trail records who accessed what data and when

---

## 10. Security & Compliance Business Case

### 10.1 PDPA 2010 Compliance (Personal Data Protection Act)

LAICIs v2.0 is designed for full compliance with the Malaysian Personal Data Protection Act 2010.

**Principles:**
- **Consent Principle:** No PII collected, processed, or stored without explicit, informed, and documented consent. Scan subjects are informed that their media will be analyzed for deepfake detection.
- **Data Minimization Principle:** Only data necessary for the stated purpose is collected. Media files are processed in memory and discarded — never stored. Only scan metadata (scores, timestamps, audit fields) is retained.
- **Purpose Principle:** Data is used only for the stated purpose (deepfake detection and scam prevention). No secondary use without fresh consent.
- **Disclosure Principle:** No data shared with third parties without explicit customer consent. Government data sharing follows formal inter-agency agreements.
- **Security Principle:** TLS 1.2+ encryption in transit, WorkBuddy platform encryption at rest, RBAC with 4 roles, immutable audit trail.
- **Data Retention Principle:** Scan metadata indefinite (anonymized), media files not stored, audit trail 7 years, OSINT raw 90 days.
- **Data Integrity Principle:** Data is accurate and kept up to date. OSINT-derived data is marked as "unverified" until cross-referenced.
- **Access Principle:** Data subjects can request access to their data. Data subject rights (access, rectification, erasure, objection) are supported.

**Breach Notification:**
- Personal data breaches are notified to the Data Protection Commissioner and affected individuals within **72 hours** of discovery
- Breach notification includes: nature of breach, data categories affected, estimated number of individuals affected, measures taken, contact point for further information

### 10.2 CMA 1998 Compliance (Communications and Multimedia Act)

LAICIs v2.0 aligns with Section 233 of the Communications and Multimedia Act 1998, which criminalizes the creation and distribution of offensive content, including deepfake impersonation content.

**Alignment:**
- LAICIs v2.0 is positioned as a **detection and prevention tool** that helps organizations identify Section 233 violations
- Detection reports can be exported as evidence for PDRM/MCMC enforcement actions
- The scammers database catalogs identifiers associated with Section 233 violations
- OSINT automation monitors for publicly reported Section 233 cases
- Compliance reports include references to CMA 1998 Section 233 for regulatory alignment

### 10.3 BNM RMCD Guidelines Compliance

Bank Negara Malaysia's Risk Management in Technology (RMCD) Guidelines require financial institutions to implement robust fraud detection and reporting mechanisms.

**LAICIs v2.0 Alignment:**
- **Fraud Detection:** 5-module detection engine with financial risk assessment meets RMCD technology risk management requirements
- **Reporting:** Automated compliance report generation for BNM regulatory submissions
- **Audit Trail:** 7-field immutable audit trail satisfies RMCD logging and monitoring requirements
- **Access Control:** RBAC with 4 roles and OAuth 2.0 authentication meets RMCD access management requirements
- **Incident Response:** 4-severity-level incident response framework aligns with RMCD incident management expectations
- **Data Protection:** No media file persistence and data minimization satisfy RMCD data protection requirements

### 10.4 Role-Based Access Control (RBAC)

LAICIs v2.0 implements 4 roles with distinct permissions:

| Role | Access Level | Key Permissions |
|------|-------------|-----------------|
| Admin | Full control | All operations, user management, API key rotation, audit trail access |
| Analyst | Operational | Scan initiation, database queries, CSV/JSON export, scammer profile management |
| Viewer | Read-only | Dashboard view, query-only (no export), no configuration changes |
| API User | API-only | REST API calls, webhook configuration, rate-limited endpoints |

**Authentication:**
- WorkBuddy platform OAuth 2.0 for interactive users (Admin, Analyst, Viewer)
- API keys for API Users: 256-bit random keys, SHA-256 hashed at rest, rotated every 30 days
- API keys stored in environment variables only — never hardcoded, never stored in database
- Session management via WorkBuddy platform (session_id logged in audit trail)

### 10.5 Encryption

| Layer | Standard |
|-------|----------|
| Data in transit | TLS 1.2+ (Transport Layer Security) |
| Data at rest | WorkBuddy platform encryption (platform-managed) |
| API keys at rest | SHA-256 hashed (never stored in plaintext) |
| Media files in memory | Processed and discarded — no persistence |
| Audit trail | Append-only, immutable (no updates or deletes) |

### 10.6 API Key Management

- API keys are 256-bit cryptographically random values
- Keys are SHA-256 hashed before storage — the plaintext key is shown only once at creation
- Keys are stored in **environment variables only** — never in source code, never in the database, never in configuration files
- Keys are rotated every 30 days (automated reminder + manual rotation by Admin)
- Key revocation is immediate and propagated to all active sessions
- Key usage is logged in the audit trail (which key, which action, which timestamp)

### 10.7 Audit Trail

The audit trail records every significant action on the platform with 7 fields:

| Field | Description |
|-------|-------------|
| timestamp | ISO 8601 timestamp of the action |
| actor | User ID or API key ID that performed the action |
| action | Action type (scan, query, export, login, config_change, key_rotation) |
| target | Object affected (scan_id, database_id, record_id, user_id) |
| result | Outcome (success, failure, denied) |
| ip | IP address of the requester |
| session_id | Session identifier for correlation |

**Properties:**
- **Append-only:** Records can be added but never modified or deleted
- **Immutable:** No UPDATE or DELETE operations permitted on audit trail records
- **Retention:** 7 years (regulatory compliance for financial institutions)
- **Tamper-evident:** Each record includes an audit hash chaining to the previous record
- **Exportable:** Admin can export audit trail to CSV/JSON for compliance audits

### 10.8 OWASP Top 10 Compliance

| OWASP Risk | Mitigation in LAICIs v2.0 |
|------------|------------------------------|
| A01: Broken Access Control | RBAC with 4 roles, OAuth 2.0, session validation |
| A02: Cryptographic Failures | TLS 1.2+ in transit, SHA-256 for API keys, platform encryption at rest |
| A03: Injection | Parameterized queries, input validation, path sanitization |
| A04: Insecure Design | STRIDE threat model, security-by-design principles |
| A05: Security Misconfiguration | Environment variables for secrets, no default credentials |
| A06: Vulnerable Components | Quarterly dependency scanning, code review before merge |
| A07: Auth Failures | OAuth 2.0, API key rotation every 30 days, session management |
| A08: Data Integrity Failures | Immutable audit trail, append-only design, tamper-evident hashing |
| A09: Logging Failures | 7-field audit trail, append-only, 7-year retention |
| A10: SSRF | Input validation, URL allowlist for OSINT sources, output sanitization |

### 10.9 STRIDE Threat Model

| Threat Category | Description | LAICIs Mitigation |
|----------------|-------------|---------------------|
| Spoofing | Attacker impersonates a legitimate user | OAuth 2.0 authentication, 256-bit API keys, session validation |
| Tampering | Attacker modifies data in transit or at rest | TLS 1.2+ encryption, immutable audit trail, tamper-evident hashing |
| Repudiation | User denies performing an action | 7-field audit trail (timestamp, actor, action, target, result, ip, session_id) |
| Information Disclosure | Sensitive data exposed to unauthorized parties | RBAC, no media persistence, data minimization, output sanitization |
| Denial of Service | Attacker overwhelms the system | Rate limiting, 50MB file size limit, input validation |
| Elevation of Privilege | User gains unauthorized access level | RBAC enforcement on every operation, API key scope validation |

### 10.10 Incident Response

LAICIs v2.0 defines 4 incident severity levels with response time targets:

| Severity | Response Time | Examples | Actions |
|----------|--------------|----------|---------|
| Critical | 1 hour | Active data breach, system compromise | Immediate containment, PDPA 72hr notification, all-hands response |
| High | 4 hours | Audit trail tampering attempt, API key leak | Key revocation, access freeze, forensic investigation |
| Medium | 24 hours | Failed access control, suspicious query pattern | Access review, logging enhancement, user notification |
| Low | 72 hours | Minor misconfiguration, dependency vulnerability | Patch, configuration update, documentation |

**Incident Response Process:**
1. **Detect:** Automated monitoring alerts or manual report
2. **Triage:** Severity assessment within response time window
3. **Contain:** Immediate actions to limit blast radius (key revocation, access freeze)
4. **Investigate:** Forensic analysis using audit trail data
5. **Notify:** PDPA breach notification within 72 hours for personal data breaches
6. **Remediate:** Fix root cause, patch, update controls
7. **Post-Mortem:** Document incident, update threat model, improve controls

### 10.11 Vulnerability Management

- **Quarterly dependency scanning:** All Python packages and WorkBuddy platform dependencies scanned for known vulnerabilities (CVE database)
- **Code review before merge:** All code changes reviewed by at least one team member before merging — security implications explicitly assessed
- **Automated testing:** Input validation tests, output sanitization tests, RBAC enforcement tests run on every deployment
- **Penetration testing:** Planned for Year 2 (aligned with ISO 27001 certification timeline)
- **Bug bounty:** Considered for Year 3 when revenue supports it

### 10.12 Input Validation

| Control | Implementation |
|---------|---------------|
| File extension whitelist | Only .jpg, .jpeg, .png, .mp4, .avi, .webm accepted |
| File size limit | 50MB maximum (rejected with clear error message) |
| Path sanitization | All file paths stripped of directory traversal sequences (../, ..\) |
| Magic bytes verification | File content verified against extension (no extension spoofing) |
| SQL injection prevention | Parameterized queries only, no string concatenation |
| XSS prevention | All user input HTML-escaped before rendering |

### 10.13 Output Sanitization

| Control | Implementation |
|---------|---------------|
| HTML escaping | All dynamic content HTML-escaped before rendering |
| Error message truncation | Error messages truncated to 200 characters, no internal details exposed |
| API response sanitization | No stack traces, no internal paths, no database schema in API responses |
| Log sanitization | No PII in logs, no API keys in logs, no media content in logs |

### 10.14 No Media File Persistence

LAICIs v2.0 does **not** store uploaded media files:
- Media is received via upload or API
- Media is processed in memory by the detection pipeline (Sightengine API, ELA analysis, ML inference, Gemini analysis)
- Media is discarded immediately after processing — never written to disk, never stored in database
- Only scan metadata (scores, timestamps, audit fields) is persisted
- This is the single most important PDPA compliance control: if media is never stored, it cannot be breached

### 10.15 Security Certification Positioning

| Certification | Target Year | Business Driver |
|---------------|------------|-----------------|
| PDPA 2010 compliance | Year 1 (launch) | Malaysian legal requirement |
| CMA 1998 alignment | Year 1 (launch) | Malaysian legal requirement |
| BNM RMCD alignment | Year 1 (launch) | Bank customer requirement |
| ISO 27001 | Year 2 | Enterprise/government sales enabler |
| SOC 2 Type II | Year 3 | International expansion enabler |

### 10.16 Data Breach Cost Avoidance (ROI Driver)

The security posture itself generates ROI through breach cost avoidance:

- **Average data breach cost in Malaysia:** RM 3.4 million (IBM Cost of a Data Breach Report, Southeast Asia)
- **LAICIs v2.0 security investment:** Included in operating costs (no separate security budget line)
- **Breach avoidance ROI:** If LAICIs's security posture prevents one data breach at a customer site, the avoided cost (RM 3.4M) exceeds the customer's entire annual subscription (RM 50K-250K) by 13.6x to 68x
- **Insurance premium reduction:** Security-conscious customers (banks, enterprises) may qualify for reduced cybersecurity insurance premiums when deploying LAICIs v2.0 with ISO 27001 certification — estimated 10-15% premium reduction
- **Reputation protection:** A single deepfake incident can cause reputational damage exceeding the direct financial loss — LAICIs's prevention capability avoids both

---

## 11. Risk Factors & Mitigation

### 11.1 Business Risks

**R1: Slow Enterprise Sales Cycle**
- *Risk:* Bank/government procurement takes 6-18 months
- *Impact:* Year 1 revenue below projections
- *Mitigation:* Launch Starter/API tiers immediately for cash flow; use government pilot programs to accelerate enterprise sales; offer 3-month free pilots to banks

**R2: API Cost Escalation**
- *Risk:* Sightengine or Gemini raise API pricing
- *Impact:* Gross margin compression on API tier
- *Mitigation:* ELA fallback reduces API dependency; ML model (local) can eventually replace Sightengine for image analysis; negotiate volume discounts; pass through to API tier pricing

**R3: Deepfake Arms Race**
- *Risk:* Generative AI improves faster than detection
- *Impact:* False negatives erode customer trust
- *Mitigation:* Multi-model approach (5 modules) provides redundancy; regular model retraining; ELA catches physical-level manipulation that AI-generated content cannot avoid; quarterly benchmark testing

**R4: Regulatory Uncertainty**
- *Risk:* Malaysian deepfake legislation could mandate specific certifications
- *Impact:* Compliance burden or market restriction
- *Mitigation:* Engage with MCMC and Ministry of Communications early; position LAICIs as the compliant solution; pursue ISO 27001 in Year 2 to pre-empt certification requirements

**R5: Single-Platform Dependency**
- *Risk:* Complete reliance on WorkBuddy ecosystem
- *Impact:* Platform changes could affect availability
- *Mitigation:* Core detection modules (Python) are portable; database schemas are documented; maintain local HTML dashboard as fallback; knowledge of platform internals reduces migration risk

### 11.2 Technical Risks

**T1: ML Model Accuracy**
- *Risk:* EfficientNetV2-S model not trained on Malaysian-context deepfakes
- *Impact:* Lower accuracy on local content
- *Mitigation:* Collect scan metadata (with consent) for domain-specific fine-tuning; Sightengine as primary, ML as secondary; quarterly benchmark testing on new deepfake samples

**T2: Gemini API Reliability**
- *Risk:* Gemini API outages or rate limits
- *Impact:* Video analysis degradation
- *Mitigation:* Fallback to 100% Sightengine visual scoring; WorkBuddy keyless LLM as alternative; ELA always available as last resort

**T3: Data Privacy Compliance**
- *Risk:* Scanned media contains PII subject to PDPA
- *Impact:* Legal liability if data mishandled
- *Mitigation:* No persistent storage of scanned media (process and discard); database stores only metadata and scores; explicit user consent for scan logging; 72-hour breach notification process

**T4: Database Scalability**
- *Risk:* Scans database grows beyond WorkBuddy library capacity
- *Impact:* Query performance degradation
- *Mitigation:* Archive records older than 2 years to cold storage; index optimization; paginated queries in the self-service portal

### 11.3 Security Risks

**S1: API Key Compromise**
- *Risk:* API key leaked or stolen
- *Impact:* Unauthorized API access, cost abuse, data exposure
- *Mitigation:* Keys are 256-bit, SHA-256 hashed, stored in environment variables only, rotated every 30 days, immediate revocation capability, rate limiting, audit trail logging of all key usage

**S2: Injection Attacks**
- *Risk:* Malicious input crafted to exploit query or command execution
- *Impact:* Data exfiltration, unauthorized access, system compromise
- *Mitigation:* Parameterized queries, file extension whitelist, magic bytes verification, path sanitization, 50MB size limit, HTML output escaping, error message truncation

**S3: Insider Threat**
- *Risk:* Authorized user intentionally or accidentally misuses data
- *Impact:* Data breach, reputational damage, regulatory penalties
- *Mitigation:* RBAC with 4 roles, immutable audit trail (7 fields, append-only), least-privilege access, Admin-only key rotation and user management, quarterly access review

**S4: Supply Chain Attack**
- *Risk:* Vulnerable dependency compromised
- *Impact:* System compromise through trusted code
- *Mitigation:* Quarterly dependency scanning (CVE database), code review before merge, dependency pinning, WorkBuddy platform security inherited

**S5: Deepfake Evasion**
- *Risk:* Attacker crafts deepfakes specifically designed to evade LAICIs's detection models
- *Impact:* False negatives, customer trust erosion
- *Mitigation:* Multi-model redundancy (5 modules), ELA catches physical-level artifacts that AI generation cannot avoid, regular model retraining, adversarial sample collection (with consent)

---

## 12. Success Metrics & KPIs

### 12.1 Business KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| Monthly Recurring Revenue (MRR) | RM 70K+ by end of Y1 | Stripe/billing system |
| Customer Acquisition Cost (CAC) | < RM 5,000 for Starter tier | Sales spend / new customers |
| Customer Lifetime Value (CLV) | > RM 30,000 for Starter | Subscription value × retention |
| Net Revenue Retention (NRR) | > 110% | Existing customer revenue growth |
| Cumulative prevented-loss value | RM 100M by end of Y2 | Loss Prevention Tracker |
| Active scammer profiles | 1,000+ by end of Y1 | Scammers database count |
| Compliance reports/month | 20+ by end of Q3 2026 | Report generation log |

### 12.2 Product KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| Detection accuracy (true positive rate) | 92%+ | Benchmark test suite |
| False positive rate | < 8% | Benchmark test suite |
| Average scan latency (images) | < 30 seconds | Scan timestamp diff |
| Average scan latency (videos) | < 120 seconds | Scan timestamp diff |
| Dashboard monthly active users | 200+ by end of Y1 | WorkBuddy analytics |
| RAG query volume | 500+/month by end of Y1 | rag_search.py logs |
| RAG relevance score | 85%+ | User feedback rating |
| CSV/JSON exports per month | 100+ by end of Y1 | Export audit trail |

### 12.3 Operational KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| API uptime | 99.5%+ | Health check monitoring |
| Average cost per scan (blended) | < RM 0.30 | API costs / total scans |
| OSINT automation success rate | 95%+ | Daily run log |
| Average scan cost (API tier) | < RM 0.50 per detection | API cost tracking |
| Workflow step completion rate | 99%+ (no crashes) | Error log analysis |

### 12.4 Security KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| Audit trail completeness | 100% of actions logged | Audit trail vs action log comparison |
| Incident response time (Critical) | < 1 hour | Incident timestamp to first response |
| Incident response time (High) | < 4 hours | Incident timestamp to first response |
| API key rotation compliance | 100% within 30 days | Key rotation log |
| Failed access attempts blocked | 100% | RBAC enforcement log |
| Dependency vulnerabilities patched | 100% within 30 days of CVE | Quarterly scan reports |
| PDPA breach notifications (late) | 0 | All within 72 hours |

### 12.5 Data KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| Financial Overview records | 500+ by end of Q2 2026 | Database count |
| Scammer profiles | 1,000+ by end of Y1 | Database count |
| Scans database records | 50,000+ by end of Y1 | Database count |
| OSINT daily run success rate | 95%+ | Automation log (ID: 2453f597) |
| New scammer profiles per week | 10+ average | Weekly database delta |
| Data portal active users | 50+ by end of Y1 | Portal access log |
| Data freshness (OSINT to library) | < 24 hours | Timestamp comparison |
| Knowledge base Q&A relevance | 85%+ satisfaction | User feedback rating |

---

## 13. Implementation Roadmap

### 13.1 Phase 1: MVP Launch (Q1 2026)

**Finance Deliverables:**
- Deploy existing v1.0 dashboard (5 detection modules, weighted scoring)
- Activate Starter (RM 3K-15K) and API (RM 0.50-2.00/detection) pricing tiers
- Populate Finance knowledge base node with pricing, ROI, and cost structure data
- Deploy basic ROI calculator widget (preset scenarios: 4.2x conservative, 41.7x optimistic)

**Data Deliverables:**
- Verify existing Scans database (fCCH5jUKxdxaQbWoVbiRVx, 22 fields) is operational
- Verify existing Scammers database (w7KwBxeUOZpa2WFiUJRqaB, 16 fields) is operational
- Create Financial Overview database (9 fields, NEW) within DORMATHON26_TECHBENG space (CSfJ5htmA2LY98nVeDfVD3)
- Populate Data knowledge base node with scam statistics (RM 5.62B, 454 cases, RM 2.72M, 76% YoY, 85% belief, 2% recovery)
- Activate OSINT automation pipeline (daily 9 AM, ID: 2453f597-10da-4990-9203-06669db4c19d)
- Deploy rag_search.py RAG Q&A engine over both knowledge base nodes
- Publish dashboard at https://workbuddy.cc/p/NgyKSRIdG71xKlqxI0JrGa

**Security Deliverables:**
- Implement RBAC with 4 roles (Admin, Analyst, Viewer, API User)
- Configure OAuth 2.0 authentication via WorkBuddy platform
- Generate 256-bit API keys with SHA-256 hashing, stored in environment variables
- Deploy input validation (file extension whitelist, 50MB limit, path sanitization, magic bytes)
- Deploy output sanitization (HTML escaping, 200-char error truncation)
- Verify no media file persistence (process and discard)
- Implement audit trail (7 fields: timestamp, actor, action, target, result, ip, session_id)
- Document PDPA 2010 compliance framework
- Document CMA 1998 Section 233 alignment
- Document BNM RMCD guidelines alignment

### 13.2 Phase 2: Financial Intelligence (Q2 2026)

**Finance Deliverables:**
- Implement Financial Risk Assessor module (Step 7 of agentic workflow: FINANCIAL_RISK_ASSESS)
- Add financial fields to Scans database (financial_risk_tier, exposure_estimate_rm, recommended_action)
- Deploy Loss Prevention Tracker on dashboard header (cumulative prevented-loss counter)
- Enhance ROI calculator with custom-input capability (customer segment, volume, transaction value)
- Populate Financial Overview database with 500+ records from LAICIs Research Report

**Data Deliverables:**
- Deploy self-service data query portal (filter, sort, search, aggregate)
- Enable CSV and JSON export from the data portal
- Expand OSINT source list (add Bernama, New Straits Times, The Star)
- Implement deduplication logic for OSINT-to-library pipeline
- Implement confidence scoring for OSINT-derived records
- Deploy automated data pipeline: WebSearch → extract → structure → library → dashboard

**Security Deliverables:**
- Enforce API key rotation policy (30-day automated reminders)
- Implement rate limiting on API endpoints
- Conduct first quarterly dependency vulnerability scan
- Implement code review process (mandatory before merge)
- Deploy STRIDE threat model documentation
- Test incident response process (4 severity levels, response time targets)
- Verify audit trail immutability (append-only enforcement)

### 13.3 Phase 3: Enterprise Features (Q3 2026)

**Finance Deliverables:**
- Implement Scenario Planner (best/worst/expected case financial impact)
- Implement Recovery Assistant (actionable recovery guidance for confirmed fraud)
- Deploy compliance reporting engine (BNM RMCD, PDPA, CMA Section 233 report templates)
- Launch Enterprise (RM 50K-250K) and Professional (RM 15K-50K) pricing tiers
- Begin quarterly Loss Prevention Impact Report publication

**Data Deliverables:**
- Enable RAG Q&A over Financial Overview database content
- Deploy data freshness monitoring (alert if OSINT run fails)
- Implement manual review queue for low-confidence OSINT records
- Expand knowledge base nodes with case study content
- Enable inter-agency data export (for government tier)

**Security Deliverables:**
- Begin ISO 27001 certification preparation (gap analysis, documentation)
- Implement penetration testing readiness (test environment setup)
- Deploy automated vulnerability scanning dashboard
- Enforce OWASP Top 10 compliance checklist (A01-A10 verified)
- Implement data subject rights process (access, rectification, erasure, objection)
- Test PDPA breach notification process (72-hour simulation drill)

### 13.4 Phase 4: Scale & Optimize (Q4 2026)

**Finance Deliverables:**
- Pursue enterprise bank contracts (target: 3+ enterprise by end of Y1)
- Pursue government contracts (custom pricing, inter-agency sharing)
- Fine-tune ML model on Malaysian-context deepfake data (domain-specific)
- Achieve break-even trajectory (base case: Year 3)
- Expand volume discount program (10K, 50K, 100K monthly API tiers)

**Data Deliverables:**
- Expand OSINT sources (add international deepfake databases)
- Achieve 1,000+ scammer profiles in Scammers database
- Achieve 50,000+ scan records in Scans database
- Deploy advanced analytics (trend prediction, seasonal analysis)
- Enable API access to Financial Overview database (for government tier)

**Security Deliverables:**
- Complete ISO 27001 certification audit (target: certified by end of Year 2)
- Begin SOC 2 Type II preparation
- Conduct first external penetration test
- Deploy bug bounty program consideration
- Implement advanced threat detection (anomalous query patterns, access behavior)
- Verify 7-year audit trail retention compliance
- Review and update STRIDE threat model based on operational experience

---

## 14. Stakeholder Map

| Stakeholder | Interest | Influence |
|-------------|----------|-----------|
| TECHBENG Team (4 developers) | Build, deploy, and operate the platform | High (developers and operators) |
| DORMATHON 2026 Judges | Evaluate agentic solution quality for Track 2 | High (evaluators and prize deciders) |
| WorkBuddy Platform | Ecosystem growth, platform adoption showcase | High (platform provider) |
| Bank Customers (Enterprise) | Fraud prevention, BNM RMCD compliance, ROI | High (buyers, RM 50K-250K/year) |
| Government Agencies | National scam monitoring, public protection | Medium-High (regulators and buyers) |
| Corporate Enterprise Customers | Executive protection, brand safety, audit trail | Medium-High (buyers, RM 15K-50K/year) |
| SME Customers | Affordable verification, scammer search | Medium (buyers, RM 3K-15K/year) |
| API Customers | Embeddable detection, uptime, pricing | Medium (buyers, RM 0.50-2.00/detection) |
| Sightengine (API supplier) | API revenue from LAICIs usage | Medium (supplier, detection dependency) |
| Google / Gemini (API supplier) | API usage revenue from LAICIs | Medium (supplier, video analysis) |
| Malaysian Public | Protection from deepfake scams | Low influence, High impact (beneficiaries) |
| PDRM CCID / Bukit Aman | National fraud statistics and enforcement | Medium-High (data source and regulator) |
| Bank Negara Malaysia | Financial system stability, RMCD compliance | High (regulator for bank customers) |
| MCMC | Communications regulation, CMA enforcement | High (regulator for content) |
| Cybersecurity Insurance Providers | Risk assessment for premium calculation | Low (future influence on enterprise sales) |

---

## 15. Constraints & Assumptions

### 15.1 Constraints

- **Team Size:** 4 developers with beginner-to-intermediate skills (Python, Java, HTML, CSS, JavaScript)
- **Platform:** Must run natively within WorkBuddy AI — no external server hosting required
- **Budget:** Hackathon project — minimal initial capital; revenue-funded growth model
- **Timeline:** MVP delivered during DORMATHON 2026; v2.0 features designed in this BRD but phased implementation across Q1-Q4 2026
- **API Dependencies:** Sightengine and Gemini API keys required for full functionality; ELA provides minimum viable detection without keys
- **Database Capacity:** WorkBuddy library databases have practical limits — archival strategy needed for Year 2+ scale
- **Regulatory Timeline:** ISO 27001 certification requires 6-12 months of documented operations before audit
- **Security Resources:** No dedicated security team — security responsibilities shared among 4 developers with quarterly external review

### 15.2 Assumptions

- Malaysian scam losses continue to grow at 30%+ annually (deepfake-specific at 76% YoY)
- WorkBuddy AI platform remains stable, available, and feature-compatible with LAICIs's requirements
- Sightengine API maintains current pricing structure and API contract
- Gemini API free tier or low-cost access remains available
- Malaysian government does not ban AI-detection tools (extremely unlikely given stated anti-scam stance)
- Enterprise customers willing to pay RM 50K-250K for deepfake defense (validated by RM 122M single-case loss)
- PDPA 2010 remains the governing data protection law (no superseding legislation in 2026)
- CMA 1998 Section 233 remains the applicable content regulation
- BNM RMCD Guidelines are not significantly revised in a way that would require re-architecture
- The 85% victim belief rate and 2% recovery rate persist, sustaining the prevention-first value proposition
- The RM 5.62 billion 3-year loss figure is approximately accurate (drawn from 25 cited sources)
- WorkBuddy library space DORMATHON26_TECHBENG (CSfJ5htmA2LY98nVeDfVD3) remains accessible for the project lifecycle
- The OSINT automation (ID: 2453f597-10da-4990-9203-06669db4c19d) continues to execute reliably at 9 AM daily
- Published dashboard (https://workbuddy.cc/p/NgyKSRIdG71xKlqxI0JrGa) remains accessible to stakeholders

---

## 16. Approval

This Business Requirements Document defines the strategic, financial, data, and security foundation for LAICIs v2.0. It covers three domains — Finance, Data, and Security — in equal depth and is intended to guide the PRD (product features), SRD (system architecture), and SRS (software specification) documents that follow.

All sections of this document are fully written out. No section defers to prior versions or is abbreviated.

### 16.1 Document Approval

| Role | Name | Responsibility | Signature |
|------|------|---------------|----------|
| Product Owner | TECHBENG Team Lead | Business requirements ownership | _________________ |
| Technical Lead | TECHBENG Senior Developer | Technical feasibility endorsement | _________________ |
| Security Officer | TECHBENG Designated Member | Security and compliance review | _________________ |
| Data Steward | TECHBENG Designated Member | Data strategy and governance review | _________________ |

### 16.2 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | January 2026 | TECHBENG | Initial BRD (finance-focused, 13 sections) |
| 2.0 | January 2026 | TECHBENG | Complete rewrite: 16 sections, 3 domains (Finance, Data, Security) fully written out |

### 16.3 Next Steps

1. **Product Requirements Document (PRD):** Translate business requirements into detailed product feature specifications
2. **System Requirements Document (SRD):** Define system architecture, components, and integrations
3. **Software Design Document (SDD):** Detail software design, data models, and algorithms
4. **Software Requirements Specification (SRS):** Define functional and non-functional software requirements
5. **Implementation:** Begin Phase 1 (MVP Launch) deliverables as defined in Section 13

---

*End of Business Requirements Document — LAICIs v2.0*
*Prepared by TECHBENG for DORMATHON 2026, Track 2: WorkBuddy Agentic Solutions*
*All sections complete. No section references prior versions or is abbreviated.*
