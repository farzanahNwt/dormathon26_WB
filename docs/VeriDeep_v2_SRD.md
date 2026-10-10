# System Requirements Document (SRD)
# LAICIs v2.0 — Agentic Deepfake Detection & Financial Scam Prevention Platform

## Document Control

- **Project:** LAICIs v2.0
- **Track:** DORMATHON 2026 — Track 2: WorkBuddy Agentic Solutions
- **Team:** TECHBENG (4 developers)
- **Document Version:** 2.0
- **Date:** January 2026
- **Status:** Final Draft
- **Predecessors:** BRD, PRD — LAICIs v2.0
- **Domains Covered:** FINANCE, DATA, SECURITY (equal weight)

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [System Architecture](#2-system-architecture)
3. [FINANCIAL Architecture](#3-financial-architecture)
4. [DATA Architecture](#4-data-architecture)
5. [SECURITY Architecture](#5-security-architecture)
6. [Infrastructure Requirements](#6-infrastructure-requirements)
7. [Integration Architecture](#7-integration-architecture)
8. [Non-Functional Requirements](#8-non-functional-requirements)
9. [System Constraints](#9-system-constraints)
10. [System Evolution Plan](#10-system-evolution-plan)

---

## 1. System Overview

### 1.1 System Description

LAICIs v2.0 is a multi-tier deepfake detection and financial scam prevention platform built natively within the WorkBuddy AI ecosystem. The system comprises five detection modules, three financial intelligence modules, a 7-step agentic workflow orchestrator, an interactive dashboard, three library databases, two knowledge base nodes, an automated OSINT pipeline, a data user self-service portal, a RAG-powered Q&A engine, a compliance reporting engine, and a comprehensive security architecture covering authentication, authorization, input validation, output sanitization, encryption, audit trail, threat modeling, and regulatory compliance.

The platform operates across three equally weighted architectural domains:

- **FINANCE Domain:** Financial risk assessment, exposure calculation, loss prevention tracking, scenario planning, recovery assistance, and three dedicated financial databases with 47 total fields across them.
- **DATA Domain:** End-to-end data flow from user upload through 7-step workflow to databases, dashboard, data portal, and exports. Covers storage strategy, retention policy, RAG architecture, OSINT pipeline, data governance, and database-dashboard synchronization.
- **SECURITY Domain:** Authentication (OAuth 2.0, API keys), authorization (RBAC, 4 roles), input validation (extension whitelist, magic bytes, path sanitization), output sanitization (HTML escaping, API filtering, error truncation), API key management (environment variables only, rotation policy), encryption (TLS 1.2+, at-rest), audit trail (7 fields, append-only, immutable), STRIDE threat model, OWASP Top 10 compliance, incident response (4 severity levels), regulatory compliance (PDPA 2010, CMA 1998, BNM RMCD), and vulnerability management.

### 1.2 System Boundaries

**Included in the system:**

- Detection engine (5 modules): SightengineAnalyzer, ELAAnalyzer, MLInferenceRunner, GeminiVideoAnalyzer, WeightedScorer
- Financial intelligence engine (3 modules): FinancialRiskAssessor, ScenarioPlanner, RecoveryAssistant
- Agentic workflow orchestrator (7 steps: UNDERSTAND, PLAN, EXECUTE, VALIDATE, INTEGRATE, DELIVER, FINANCIAL_RISK_ASSESS)
- Interactive dashboard (single-page HTML, dark theme, 10 sections)
- Library databases (3): Scans (22 fields), Scammers (16 fields), Financial Overview (9 fields)
- Knowledge base nodes (2): Data node, Finance node
- OSINT automation pipeline (daily 9 AM, recurring)
- Data user portal (query, filter, paginate, export)
- RAG Q&A engine (rag_search.py, embedding + rerank)
- Compliance reporting engine (BNM, PDRM, Board Governance, Audit Trail)
- Audit trail logging (7 fields, append-only, immutable)
- Security architecture (auth, RBAC, input validation, output sanitization, key management, encryption, STRIDE, OWASP, incident response, compliance, vulnerability management)

**External to the system (consumed as services):**

- Sightengine API (cloud-based AI detection, image + video)
- Google Gemini API (video transcription and LLM analysis, gemini-2.0-flash)
- WorkBuddy Library Platform (storage, RAG, automation, publishing)
- WorkBuddy Cloud Service (optional keyless LLM)

### 1.3 System Context Diagram

```
[User/Analyst] --> [Auth Gateway] --> [RBAC Engine]
                                              |
                                   [LAICIs Dashboard (HTML)]
                                              |
                                   [7-Step Workflow Orchestrator]
                                              |
                    +-------------------------+-------------------------+
                    |                         |                         |
              [Detection Layer]         [Financial Layer]          [Security Layer]
                    |                         |                         |
         +----------+----------+    +----------+----------+    +--------+--------+
         |          |          |    |          |          |    |        |        |
    [Sightengine] [ELA]   [ML Inf] [Risk Assessor] [Scenario] [Audit] [RBAC] [Validator]
    (Cloud API)  (Local)  (PyTorch) [Recovery Asst]  [Planner]  [Trail] [Engine] [+Sanitize]
         |          |          |    |                         |
         +----+-----+----+-----+    +----------+--------------+
              |                        |
        [Weighted Scorer]          [Scammers DB]
              |                   Cross-Reference
              |                        |
     +--------+--------+         +-----+-----+
     |                 |         |           |
[Delivery & Storage]  |   [Financial Overview] [Loss Prevention Tracker]
     |                 |
[Scans DB] [Scammers DB] [Financial Overview DB] [Audit Trail]
     |
+----+----+----+----+
|    |    |    |
[Data  [RAG  [Compliance  [CSV/JSON
Portal] Q&A]  Reports]     Export]
```

---

## 2. System Architecture

### 2.1 Layered Architecture Diagram

LAICIs v2.0 follows a **layered modular monolith** pattern within the WorkBuddy ecosystem. Each layer has well-defined responsibilities and communicates only with adjacent layers.

```
+-----------------------------------------------------------+
|                  PRESENTATION LAYER                        |
|  Dashboard (HTML/CSS/JS) - 10 sections, tabbed navigation |
|  Dark theme: #0a0e1a bg, #00d4ff accent, #ff4757 danger   |
+-----------------------------------------------------------+
|                  SECURITY LAYER                            |
|  Auth Gateway | RBAC Engine | Input Validator | Sanitizer |
|  Rate Limiter | Audit Logger | Session Manager              |
|  Key Manager (env vars) | Encryption (TLS 1.2+)            |
+-----------------------------------------------------------+
|               ORCHESTRATION LAYER                          |
|  VeriGuardWorkflow - 7-step agentic pipeline               |
|  UNDERSTAND > PLAN > EXECUTE > VALIDATE > INTEGRATE >      |
|  DELIVER > FINANCIAL_RISK_ASSESS                           |
+-----------------------------------------------------------+
|               DETECTION LAYER                              |
|  SightengineAnalyzer | ELAAnalyzer | MLInferenceRunner     |
|  GeminiVideoAnalyzer | WeightedScorer                       |
+-----------------------------------------------------------+
|          FINANCIAL INTELLIGENCE LAYER                      |
|  FinancialRiskAssessor | ScenarioPlanner | RecoveryAssistant|
+-----------------------------------------------------------+
|               DATA LAYER                                   |
|  Scans DB (22 fields) | Scammers DB (16 fields)            |
|  Financial Overview DB (9 fields) | Audit Trail (7 fields)  |
+-----------------------------------------------------------+
|            INTELLIGENCE LAYER                               |
|  RAG Q&A Engine | Knowledge Base (Data + Finance nodes)   |
|  OSINT Automation Pipeline                                  |
+-----------------------------------------------------------+
|            INTEGRATION LAYER                               |
|  Sightengine API | Gemini API | WorkBuddy Library SDK      |
|  WorkBuddy Sites | WorkBuddy Cloud Service                 |
+-----------------------------------------------------------+
```

### 2.2 Component Diagram

```
                        [User]
                          |
                    [Auth Gateway] <-- WorkBuddy Platform Auth (OAuth 2.0)
                          |
                    [RBAC Engine] -- Role: Admin / Analyst / Viewer / API User
                          |
                    [Input Validator] -- File type, size, path, magic bytes
                          |
                    [Rate Limiter] -- 10 scans / 5 min (Sightengine)
                          |
                    [Output Sanitizer] -- HTML escape, API filter, error truncate
                          |
                 [Dashboard (HTML)]
                          |
              [VeriGuardWorkflow Orchestrator]
                    /     |     \
    +---------------+     |      +---------------+
    |               |     |      |               |
[Step 1-6]    [Step 7: FIN]    [Audit Logger]
(Detection)   (Financial)      (Immutable log)
    |               |
    v               v
[Detection     [FinancialRiskAssessor]
 Modules]           |
    |          [Scammers DB
    |           Cross-Ref]
    v               |
[WeightedScorer]    v
    |          [RecoveryAssistant]
    v
[Delivery] --> [Scans DB] --> [Financial Overview DB]
                    |
              [Audit Trail] --> [Compliance Reports]
```

### 2.3 Deployment Diagram

```
[WorkBuddy Cloud Platform]
    |
    +-- [Published Dashboard] (workbuddy.cc/p/...)
    |       |
    |       +-- HTML/CSS/JS (static, served by WorkBuddy Sites)
    |       +-- Page<->Database bindings (runtime data signals)
    |       +-- __SMART_PAGE__.database runtime signals
    |
    +-- [Library Space: DORMATHON26_TECHBENG]
    |       |   (spaceId: CSfJ5htmA2LY98nVeDfVD3)
    |       |
    |       +-- Scans Database (nodeId: fCCH5jUKxdxaQbWoVbiRVx)
    |       +-- Scammers Database (nodeId: w7KwBxeUOZpa2WFiUJRqaB)
    |       +-- Financial Overview Database (NEW)
    |       +-- Data Knowledge Base Node (doc)
    |       +-- Finance Knowledge Base Node (doc)
    |       +-- Audit Trail (database or doc)
    |
    +-- [Automations]
    |       |
    |       +-- OSINT Pipeline (daily 9 AM)
    |           (ID: 2453f597-10da-4990-9203-06669db4c19d)
    |
    +-- [Python Runtime] (managed, isolated)
    |       |
    |       +-- Detection modules (src/detection/)
    |       +-- Financial modules (src/financial/)
    |       +-- Workflow orchestrator (src/workflow/)
    |       +-- RAG search (search/rag_search.py)
    |       +-- Security utilities (src/security/)
    |
    +-- [External APIs] (called from Python runtime)
            |
            +-- Sightengine API (HTTPS REST)
            +-- Google Gemini API (HTTPS REST)
```

### 2.4 Architectural Pattern

LAICIs v2.0 follows a **modular monolith** pattern:

- **Presentation Layer:** Single-page HTML dashboard with tabbed navigation, 10 sections, dark theme
- **Security Layer:** Authentication gateway, RBAC engine, input validator, output sanitizer, rate limiter, audit logger, session manager, key manager, encryption
- **Orchestration Layer:** Python-based agentic workflow that chains detection modules and financial modules in a 7-step pipeline
- **Detection Layer:** 5 independent detection modules, each with a well-defined interface (analyze method returning structured dict)
- **Financial Intelligence Layer:** 3 financial modules for risk assessment, scenario planning, and recovery assistance
- **Data Layer:** WorkBuddy Library databases (native tables, not external databases) — Scans (22 fields), Scammers (16 fields), Financial Overview (9 fields), Audit Trail (7 fields)
- **Intelligence Layer:** RAG search engine, knowledge base nodes (Data + Finance), OSINT automation pipeline
- **Integration Layer:** REST API calls to Sightengine and Gemini, WorkBuddy Library SDK for all database and knowledge base operations

---

## 3. FINANCIAL Architecture

### 3.1 Financial Modules Overview

LAICIs v2.0 introduces three new financial intelligence modules that layer financial risk assessment, scenario simulation, and recovery guidance on top of the existing 5-module detection engine. These modules execute as Step 7 of the agentic workflow and are also independently accessible from the dashboard for scenario planning and recovery assistance.

### 3.2 Financial Module 1: FinancialRiskAssessor

**File:** `src/financial/risk_assessor.py` (to be built)

**Type:** Pure Python computation + Library database lookups

**Inputs:**
- `final_score` (float 0.0-1.0) — from Step 5 (Integrate/WeightedScorer)
- `media_type` (string: image/video)
- `is_deepfake` (boolean)
- `user_context` (string — e.g., "marketplace seller photo", "executive video call")
- `scammer_match` (dict or None — from Scammers DB cross-reference)
- `segment` (string: bank/corporate/government/sme/individual)

**Outputs:**
- `risk_tier` (string: LOW / MODERATE / HIGH / CRITICAL)
- `estimated_exposure_rm` (float — RM amount)
- `scam_category` (string: job/investment/romance/phishing/impersonation/marketplace/other)
- `segment_specific_range` (dict — e.g., {"bank": "RM 50K-500K", "individual": "RM 500-5K"})
- `prevention_value_rm` (float — estimated value of detecting this scam)
- `recovery_recommendation` (string — immediate action steps)

**Risk Tier Mapping:**

| Risk Tier | Score Range | Exposure Range (RM) | Color |
|-----------|-------------|---------------------|-------|
| LOW | 0.0 - 0.3 | 0 - 500 | Green |
| MODERATE | 0.3 - 0.5 | 500 - 5,000 | Yellow |
| HIGH | 0.5 - 0.8 | 5,000 - 50,000 | Orange |
| CRITICAL | 0.8 - 1.0 | 50,000 - 500,000 | Red |

**Segment Multipliers:**

| Segment | Multiplier | Rationale |
|---------|------------|-----------|
| Bank | 10x | High-value transactions, KYC fraud potential |
| Corporate | 5x | Executive impersonation, brand damage |
| Government | 8x | National security, public trust |
| SME | 1x | Moderate transaction values |
| Individual | 0.1x | Lower per-case exposure |

**Exposure Calculation Formula:**

```
estimated_exposure_rm = base_exposure_midpoint(risk_tier)
                      × segment_multiplier(segment)
                      × scammer_history_factor(scammer_match)
```

Where:
- `base_exposure_midpoint` = (min + max) / 2 of the risk tier's exposure range
- `segment_multiplier` = from the segment multipliers table above
- `scammer_history_factor` = 1.5 if scammer match found with known losses, 1.0 otherwise

**Average Loss by Scam Category:**

| Scam Category | Average Loss (RM) | Prevention Value (25% of avg) |
|---------------|-------------------|-------------------------------|
| Job scam | 5,000 | 1,250 |
| Investment scam | 50,000 | 12,500 |
| Romance scam | 15,000 | 3,750 |
| Phishing | 2,000 | 500 |
| Impersonation | 100,000 | 25,000 |
| Marketplace fraud | 800 | 200 |
| Other | 3,000 | 750 |

**Scam Categorization Logic:**
- Uses context-based NLP matching against known scam patterns
- Substring matching (not regex — prevents ReDoS)
- If context contains "job" or "employment" → job scam
- If context contains "investment" or "return" → investment scam
- If context contains "love" or "dating" or "romance" → romance scam
- If context contains "phishing" or "email" or "link" → phishing
- If context contains "executive" or "CEO" or "director" → impersonation
- If context contains "marketplace" or "seller" or "buyer" → marketplace fraud
- Default → other

**Prevention Value Calculation:**

```
prevention_value_rm = average_loss[scam_category] × 0.25
```

The prevention value represents 25% of the average loss for the matched scam category. This conservative estimate reflects that LAICIs prevents a portion of potential losses through early detection, not the full amount (since some victims may still be targeted through other channels).

### 3.3 Financial Module 2: ScenarioPlanner

**File:** `src/financial/scenario_planner.py` (to be built)

**Type:** Pure Python computation + Library RAG search

**Inputs:**
- `scenario_type` (enum: executive_impersonation, fake_news_video, marketplace_deepfake, political_disinformation)
- `target` (string — e.g., "CEO name", "brand name")
- `distribution_channel` (string: social_media, email, direct_message, broadcast)
- `audience_reach` (integer: 1,000 - 1,000,000)

**Outputs:**
- `projected_exposure_rm` (float — projected financial impact)
- `response_playbook` (list of action items with timelines)
- `notification_template` (string — pre-filled email/announcement template)
- `historical_precedents` (list of similar past incidents with outcomes)

**Exposure Projection Model:**

```
projected_exposure_rm = historical_anchor_loss(scenario_type)
                      × reach_factor(audience_reach)
                      × segment_multiplier(segment)
```

Where:
- `historical_anchor_loss`: RM 122 million for executive impersonation (reference case), scaled down for other scenario types
- `reach_factor`: log10(audience_reach / 1000) — logarithmic scaling (1000 reach = 1x, 10000 = 2x, 100000 = 3x, 1000000 = 4x)
- `segment_multiplier`: from the segment multipliers table

**Response Playbook Structure:**
- Immediate Actions (Hours 0-4): Identify, contain, communicate internally
- Short-term Actions (Hours 4-48): Public statement, legal notification, platform takedown request
- Long-term Actions (Days 1-30): Recovery, review, preventive measures, stakeholder update

**Historical Precedent Retrieval:**
- Uses RAG search over the Data knowledge base node
- Queries for similar past incidents by scenario type
- Returns: case description, financial impact, resolution outcome, lessons learned

### 3.4 Financial Module 3: RecoveryAssistant

**File:** `src/financial/recovery_assistant.py` (to be built)

**Type:** Template-based generation + database lookup

**Inputs:**
- `scam_type` (string — from FinancialRiskAssessor output)
- `estimated_exposure` (float — RM amount)
- `victim_type` (string: individual, corporate, government)
- `time_since_incident_hours` (float — hours since incident occurred)

**Outputs:**
- `immediate_actions` (list of strings — freeze accounts, report to BNM, contact PDRM CCID)
- `regulatory_filings` (list — PDPA notification, CMA Section 233 report)
- `evidence_checklist` (list — preserve media, screenshots, communication logs, transaction records)
- `contact_directory` (dict — Malaysian regulatory contacts)
- `legal_recourse` (list — options for legal action)
- `insurance_guidance` (string — claim process if applicable)

**Contact Directory (Hardcoded from Verified Sources):**

| Organization | Contact | Purpose |
|-------------|---------|---------|
| BNM FEN | 1-300-88-5465 | Financial fraud reporting |
| PDRM CCID | 03-26101599 | Commercial crime reporting |
| MCMC | 1-800-188-299 | Content/online fraud |
| CyberSecurity Malaysia | 1-300-88-2999 | Cyber incident response |

**Recovery Plan Logic:**
- If time_since_incident < 24 hours: emphasize immediate account freezing and BNM reporting
- If time_since_incident 24-72 hours: add evidence preservation and PDRM filing
- If time_since_incident > 72 hours: focus on legal recourse and insurance claims
- If exposure > RM 50,000: escalate to CRITICAL tier, add board notification and legal counsel
- All contact information hardcoded from verified government sources — not user-editable
- All recovery steps are template-based (no dynamic code execution)

### 3.5 Financial Data Flow

The financial data flow adds Step 7 (FINANCIAL_RISK_ASSESS) after Steps 1-6 complete the detection pipeline:

```
Steps 1-6 Complete (Detection)
    |
    v
Step 7: FINANCIAL_RISK_ASSESS
    |
    +-- 7a: Extract final_score, is_deepfake, user_context from Step 6 delivery
    |
    +-- 7b: Cross-reference Scammers DB
    |       (search by email, phone, website from user_context)
    |       (read-only via Library SDK)
    |
    +-- 7c: Run FinancialRiskAssessor.assess_risk()
    |       (map score to risk tier)
    |       (calculate estimated exposure)
    |       (categorize scam type)
    |       (calculate prevention value)
    |       (generate recovery recommendation)
    |
    +-- 7d: Merge financial fields into delivery dict
    |       (risk_tier, estimated_exposure_rm, scam_category,
    |        prevention_value_rm, scammer_match_id, segment,
    |        recovery_action_taken)
    |
    +-- 7e: Update Loss Prevention Tracker
    |       (if is_ai_generated == true,
    |        add prevention_value_rm to cumulative counter)
    |
    +-- 7f: Write to Scans DB (all 22 fields including 7 financial)
    |
    +-- 7g: Update Financial Overview DB (daily aggregate)
    |
    +-- 7h: Log to Audit Trail
            (action="scan_financial_assessment",
             target=scan_id, result="success")
    |
    v
Display: Dashboard result card with financial fields
         Scan history with risk tier, exposure columns
         Loss prevention tracker in header
```

### 3.6 Risk Tier Mapping (Full Specification)

| Tier | Score Min | Score Max | Exposure Min (RM) | Exposure Max (RM) | Color | Action Required |
|------|-----------|-----------|---------------------|---------------------|-------|-----------------|
| LOW | 0.0 | 0.3 | 0 | 500 | Green | Log, monitor |
| MODERATE | 0.3 | 0.5 | 500 | 5,000 | Yellow | Notify analyst, review |
| HIGH | 0.5 | 0.8 | 5,000 | 50,000 | Orange | Escalate, investigate |
| CRITICAL | 0.8 | 1.0 | 50,000 | 500,000 | Red | Immediate action, escalate to admin |

**Tier Escalation Rules:**
- If scammer match found with known losses > RM 10,000: escalate one tier
- If context indicates "corporate" or "executive": escalate one tier
- If context indicates "bank" or "government": escalate one tier
- Maximum escalation: CRITICAL (no escalation above CRITICAL)

### 3.7 Loss Prevention Tracker

**Purpose:** A cumulative counter of estimated prevented losses (in RM) across all scans performed on the platform. Serves as both a stakeholder reporting tool and a marketing asset.

**Location:** Dashboard header, displayed as a large RM counter.

**Display:**
- Large RM counter: "RM X,XXX,XXX prevented"
- Subtitle: "across X scans since [date]"
- Color-coded: green for < RM 100K, blue for RM 100K-1M, purple for > RM 1M
- Click to expand: breakdown by scam category, by customer segment, by month

**Calculation:**
- For each scan where `is_ai_generated == true`: add `prevention_value_rm` from the Financial Risk Assessor to the cumulative total
- If a scammer match was found and the scammer has known loss history: add the historical average loss per case
- The counter never resets — it is cumulative since platform inception
- Updated in Step 7e of the workflow

**Data Source:** `total_prevented_loss_rm` field in the Financial Overview database.

### 3.8 Financial Databases

#### 3.8.1 Scans Database — Financial Fields (7 NEW in v2.0)

The Scans database extends from 15 fields (v1.0) to 22 fields (v2.0). The 7 new financial fields capture the output of the FinancialRiskAssessor:

| # | Field | Type | Description |
|---|-------|------|-------------|
| 16 | risk_tier | string | LOW / MODERATE / HIGH / CRITICAL |
| 17 | estimated_exposure_rm | float | Estimated monetary exposure in RM |
| 18 | scam_category | string | job/investment/romance/phishing/impersonation/marketplace/other |
| 19 | prevention_value_rm | float | Estimated value of detecting this scam |
| 20 | scammer_match_id | string | Linked record ID from Scammers DB |
| 21 | segment | string | bank/corporate/government/sme/individual |
| 22 | recovery_action_taken | string | Summary of recovery actions taken |

**Full Scans DB field list (22 fields):**
1. scan_id (string, primary key)
2. scan_date (datetime)
3. media_type (string: image/video)
4. media_filename (string — filename only, not full path)
5. has_faces (boolean)
6. final_score (float 0.0-1.0)
7. is_ai_generated (boolean)
8. is_deepfake (boolean)
9. method_used (string)
10. component_scores (JSON)
11. ela_analysis (JSON)
12. indicators (JSON — sanitized strings)
13. recommendation (string — sanitized)
14. context (string — sanitized, max 500 chars)
15. user_id (string — WorkBuddy UID)
16. risk_tier (string)
17. estimated_exposure_rm (float)
18. scam_category (string)
19. prevention_value_rm (float)
20. scammer_match_id (string)
21. segment (string)
22. recovery_action_taken (string)

#### 3.8.2 Scammers Database — Financial Fields (5 NEW in v2.0)

The Scammers database extends from 11 fields (v1.0) to 16 fields (v2.0). The 5 new financial fields capture historical loss data for identified scammers:

| # | Field | Type | Description |
|---|-------|------|-------------|
| 12 | total_known_losses_rm | float | Cumulative losses attributed to this scammer |
| 13 | average_loss_per_case_rm | float | Average loss per incident |
| 14 | case_count | integer | Number of confirmed cases |
| 15 | first_seen_date | date | Earliest recorded activity |
| 16 | risk_level | string | LOW / MEDIUM / HIGH / CRITICAL |

**Full Scammers DB field list (16 fields):**
1. scammer_id (string, primary key)
2. email (string)
3. phone (string)
4. website (string)
5. social_media (string)
6. scam_type (string)
7. first_reported (datetime)
8. last_seen (datetime)
9. reports_count (integer)
10. source (string — data provenance)
11. notes (string)
12. total_known_losses_rm (float)
13. average_loss_per_case_rm (float)
14. case_count (integer)
15. first_seen_date (date)
16. risk_level (string)

#### 3.8.3 Financial Overview Database (NEW — 9 fields)

A new library database that aggregates financial intelligence across all scans and scammers for dashboard display and reporting. No individual user data — only aggregate counts and sums.

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | date | date | Aggregation date (daily or monthly) |
| 2 | total_scans | integer | Total scans on this date |
| 3 | total_deepfakes_detected | integer | Deepfakes found on this date |
| 4 | total_prevented_loss_rm | float | Cumulative prevention value |
| 5 | total_estimated_exposure_rm | float | Cumulative exposure detected |
| 6 | scam_breakdown | JSON | {scam_type: count} breakdown |
| 7 | segment_breakdown | JSON | {segment: count} breakdown |
| 8 | new_scammers_identified | integer | New scammer profiles added |
| 9 | osint_updates | integer | OSINT data points added |

### 3.9 Financial Knowledge Base Node

**Node:** Finance (existing but to be populated)

**Content:**
- Pricing tiers (Enterprise, Professional, Starter, API, Government)
- ROI calculations (4.2x conservative, 41.7x optimistic for banks)
- Cost structures (personnel, infrastructure, API costs, marketing, legal)
- Revenue scenarios (conservative, base, optimistic — 3-year projections)
- Break-even analysis (Year 3 base case, Year 2 optimistic)
- Customer segment financials (5 segments with budgets and success criteria)
- Average loss by scam category (7 categories)
- Segment multipliers (5 segments)
- Risk tier thresholds (4 tiers with exposure ranges)

**Sources:** LAICIs Financial Feasibility Proposal, LAICIs Research Report

**Queryable via:** RAG search (rag_search.py)

---

## 4. DATA Architecture

### 4.1 Data Flow Diagram

The end-to-end data flow covers the complete journey from user upload through the 7-step workflow to databases, dashboard, data portal, and exports:

```
[User Uploads Media]
    |
    v
[Input Validation]
    |--- Extension whitelist check
    |--- File size check (50MB max)
    |--- Path sanitization (reject ..)
    |--- Magic bytes verification
    |
    v
[7-Step Workflow]
    |
    +-- Step 1: UNDERSTAND
    |       (parse file, detect media type, auto-detect faces)
    |
    +-- Step 2: PLAN
    |       (select detection models based on media type and face presence)
    |
    +-- Step 3: EXECUTE
    |       (run selected detection modules in parallel)
    |       |--- Sightengine API (cloud, image + video)
    |       |--- ELA Analysis (local, Pillow + numpy)
    |       |--- ML Inference (local, PyTorch EfficientNetV2-S)
    |       |--- Gemini Video API (cloud, video only)
    |
    +-- Step 4: VALIDATE
    |       (cross-check results, detect conflicts, verify method coverage)
    |
    +-- Step 5: INTEGRATE
    |       (apply weighted scoring, produce final score 0.0-1.0)
    |
    +-- Step 6: DELIVER
    |       (package results, generate scan_id, prepare for storage)
    |
    +-- Step 7: FINANCIAL_RISK_ASSESS
    |       (map score to risk tier, calculate exposure,
    |        cross-reference Scammers DB, calculate prevention value,
    |        update Loss Prevention Tracker, log to audit trail)
    |
    v
[Database Storage]
    |--- Scans DB (22 fields, all scan + financial data)
    |--- Scammers DB (16 fields, if new scammer identified)
    |--- Financial Overview DB (9 fields, daily aggregate)
    |--- Audit Trail (7 fields, action log)
    |
    v
[Dashboard Display]
    |--- Result card (detection score + financial fields)
    |--- Scan history table (with risk tier, exposure columns)
    |--- Loss prevention tracker (header counter)
    |--- Market intelligence panel (national statistics)
    |--- Scammer search results (with loss data)
    |
    v
[Data Portal]
    |--- Filter (by date, type, score, risk tier, scam category)
    |--- Query (Scans DB, Scammers DB)
    |--- Paginate (50 records per page)
    |--- Export (CSV, JSON)
    |
    v
[Exports]
    |--- CSV download (filtered scan/scammer data)
    |--- JSON API response (for API tier)
    |--- Compliance reports (BNM, PDRM, Board)
```

### 4.2 Data Storage Strategy

LAICIs v2.0 employs a data minimization strategy — only necessary data is stored, and media files are never persisted.

| Data Type | Storage Location | Persistence | Rationale |
|-----------|-----------------|-------------|-----------|
| Uploaded media files | NOT stored | Processed and discarded | PDPA compliance, privacy protection |
| Scan metadata | Scans DB (22 fields) | Indefinite | Historical analysis, trend detection |
| Scammer profiles | Scammers DB (16 fields) | Indefinite | Cross-referencing future scans |
| Financial aggregates | Financial Overview DB (9 fields) | Indefinite | Longitudinal trend analysis |
| Knowledge base content | Data + Finance doc nodes | Indefinite | Accumulating intelligence |
| Audit trail | Audit Trail (7 fields) | 7 years | Regulatory compliance (PDPA, BNM) |
| OSINT raw data | Data knowledge base node | 90 days raw, aggregated indefinitely | Storage efficiency |
| API keys | Environment variables | Never in database | Security — no secrets in storage |
| Raw API responses | NOT persisted | Discarded after parsing | Data minimization |

**Media File Handling:**
1. File loaded into memory or temp directory for processing
2. After detection modules complete, temp file deleted in `finally` block
3. Only metadata (filename, type, size) stored in Scans DB — not the file itself
4. Temp directory created with `tempfile.mkdtemp(prefix="veriguard_")`
5. Temp directory removed with `shutil.rmtree(ignore_errors=True)`

### 4.3 Data Retention Policy

| Data Type | Retention Period | Rationale |
|-----------|-----------------|-----------|
| Scan metadata (Scans DB) | Indefinite | Historical analysis, trend detection, longitudinal reporting |
| Scammer profiles (Scammers DB) | Indefinite | Cross-referencing future scans, building threat intelligence |
| Financial Overview | Indefinite | Long-term trend analysis, board reporting, regulatory inspection |
| Knowledge base content | Indefinite | Accumulating intelligence, RAG search corpus |
| Audit trail | 7 years | Regulatory compliance (PDPA 2010, BNM RMCD guidelines) |
| Media files (uploaded) | NOT stored | Privacy protection (PDPA), data minimization |
| OSINT raw data | 90 days raw, aggregated indefinitely | Storage efficiency; aggregated data retained |
| API responses (raw) | NOT persisted | Data minimization; only parsed fields stored |
| Temp files | Deleted in finally block | Prevent data leakage; cleanup after processing |

### 4.4 RAG Architecture

**Technology:** WorkBuddy Library built-in RAG search

**Script:** `search/rag_search.py`

**Index Scope:** All content in Data and Finance knowledge base nodes

**Retrieval Process:**

```
[User Query (natural language)]
    |
    v
[Embedding Generation]
    |--- Query text embedded into vector representation
    |--- Uses WorkBuddy Library embedding model
    |
    v
[Chunk-Level Retrieval]
    |--- Knowledge base content pre-chunked into segments
    |--- Vector similarity search over all chunks
    |--- Top-K chunks retrieved (default K=5)
    |
    v
[Rerank]
    |--- Retrieved chunks reranked by relevance score
    |--- Reranking model applied for precision
    |--- Top-N chunks selected for answer generation
    |
    v
[Answer Generation]
    |--- LLM generates answer from selected chunks
    |--- Answer includes source citation
    |--- Source: document name, section
    |
    v
[Response]
    +-- Answer text (paragraph)
    +-- Source citation (document name, section)
```

**Capabilities:**
- Chunk-level semantic retrieval (not just document-level)
- Embedding + rerank pipeline for high precision
- Source citations on every answer (document name, section)
- Supports natural language queries in English (Bahasa Malaysia planned for Phase 4)
- Queries both Data and Finance nodes simultaneously

**Example Interactions:**
- Query: "How much did Malaysians lose to scams in 2023-2025?"
- Answer: "Malaysians lost RM 5.62 billion to scams from 2023 to 2025. Source: LAICIs Research Report, Executive Summary."

- Query: "What's the ROI for a bank using LAICIs?"
- Answer: "Banks can expect a 4.2x ROI (conservative) to 41.7x ROI (optimistic). The 41.7x figure is grounded in the RM 122 million single-case loss. Source: LAICIs Financial Feasibility Proposal, ROI Analysis section."

### 4.5 OSINT Pipeline

**Automation ID:** `2453f597-10da-4990-9203-06669db4c19d`

**Schedule:** Daily at 9:00 AM (recurring WorkBuddy automation)

**Pipeline Steps:**

```
[Daily 9 AM Trigger]
    |
    v
[Step 1: WebSearch]
    |--- Query: latest Malaysian scam news, deepfake incidents
    |--- Uses WorkBuddy WebSearch tool
    |--- Search for loss amounts, case counts, scam types
    |
    v
[Step 2: Extract]
    |--- Extract key data points from search results
    |--- Parse: loss amounts (RM), case counts, scam types, dates
    |--- Filter for Malaysian relevance
    |
    v
[Step 3: Structure as JSON]
    |--- Format extracted data as structured JSON
    |--- Fields: date, source, headline, loss_amount,
    |           case_count, scam_type, segment, url
    |
    v
[Step 4: Append to Data Knowledge Base Node]
    |--- Append JSON to existing Data node content
    |--- Uses WorkBuddy Library doc operations
    |--- Content becomes searchable via RAG
    |
    v
[Step 5: Update Financial Overview Database]
    |--- Update osint_updates field (increment count)
    |--- Update scam_breakdown if new scam types found
    |--- Update segment_breakdown if new segments found
    |
    v
[Step 6: Log to Audit Trail]
    +-- action: "osint_update"
    +-- actor: "system"
    +-- target: "Data node"
    +-- result: "success" or "failure"
    +-- details: JSON with data points collected (max 500 chars)
```

**Automation Constraints:**
- Prompt must be self-contained (no session context — automation runs headless)
- Runs as WorkBuddy recurring automation
- Failure handling: retry on next scheduled run, log failure to audit trail
- Manual trigger available: dashboard button "Run OSINT Scan Now"

### 4.6 Data Portal Architecture

The data user self-service portal enables analysts and data users to query, filter, sort, paginate, and export scan and scammer data without developer assistance.

**Architecture Pipeline:**

```
[User Selects Filters]
    |--- Database: Scans or Scammers
    |--- Filter fields: date range, media type, score range,
    |    risk tier, scam category, has_deepfake
    |--- Sort: by any column, ascending/descending
    |
    v
[Query Construction]
    |--- Filter parameters validated (SQL injection prevention via SDK)
    |--- Query built using WorkBuddy Library SDK
    |--- Parameterized queries (SDK-enforced)
    |
    v
[Query Execution]
    |--- Library SDK executes query against database
    |--- Results returned as JSON array
    |
    v
[Pagination]
    |--- Results paginated (50 records per page)
    |--- Page number and total count displayed
    |--- "Showing X-Y of Z records"
    |
    v
[Display + Export]
    +-- Display: Results table (paginated, sortable)
    +-- Export CSV: Download filtered results as CSV
    +-- Export JSON: Download filtered results as JSON
```

**Filter Capabilities (Scans DB):**
- Date range (from/to)
- Media type (image/video/all)
- Score range (min/max slider 0.0-1.0)
- Risk tier (LOW/MODERATE/HIGH/CRITICAL/all)
- Scam category (dropdown, all 7 categories + all)
- Has deepfake (yes/no/all)
- Segment (bank/corporate/government/sme/individual/all)

**Filter Capabilities (Scammers DB):**
- Email (substring search)
- Phone (substring search)
- Website (substring search)
- Scam type (dropdown)
- First seen date range
- Risk level (LOW/MEDIUM/HIGH/CRITICAL/all)

**Export Formats:**
- CSV: Standard comma-separated values, all filtered fields, UTF-8 encoding
- JSON: Structured JSON array, all filtered fields, pretty-printed

### 4.7 Database-to-Dashboard Synchronization

**Mechanism:** WorkBuddy Library page-to-database relation bindings

**Runtime Signals:** `__SMART_PAGE__.database` runtime signals enable real-time data flow between published dashboard pages and Library databases.

**How It Works:**

```
[Dashboard Page (Published)]
    |
    +-- Page contains __SMART_PAGE__.database relation bindings
    |
    +-- On page load:
    |       __SMART_PAGE__.database.query("scans_db", filters)
    |       Returns: JSON array of scan records
    |       Dashboard renders results in scan history table
    |
    +-- On new scan:
    |       Workflow writes to Scans DB via Library SDK
    |       Dashboard polls or receives update signal
    |       Scan history table refreshes
    |       Loss prevention tracker updates
    |
    +-- On data portal query:
    |       User selects filters in dashboard UI
    |       __SMART_PAGE__.database.query("scans_db", filters)
    |       Results displayed in paginated table
    |       Export button triggers CSV/JSON download
```

**Bound Databases:**
- Scans DB ↔ Dashboard scan history table, result cards
- Scammers DB ↔ Dashboard scammer search results
- Financial Overview DB ↔ Dashboard header stats, market intelligence panel, loss prevention tracker
- Audit Trail ↔ Dashboard compliance/audit tab (Admin only)

### 4.8 Data Governance

**Principles:**

1. **Data Minimization:** Only collect and store data that is necessary for the platform's purpose (deepfake detection and financial risk assessment). No PII stored without explicit consent.

2. **No PII Without Consent:** Scan metadata is anonymized — no names, ID numbers, or addresses stored. The `user_id` field is a WorkBuddy platform UID, not a personal identifier. The `context` field is sanitized and max 500 chars.

3. **Data Subject Deletion Rights:** On request, an Admin can delete scan records associated with a specific user. Deletion is logged to the audit trail (action="data_subject_deletion"). Scammer data is OSINT (publicly available) and not subject to deletion requests.

4. **Purpose Limitation:** Data collected for deepfake detection and financial risk assessment is not used for any other purpose without explicit consent.

5. **Transparency:** Users are informed about what data is collected, how it is used, and how long it is retained (this SRD serves as the documentation).

6. **Accuracy:** Scammer data is sourced from OSINT and may contain inaccuracies. The `source` field tracks data provenance for accountability. Users can report inaccurate data.

7. **Storage Limitation:** Data retention follows the policy in Section 4.3. Media files are not stored. OSINT raw data is retained for 90 days then aggregated.

8. **Integrity:** Database writes go through the WorkBuddy Library SDK only (no direct database access). Audit trail is append-only and immutable. Data integrity is enforced at the platform level.

---

## 5. SECURITY Architecture

### 5.1 Security Design Principles

1. **Defense in Depth:** Multiple security layers — authentication, RBAC, input validation, output sanitization, audit logging, encryption. A breach of one layer does not compromise the system.

2. **Least Privilege:** Each module, user role, and system component has the minimum permissions required to perform its function. No component has access to data or functionality it does not need.

3. **Fail Secure:** If any security check fails, the request is denied (never fails open). Error messages do not reveal which security check failed or internal system details.

4. **No Secrets in Code:** All API keys, credentials, and secrets stored in environment variables only — never in source code, never in databases, never in config files.

5. **Data Minimization:** Store only what is necessary for the platform's purpose. Media files are processed and discarded. No PII stored without explicit consent. Raw API responses are not persisted.

6. **Immutable Audit:** Audit trail is append-only with no deletion or modification capability. WorkBuddy platform enforces immutability at the storage level.

7. **Separation of Duties:** Detection modules cannot write to databases directly; only the workflow orchestrator writes through the Library SDK. No module has both read and write access to audit trail.

8. **Complete Mediation:** Every access to data or functionality passes through the security layer. No shortcut paths exist that bypass authentication or authorization.

### 5.2 Authentication

**Authentication Methods:**

| Method | Used By | Implementation |
|--------|---------|----------------|
| WorkBuddy OAuth 2.0 | Web dashboard users | Inherited from WorkBuddy platform |
| API Key (X-LAICIs-Key header) | API tier users | 256-bit random, SHA-256 hashed |
| WorkBuddy automation service account | OSINT pipeline | System-level, inherited |

**WorkBuddy Platform Authentication (OAuth 2.0):**
- All dashboard access requires WorkBuddy platform authentication (OAuth 2.0 session)
- Session token generated and validated by WorkBuddy platform
- No custom authentication code — inherited from platform
- Session timeout: 30 minutes of inactivity
- Session ID: WorkBuddy platform-generated (not custom)
- Concurrent sessions: Maximum 3 per user
- Session invalidation on password change

**API Key Authentication:**
- API keys are 256-bit random tokens generated by Admin
- Keys stored as SHA-256 hashes in database (never plaintext)
- Key validation: hash incoming key with SHA-256, compare to stored hash
- API key passed in header: `X-LAICIs-Key: <key>`
- Invalid key: return 401 Unauthorized, log to audit trail (action="auth_failure")
- Key rotation: every 30 days for API user keys, every 90 days for Sightengine/Gemini keys

**Account Lockout Policy:**
- After 5 failed authentication attempts within 15 minutes, account is locked for 30 minutes
- Implemented at WorkBuddy platform level (inherited)
- Lockout events logged to audit trail
- Admin can manually unlock accounts

**Authentication Flow:**

```
[User Request]
      |
[WorkBuddy Platform Authentication] -- OAuth 2.0 / session token
      |
[Session Validation] -- Check session validity, timeout (30 min)
      |
[Auth Gateway]
      |
      +-- If valid: proceed to RBAC
      +-- If invalid: return 401, log to audit trail
```

### 5.3 Authorization (RBAC)

**Role Definitions:**

| Role | Permissions | Database Access | Module Access |
|------|-------------|-----------------|--------------|
| Admin | All operations | All DBs (full), audit trail (full) | All modules, settings, key management |
| Analyst | Scan, query, export, report | Scans (read/write), Scammers (read/write), Financial Overview (read) | ScenarioPlanner, RecoveryAssistant, compliance reports |
| Viewer | Read-only dashboard | Scans (read), Scammers (read), Financial Overview (read) | Market intelligence only |
| API User | API endpoints only | Scans (read own only), stats endpoint | REST API scan endpoint only |

**Data Access Control Matrix:**

| Resource | Admin | Analyst | Viewer | API User |
|----------|-------|---------|--------|----------|
| Scans DB (read) | Yes | Yes | Yes | Own scans only |
| Scans DB (write) | Yes | Yes | No | No (via API only) |
| Scammers DB (read) | Yes | Yes | Yes | No |
| Scammers DB (write) | Yes | Yes | No | No |
| Financial Overview (read) | Yes | Yes | Yes | Stats only |
| Financial Overview (write) | Yes | No | No | No |
| Audit Trail (read) | Yes | Own actions only | No | No |
| Audit Trail (write) | System only | System only | System only | System only |
| Compliance Reports | Yes | Yes | No | No |
| Data Export | Yes | Yes | No | No |
| RAG Q&A | Yes | Yes | Yes | No |
| Scenario Planner | Yes | Yes | No | No |
| Recovery Assistant | Yes | Yes | No | No |
| Settings/Key Mgmt | Yes | No | No | No |

**Module-Level Authorization:**
- SightengineAnalyzer: Called by workflow orchestrator only (no direct user access)
- ELAAnalyzer: Called by workflow orchestrator only
- MLInferenceRunner: Called by workflow orchestrator only
- GeminiVideoAnalyzer: Called by workflow orchestrator only
- WeightedScorer: Called by workflow orchestrator only
- FinancialRiskAssessor: Called by workflow orchestrator only
- ScenarioPlanner: Called by Analyst/Admin via dashboard
- RecoveryAssistant: Called by Analyst/Admin via dashboard
- Compliance Reports: Analyst/Admin only
- Audit Trail: Admin only (full), Analyst (own actions only)
- Data Export: Analyst/Admin only

**Authorization Flow:**

```
[Request] -> [Auth Gateway] -> [RBAC Engine]
                                 |
                                 +-- Extract user role from WorkBuddy session
                                 +-- Check role against requested action permission matrix
                                 +-- If authorized: proceed
                                 +-- If unauthorized: return 403, log to audit trail
                                     (action="rbac_denied", actor=user_id,
                                      target=requested_action)
```

### 5.4 Input Validation

**File Upload Validation:**

| Validation Step | Rule | Failure Action |
|----------------|------|----------------|
| File existence | File must exist at path | Return error, log to audit |
| Extension whitelist | .jpg, .jpeg, .png, .webp, .bmp, .tiff, .mp4, .mov, .avi, .mkv, .webm | Return error, log to audit |
| File size | <= 50 MB (50 * 1024 * 1024 bytes) | Return error, log to audit |
| Path sanitization | Reject paths containing "..", reject absolute paths without normalization | Return error, log to audit |
| Magic bytes verification | Verify file content header matches claimed extension type | Return error, log to audit |

**Magic Bytes Verification:**

| Extension | Magic Bytes (hex) |
|-----------|------------------|
| .jpg | FF D8 FF |
| .png | 89 50 4E 47 0D 0A 1A 0A |
| .mp4 | 00 00 00 18 66 74 79 70 (or 00 00 00 20 66 74 79 70) |

**Text Input Sanitization:**
- All user-provided text inputs (context, search queries, scenario inputs) are HTML-escaped before display (prevent XSS)
- Truncated to maximum length: context 500 chars, search 200 chars, scenario target 200 chars
- No shell command execution with user input (prevent command injection)
- No SQL queries built from user input (prevent SQL injection — WorkBuddy SDK uses parameterized queries internally)
- Scam categorization uses simple substring matching (no regex — prevents ReDoS)

**URL Validation (SSRF Prevention):**
- For Sightengine URL analysis: reject URLs matching internal IP ranges (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16, localhost)
- Only allow http:// and https:// schemes (no file://, ftp://, gopher://)
- Do not follow redirects to internal IPs

### 5.5 Output Sanitization

**HTML Output Escaping:**
- All dynamic content rendered in dashboard HTML is escaped using `textContent` (not `innerHTML`)
- `escapeHtml()` utility function used for all template-inserted content
- Indicators, recommendations, scammer details, context strings — all escaped
- JSON parsed safely with error handling (fail safe — return null on parse error)
- API response structure validated before rendering (check `success` is boolean, `final_score` is number 0-1)

**API Response Filtering:**
- API responses (REST API) do not include:
  - API keys or credentials
  - Raw API responses from Sightengine/Gemini (only parsed fields)
  - Internal file paths
  - Stack traces or error internals
  - Other users' data (API user only sees own scans)

**Error Message Sanitization:**
- All error messages truncated to 200 characters
- No stack traces in error messages
- No file paths in error messages
- No API keys or credentials in error messages
- No database schema details in error messages
- Generic for security failures (e.g., "Security validation failed" — not "Path traversal detected in /etc/passwd")

### 5.6 API Key Management

**Storage Policy:**
- All API keys stored ONLY in environment variables — never in source code, never in database, never in config files

| Variable | Purpose | Rotation |
|----------|---------|----------|
| SIGHTENGINE_USER | Sightengine API user key | 90 days |
| SIGHTENGINE_SECRET | Sightengine API secret key | 90 days |
| GEMINI_API_KEY | Google Gemini API key | 90 days |
| VERIGUARD_MODEL_PATH | Path to ML model weights | N/A (filesystem path) |
| WORKBUDDY_CONFIG_DIR | WorkBuddy auth config path | N/A (platform config) |

**Key Generation:**
- LAICIs API user keys: 256-bit random tokens generated by Admin
- Stored as SHA-256 hashes (plaintext key never persisted)
- Comparison: hash incoming key with SHA-256, compare to stored hash

**Key Rotation Policy:**
- Sightengine keys: rotate every 90 days
- Gemini API key: rotate every 90 days
- API user keys (X-LAICIs-Key): rotate every 30 days
- Rotation logged to audit trail (action="api_key_rotation", old key hash, new key hash)
- Admin notified 7 days before scheduled rotation

### 5.7 Encryption

| Data State | Encryption Method | Implementation |
|------------|-------------------|----------------|
| In transit (API calls to Sightengine) | TLS 1.2+ | HTTPS enforced by `requests` library |
| In transit (API calls to Gemini) | TLS 1.2+ | HTTPS enforced |
| In transit (dashboard) | TLS 1.2+ | WorkBuddy platform HTTPS |
| In transit (API responses) | TLS 1.2+ | WorkBuddy platform HTTPS |
| At rest (Scans DB) | WorkBuddy platform encryption | Inherited, transparent to application |
| At rest (Scammers DB) | WorkBuddy platform encryption | Inherited |
| At rest (Financial Overview DB) | WorkBuddy platform encryption | Inherited |
| At rest (Knowledge base nodes) | WorkBuddy platform encryption | Inherited |
| At rest (Audit trail) | WorkBuddy platform encryption | Inherited, immutable |
| API keys at rest | N/A | Environment variables only — never persisted |

**Requirements:**
- All network communication uses TLS 1.2+ (no TLS 1.0, 1.1, or plaintext)
- No hardcoded keys anywhere in the codebase
- No secrets in database tables
- No secrets in configuration files
- WorkBuddy platform provides encryption at rest (transparent to application)

### 5.8 Audit Trail

**Design Principles:**
- **Append-only:** No UPDATE or DELETE operations available
- **Immutable:** WorkBuddy platform enforces immutability at storage level
- **Complete:** Every scan, query, export, report, auth event, RBAC decision logged
- **Searchable:** Admin can query by date range, action type, actor, result
- **Exportable:** Audit trail exportable for regulatory inspection (BNM, PDRM)

**Audit Trail Fields (7 fields):**

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | timestamp | datetime | ISO 8601, server time |
| 2 | actor | string | user_id or "system" |
| 3 | action | string | scan/query/export/report_generated/osint_update/auth_failure/rbac_denied/rate_limit_hit/input_validation_failed/api_key_rotation/security_incident |
| 4 | target | string | scan_id, db_record_id, report_type, or "N/A" |
| 5 | result | string | success/failure/denied |
| 6 | ip_address | string | If available from WorkBuddy session |
| 7 | session_id | string | WorkBuddy platform session ID |

**Security-Specific Audit Events:**
- `auth_failure`: Failed authentication attempt (logged with IP)
- `rbac_denied`: Authorization denied (logged with role + attempted action)
- `rate_limit_hit`: Rate limit exceeded (logged with user + endpoint)
- `input_validation_failed`: Invalid input blocked (logged with reason)
- `api_key_rotation`: Key rotated (logged with old hash + new hash)
- `security_incident`: Security incident detected (logged with severity)

**Audit Trail Query Capabilities (Admin only):**
- Filter by date range (from/to)
- Filter by action type
- Filter by actor (user_id)
- Filter by result (success/failure/denied)
- Full-text search on details field
- Paginated results (50 per page)
- Export as CSV

### 5.9 STRIDE Threat Model

#### Spoofing

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| S1 | Attacker spoofs API key to bypass authentication | API keys are 256-bit random tokens, stored as SHA-256 hashes, rate-limited, rotated every 30 days |
| S2 | Deepfake content spoofs a real person's identity | Core detection capability — 5-module multi-model detection with 85%+ accuracy, ELA always available as fallback |

#### Tampering

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| T1 | Attacker tampers with scan results in database | WorkBuddy Library SDK is the only write path; RBAC restricts write access to workflow orchestrator only; audit trail records all writes |
| T2 | Attacker tampers with audit trail | Audit trail is append-only with no UPDATE/DELETE API; WorkBuddy platform enforces immutability at storage level |
| T3 | Man-in-the-middle tampers with API responses | TLS 1.2+ encryption on all API calls; Sightengine and Gemini APIs enforce HTTPS |

#### Repudiation

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| R1 | User denies performing a scan or export | Every action logged in immutable audit trail with timestamp, actor, action, target, result, session_id — non-repudiable |

#### Information Disclosure

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| I1 | PII leaked through scan metadata | No PII stored in databases — scan records contain only technical metadata (filename, score, timestamps); `user_id` is WorkBuddy UID, not personal identifier |
| I2 | API keys leaked in error messages or logs | Error messages truncated to 200 chars; API keys never in error messages; error strings do not include credentials |
| I3 | Uploaded media leaked to third parties | Media processed in-memory/temp files, immediately discarded after analysis; Sightengine and Gemini receive the file but do not persist it permanently |
| I4 | Dashboard exposes data to unauthorized users | RBAC enforcement; viewer role has read-only access to limited data; API user role has scoped access only (own scans) |

#### Denial of Service

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| D1 | Attacker floods API with scan requests | Rate limiting: 10 scans per 5 minutes for Sightengine; API tier rate limits configurable per key; WorkBuddy platform DDoS protection |
| D2 | Large file upload exhausts memory | 50 MB file size limit; file validation before processing; temp file cleanup in `finally` blocks |

#### Elevation of Privilege

| Threat ID | Threat | Mitigation |
|-----------|--------|------------|
| E1 | API user escalates to analyst privileges | RBAC engine checks role on every request; API user role has separate permission set; no role escalation endpoint exists |
| E2 | Workflow orchestrator writes to unauthorized database | Orchestrator only writes to Scans DB and Audit Trail via Library SDK; no direct database access; SDK enforces space-level permissions |

### 5.10 OWASP Top 10 Mitigation Matrix

| OWASP Risk | LAICIs Mitigation |
|------------|---------------------|
| A01: Broken Access Control | RBAC engine on every request; module-level authorization; data access control matrix; least privilege principle |
| A02: Cryptographic Failures | TLS 1.2+ everywhere; no hardcoded keys; environment variables only; SHA-256 hashing for API key storage |
| A03: Injection | No SQL (WorkBuddy SDK parameterized queries); no shell commands with user input; HTML escaping on all output; no regex on user input (ReDoS prevention) |
| A04: Insecure Design | Threat modeling (STRIDE analysis); secure SDLC; security requirements in SRS; security design review before implementation |
| A05: Security Misconfiguration | Environment variables for secrets; least privilege; no default credentials; error message sanitization |
| A06: Vulnerable Components | Dependency tracking (requirements.txt); quarterly pip audit/safety check; security review for new dependencies before adding |
| A07: Authentication Failures | WorkBuddy platform auth (OAuth 2.0); session timeout (30 min); account lockout (5 failures/15 min); rate limiting |
| A08: Software and Data Integrity Failures | Immutable audit trail; chain-of-custody logging; append-only logs; no UPDATE/DELETE on audit trail |
| A09: Security Logging and Monitoring Failures | Comprehensive audit trail; every action logged (scan, query, export, report, auth, RBAC, rate limit); searchable and filterable; security event logging |
| A10: Server-Side Request Forgery (SSRF) | URL validation for Sightengine URL analysis; internal IP range blocking; protocol whitelist (http/https only); redirect blocking to internal IPs |

### 5.11 Incident Response

**Incident Severity Classification:**

| Severity | Definition | Response Time | Escalation |
|----------|------------|---------------|------------|
| Critical | Data breach, API key compromise, system compromise | 1 hour | Admin + security team |
| High | Audit trail tampering attempt, RBAC bypass attempt | 4 hours | Admin |
| Medium | Rate limit abuse, input validation attacks | 24 hours | Analyst |
| Low | Failed auth attempts (isolated) | 72 hours | Logged, monitored |

**Incident Response Playbook:**

1. **Detect:** Audit trail alert or user report triggers incident. Automated alerts on security-specific audit events (auth_failure, rbac_denied, rate_limit_hit, input_validation_failed, security_incident).

2. **Classify:** Severity assigned based on classification table. Critical and High severity incidents trigger immediate Admin notification.

3. **Contain:** Revoke compromised API keys immediately. Disable affected sessions. Block offending IP addresses. Isolate affected modules if necessary.

4. **Investigate:** Query audit trail for full scope of incident. Determine: which accounts affected, what data accessed, what actions performed, timeline of events.

5. **Eradicate:** Remove malicious data (if any injected). Patch identified vulnerability. Rotate all API keys (Sightengine, Gemini, API user keys). Update security rules if needed.

6. **Recover:** Restore normal operations. Verify system integrity. Confirm no persistent compromise. Re-enable affected accounts after password reset.

7. **Review:** Post-incident analysis. Document lessons learned. Update security measures. Update threat model if new threat vector identified. Report to stakeholders.

### 5.12 Compliance

#### PDPA 2010 (Personal Data Protection Act)

| Requirement | Implementation |
|-------------|----------------|
| No PII without consent | No personal data stored without explicit user consent; scan metadata is anonymized |
| Data minimization | Only technical metadata stored; media files not persisted; raw API responses not stored |
| Data breach notification | 72-hour notification to PDP Commissioner if breach detected |
| Data subject rights | Scan data deletable on request (Admin can delete scan records); deletion logged to audit trail |
| Purpose limitation | Data used only for deepfake detection and financial risk assessment |
| Data retention policy | Defined in Section 4.3 (scan metadata indefinite, audit trail 7 years, media not stored) |

#### CMA 1998 (Communications and Multimedia Act)

| Requirement | Implementation |
|-------------|----------------|
| Section 233 (offensive content) | Deepfake detection supports law enforcement in identifying and prosecuting deepfake content creators |
| Evidence preservation | Audit trail provides chain of custody for legal proceedings; immutable, append-only logs |
| Cooperation with authorities | PDRM/MCMC can request audit trail exports for investigations; data exportable for legal proceedings |

#### BNM RMCD (Risk Management and Control Division)

| Requirement | Implementation |
|-------------|----------------|
| Fraud detection reporting | Financial institutions using LAICIs can generate BNM compliance reports |
| Audit trail for inspection | Audit trail available for BNM regulatory inspection; exportable as CSV |
| Compliance reports | BNM Fraud Report type includes: scan count, deepfake count, total exposure, prevention value |

### 5.13 Vulnerability Management

**Dependency Scanning:**
- Quarterly: Run `pip audit` or `safety check` on all Python dependencies
- Before any dependency update: Check CVE database for the new version
- Before adding any new dependency: Security review required
- Tracked dependencies: requests, Pillow (PIL), numpy, torch, timm

**Code Review:**
- All code changes reviewed before merge
- Security-focused review for: API key handling, input validation, output sanitization, authentication/authorization logic
- No code merged without at least one reviewer approval
- Security review checklist: no hardcoded secrets, input validation on all user-facing endpoints, output sanitization on all responses, audit logging on all data access

**Security Review for New Dependencies:**
- Document: purpose, source, license, known CVEs
- Review: maintainers, update frequency, community support
- Approval: Admin must approve new dependency addition
- Logging: new dependency addition logged to audit trail

### 5.14 Security Headers

All dashboard and API HTTP responses include the following security headers:

| Header | Value | Purpose |
|--------|-------|---------|
| X-Content-Type-Options | nosniff | Prevent MIME type sniffing |
| X-Frame-Options | DENY | Prevent clickjacking |
| X-XSS-Protection | 1; mode=block | Enable browser XSS filter |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | Enforce HTTPS (HSTS) |
| Content-Security-Policy | default-src 'self'; script-src 'self' 'unsafe-inline' | Control resource loading |

---

## 6. Infrastructure Requirements

### 6.1 WorkBuddy Platform (Primary Infrastructure)

LAICIs v2.0 runs entirely within the WorkBuddy AI ecosystem. No external server hosting is required.

| Component | WorkBuddy Service | Usage |
|-----------|------------------|-------|
| Dashboard hosting | Sites (publish_page) | HTML dashboard published to workbuddy.cc |
| Database storage | Library databases | Scans, Scammers, Financial Overview |
| Knowledge base | Library docs | Data node, Finance node |
| RAG search | Library rag_search.py | Knowledge base Q&A |
| Automation | WorkBuddy automations | Daily OSINT pipeline |
| LLM (optional) | Cloud Service | Keyless Gemini alternative |
| Authentication | WorkBuddy Platform Auth | OAuth 2.0, session management |
| Encryption at rest | WorkBuddy Platform | Transparent to application |
| DDoS protection | WorkBuddy Platform | Inherited |

### 6.2 External API Infrastructure

| API | Endpoint | Auth Method | Rate Limit | Timeout |
|-----|----------|-------------|------------|---------|
| Sightengine Image | api.sightengine.com/1.0/check.json | API user + secret (form data) | 10/5min (code-enforced) | 60s |
| Sightengine Video | api.sightengine.com/1.0/video/check-sync.json | API user + secret (form data) | 10/5min | 120s |
| Gemini Upload | generativelanguage.googleapis.com/upload/v1beta/files | API key (query param) | Google quotas | 30s |
| Gemini Poll | generativelanguage.googleapis.com/v1beta/{file_name} | API key (query param) | Google quotas | 5s per poll |
| Gemini Generate | generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent | API key (query param) | Google quotas | 60s |

### 6.3 Local Runtime Environment

| Component | Requirement | Purpose |
|-----------|-------------|---------|
| Python 3.13+ | Managed runtime | Detection modules, workflow orchestrator, financial modules |
| Node.js 22+ | Managed runtime | Dashboard local preview, build tools |
| Pillow (PIL) | Python package | ELA analysis (image processing) |
| numpy | Python package | ELA pixel array operations |
| requests | Python package | Sightengine + Gemini API calls (HTTPS) |
| torch + timm | Python package (optional) | ML model inference (EfficientNetV2-S) |
| WorkBuddy Library SDK | space_api.py + module scripts | Database operations, RAG, automation, publishing |

### 6.4 Environment Variables

| Variable | Purpose | Required | Rotation |
|----------|---------|----------|----------|
| SIGHTENGINE_USER | Sightengine API user | For full detection | 90 days |
| SIGHTENGINE_SECRET | Sightengine API secret | For full detection | 90 days |
| GEMINI_API_KEY | Google Gemini API key | For video analysis | 90 days |
| VERIGUARD_MODEL_PATH | Path to ML model weights | For ML inference | N/A |
| WORKBUDDY_CONFIG_DIR | WorkBuddy auth config path | For library scripts | N/A |

**Security Policy:** Environment variables are the ONLY storage mechanism for API keys. Keys are never in source code, never in databases, never in configuration files, never in log output.

---

## 7. Integration Architecture

### 7.1 Sightengine API Integration

**Protocol:** HTTPS REST (POST)

**Authentication:** API user + secret (form data)

**Image Endpoint:** POST `api.sightengine.com/1.0/check.json`
- Form fields: models (genai, deepfake), api_user, api_secret, media (file upload)
- Response: JSON with type.ai_generated, type.deepfake, frames[]

**Video Endpoint:** POST `api.sightengine.com/1.0/video/check-sync.json`
- Form fields: models (genai), api_user, api_secret, media (file upload)
- Response: JSON with type.ai_generated, frames[]

**Rate Limiting:**
- 10 scans per 300 seconds, enforced in Python code
- Rate limit check before each API call
- Rate limit hits logged to audit trail (action="rate_limit_hit")

**Error Handling:**
- Timeout: 60s (image), 120s (video)
- Request exceptions: caught, fallback result returned
- JSON parse errors: caught, fallback result returned
- Fallback: if Sightengine unavailable, ELA + ML model take over scoring (WeightedScorer adjusts automatically)

**Security:**
- API secret sent as form data over HTTPS (TLS 1.2+)
- Raw API response NOT persisted to database (data minimization)
- Error messages truncated to 200 chars (no stack traces)

### 7.2 Gemini API Integration

**Protocol:** HTTPS REST (POST)

**Authentication:** API key (query parameter)

**Step 1 — Upload:** POST `generativelanguage.googleapis.com/upload/v1beta/files`
- Headers: X-Goog-Upload-Protocol: resumable, X-Goog-Upload-Command: start
- Upload file content to returned URL

**Step 2 — Poll:** GET `generativelanguage.googleapis.com/v1beta/{file_name}`
- Check state: ACTIVE / FAILED / PROCESSING
- Max 12 attempts, 5s intervals (60s total)

**Step 3 — Transcribe:** POST `models/gemini-2.0-flash:generateContent`
- Payload: file_data (video URI) + text prompt
- Temperature: 0.1 (deterministic)

**Step 4 — Analyze:** POST `models/gemini-2.0-flash:generateContent`
- Payload: analysis prompt + transcript (truncated to 8000 chars)
- Response: JSON with confidence_score, is_deepfake, scam_type, indicators

**Security:**
- API key from environment variable (GEMINI_API_KEY) — passed as URL query parameter (HTTPS only)
- Transcript truncated to 8000 chars before LLM analysis (prevent prompt injection via long transcripts)
- Analysis prompt is a fixed template (ANALYSIS_PROMPT constant — not user-controlled, prevents prompt injection)
- User content (transcript) appended AFTER the instruction; LLM instructed to return ONLY JSON
- Fallback: if Gemini unavailable, 100% Sightengine visual scoring

### 7.3 WorkBuddy Library Integration

**Script:** `space_api.py` (unified entry point)

**Auth:** WORKBUDDY_CONFIG_DIR environment variable

**Space:** DORMATHON26_TECHBENG (spaceId: CSfJ5htmA2LY98nVeDfVD3)

**Operations:**

| Operation | Script | Purpose |
|-----------|--------|---------|
| Database CRUD | space.workspace.database.* | Scans, Scammers, Financial Overview operations |
| Doc creation | create_doc.py | Knowledge base node content creation |
| Doc editing | submit_doc_edit.py | Knowledge base node content updates |
| Doc review | get_doc_reviews.py | Review doc content for RAG indexing |
| RAG search | rag_search.py | Semantic search over Data + Finance nodes |
| Page publishing | publish_page.py | Dashboard deployment to workbuddy.cc |
| Automation | automation_update tool | OSINT pipeline scheduling |

**Security:**
- All database access through Library SDK only (no direct database access)
- SDK enforces parameterized queries (SQL injection prevention)
- SDK enforces space-level permissions
- Audit trail logging on every database write

### 7.4 Dashboard-to-Backend Integration

**Current (v1.0):** Simulated results in JavaScript (dashboard is a demo/prototype)

**Target (v2.0):** Dashboard calls Python workflow via three possible approaches:

| Option | Method | Description |
|--------|--------|-------------|
| A | WorkBuddy Agent | Agent triggers workflow on user upload |
| B | REST API wrapper | Wrapper around VeriGuardWorkflow.run() |
| C | Library page bindings | __SMART_PAGE__.database runtime signals for page-to-database sync |

**Database Synchronization:**
- Dashboard reads from Library databases using page-to-database relation bindings
- `__SMART_PAGE__.database` runtime signals enable real-time data flow
- Scan history table: bound to Scans DB, auto-refreshes on new scan
- Loss prevention tracker: bound to Financial Overview DB, updates on scan completion
- Scammer search: bound to Scammers DB, queries on user search input
- Market intelligence: bound to Financial Overview DB + Data knowledge base node

---

## 8. Non-Functional Requirements

### 8.1 Performance Requirements

| Metric | Target | Measurement |
|--------|--------|-------------|
| Image scan (full pipeline) | < 30 seconds | End-to-end from upload to result display |
| Video scan (full pipeline) | < 120 seconds | End-to-end, including Gemini transcription |
| ELA analysis | < 5 seconds | Single image processing |
| ML inference | < 10 seconds | Single image (if model available) |
| Sightengine API call (image) | < 60 seconds | Image API call timeout |
| Sightengine API call (video) | < 120 seconds | Video API call timeout |
| Gemini full cycle | < 90 seconds | Upload + poll + transcribe + analyze |
| Dashboard initial load | < 3 seconds | First contentful paint |
| Data portal query (10K records) | < 5 seconds | Filtered + paginated results |
| RAG Q&A response | < 10 seconds | Query to answer |
| CSV export (5K records) | < 10 seconds | Query to file download |
| Compliance report generation | < 15 seconds | Report type + date range to output |
| Financial risk assessment (Step 7) | < 3 seconds | Risk tier mapping + exposure calculation + scammer cross-ref |

### 8.2 Availability Requirements

| Component | Target Uptime | Failure Mode |
|-----------|---------------|--------------|
| Dashboard (published page) | 99.5% | WorkBuddy platform dependency |
| Scans/Scammers databases | 99.9% | WorkBuddy Library dependency |
| Sightengine API | 95% (external) | Fallback to ELA + ML |
| Gemini API | 95% (external) | Fallback to 100% Sightengine |
| ELA Analysis | 99.9% (local) | No external dependencies |
| ML Model | 95% (local) | Fallback to Sightengine-only |
| OSINT Automation | 90% | Retry on failure, log to audit |
| RAG Search | 99% | WorkBuddy Library dependency |
| Audit Trail | 99.9% | WorkBuddy Library dependency |
| Financial Risk Assessor | 99.9% (local) | No external dependencies |

### 8.3 Scalability Requirements

| Dimension | Year 1 Target | Year 3 Target |
|-----------|---------------|---------------|
| Monthly scans | 5,000 | 50,000 |
| Concurrent users | 10 | 100 |
| Database records (Scans) | 60,000 | 600,000 |
| Database records (Scammers) | 1,000 | 10,000 |
| API calls per day | 500 | 5,000 |
| RAG queries per month | 200 | 2,000 |
| OSINT data points per month | 300 | 1,500 |
| Audit trail entries per month | 10,000 | 100,000 |

### 8.4 Security Requirements

- API key storage: environment variables only (never in code, never in database)
- User authentication: WorkBuddy platform authentication (OAuth 2.0, inherited)
- Data encryption: TLS 1.2+ in transit, WorkBuddy platform encryption at rest (inherited)
- Audit logging: every data access, scan, query, export, report generation, auth event, RBAC decision logged
- PDPA compliance: no personal data (names, ID numbers) stored without consent
- Input validation: file type validation (extension whitelist), file size limit (50MB), path sanitization, magic bytes verification
- Output sanitization: all user-facing output HTML-escaped to prevent XSS; error messages truncated to 200 chars
- Rate limiting: Sightengine 10/5min enforced; API tier rate limits configurable per key
- Account lockout: 5 failed auth attempts within 15 min triggers 30-min lockout
- Session timeout: 30 minutes of inactivity
- Key rotation: Sightengine/Gemini 90 days, API user keys 30 days
- RBAC: 4 roles (Admin, Analyst, Viewer, API User), module-level authorization, data access control matrix
- STRIDE threat model: all 6 threat categories mitigated
- OWASP Top 10: all 10 risks mitigated
- Incident response: 4 severity levels with defined response times and playbook
- Vulnerability management: quarterly pip audit, code review before merge, security review for new dependencies

### 8.5 Maintainability Requirements

- Code structure: modular — each detection and financial module in separate file, clear interfaces
- Documentation: README, demo script, artifacts index, BRD, PRD, SRD, SDD, SRS in library
- Testing: CLI entry points for each module (python module.py with args)
- Logging: task log in workflow orchestrator records every step with status and timestamp
- Error handling: every module returns structured error results with messages; workflow catches exceptions and returns failure dict
- Configuration: environment variables for all API keys and model paths; WEIGHTS dict in scorer for easy adjustment
- Security review: all code changes reviewed for security implications before merge
- Dependency scanning: quarterly pip audit/safety check on all dependencies

### 8.6 Observability Requirements

- Workflow task log: step-by-step execution log with timestamps and statuses
- Component status: dashboard shows real-time status of each detection module (active/inactive/partial)
- Audit trail: searchable, filterable log of all system actions (scan, query, export, report, auth, RBAC, rate limit)
- OSINT automation log: daily execution status (success/failure, data points collected)
- Error reporting: structured error dicts from every module (error message + context, truncated to 200 chars)
- Performance metrics: scan latency tracking (elapsed_seconds in workflow result)
- Security status: dashboard header shows system security state (green/yellow/red)
- Loss prevention tracker: cumulative counter visible in dashboard header
- Risk tier breakdown: mini bar showing percentage of scans in each risk tier

---

## 9. System Constraints

### 9.1 Platform Constraints

- WorkBuddy Native: All data storage must use WorkBuddy Library databases — no MySQL, PostgreSQL, or external databases
- Library API limits: Large GFM tables in docs cause 524 timeouts (>20K tokens) — use bullet lists or split into segments
- Database script auth: Requires WORKBUDDY_CONFIG_DIR environment variable set to `C:\Users\FARZANAH\.workbuddy-ai`
- Page publishing: Dashboard published via WorkBuddy Sites (workbuddy.cc domain)
- Automation limits: OSINT automation runs as WorkBuddy recurring automation — prompt must be self-contained (no session context)
- Page-to-database bindings: `__SMART_PAGE__.database` runtime signals for real-time data sync

### 9.2 Team Constraints

- Team size: 4 developers, beginner-to-intermediate skill level
- Languages: Python, Java, HTML, CSS, JavaScript
- Timeline: MVP (v1.0) complete; v2.0 features designed but implementation phased
- Budget: Hackathon project — no paid infrastructure beyond API costs

### 9.3 Technical Constraints

- No GPU: ML inference runs on CPU (PyTorch CPU mode) — affects latency, limits model choice to EfficientNetV2-S
- No persistent server: Workflow runs on-demand, not as an always-on service
- File size limit: 50 MB max for uploaded media (Sightengine API constraint)
- Video formats: MP4, MOV, AVI, MKV, WebM supported; others rejected at validation
- Image formats: JPG, JPEG, PNG, WebP, BMP, TIFF supported; ELA only on JPG/PNG
- Rate limits: Sightengine 10 calls per 5 minutes — enforced in code
- Gemini poll: Max 12 attempts, 5s intervals (60s total) — if not ACTIVE, fallback to Sightengine
- ML model weights: Must be trained or downloaded separately; if unavailable, scorer adjusts weights automatically

---

## 10. System Evolution Plan

### Phase 1: v1.0 MVP (Complete)

- 5 detection modules (Sightengine, ELA, ML Inference, Gemini Video, Weighted Scorer)
- 6-step agentic workflow (UNDERSTAND through DELIVER)
- Dashboard published (single-page HTML, 5 sections, dark theme)
- 2 library databases: Scans (15 fields), Scammers (11 fields)
- OSINT automation (daily 9 AM, recurring)
- WorkBuddy Library space: CSfJ5htmA2LY98nVeDfVD3

### Phase 2: Financial Intelligence (Q2 2026)

- FinancialRiskAssessor module (risk tier mapping, exposure calculation, scam categorization, prevention value)
- Step 7 (FINANCIAL_RISK_ASSESS) added to workflow
- Financial database fields: Scans DB +7 fields (22 total), Scammers DB +5 fields (16 total)
- Financial Overview database (NEW, 9 fields)
- Loss Prevention Tracker (cumulative counter in dashboard header)
- Market Intelligence Panel (national scam statistics)
- Populate Data and Finance knowledge base nodes with structured content
- Risk tier thresholds: LOW/MODERATE/HIGH/CRITICAL with RM exposure ranges
- Segment multipliers: bank 10x, corporate 5x, government 8x, sme 1x, individual 0.1x
- Average loss by category: job RM5K, investment RM50K, romance RM15K, phishing RM2K, impersonation RM100K, marketplace RM800, other RM3K

### Phase 3: Data User and Compliance (Q3 2026)

- ScenarioPlanner module (scenario simulation, exposure projection, response playbook)
- RecoveryAssistant module (recovery plan generation, contact directory, regulatory filings)
- Self-service data query portal (filter, query, paginate, export)
- RAG-powered Q&A interface (rag_search.py, embedding + rerank, source citations)
- CSV/JSON export from any query result
- Compliance reporting engine (BNM Fraud Report, PDRM Intelligence Brief, Board Governance Report, Audit Trail Log)
- Audit trail logging (7 fields, append-only, immutable, searchable)
- Pricing and ROI calculator (dashboard widget)
- OSINT pipeline enhancement (WebSearch, extract, JSON structure, Data node append, Financial Overview update, audit log)
- Data portal architecture: filter, query, paginate, export pipeline
- Database-to-dashboard sync: page-to-database relation bindings, `__SMART_PAGE__.database` runtime signals
- Data governance: data minimization, no PII without consent, data subject deletion rights

### Phase 4: Scale and Optimize (Q4 2026)

- ML model fine-tuning on Malaysian-context deepfake data
- Expanded OSINT sources (additional search queries, broader Malaysian scam coverage)
- Mobile-responsive dashboard (responsive CSS, touch-friendly UI)
- Webhook callbacks for API tier (async notification on scan completion)
- Multi-language support (Bahasa Malaysia, Simplified Chinese)
- Performance optimization for 50K+ monthly scans
- ISO 27001 certification preparation (target Year 2)
- SOC 2 Type II certification preparation (target Year 3)
- Advanced data governance: automated data subject deletion workflow
- Enhanced threat intelligence: real-time threat feed integration
- Expanded segment multipliers and scam categories based on accumulated data
- Predictive analytics: trend forecasting for scam patterns

---

## Document Approval

This System Requirements Document defines the complete architecture for LAICIs v2.0, covering three domains equally: FINANCIAL Architecture (3 modules, financial data flow, risk tier mapping, loss prevention tracker, 3 databases with 47 total fields), DATA Architecture (data flow, storage strategy, retention policy, RAG architecture, OSINT pipeline, data portal, data governance, database-dashboard sync), and SECURITY Architecture (authentication, RBAC, input validation, output sanitization, key management, encryption, audit trail, STRIDE threat model, OWASP Top 10, incident response, compliance, vulnerability management, security headers).

**Prepared by:** TECHBENG Team
**Date:** January 2026
**Next Steps:** Proceed to Software Design Document (SDD) for detailed component-level design, and Software Requirements Specification (SRS) for module-level software requirements, interfaces, and acceptance criteria.
