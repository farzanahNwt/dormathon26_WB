# Product Requirements Document (PRD)
# LAICIs v2.0 — Agentic Deepfake Detection & Financial Scam Prevention Platform

## Document Control

| Field | Value |
|-------|-------|
| **Project** | LAICIs v2.0 |
| **Track** | DORMATHON 2026 — Track 2: WorkBuddy Agentic Solutions |
| **Team** | TECHBENG (4 beginner developers: Python, Java, HTML, CSS, JavaScript) |
| **Document Version** | 2.0 |
| **Date** | January 2026 |
| **Status** | Final Draft |
| **Predecessor** | BRD — LAICIs v2.0 |
| **Successor** | SRD — LAICIs v2.0 |

---

## Table of Contents

1. Product Vision & Principles
2. User Personas
3. Feature Roadmap
4. Version Comparison
5. FINANCE Feature Specifications
6. DATA Feature Specifications
7. SECURITY Feature Specifications
8. Dashboard Layout
9. User Stories Backlog
10. Non-Functional Requirements
11. Dependencies
12. Acceptance Criteria
13. Out of Scope

---

## 1. Product Vision & Principles

### 1.1 Vision Statement

**"Every Malaysian should be able to verify the authenticity of any media in under 30 seconds — and instantly understand the financial risk it poses, query the data behind it, and trust that every action is secure and auditable."**

LAICIs v2.0 transforms deepfake detection from a technical diagnostic into a comprehensive business intelligence, data management, and security platform. When a user uploads a suspicious image or video, the platform not only tells them *whether* it is AI-generated, but also *how much money is at risk*, *what type of scam it matches*, *what recovery steps to take*, *how to query and export the underlying data*, and *provides a full audit trail for compliance and chain-of-custody* — all through an autonomous agentic workflow built natively in WorkBuddy AI.

### 1.2 Product Tagline

**"Detect. Quantify. Query. Protect."** — The Malaysian deepfake defense platform with financial intelligence, self-service data, and security-by-design.

### 1.3 Product Principles

1. **Detection First, Intelligence Always:** Every scan produces a technical verdict, a financial intelligence output, a queryable data record, and an audit trail entry. No scan is a dead end — it feeds all three domains simultaneously.

2. **Self-Service by Design:** Data users never need a developer to query results, export data, or ask questions about the knowledge base. The self-service portal, RAG Q&A, and CSV/JSON exports eliminate the IT bottleneck entirely.

3. **Security by Architecture, Not by Afterthought:** Authentication, authorization, input validation, output sanitization, audit trails, and threat mitigation are built into every feature from the ground up — not bolted on after deployment. Every user action is authenticated, authorized, validated, sanitized, and logged.

4. **Graceful Degradation:** If any API is down, the platform still works. ELA is always available (no API key required), the weighted scorer adjusts automatically, financial assessment runs on local data, and the audit trail continues logging. The system never has zero-coverage.

5. **Financial Context Native:** Malaysian Ringgit throughout. Malaysian scam statistics. Malaysian regulations (BNM, PDRM, MCMC, CyberSecurity Malaysia). Malaysian legal framework (PDPA 2010, CMA 1998). This is not a global tool localized for Malaysia — it is built for Malaysia from the ground up.

6. **Agentic, Not Transactional:** The platform follows a 7-step autonomous workflow: UNDERSTAND → PLAN → EXECUTE → VALIDATE → INTEGRATE → DELIVER → FINANCIAL_RISK_ASSESS. It is not just an API endpoint that returns a score. It understands context, plans its approach, validates results, integrates multiple signals, delivers a comprehensive report, and assesses financial risk — all autonomously.

7. **Data as a First-Class Citizen:** Scan results, scammer profiles, financial aggregates, and knowledge base content are not just stored — they are queryable, exportable, searchable via natural language, and synchronized between databases and the dashboard in real time. Data users are a primary audience, not an afterthought.

8. **Compliance is a Feature, Not a Burden:** BNM fraud reports, PDRM intelligence briefs, board governance reports, and audit trail logs are generated with one click. Chain-of-custody is automatic. Regulatory compliance is a selling point, not overhead.

---

## 2. User Personas

### Persona 1: Aisha — Bank Fraud Analyst (Enterprise Tier)

**Profile:**

| Attribute | Value |
|-----------|-------|
| Role | Senior Fraud Analyst at a top-5 Malaysian bank |
| Age | 32 |
| Location | Kuala Lumpur |
| Technical Level | Intermediate — comfortable with dashboards, SQL basics, API concepts |
| Tier | Enterprise (RM 50,000–250,000/yr) |

**Daily Workflow:**
- Reviews flagged transactions and customer-submitted media at the KYC onboarding gate
- Needs to verify if a customer's ID photo is a deepfake during KYC onboarding
- Must generate compliance reports for Bank Negara Malaysia quarterly
- Tracks fraud prevention metrics for internal KPIs and department reporting
- Cross-references identified scammers against new customer submissions
- Escalates confirmed deepfake cases to the fraud investigation team

**Pain Points:**
- Current tools only say "AI-generated: 87%" — no financial context, no risk tier, no exposure estimate
- Cannot easily export data for regulatory reporting — has to file tickets with IT for custom queries
- No historical database of identified scammers to cross-reference against new submissions
- Spends 3+ hours per week asking developers for custom data pulls
- No audit trail for chain-of-custody when cases go to legal proceedings
- No recovery playbook when a deepfake incident is confirmed

**What She Needs from LAICIs v2.0:**

*FINANCE:*
- Upload a customer photo, get: detection score + financial risk rating (LOW/MODERATE/HIGH/CRITICAL) + estimated RM exposure + matched scammer profiles + compliance-ready report
- Loss prevention tracker showing her department's cumulative prevented-loss value in RM
- Pricing & ROI calculator to justify renewal to her procurement team
- Recovery Assistant with actionable steps when a deepfake case is confirmed

*DATA:*
- Self-service query portal to pull her own reports without IT — filter by date, risk tier, scam category
- CSV exports of all scans for BNM quarterly reporting with one click
- RAG-powered Q&A to ask "How many deepfake cases were detected in Q1 2026?" without reading full reports

*SECURITY:*
- Authentication via WorkBuddy platform OAuth — no separate login
- RBAC: Analyst role — can scan, query, export, and generate reports, but cannot modify system config
- Audit trail for every scan she runs — admissible as chain-of-custody evidence in legal proceedings
- Compliance reports: BNM Fraud Report generated with one click, including audit trail log
- Session timeout warning so she doesn't lose work during long analysis sessions

---

### Persona 2: Inspector Rahman — Police CCID Officer (Government Tier)

**Profile:**

| Attribute | Value |
|-----------|-------|
| Role | Commercial Crime Investigation Department (CCID), Bukit Aman |
| Age | 45 |
| Location | Putrajaya |
| Technical Level | Basic — uses government systems, limited programming knowledge |
| Tier | Government (custom pricing) |

**Daily Workflow:**
- Tracks deepfake and scam case trends nationally across all Malaysian states
- Maintains scammer databases (phone numbers, emails, websites, social media accounts)
- Prepares intelligence briefings for senior officers and the Inspector General of Police
- Coordinates with Bank Negara Malaysia, MCMC, and CyberSecurity Malaysia on cross-agency cases
- Testifies in court using digital evidence — needs provable chain-of-custody

**Pain Points:**
- No centralized database of identified scammers across agencies — each agency maintains its own
- Manual OSINT collection from news websites takes 2+ hours daily
- Cannot easily correlate deepfake cases with financial losses across jurisdictions
- No audit trail for evidence — defense attorneys challenge digital evidence authenticity
- Government systems are slow and not user-friendly

**What He Needs from LAICIs v2.0:**

*FINANCE:*
- Market intelligence panel showing national scam statistics (RM 5.62B total losses, 454 deepfake cases, 76% YoY increase) for briefing superiors
- Financial Overview database for national-level aggregate reporting
- Recovery Assistant with Malaysian regulatory contact directory (BNM FEN, PDRM CCID hotline 03-26101599, MCMC, CyberSecurity Malaysia)

*DATA:*
- Scammer database search across phone, email, website, scam type — cross-agency
- Automated daily OSINT feeds populated into the knowledge base at 9 AM every morning
- RAG-powered Q&A: "How many deepfake cases were reported in Q2 2024?" — get answers without reading 116KB reports
- Data export (CSV/JSON) of scammer records for inter-agency sharing

*SECURITY:*
- Audit trail with 7 fields (timestamp, actor, action, target, result, IP, session ID) for every action — chain-of-custody for court evidence
- Compliance reports: PDRM Intelligence Brief generated with one click
- RBAC: Viewer role — read-only access to scammer database and scan history (no modification)
- Security status indicator showing system health before relying on data for briefings
- Incident response playbook for when a new deepfake scam pattern is detected

---

### Persona 3: Sarah — Corporate Security Manager (Professional Tier)

**Profile:**

| Attribute | Value |
|-----------|-------|
| Role | Head of Corporate Security at a Bursa Malaysia-listed company |
| Age | 38 |
| Location | Selangor |
| Technical Level | Intermediate — security professional, not a developer |
| Tier | Professional (RM 15,000–50,000/yr) |

**Daily Workflow:**
- Monitors for deepfake impersonation of C-suite executives on social media
- Evaluates risk of AI-generated disinformation targeting the company brand
- Prepares board-level risk assessments for quarterly governance meetings
- Manages employee awareness training programs
- Coordinates with IT security team on incident response

**Pain Points:**
- No tool to scenario-plan: "What if a deepfake video of our CEO appears on social media?"
- Cannot quantify financial exposure for board reporting — board wants RM figures, not "high risk"
- No recovery playbook when a deepfake incident occurs — ad hoc response is chaotic
- Board governance reports take days to prepare manually

**What She Needs from LAICIs v2.0:**

*FINANCE:*
- Scenario Planner: input a hypothetical deepfake scenario (executive impersonation, fake news, marketplace, political), get projected RM exposure and response playbook
- Financial Risk Assessor: map detection score to company-specific financial exposure
- Recovery Assistant: step-by-step playbook for deepfake incident response with Malaysian contacts
- Pricing & ROI calculator to justify LAICIs subscription to her CFO
- Loss prevention tracker for board reporting

*DATA:*
- RAG-powered Q&A to research deepfake trends and case studies for board presentations
- Data export of scan results for internal governance documentation
- Financial Overview database for quarterly trend analysis

*SECURITY:*
- Compliance reports: Board Governance Report generated with one click
- RBAC: Admin role for herself, Analyst role for her team members
- Audit trail for corporate governance — every scan and report generation logged
- Security dashboard elements: security status indicator, role badge, session timeout warning
- Incident response: 4 severity levels with response playbook (detect/classify/contain/investigate/eradicate/recover/review)
- Threat mitigation: STRIDE analysis and OWASP Top 10 coverage documented for board assurance

---

### Persona 4: Dev — Data Analyst (API/Starter Tier)

**Profile:**

| Attribute | Value |
|-----------|-------|
| Role | Data analyst at a cybersecurity firm |
| Age | 28 |
| Location | Penang |
| Technical Level | Advanced — Python, SQL, API integration |
| Tier | API/Starter (RM 3,000–15,000/yr + RM 0.50–2.00/detection) |

**Daily Workflow:**
- Queries scan results for trend analysis and pattern detection
- Builds dashboards and reports from scan data for clients
- Researches emerging deepfake patterns and scam methodologies
- Exports data for client deliverables and custom analysis
- Integrates with third-party tools via REST API

**Pain Points:**
- Needs to run custom queries but no self-service portal exists — always dependent on developers
- Knowledge base content is scattered across documents, not searchable semantically
- Manual CSV exports are tedious and error-prone
- No semantic search over historical intelligence — keyword search misses context
- No API access for programmatic integration with his Python pipelines

**What He Needs from LAICIs v2.0:**

*FINANCE:*
- Financial database fields on scans and scammers for quantitative analysis
- Financial Overview database for trend analysis and aggregation
- Market intelligence statistics for context in his client reports

*DATA:*
- Self-service query portal with filter/sort/export — filter scans by date, type, score, risk, category; filter scammers by email, phone, website, type, risk; paginated results (50/page)
- RAG-powered Q&A over the Data and Finance knowledge base nodes — natural language questions with source citations
- CSV/JSON export of any query result with one click
- Automated OSINT data pipeline — daily 9 AM WebSearch for Malaysian scam news, appended to knowledge base
- Database ↔ dashboard sync via `__SMART_PAGE__.database` runtime signals and page↔database relation bindings

*SECURITY:*
- RBAC: API User role — REST API access only, no dashboard UI
- API keys: 256-bit, hashed, rotated every 30 days
- Session timeout: 30 minutes
- Input validation on all API endpoints — file extension whitelist, size limit 50MB, path sanitization, magic bytes verification
- Output sanitization — API response filtering (no raw responses, paths, or keys exposed)
- Audit trail logging for all API calls — every API action tracked

---

## 3. Feature Roadmap

### 3.1 Feature Priority Matrix

Features are prioritized P0 (MVP, already built in v1.0), P1 (v2.0 Phase 2 — essential), P2 (v2.0 Phase 3 — important), P3 (Future — nice to have).

**P0 — MVP (v1.0, Complete):**

| Feature | Phase | Persona |
|---------|-------|---------|
| Multi-model detection (5 modules) | v1.0 Complete | All |
| Dashboard with upload + results | v1.0 Complete | All |
| 6-step agentic workflow | v1.0 Complete | All |
| Scans database (15 fields) | v1.0 Complete | All |
| Scammers database (11 fields) | v1.0 Complete | All |
| Scammer search + OSINT | v1.0 Complete | Rahman, Aisha |
| Dark theme dashboard | v1.0 Complete | All |
| Conic-gradient result circles | v1.0 Complete | All |
| Component status display | v1.0 Complete | All |

**P1 — v2.0 Phase 2 (Financial Intelligence + Security Foundation):**

| Feature | Phase | Persona |
|---------|-------|---------|
| Financial Risk Assessor module | Phase 2 | Aisha, Sarah |
| Loss Prevention Tracker (dashboard header) | Phase 2 | Aisha, Sarah |
| Financial fields on Scans DB (+7) | Phase 2 | Aisha, Dev |
| Financial fields on Scammers DB (+5) | Phase 2 | Aisha, Rahman |
| Financial Overview database (new, 9 fields) | Phase 2 | Aisha, Sarah |
| Market Intelligence Panel (7 statistics) | Phase 2 | All |
| Populate Data knowledge base node | Phase 2 | Dev, Rahman |
| Populate Finance knowledge base node | Phase 2 | Dev, Sarah |
| OSINT data pipeline (daily 9 AM automation) | Phase 2 | Rahman |
| Authentication (OAuth 2.0, API keys) | Phase 2 | All |
| RBAC (4 roles) | Phase 2 | All |
| Input validation (file/size/path/magic bytes) | Phase 2 | All |
| Output sanitization (HTML escape, API filter) | Phase 2 | All |
| Audit trail logging (7 fields) | Phase 2 | Rahman, Aisha |

**P2 — v2.0 Phase 3 (Scenario, Recovery, Data Portal, Compliance):**

| Feature | Phase | Persona |
|---------|-------|---------|
| Scenario Planner module | Phase 3 | Sarah |
| Recovery Assistant module | Phase 3 | Sarah, Aisha |
| Pricing & ROI Calculator widget | Phase 3 | All |
| Self-service data query portal | Phase 3 | Dev, Aisha |
| RAG-powered knowledge base Q&A | Phase 3 | Dev, Rahman |
| CSV/JSON export from any query | Phase 3 | Dev, Aisha |
| Database ↔ dashboard sync | Phase 3 | Dev |
| Compliance reports (BNM, PDRM, Board, Audit) | Phase 3 | Aisha, Rahman |
| Security dashboard elements (status, badges, banners) | Phase 3 | All |
| STRIDE threat mitigation | Phase 3 | Sarah |
| OWASP Top 10 compliance | Phase 3 | Sarah |
| Incident response playbook (4 severity levels) | Phase 3 | Sarah |
| Vulnerability management (quarterly scanning) | Phase 3 | Sarah |

**P3 — Future (v3.0+):**

| Feature | Phase | Persona |
|---------|-------|---------|
| Mobile-responsive dashboard | Phase 4 | All |
| Webhook callbacks for API tier | Phase 4 | Dev |
| ML model fine-tuning on Malaysian data | Phase 4 | All |
| Multi-language support (BM, EN, CN) | Phase 4 | All |
| Real-time video stream analysis | Phase 4 | All |
| SIEM/SOAR integration | Phase 4 | Sarah |
| Blockchain evidence storage | Phase 4 | Rahman |
| Multi-country expansion (SG, TH, ID) | Phase 4 | All |

### 3.2 Phased Delivery Plan

**Phase 2 (Q2 2026) — Financial Intelligence + Security Foundation:**
The Financial Risk Assessor module is built and inserted as Step 7 in the agentic workflow. Financial fields are added to the Scans and Scammers databases. The Financial Overview database is created. The Loss Prevention Tracker and Market Intelligence Panel are added to the dashboard header. The Data and Finance knowledge base nodes are populated with structured, queryable content. The OSINT automation pipeline begins daily runs. Authentication, RBAC, input validation, output sanitization, and audit trail logging are implemented as foundational security infrastructure.

**Phase 3 (Q3 2026) — Scenario, Recovery, Data Portal, Compliance:**
The Scenario Planner and Recovery Assistant modules are built. The Pricing & ROI Calculator widget is added to the dashboard. The self-service data query portal is deployed with filtering, sorting, pagination, and CSV/JSON export. The RAG-powered Q&A interface is connected to the populated knowledge base nodes. The compliance reporting engine generates BNM, PDRM, Board Governance, and Audit Trail reports. Security dashboard elements (status indicator, role badge, session timeout warning, incident banner, audit trail tab) are added. STRIDE and OWASP Top 10 threat mitigation documentation is finalized. Incident response playbooks are published.

**Phase 4 (Q4 2026+) — Scale & Optimize:**
Mobile-responsive dashboard, webhook callbacks, ML model fine-tuning, multi-language support, and advanced integrations are deferred to v3.0.

---

## 4. Version Comparison

### v1.0 vs v2.0 — Full Comparison

| Aspect | v1.0 (VeriGuard AI) | v2.0 (LAICIs) |
|--------|---------------------|-----------------|
| Detection Modules | 5 (Sightengine, ELA, ML, Gemini, WeightedScorer) | 5 (same modules, same architecture) |
| Financial Modules | 0 | 3 (Financial Risk Assessor, Scenario Planner, Recovery Assistant) |
| Workflow Steps | 6 (UNDERSTAND→PLAN→EXECUTE→VALIDATE→INTEGRATE→DELIVER) | 7 (added FINANCIAL_RISK_ASSESS as Step 7) |
| Dashboard Sections | 5 (header, upload, results, history, scammer search) | 10 (added market intel, loss tracker, pricing calculator, data portal, compliance/audit) |
| Database Fields (Scans) | 15 | 22 (added 7 financial fields) |
| Database Fields (Scammers) | 11 | 16 (added 5 financial fields) |
| New Database | 0 | 1 (Financial Overview, 9 fields) |

| Aspect | v1.0 (VeriGuard AI) | v2.0 (LAICIs) |
|--------|---------------------|-----------------|
| Knowledge Base Nodes | README, Demo Script, Artifacts Index (3, empty data/finance nodes) | 5 (added populated Data node, populated Finance node) |
| Data User Tools | None | Self-service portal, RAG Q&A, CSV/JSON export, automated OSINT pipeline |
| Authentication | None (open dashboard) | WorkBuddy OAuth 2.0, 256-bit API keys, 30-min session timeout, 5-failure lockout |
| Authorization | None (all access) | RBAC with 4 roles (Admin, Analyst, Viewer, API User) |
| Input Validation | Basic file type check | Extension whitelist, 50MB size limit, path sanitization, magic bytes verification |
| Output Sanitization | None | HTML escaping (escapeHtml utility), API response filtering, error truncation (200 chars) |

| Aspect | v1.0 (VeriGuard AI) | v2.0 (LAICIs) |
|--------|---------------------|-----------------|
| Audit Trail | None | 7 fields (timestamp, actor, action, target, result, ip, session_id), append-only, immutable |
| Compliance Reports | None | 4 types (BNM Fraud Report, PDRM Intelligence Brief, Board Governance Report, Audit Trail Log) |
| Threat Mitigation | None | STRIDE (6 threats mitigated), OWASP Top 10 (A01–A10 addressed) |
| Incident Response | None | 4 severity levels with 7-step playbook (detect→classify→contain→investigate→eradicate→recover→review) |
| Vulnerability Management | None | Quarterly dependency scanning, code review before merge |
| Pricing/ROI Tools | None | Interactive calculator widget (segment, volume, loss → ROI) |

| Aspect | v1.0 (VeriGuard AI) | v2.0 (LAICIs) |
|--------|---------------------|-----------------|
| Scenario Planning | None | 4 scenario types (executive impersonation, fake news, marketplace, political) with projected RM exposure |
| Recovery Guidance | None | Actionable recovery steps, regulatory filings, evidence checklist, contact directory (BNM/PDRM/MCMC/CyberSecurity Malaysia) |
| Data Governance | None | Retention policy, data minimization, no PII without consent |
| Database ↔ Dashboard Sync | None | Page↔database relation bindings, `__SMART_PAGE__.database` runtime signals |
| User Personas | 1 (generic user) | 4 (Aisha, Rahman, Sarah, Dev) with detailed pain points and feature mappings |

---

## 5. FINANCE Feature Specifications

This section specifies all 8 financial features in detail. Each specification includes description, inputs, outputs/capabilities, processing logic, UI elements, and user stories.

---

### 5.1 Financial Risk Assessor Module

**Description:**
A new detection module that runs as Step 7 in the 7-step agentic workflow. After the WeightedScorer produces a final detection score (0–1) in Step 5, and results are packaged in Step 6, the Financial Risk Assessor maps that score to a financial risk tier, estimates potential monetary exposure in Malaysian Ringgit, categorizes the scam type, and calculates the prevention value of detecting this scam. This module transforms a technical detection score into actionable financial intelligence.

**Inputs:**

| Input | Type | Source | Required |
|-------|------|--------|----------|
| Final detection score | float (0.0–1.0) | WeightedScorer output (Step 5) | Yes |
| Media type | string (image/video) | UNDERSTAND step (Step 1) | Yes |
| Is deepfake flag | boolean | WeightedScorer output | Yes |
| User context | string | User input at upload (e.g., "marketplace seller photo", "executive video call", "KYC onboarding") | No |
| Scammer match results | list[dict] | Scammers database cross-reference | No |
| Segment | string | User selection (bank/corporate/government/sme/individual) | No |

**Risk Tier Mapping:**

| Score Range | Risk Tier | Estimated Exposure Range (RM) | Color | Description |
|-------------|-----------|-------------------------------|-------|-------------|
| 0.0–0.3 | LOW | 0–500 | Green (#2ed573) | Likely authentic media, minimal financial risk |
| 0.3–0.5 | MODERATE | 500–5,000 | Yellow (#ffa502) | Possibly AI-generated, moderate exposure to scam |
| 0.5–0.8 | HIGH | 5,000–50,000 | Orange (#ff7f50) | Likely AI-generated, significant financial risk |
| 0.8–1.0 | CRITICAL | 50,000–500,000+ | Red (#ff4757) | Almost certainly deepfake, severe financial exposure |

**Processing Logic:**

1. Map detection score to risk tier using the thresholds above
2. Set base exposure range from the tier's RM range
3. If user context indicates "corporate/executive/KYC", escalate exposure to the upper bound of the tier
4. If scammer match found in Scammers database, add known loss history (`total_known_losses_rm` / `case_count`) to exposure estimate
5. Categorize scam type based on user context keywords:
   - "job", "recruitment", "offer" → job scam
   - "investment", "return", "profit", "crypto" → investment scam
   - "love", "dating", "romance", "girlfriend", "boyfriend" → romance scam
   - "bank", "login", "password", "otp" → phishing
   - "ceo", "executive", "director", "impersonation" → impersonation
   - "seller", "marketplace", "product", "shopee", "carousell" → marketplace fraud
   - No match → other
6. Calculate prevention value: 25% of the average loss for the matched scam category

**Scam Category Average Losses (Malaysian market data):**

| Scam Category | Average Loss per Case (RM) | Prevention Value (25%) |
|---------------|---------------------------|------------------------|
| Job scam | 3,000 | 750 |
| Investment scam | 50,000 | 12,500 |
| Romance scam | 15,000 | 3,750 |
| Phishing | 2,000 | 500 |
| Impersonation | 122,000 | 30,500 |
| Marketplace fraud | 1,500 | 375 |
| Other | 5,991 | 1,498 |

*Note: Average loss figures derived from PDRM CCID statistics and LAICIs Research Report. Impersonation average anchored to RM 122M single-case loss distributed across portfolio. "Other" uses RM 2.72M / 454 cases = RM 5,991 average.*

**Outputs:**

| Output Field | Type | Description |
|--------------|------|-------------|
| `risk_tier` | string | LOW / MODERATE / HIGH / CRITICAL |
| `estimated_exposure_rm` | float | Estimated monetary exposure in RM |
| `scam_category` | string | job/investment/romance/phishing/impersonation/marketplace/other |
| `segment_specific_range` | dict | e.g., `{"bank": "RM 50K–500K", "individual": "RM 500–5K"}` |
| `prevention_value_rm` | float | Estimated value of detecting this scam (25% of category average loss) |
| `recovery_recommendation` | string | Immediate action steps (links to Recovery Assistant if confirmed) |

**UI Elements:**
- Risk tier badge displayed next to detection score circle: colored pill with tier name (LOW=green, MODERATE=yellow, HIGH=orange, CRITICAL=red)
- Estimated exposure displayed as "Est. Exposure: RM X,XXX" in large font
- Scam category displayed as a tag/chip below the risk tier badge
- Prevention value displayed as "Prevention Value: RM X,XXX" in accent color
- If scammer match found: alert banner "Scammer Match Found — X known cases, RM Y total losses"

**User Story:**
*As a bank fraud analyst (Aisha), when I upload a suspicious KYC photo and it scores 0.85, I want the system to tell me "CRITICAL RISK, estimated exposure RM 50,000–500,000, scam category: identity fraud, prevention value: RM 30,500" so I can escalate immediately to the fraud investigation team and freeze the onboarding process.*

**Acceptance Criteria:**
- Every scan result displays risk_tier, estimated_exposure_rm, scam_category, and prevention_value_rm
- Risk tier mapping is correct for all 4 tiers at boundary values (0.3, 0.5, 0.8)
- Scammer cross-reference adds historical loss data to exposure estimate
- Prevention value equals 25% of the category average loss
- Results are persisted in the Scans database (7 new financial fields)

---

### 5.2 Loss Prevention Tracker

**Description:**
A dashboard header widget that displays a cumulative counter of estimated prevented losses (in RM) across all scans performed on the platform. This serves as both a stakeholder reporting tool (for boards, regulators, and procurement teams) and a marketing asset demonstrating the platform's tangible value.

**Display:**

| Element | Specification |
|---------|---------------|
| Counter | Large RM counter in dashboard header, formatted as "RM X,XXX,XXX prevented" |
| Subtitle | "across X scans since [platform inception date]" |
| Color coding | Green (#2ed573) for < RM 100K, Blue (#00d4ff) for RM 100K–1M, Purple (#a55eea) for > RM 1M |
| Animation | Counter animates from previous value to new value on scan completion |
| Click to expand | Modal showing breakdown by scam category, by customer segment, by month |
| Tooltip | "Prevention value = 25% of average loss per scam category. Based on Malaysian PDRM CCID statistics." |

**Color Thresholds:**

| Cumulative Prevention Value | Color | CSS Variable | Meaning |
|----------------------------|-------|-------------|---------|
| RM 0 – 99,999 | Green | `--success` (#2ed573) | Early stage / startup impact |
| RM 100,000 – 999,999 | Blue | `--accent` (#00d4ff) | Growing impact / significant value |
| RM 1,000,000+ | Purple | `--purple` (#a55eea) | Major impact / enterprise-scale value |

**Calculation Logic:**
1. For each scan with `is_ai_generated = true`, retrieve the `prevention_value_rm` from the Financial Risk Assessor output
2. Add `prevention_value_rm` to the cumulative total in the Financial Overview database
3. If a scammer match was found and the scammer has `total_known_losses_rm > 0`, add the historical average (`average_loss_per_case_rm`) as additional prevention value
4. The counter never resets — it is cumulative since platform inception
5. Counter updates within 5 seconds of scan completion via database↔dashboard sync (`__SMART_PAGE__.database` runtime signal)
6. Financial Overview database `total_prevented_loss_rm` field is the source of truth

**Expanded View (click modal):**

| Breakdown Dimension | Display |
|---------------------|---------|
| By scam category | Bar chart: investment, impersonation, romance, phishing, job, marketplace, other |
| By customer segment | Pie chart: bank, corporate, government, sme, individual |
| By month | Line chart showing cumulative growth over time |
| Top 5 prevention values | Table of highest-value scans with date, category, prevention value |

**User Story:**
*As a corporate security manager (Sarah), I want to show my board that LAICIs has prevented RM 2.3 million in potential losses across 450 scans this quarter, with the counter color-coded purple to indicate enterprise-scale impact, so they renew the contract and expand to other business units.*

**Acceptance Criteria:**
- Loss prevention tracker displays in the dashboard header alongside existing stat pills
- Counter updates within 5 seconds of scan completion
- Color changes correctly at RM 100K (green→blue) and RM 1M (blue→purple) thresholds
- Click-to-expand modal shows breakdown by category, segment, and month
- Counter is cumulative and never resets
- Source of truth is Financial Overview database `total_prevented_loss_rm` field

---

### 5.3 Market Intelligence Panel

**Description:**
A dashboard section displaying real-time Malaysian scam statistics sourced from the populated Finance knowledge base node and the OSINT automation feed. This panel keeps all users informed about the national threat landscape without needing to read lengthy reports. Statistics are auto-updated when the daily OSINT pipeline runs.

**Content — 7 Key Statistics:**

| # | Statistic | Value | Source | Display Format |
|---|-----------|-------|--------|----------------|
| 1 | Total Malaysian scam losses (2023–2025) | RM 5.62 billion | PDRM CCID, BNM SFMS | "RM 5.62B" (large), "Total scam losses 2023–2025" (small) |
| 2 | Deepfake fraud cases (H1 2024) | 454 cases | Bukit Aman CCID | "454" (large), "Deepfake cases H1 2024" (small) |
| 3 | Deepfake fraud losses (H1 2024) | RM 2.72 million | Bukit Aman CCID | "RM 2.72M" (large), "Deepfake losses H1 2024" (small) |
| 4 | Largest single corporate deepfake fraud | RM 122 million | LAICIs Research Report | "RM 122M" (large), "Largest single case" (small) |
| 5 | Victim belief rate | 85% | Sumsub / LAICIs Research | "85%" (large), "Victim belief rate" (small) |
| 6 | National recovery rate | 2% | PDRM CCID | "2%" (large), "National recovery rate" (small) |
| 7 | YoY increase in deepfake cases | 76% | Bukit Aman CCID | "76%↑" (large, up arrow), "YoY increase" (small) |

**Display Layout:**
- Full-width card below the dashboard header
- 3-column grid (responsive: 2-column on tablet, 1-column on mobile in Phase 4)
- Each stat is a "stat pill" card: large number (28px font, accent color), small label (12px, muted), source attribution (10px, italic)
- Trend arrows: up arrow (↑) for increasing trends (red for losses/cases, green for prevention), down arrow (↓) for decreasing trends
- "Last updated: [date]" footer, sourced from OSINT automation last-run timestamp
- Auto-refresh: statistics update when OSINT pipeline completes (daily 9 AM)

**Data Flow:**
1. OSINT automation runs WebSearch at 9 AM daily for Malaysian scam news
2. Extracted data points are appended to the Data knowledge base node
3. Financial Overview database is updated with new aggregate figures
4. Market Intelligence Panel reads from Financial Overview database via `__SMART_PAGE__.database` runtime signal
5. Panel auto-refreshes with updated statistics

**User Story:**
*As a police CCID officer (Rahman), I want to see the latest national scam statistics — RM 5.62 billion in total losses, 454 deepfake cases, 76% year-over-year increase — on the dashboard so I can brief my superiors at Bukit Aman with current data without compiling a separate report.*

**Acceptance Criteria:**
- Market Intelligence Panel displays all 7 statistics with correct values
- Each statistic shows source attribution
- Panel auto-updates when OSINT automation runs
- "Last updated" timestamp reflects most recent OSINT run
- YoY trend arrow displays correctly (76%↑)
- Panel is visible to all roles (Admin, Analyst, Viewer, API User sees it in API response)

---

### 5.4 Pricing & ROI Calculator

**Description:**
An interactive dashboard widget that lets users (especially prospects and existing customers) calculate the return on investment (ROI) of using LAICIs based on their customer segment, expected scan volume, and historical fraud loss exposure. This widget serves as both a sales tool and a renewal-justification tool.

**Inputs:**

| Input | Type | Options / Range | Default |
|-------|------|-----------------|---------|
| Customer segment | Dropdown | Bank, Corporate, Government, SME, API | Bank |
| Expected monthly scan volume | Slider | 10–10,000 | 500 |
| Historical annual fraud loss (RM) | Number input | RM 1,000–RM 100,000,000 | RM 500,000 |
| Selected pricing tier | Dropdown | Starter (RM 3K), Professional (RM 15K), Enterprise (RM 50K), Enterprise+ (RM 250K) | Professional |

**Calculation Logic:**

1. **Annual cost** = tier price + (API calls × per-detection rate if applicable)
   - Per-detection rate: RM 0.50 (standard), RM 0.43 (10K+ volume, 15% discount), RM 0.38 (50K+, 25% discount), RM 0.33 (100K+, 35% discount)
2. **Estimated prevention value** = historical annual fraud loss × prevention rate
   - Without LAICIs: 15% of fraud is caught (85% victim belief rate means 85% of deepfakes are believed)
   - With LAICIs: 80% prevention (multi-model detection catches deepfakes before transaction)
   - Net prevention improvement: 80% − 15% = 65% of historical fraud loss prevented
   - Estimated prevention = historical loss × 0.65
3. **ROI** = Estimated prevention / Annual cost
4. **Payback period** = Annual cost / (Estimated prevention / 12)

**ROI Reference Table (pre-computed examples):**

| Segment | Annual Cost | Historical Loss | Estimated Prevention | ROI |
|---------|------------|-----------------|---------------------|-----|
| Bank (conservative) | RM 100,000 | RM 1,000,000 | RM 650,000 | 6.5x |
| Bank (optimistic) | RM 100,000 | RM 122,000,000 | RM 79,300,000 | 793x |
| Corporate | RM 30,000 | RM 300,000 | RM 195,000 | 6.5x |
| Government | RM 200,000 | RM 2,000,000 | RM 1,300,000 | 6.5x |
| SME | RM 5,000 | RM 50,000 | RM 32,500 | 6.5x |

*Note: The BRD cites 4.2x conservative and 41.7x optimistic for banks. The 4.2x figure uses a different prevention rate assumption. The calculator uses 65% net prevention improvement as the default, adjustable by the user.*

**Display:**

| Element | Specification |
|---------|---------------|
| ROI ratio | Large number (48px, accent color), e.g., "6.5x ROI" |
| Annual cost breakdown | "Annual Cost: RM 30,000 (subscription) + RM 3,000 (API calls) = RM 33,000" |
| Estimated prevented loss | "Estimated Prevention: RM 195,000/year" |
| Comparison | "Without LAICIs: RM 500,000 lost. With LAICIs: RM 195,000 saved." |
| Payback period | "Payback: 2.0 months" |
| Color | ROI > 5x: green, ROI 2–5x: blue, ROI < 2x: yellow |

**UI Layout:**
- Card widget in the dashboard (right column, below scammer search)
- Input controls in top half (segment dropdown, volume slider, loss input, tier dropdown)
- Results display in bottom half (ROI ratio, cost breakdown, prevention estimate, comparison)
- "Save Calculation" button (stores to Financial Overview database for reference)
- "Export as PDF" button (generates a one-page ROI summary for procurement teams)

**User Story:**
*As a prospect evaluating LAICIs (Sarah's CFO), I want to input my company's annual fraud losses of RM 2 million, select the Professional tier at RM 30,000, and see that I'll save RM 1.3 million per year (6.5x ROI, 2-month payback) so I can justify the purchase to the board.*

**Acceptance Criteria:**
- Calculator produces ROI for all 5 customer segments
- Volume slider adjusts API call costs with correct volume discounts
- ROI ratio, cost breakdown, prevention estimate, and comparison all display simultaneously
- Payback period calculates correctly
- "Export as PDF" generates a downloadable one-page summary
- Calculations match the ROI reference table for pre-computed examples

---

### 5.5 Scenario Planner

**Description:**
A module that lets corporate security managers simulate hypothetical deepfake scenarios and get projected financial impact plus response playbooks. This is a planning tool, not a detection tool — it helps organizations prepare for deepfake incidents before they happen.

**Inputs:**

| Input | Type | Options / Range | Required |
|-------|------|-----------------|----------|
| Scenario type | Dropdown | Executive impersonation, Fake news video, Marketplace deepfake, Political disinformation | Yes |
| Target | Text input | Executive name, brand name, public figure name | Yes |
| Distribution channel | Dropdown | Social media, Email, Direct message, Broadcast media | Yes |
| Estimated audience reach | Slider | 1,000–1,000,000 | Yes |
| Segment | Dropdown | Bank, Corporate, Government, SME | Yes |

**Scenario Types and Exposure Models:**

**Executive Impersonation:**
- Anchor case: RM 122 million single-case loss (corporate executive impersonation via deepfake video call)
- Exposure model: RM 122M × (audience_reach / 1,000,000) × segment_multiplier
- Segment multipliers: Bank = 5.0, Corporate = 1.0, Government = 2.0, SME = 0.1
- Example: 500K audience, Corporate segment → RM 122M × 0.5 × 1.0 = RM 61M projected exposure

**Fake News Video:**
- Anchor: average brand damage from viral disinformation = RM 5M (estimated from Malaysian cases)
- Exposure model: RM 5M × (audience_reach / 100,000) × segment_multiplier
- Segment multipliers: Bank = 3.0, Corporate = 1.5, Government = 2.0, SME = 0.5
- Example: 200K audience, Corporate → RM 5M × 2.0 × 1.5 = RM 15M projected exposure

**Marketplace Deepfake:**
- Anchor: average marketplace scam loss = RM 1,500 per victim
- Exposure model: RM 1,500 × (audience_reach × 0.05 conversion rate)
- Example: 10,000 audience → RM 1,500 × 500 = RM 750,000 projected exposure

**Political Disinformation:**
- Anchor: estimated electoral/reputational impact = RM 10M (estimated)
- Exposure model: RM 10M × (audience_reach / 500,000)
- Example: 500K audience → RM 10M × 1.0 = RM 10M projected exposure

**Outputs:**

| Output Field | Type | Description |
|--------------|------|-------------|
| `projected_exposure_rm` | float | Projected financial exposure based on scenario parameters |
| `response_playbook` | list[dict] | Timed action items (see below) |
| `notification_template` | string | Pre-filled email/announcement template for stakeholders |
| `historical_precedents` | list[dict] | Similar past incidents with outcomes and lessons learned |

**Response Playbook Structure (timed action items):**

| Time Window | Actions |
|-------------|---------|
| Hours 0–4 (Immediate) | Verify authenticity with LAICIs scan, alert CISO/security team, contact PDRM CCID (03-26101599), preserve all evidence (screenshots, URLs, metadata) |
| Hours 4–48 (Short-term) | Issue takedown request to platform (social media/email provider), notify BNM FEN if financial fraud involved, file CMA Section 233 report with MCMC, notify CyberSecurity Malaysia (mycert@cybersecurity.my), draft public statement if needed |
| Days 1–30 (Long-term) | Conduct internal investigation, implement additional verification protocols, update employee training materials, brief board of directors, file insurance claim if applicable, track recovery through PDRM and bank channels |

**Notification Template:**
Pre-filled email template including: scenario description, projected exposure, immediate actions taken, stakeholder contact list, and next steps. User fills in company-specific details.

**Historical Precedents:**
- RM 122M corporate executive impersonation case (2024)
- 454 deepfake fraud cases H1 2024 (aggregate)
- Relevant OSINT-sourced cases from the Data knowledge base node

**UI Layout:**
- Dedicated tab in the dashboard: "Scenario Planner"
- Input form in left panel (scenario type, target, channel, audience, segment)
- Results display in right panel: projected exposure (large RM figure), response playbook (timeline), notification template (editable text area), historical precedents (list)
- "Save Scenario" button (stores to Financial Overview database)
- "Export Playbook as PDF" button

**User Story:**
*As a corporate security manager (Sarah), I want to simulate "what if a deepfake video of our CEO appears on TikTok reaching 500K viewers" and get a projected RM 61 million exposure plus a step-by-step response plan covering hours 0–4 (verify, alert, contact PDRM), hours 4–48 (takedown, file CMA report, notify CyberSecurity Malaysia), and days 1–30 (investigate, train, brief board).*

**Acceptance Criteria:**
- Scenario Planner produces `projected_exposure_rm` for all 4 scenario types
- Exposure calculations match the defined models for each scenario type
- Response playbook generates with all 3 time windows (0–4h, 4–48h, 1–30d)
- Playbook includes Malaysian regulatory contacts (PDRM CCID, BNM FEN, MCMC, CyberSecurity Malaysia)
- Notification template is pre-filled and editable
- Historical precedents are sourced from the Data knowledge base node

---

### 5.6 Recovery Assistant

**Description:**
A module that provides actionable recovery guidance when a deepfake incident is confirmed. Guidance is tailored to the confirmed scam type, financial exposure level, victim type, and time elapsed since the incident. This module transforms the Recovery Recommendation from the Financial Risk Assessor into a comprehensive, step-by-step recovery playbook.

**Inputs:**

| Input | Type | Source | Required |
|-------|------|--------|----------|
| Confirmed scam type | string | Financial Risk Assessor `scam_category` | Yes |
| Estimated financial exposure | float | Financial Risk Assessor `estimated_exposure_rm` | Yes |
| Victim type | string (individual/corporate/government) | User selection | Yes |
| Time since incident | string (hours/days) | User input | Yes |
| Scammer match | dict | Scammers database (if matched) | No |

**Outputs:**

| Output | Type | Description |
|--------|------|-------------|
| Immediate actions | list[string] | Actions to take immediately (freeze, report, preserve) |
| Regulatory filings | list[dict] | Required regulatory filings with deadlines |
| Evidence checklist | list[string] | Items to preserve for legal/investigation |
| Contact directory | dict | Malaysian regulatory and law enforcement contacts |
| Legal recourse options | list[string] | Legal actions available under Malaysian law |
| Insurance claim guidance | list[string] | Steps for insurance claims (if applicable) |

**Immediate Actions (by scam type):**

| Scam Type | Immediate Actions |
|-----------|-------------------|
| Investment scam | Freeze bank accounts, report to bank's fraud department, file report with BNM FEN, contact PDRM CCID, preserve all communication records and bank transfer receipts |
| Impersonation | Verify through secondary channel, freeze all outgoing transactions, contact PDRM CCID immediately, notify CyberSecurity Malaysia, preserve video/audio evidence |
| Romance scam | Freeze bank accounts, report to bank, file PDRM CCID report, preserve chat logs and transfer records, contact CyberSecurity Malaysia |
| Phishing | Change all passwords, enable 2FA, freeze affected accounts, report to bank, file MCMC report under CMA Section 233, preserve phishing emails/screenshots |
| Job scam | Cease all communication, report to bank if money transferred, file PDRM CCID report, report to Ministry of Human Resources, preserve job offer emails and WhatsApp messages |
| Marketplace fraud | Report to platform (Shopee/Carousell/etc.), file PDRM CCID report, contact bank for chargeback if applicable, preserve product listings and chat logs |

**Regulatory Filings:**

| Filing | Authority | Deadline | Description |
|--------|-----------|----------|-------------|
| Fraud notification | Bank Negara Malaysia (BNM) FEN | Within 24 hours | For financial fraud involving RM 50K+ |
| Police report | PDRM CCID | Within 48 hours | All confirmed scam cases |
| CMA Section 233 report | Malaysian Communications and Multimedia Commission (MCMC) | Within 72 hours | For deepfake content distributed online |
| PDPA notification | Department of Personal Data Protection | Within 72 hours | If personal data was breached |
| Cybersecurity incident | CyberSecurity Malaysia (MyCERT) | Within 24 hours | Report via mycert@cybersecurity.my or 1300-88-2999 |

**Evidence Preservation Checklist:**
- [ ] Original media file (image/video) — do not modify or recompress
- [ ] LAICIs scan report (detection score, risk tier, exposure estimate)
- [ ] Screenshots of all communications (WhatsApp, email, social media DMs)
- [ ] Bank transfer records (screenshots or PDF statements)
- [ ] URLs where deepfake content was distributed
- [ ] Metadata of media files (EXIF data, creation timestamps)
- [ ] Witness statements (if applicable)
- [ ] Audit trail export from LAICIs (chain-of-custody proof)

**Contact Directory:**

| Organization | Contact | Purpose |
|--------------|---------|---------|
| BNM Financial Intelligence and Enforcement Network (FEN) | 1-300-88-5465 | Financial fraud reporting |
| PDRM CCID Hotline | 03-26101599 | Commercial crime reporting |
| MCMC Complaints | aduanskmm@mcmc.gov.my | Online content complaints |
| CyberSecurity Malaysia (MyCERT) | mycert@cybersecurity.my / 1300-88-2999 | Cybersecurity incident reporting |
| Bank Negara Malaysia Teleduhan | 1-300-88-5465 | Financial dispute resolution |
| National Fraud Response Portal | 997 (call or SMS) | National scam reporting hotline |

**UI Layout:**
- Triggered from scan results when `is_ai_generated = true` and `risk_tier >= HIGH`
- "View Recovery Plan" button opens a modal or dedicated tab
- Sections: Immediate Actions (checkbox list), Regulatory Filings (table with deadlines), Evidence Checklist (checkbox list), Contact Directory (card grid), Legal Recourse (bullet list), Insurance Guidance (bullet list)
- "Export Recovery Plan as PDF" button — generates a printable recovery document
- "Export Evidence Checklist as PDF" button — for legal proceedings

**User Story:**
*As a bank fraud analyst (Aisha), when a confirmed deepfake case with RM 500K exposure is detected (impersonation category), I want a recovery plan that says: "1. Freeze all outgoing transactions immediately. 2. Report to BNM FEN within 24 hours (call 1-300-88-5465). 3. File PDRM CCID report within 48 hours (call 03-26101599). 4. File CMA Section 233 report with MCMC within 72 hours. 5. Contact CyberSecurity Malaysia at mycert@cybersecurity.my. 6. Preserve evidence: original media, LAICIs scan report, communication screenshots, bank transfer records." so I don't miss critical steps under pressure.*

**Acceptance Criteria:**
- Recovery Assistant provides actionable steps for all 7 confirmed scam types
- Regulatory filing deadlines are correct (BNM 24h, PDRM 48h, MCMC 72h, PDPA 72h, MyCERT 24h)
- Contact directory includes all 6 Malaysian contacts with correct phone numbers and emails
- Evidence checklist includes all 8 items
- "Export as PDF" generates a printable recovery plan
- Triggered automatically when risk tier >= HIGH

---

### 5.7 Financial Database Fields

#### 5.7.1 Scans Database Extension (15 → 22 fields)

**Description:**
Extend the existing Scans database (15 fields from v1.0) with 7 new financial fields to capture the financial intelligence output from the Financial Risk Assessor module.

**v1.0 Fields (15, retained):**

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | `scan_id` | string | Unique scan identifier |
| 2 | `scan_date` | datetime | Timestamp of scan execution |
| 3 | `media_type` | string | image / video |
| 4 | `media_filename` | string | Original filename (not stored file) |
| 5 | `has_faces` | boolean | Whether faces detected in media |
| 6 | `final_score` | float (0–1) | Weighted detection score |
| 7 | `is_ai_generated` | boolean | True if score >= 0.5 |
| 8 | `is_deepfake` | boolean | True if deepfake indicators detected |
| 9 | `method_used` | string | Scoring algorithm used |
| 10 | `component_scores` | JSON | Individual module scores |
| 11 | `ela_analysis` | JSON | ELA analysis details |
| 12 | `indicators` | JSON | Detection indicators list |
| 13 | `recommendation` | string | Text recommendation |
| 14 | `context` | string | User-provided context |
| 15 | `user_id` | string | User who performed scan |

**v2.0 NEW Fields (7, financial):**

| # | Field | Type | Description | Source |
|---|-------|------|-------------|--------|
| 16 | `risk_tier` | string | LOW / MODERATE / HIGH / CRITICAL | Financial Risk Assessor |
| 17 | `estimated_exposure_rm` | float | Estimated monetary exposure in RM | Financial Risk Assessor |
| 18 | `scam_category` | string | job/investment/romance/phishing/impersonation/marketplace/other | Financial Risk Assessor |
| 19 | `prevention_value_rm` | float | Estimated value of detecting this scam (25% of category average) | Financial Risk Assessor |
| 20 | `scammer_match_id` | string | Linked record ID from Scammers database (null if no match) | Scammers DB cross-ref |
| 21 | `segment` | string | bank/corporate/government/sme/individual | User selection |
| 22 | `recovery_action_taken` | string | Summary of recovery actions taken (user-filled after Recovery Assistant) | User input |

#### 5.7.2 Scammers Database Extension (11 → 16 fields)

**Description:**
Extend the existing Scammers database (11 fields from v1.0) with 5 new financial fields to capture historical loss data for identified scammers, enabling cross-referencing during financial risk assessment.

**v1.0 Fields (11, retained):**

| # | Field | Type | Description |
|---|-------|------|-------------|
| 1 | `scammer_id` | string | Unique scammer identifier |
| 2 | `email` | string | Email address (if known) |
| 3 | `phone` | string | Phone number (if known) |
| 4 | `website` | string | Website URL (if known) |
| 5 | `social_media` | JSON | Social media accounts |
| 6 | `scam_type` | string | Primary scam type |
| 7 | `first_reported` | date | First reported date |
| 8 | `last_seen` | date | Most recent activity date |
| 9 | `reports_count` | integer | Number of reports filed |
| 10 | `source` | string | Source of information |
| 11 | `notes` | string | Additional notes |

**v2.0 NEW Fields (5, financial):**

| # | Field | Type | Description | Source |
|---|-------|------|-------------|--------|
| 12 | `total_known_losses_rm` | float | Cumulative losses attributed to this scammer across all known cases | Case aggregation |
| 13 | `average_loss_per_case_rm` | float | Average loss per incident (`total_known_losses_rm` / `case_count`) | Computed |
| 14 | `case_count` | integer | Number of confirmed cases involving this scammer | Case aggregation |
| 15 | `first_seen_date` | date | Earliest recorded activity (may differ from `first_reported`) | Historical data |
| 16 | `risk_level` | string | LOW / MEDIUM / HIGH / CRITICAL (based on cumulative losses) | Computed |

**Risk Level Calculation for Scammers:**

| Total Known Losses (RM) | Risk Level |
|------------------------|------------|
| < 1,000 | LOW |
| 1,000–10,000 | MEDIUM |
| 10,000–100,000 | HIGH |
| > 100,000 | CRITICAL |

#### 5.7.3 Financial Overview Database (NEW — 9 fields)

**Description:**
A new library database that aggregates financial intelligence across all scans and scammers for dashboard display, reporting, and trend analysis. Updated after every scan and by the OSINT automation pipeline.

| # | Field | Type | Description | Update Trigger |
|---|-------|------|-------------|----------------|
| 1 | `date` | date | Aggregation date (daily entry) | Daily at midnight |
| 2 | `total_scans` | integer | Total scans performed (cumulative) | After each scan |
| 3 | `total_deepfakes_detected` | integer | Total deepfakes detected (cumulative) | After each scan with `is_ai_generated=true` |
| 4 | `total_prevented_loss_rm` | float | Cumulative prevention value | After each scan with prevention_value_rm |
| 5 | `total_estimated_exposure_rm` | float | Cumulative estimated exposure detected | After each scan with estimated_exposure_rm |
| 6 | `scam_breakdown` | JSON | `{scam_type: count}` breakdown | After each scan |
| 7 | `segment_breakdown` | JSON | `{segment: count}` breakdown | After each scan |
| 8 | `new_scammers_identified` | integer | New scammers added today | After scammer DB update |
| 9 | `osint_updates` | integer | Number of OSINT data points added today | After OSINT pipeline run |

**User Story:**
*As a data analyst (Dev), I want the Financial Overview database to aggregate all scan data daily so I can query trends like "how has the average prevention value per scan changed over the last 30 days" and export the results as CSV for my client report.*

**Acceptance Criteria (all database fields):**
- Scans database has all 22 fields (15 original + 7 new financial fields)
- Scammers database has all 16 fields (11 original + 5 new financial fields)
- Financial Overview database has all 9 fields and is updated after every scan
- Risk level for scammers is computed correctly from total_known_losses_rm
- Prevention value (field 19) equals 25% of the scam category average loss
- All financial fields are populated by the Financial Risk Assessor during Step 7 of the workflow

---

### 5.8 Financial Knowledge Base Node

**Description:**
The Finance knowledge base node in the WorkBuddy Library is populated with structured, queryable content covering pricing, ROI, cost structures, and revenue scenarios. This content is the source for RAG-powered Q&A and provides the financial intelligence foundation for the platform.

**Content Structure:**

**Section 1: Pricing Tiers**

| Tier | Price Range | Target Segment | Key Deliverables |
|------|-------------|----------------|------------------|
| Enterprise | RM 50,000–250,000/yr | Banks & Financial | Full platform, API, compliance, audit trail, dedicated support |
| Professional | RM 15,000–50,000/yr | Corporate Enterprise | Dashboard, financial risk, scenario planner, compliance reports |
| Starter | RM 3,000–15,000/yr | SME & Professional | Dashboard, scan history, CSV export, scammer search |
| API | RM 0.50–2.00/detection | Platform Integrators | REST API, webhooks, rate-limited endpoints |
| Government | Custom | Government & Regulatory | Full platform, OSINT automation, inter-agency sharing |

Volume discounts: 10K+/mo = 15% off, 50K+/mo = 25% off, 100K+/mo = 35% off + priority support.

**Section 2: ROI Calculations**
- Bank (conservative): RM 100K investment → RM 420K prevention = 4.2x ROI
- Bank (optimistic): RM 100K investment → RM 4,170K prevention = 41.7x ROI (based on RM 122M single-case loss)
- Corporate: RM 30K investment → RM 150K prevention = 5.0x ROI
- Government: RM 200K investment → RM 2,000K prevention = 10.0x ROI
- SME (per scan): RM 50 investment → RM 500 prevention = 10.0x ROI
- The 41.7x optimistic ROI averages the RM 122M single-case loss across a portfolio of incidents.

**Section 3: Cost Structure (3-Year)**

| Cost Category | Year 1 | Year 2 | Year 3 |
|---------------|--------|--------|--------|
| Personnel (4→8 FTE) | RM 960K | RM 1,440K | RM 2,400K |
| Infrastructure | RM 120K | RM 180K | RM 280K |
| API Costs | RM 240K | RM 420K | RM 720K |
| Marketing & Sales | RM 180K | RM 320K | RM 560K |
| Legal & Compliance | RM 80K | RM 140K | RM 240K |
| R&D / Model Training | RM 50K | RM 90K | RM 160K |
| Office & Operations | RM 0 | RM 80K | RM 130K |
| Contingency (10%) | RM 161K | RM 265K | RM 449K |
| **Total** | **RM 1,791K** | **RM 2,935K** | **RM 4,939K** |

**Section 4: Revenue Scenarios**
- Conservative 3-year cumulative: RM 2.96M (no break-even)
- Base 3-year cumulative: RM 5.37M (break-even Year 3)
- Optimistic 3-year cumulative: RM 8.07M (break-even Year 2)
- Base Year 3 revenue mix: Enterprise 52%, Professional 26%, Starter 15%, API 5%, Government 2%

**Section 5: Break-Even Analysis**
- Base case: Year 3 (RM 2.9M revenue approaches RM 4.94M cost with partial recognition)
- Optimistic: Year 2 (RM 2.48M revenue vs RM 2.94M cost — near break-even)
- Conservative: No break-even within 3 years without additional funding

**Section 6: Malaysian Market Sizing**
- Total scam losses 2023–2025: RM 5.62 billion
- Deepfake cases H1 2024: 454 (76% YoY increase)
- Deepfake losses H1 2024: RM 2.72 million
- Largest single case: RM 122 million
- Victim belief rate: 85%
- National recovery rate: 2%
- Average loss per deepfake case: RM 5,991

**Queryability:**
- All content is indexed by the WorkBuddy Library RAG search engine (`rag_search.py`)
- Users can ask natural language questions and get answers with source citations
- Content is structured with clear headings for chunk-level retrieval
- Updated when OSINT pipeline discovers new financial data
- Accessible to all roles via the RAG Q&A interface

**Example RAG Queries:**
- "What is the ROI for banks using LAICIs?" → "Banks can expect 4.2x conservative to 41.7x optimistic ROI. Source: Finance Knowledge Base, ROI Calculations section."
- "What is the break-even point?" → "Base case break-even is Year 3. Optimistic case is Year 2. Source: Finance Knowledge Base, Break-Even Analysis section."
- "How much did Malaysians lose to scams?" → "RM 5.62 billion from 2023 to 2025. Source: Finance Knowledge Base, Malaysian Market Sizing section."

**User Story:**
*As a data analyst (Dev), I want to ask the knowledge base "What are LAICIs's pricing tiers?" and get a structured answer with all 5 tiers, price ranges, and target segments, with a citation to the Finance Knowledge Base, so I can include accurate pricing in my client proposal.*

**Acceptance Criteria:**
- Finance knowledge base node contains all 6 sections with complete content
- Content is structured with clear headings for RAG chunk-level retrieval
- RAG search returns answers with source citations for 80%+ of financial queries
- Content is updated when OSINT pipeline discovers new financial data
- All 7 market statistics from the Market Intelligence Panel are present in the node

---

## 6. DATA Feature Specifications

This section specifies all 7 data features in detail. Each specification includes description, capabilities, UI elements, data flow, and user stories.

---

### 6.1 Self-Service Data Query Portal

**Description:**
A dashboard-integrated portal where data users can query scan results and scammer data without developer assistance. Supports filtering, sorting, aggregation, pagination, and export. This eliminates the IT bottleneck for data access and empowers analysts to self-serve their reporting needs.

**Capabilities:**

**Scan Filtering:**

| Filter | Type | Options | UI Element |
|--------|------|---------|------------|
| Date range | Date range picker | From / To (DD/MM/YYYY) | Dual date picker |
| Media type | Dropdown | All / Image / Video | Select dropdown |
| Score range | Dual slider | 0.0–1.0 (min, max) | Range slider |
| Risk tier | Multi-select | LOW / MODERATE / HIGH / CRITICAL | Checkbox group |
| Scam category | Multi-select | job/investment/romance/phishing/impersonation/marketplace/other | Checkbox group |
| Is AI generated | Toggle | All / Yes / No | Toggle switch |
| Segment | Multi-select | bank/corporate/government/sme/individual | Checkbox group |
| Has scammer match | Toggle | All / Yes / No | Toggle switch |

**Scammer Filtering:**

| Filter | Type | Options | UI Element |
|--------|------|---------|------------|
| Email | Text input | Partial match (contains) | Text field |
| Phone | Text input | Partial match (contains) | Text field |
| Website | Text input | Partial match (contains) | Text field |
| Scam type | Dropdown | All / job / investment / romance / phishing / impersonation / marketplace / other | Select dropdown |
| Risk level | Multi-select | LOW / MEDIUM / HIGH / CRITICAL | Checkbox group |
| First seen date | Date range picker | From / To | Dual date picker |

**Sorting:**
- Sort by any column, ascending or descending
- Click column header to toggle sort direction
- Default sort: scan_date descending (newest first) for scans, reports_count descending for scammers

**Pagination:**
- 50 records per page
- Page navigation: First, Prev, [page numbers], Next, Last
- "Showing X–Y of Z records" display
- "Page X of N" indicator
- Jump-to-page input field

**Aggregation (summary view):**
- Count: total records matching filter
- Sum: total estimated_exposure_rm, total prevention_value_rm
- Average: average final_score, average estimated_exposure_rm
- Group by: day, week, month, scam type, segment, risk tier

**UI Layout:**
- Tab: "Data Portal" in the dashboard navigation
- Sub-tabs: "Query Scans" | "Query Scammers"
- Left sidebar (25% width): filter controls (dropdowns, sliders, date pickers, toggles)
- Main area (75% width): results table (paginated, sortable)
- Top bar: "Export CSV" and "Export JSON" buttons, record count display
- Bottom bar: pagination controls
- "Aggregation View" toggle: switches between table view and summary statistics view

**Data Flow:**
1. User selects filters in the left sidebar
2. Frontend sends query parameters to the database via `__SMART_PAGE__.database` runtime signal
3. WorkBuddy Library database returns filtered, sorted, paginated results
4. Results render in the table with 50 records per page
5. User clicks "Export CSV" or "Export JSON" — frontend generates file from current query results
6. All queries are logged to the audit trail (actor, action="query", target="scans_db", result="success")

**User Story:**
*As a data analyst (Dev), I want to filter scans from January 2026 where risk_tier=CRITICAL and scam_category=impersonation, see the results in a paginated table (50 per page), and export the 127 matching records as CSV for my monthly fraud trend report — all without asking a developer to write a custom query.*

**Acceptance Criteria:**
- Data portal supports filtering by all Scans database fields (22 fields)
- Data portal supports filtering by all Scammers database fields (16 fields)
- Results are paginated at 50 records per page
- Sorting works on all columns (ascending and descending)
- Aggregation view shows count, sum, and average for numeric fields
- Export CSV and Export JSON buttons produce valid files with all filtered records
- All queries are logged to the audit trail
- Query response time < 5 seconds for up to 10,000 records

---

### 6.2 RAG-Powered Knowledge Base Q&A

**Description:**
A natural-language Q&A interface over the Data and Finance knowledge base nodes in the WorkBuddy Library. Users ask questions in plain English (or Bahasa Malaysia in Phase 4) and get answers with source citations. This eliminates the need to read lengthy reports and makes the accumulated intelligence accessible to non-technical users.

**Underlying Technology:**
- WorkBuddy Library's built-in RAG search engine (`rag_search.py`)
- Chunk-level semantic retrieval with embedding and rerank
- Index: all content in the Data and Finance knowledge base nodes
- Output: answer text + source citation (document name, section)

**Content Sources (populated knowledge base nodes):**
- **Data node:** Malaysian scam statistics (RM 5.62B total losses, 454 deepfake cases, 76% YoY increase, 85% belief rate, 2% recovery rate), deepfake case data, recovery rates, victim demographics, trend analysis, OSINT-sourced daily scam news
- **Finance node:** Pricing tiers (5 tiers from Starter to Enterprise+), ROI calculations (4.2x–41.7x for banks), cost structures (3-year projections), revenue scenarios (conservative/base/optimistic), break-even analysis (Year 2–3), customer segment financials

**UI Layout:**
- Tab: "Ask the Knowledge Base" in the Data Portal section
- Chat-style interface: message history (user questions + system answers) stacked vertically
- Input box at bottom: "Ask anything about Malaysian scams, deepfake statistics, LAICIs pricing, or ROI..."
- "Send" button (or press Enter)
- Each answer includes: answer paragraph, "Source: [document name, section]" citation, confidence indicator (high/medium/low)
- Suggested questions displayed below the input box as clickable chips

**Suggested Questions (default display):**
1. "How much did Malaysians lose to scams in 2023–2025?"
2. "How many deepfake cases were reported in H1 2024?"
3. "What is the ROI for banks using LAICIs?"
4. "What is the national recovery rate for scam losses?"
5. "What are LAICIs's pricing tiers?"
6. "What is the largest single deepfake fraud case in Malaysia?"
7. "What is the year-over-year increase in deepfake cases?"
8. "What is LAICIs's break-even point?"

**Example Interactions:**

**Interaction 1:**
- User: "How much did Malaysians lose to scams in 2023–2025?"
- System: "Malaysians lost RM 5.62 billion to scams from 2023 to 2025, according to PDRM CCID and Bank Negara Malaysia SFMS statistics. Of this, RM 5.51 billion (98%) is permanently unrecovered due to the 2% national recovery rate. Source: Data Knowledge Base, Malaysian Scam Statistics section."

**Interaction 2:**
- User: "What's the ROI for a bank using LAICIs?"
- System: "Banks can expect a 4.2x ROI (conservative) to 41.7x ROI (optimistic) when using LAICIs. The conservative figure assumes RM 100K annual investment preventing RM 420K in fraud. The 41.7x optimistic figure is grounded in the RM 122 million single-case corporate loss: if LAICIs prevents one such incident at RM 250K annual subscription, the ROI is 488x for that year. Source: Finance Knowledge Base, ROI Calculations section."

**Interaction 3:**
- User: "What's the trend in deepfake cases year over year?"
- System: "Deepfake fraud cases increased 76% year-over-year, from 258 cases in H1 2023 to 454 cases in H1 2024. This trend is expected to accelerate as generative AI tools become more accessible. Source: Data Knowledge Base, Deepfake Case Trends section."

**Interaction 4:**
- User: "What should I do if I've been scammed?"
- System: "If you've been scammed: (1) Freeze your bank accounts immediately by calling your bank's fraud hotline. (2) Report to PDRM CCID at 03-26101599 within 48 hours. (3) Report to BNM FEN at 1-300-88-5465 within 24 hours if the loss exceeds RM 50,000. (4) File a CMA Section 233 report with MCMC at aduanskmm@mcmc.gov.my within 72 hours. (5) Contact CyberSecurity Malaysia at mycert@cybersecurity.my. (6) Preserve all evidence: original media, communication screenshots, bank transfer records. Source: Data Knowledge Base, Recovery Guidance section."

**Performance:**
- RAG Q&A response time: < 10 seconds for knowledge base queries
- Relevance target: 85%+ of answers rated as relevant by users
- Coverage: 80%+ of questions about content in the knowledge base return answers with citations

**Data Flow:**
1. User types a natural language question in the chat interface
2. Frontend sends the question to `rag_search.py` via the WorkBuddy Library SDK
3. RAG engine performs chunk-level semantic retrieval with embedding and rerank across the Data and Finance knowledge base nodes
4. Engine returns the best-matching answer text plus source citation
5. Frontend displays the answer with citation and suggested follow-up questions
6. Query and answer are logged to the audit trail (actor, action="rag_query", target="data_kb/finance_kb", result="success")

**User Story:**
*As a police officer (Rahman), I want to ask "What's the trend in deepfake cases year over year?" and get "76% increase year-over-year, from 258 cases in H1 2023 to 454 cases in H1 2024. Source: Data Knowledge Base" without reading the full 116KB research report — so I can include the statistic in my intelligence briefing at Bukit Aman.*

**Acceptance Criteria:**
- RAG Q&A returns answers with source citations for 80%+ of queries about knowledge base content
- Response time < 10 seconds per query
- 8 suggested questions are displayed by default
- Both Data and Finance knowledge base nodes are indexed and searchable
- Answers include specific RM figures and percentages from the source content
- All RAG queries are logged to the audit trail
- Confidence indicator (high/medium/low) is displayed with each answer

---

### 6.3 Automated OSINT Data Pipeline

**Description:**
An automated data pipeline that runs daily at 9 AM to collect OSINT (Open Source Intelligence) on Malaysian scams and deepfakes, extract structured data, and append it to the Data knowledge base node and update the Financial Overview database. This ensures the platform's intelligence is always current without manual research effort.

**Pipeline Architecture:**

| Step | Action | Technology | Output |
|------|--------|------------|--------|
| 1 | WebSearch for latest Malaysian scam news and deepfake incidents | WorkBuddy WebSearch tool | Raw search results (headlines, URLs, snippets) |
| 2 | Extract key data points: loss amounts, case counts, scam types, dates, locations | LLM extraction (Gemini or WorkBuddy Cloud Service) | Structured JSON: `[{date, title, source, loss_rm, cases, scam_type, location, summary}]` |
| 3 | Structure as formatted markdown with headings | Python string formatting | Markdown document chunk |
| 4 | Append to Data knowledge base node in the WorkBuddy Library | `submit_doc_edit.py` script | Updated Data node content |
| 5 | Update Financial Overview database with new aggregate figures | Database API | Updated Financial Overview record |
| 6 | Update Market Intelligence Panel statistics | `__SMART_PAGE__.database` runtime signal | Refreshed dashboard statistics |
| 7 | Log pipeline execution to audit trail | Audit trail logging | Audit trail entry (actor="system", action="osint_update") |

**Search Queries (executed at 9 AM daily):**
- "Malaysia scam news today"
- "Malaysia deepfake fraud case"
- "Malaysia online scam loss RM"
- "Bukit Aman CCID scam statistics"
- "Bank Negara Malaysia fraud alert"
- "MCMC deepfake complaint Malaysia"

**Scheduling:**
- Automation type: Recurring (daily)
- Schedule: Every day at 9:00 AM Malaysia time (UTC+8)
- Existing automation ID: 2453f597-10da-4990-9203-06669db4c19d
- Manual trigger: "Run OSINT Scan Now" button on the dashboard (in the Data Portal tab)
- Manual trigger is available to Admin and Analyst roles only

**Data Extraction Schema:**
Each extracted OSINT data point is structured as:

| Field | Type | Description |
|-------|------|-------------|
| `date` | date | Date of the news article or incident |
| `title` | string | Headline or title |
| `source` | string | News outlet or official source |
| `loss_rm` | float | Loss amount in RM (if mentioned) |
| `cases` | integer | Number of cases (if mentioned) |
| `scam_type` | string | Categorized scam type |
| `location` | string | Malaysian state/city (if mentioned) |
| `summary` | string | Brief summary of the incident |
| `url` | string | Source URL |

**UI Elements:**
- "Run OSINT Scan Now" button in the Data Portal tab (Admin and Analyst roles only)
- OSINT status indicator: "Last OSINT run: [date] at 9:00 AM — X data points added"
- OSINT log: table of recent OSINT runs with date, data points collected, status (success/failure)
- "View OSINT Data" link: opens the Data knowledge base node in a reader view

**Failure Handling:**
- If WebSearch fails: retry 3 times with 5-second intervals, log failure to audit trail
- If extraction fails: log raw search results without structured extraction, flag for manual review
- If database update fails: queue update for next successful run, log to audit trail
- Pipeline failure does not affect any other platform functionality

**User Story:**
*As a police officer (Rahman), I want the knowledge base to automatically update with the latest Malaysian scam news every morning at 9 AM so that when I query "What are the latest scam trends?", the RAG Q&A returns current data from yesterday's news — not stale data from last month's report.*

**Acceptance Criteria:**
- OSINT automation runs daily at 9 AM Malaysia time
- Pipeline extracts structured data (loss amounts, case counts, scam types, dates)
- Extracted data is appended to the Data knowledge base node
- Financial Overview database is updated with new aggregate figures
- Market Intelligence Panel statistics refresh after OSINT run
- "Run OSINT Scan Now" button works for manual triggering
- Pipeline execution is logged to the audit trail (actor="system", action="osint_update")
- Failure handling: 3 retries on WebSearch failure, audit trail entry on any failure

---

### 6.4 Populated Data & Finance Knowledge Base Nodes

**Description:**
Both the Data and Finance knowledge base nodes in the WorkBuddy Library are populated with structured, queryable content. This content is the foundation for RAG-powered Q&A, the Market Intelligence Panel, and the data user self-service portal. Content is structured with clear headings for chunk-level semantic retrieval.

#### Data Knowledge Base Node Content

**Section 1: Malaysian Scam Statistics (2023–2025)**
- Total losses: RM 5.62 billion across all scam categories from 2023 to 2025
- Macau Scam and phone scams dominate volume
- Investment scams (often deepfake-assisted) represent the highest per-case value
- AUH (Authentication Under Hand) and parcel scams remain persistent
- E-commerce scams growing with platform adoption
- Sources: PDRM CCID, BNM SFMS, Royal Malaysia Police Bukit Aman

**Section 2: Deepfake-Specific Impact (H1 2024)**
- 454 confirmed deepfake fraud cases in 6 months (Jan–Jun 2024)
- RM 2.72 million in direct losses
- 76% year-over-year increase in case volume (258 cases H1 2023 → 454 cases H1 2024)
- Single largest case: RM 122 million (corporate executive impersonation)
- Average loss per deepfake case: RM 5,991 (RM 2.72M / 454 cases)
- 85% of victims believed the deepfake content was authentic at time of transaction
- Sources: Bukit Aman CCID, Sumsub, LAICIs Research Report (25 sources)

**Section 3: Recovery Gap**
- National scam recovery rate: 2% (RM 0.02 recovered per RM 1.00 lost)
- RM 5.51 billion of RM 5.62 billion total is permanently unrecovered
- This gap represents the primary value proposition: prevention is the only viable strategy
- Recovery is higher for cases reported within 24 hours (estimated 5–8%) vs. after 7 days (< 1%)

**Section 4: Global Context**
- FBI reported 126% increase in deepfake-related complaints (US, 2023–2024)
- Sumsub detected 10x increase in deepfakes in identity verification (2023)
- Sensity AI tracked 500M deepfake videos online by mid-2024
- Deloitte predicted 30–40% of social media content could be AI-generated by 2026
- Gartner: deepfake detection market reaching USD 1.8 billion by 2027

**Section 5: Regulatory Environment**
- PDPA 2010 (Personal Data Protection Act): Organizations must protect personal data including biometric data
- CMA 1998 (Communications and Multimedia Act): Section 233 criminalizes offensive content including deepfake impersonation
- BNM RMCD Guidelines: Financial institutions required to implement fraud detection
- Proposed Anti-Deepfake Legislation: Malaysian government announced intent for 2025–2026
- Bursa Malaysia Listing Requirements: Public-listed companies must disclose material fraud incidents

**Section 6: Recovery Guidance**
- Immediate actions by scam type (freeze accounts, report to authorities, preserve evidence)
- Regulatory filing deadlines (BNM 24h, PDRM 48h, MCMC 72h, PDPA 72h, MyCERT 24h)
- Contact directory: BNM FEN (1-300-88-5465), PDRM CCID (03-26101599), MCMC (aduanskmm@mcmc.gov.my), CyberSecurity Malaysia (mycert@cybersecurity.my / 1300-88-2999), National Fraud Hotline (997)
- Evidence preservation checklist (8 items)

**Section 7: OSINT Daily Feed (auto-appended)**
- Daily OSINT data points from the automated pipeline (Section 6.3)
- Structured as chronological entries with date, title, source, loss amount, cases, scam type, location, summary, URL
- Accumulates over time, providing a longitudinal record of Malaysian scam incidents

#### Finance Knowledge Base Node Content

Full content detailed in Section 5.8 — Financial Knowledge Base Node specification. Contains: Pricing Tiers, ROI Calculations, Cost Structure, Revenue Scenarios, Break-Even Analysis, and Malaysian Market Sizing.

**Queryability:**
- Both nodes are indexed by `rag_search.py` for chunk-level semantic retrieval
- Content uses clear hierarchical headings (H2, H3) for optimal chunk boundaries
- Tables are formatted as bullet lists where possible (WorkBuddy Library constraint: large GFM tables cause 524 timeouts)
- Content is accessible to all roles via RAG Q&A interface
- Content is accessible via CSV/JSON export from the self-service data portal

**User Story:**
*As a data analyst (Dev), I want both knowledge base nodes to contain structured, queryable content so that when I ask the RAG Q&A "What is the victim belief rate for deepfakes?", I get "85% of victims believed the deepfake content was authentic at time of transaction. Source: Data Knowledge Base, Deepfake-Specific Impact section." — with the specific statistic and citation, not a generic response.*

**Acceptance Criteria:**
- Data knowledge base node contains all 7 sections with complete content
- Finance knowledge base node contains all 6 sections with complete content
- All 7 market statistics are present in the Data node
- All pricing tiers and ROI figures are present in the Finance node
- Content is structured with clear headings for RAG chunk-level retrieval
- RAG search returns answers with source citations for 80%+ of queries
- OSINT daily feed appends to the Data node automatically

---

### 6.5 Database ↔ Dashboard Sync

**Description:**
Real-time synchronization between the WorkBuddy Library databases (Scans, Scammers, Financial Overview) and the dashboard frontend. When a scan completes, the dashboard header counters, scan history table, and loss prevention tracker update without a page reload. This is implemented using WorkBuddy's page↔database relation bindings and `__SMART_PAGE__.database` runtime signals.

**Implementation Architecture:**

| Component | Technology | Purpose |
|-----------|------------|---------|
| Page↔database relation bindings | WorkBuddy Sites page configuration | Binds dashboard HTML elements to database fields |
| `__SMART_PAGE__.database` | Runtime signal in published page | Provides real-time database access to frontend JavaScript |
| Dashboard JavaScript | Vanilla JS event handlers | Listens for database changes and updates UI elements |
| Library database API | `space_api.py` + module scripts | Backend CRUD operations on databases |

**Synced Elements:**

| Dashboard Element | Source Database | Source Field | Sync Trigger |
|-------------------|----------------|-------------|--------------|
| Total Scans stat pill | Scans DB | count(scan_id) | New scan inserted |
| Deepfakes Found stat pill | Scans DB | count(is_ai_generated=true) | New scan with deepfake |
| Scammers ID'd stat pill | Scammers DB | count(scammer_id) | New scammer inserted |
| Loss Prevented counter | Financial Overview DB | total_prevented_loss_rm | New scan with prevention_value |
| Risk Tier Breakdown bar | Scans DB | group by risk_tier | New scan inserted |
| Scan History table | Scans DB | latest 10 records | New scan inserted |
| Scammer Search results | Scammers DB | filtered by query | Search query or new scammer |
| Market Intelligence Panel | Financial Overview DB | aggregate fields | OSINT update or new scan |
| Component Status | Runtime check | module availability | Page load |

**Data Flow:**
1. User performs a scan → workflow completes Step 7 → scan record inserted into Scans DB
2. Financial Overview DB updated with new aggregate figures
3. `__SMART_PAGE__.database` runtime signal detects database change
4. Dashboard JavaScript receives signal and updates: Total Scans counter increments, Deepfakes Found counter increments if applicable, Loss Prevented counter adds prevention_value_rm, Risk Tier Breakdown bar updates, Scan History table prepends new record
5. If scammer identified: Scammers DB updated → Scammers ID'd counter increments
6. All updates happen within 5 seconds of scan completion
7. No page reload required — all updates are incremental

**User Story:**
*As a bank fraud analyst (Aisha), when I complete a scan that detects a CRITICAL risk deepfake, I want the dashboard header to immediately update: Total Scans +1, Deepfakes Found +1, Loss Prevented +RM 30,500, and the new scan to appear at the top of the Scan History table — all without refreshing the page, so I can continue my workflow without interruption.*

**Acceptance Criteria:**
- Dashboard header counters update within 5 seconds of scan completion
- Scan History table prepends new records without page reload
- Loss Prevention Tracker updates with new prevention value
- Market Intelligence Panel refreshes after OSINT pipeline run
- Page↔database relation bindings are configured for all synced elements
- `__SMART_PAGE__.database` runtime signal is functional in the published dashboard
- No manual refresh required for any database-backed dashboard element

---

### 6.6 Data Export (CSV/JSON)

**Description:**
Any query result in the self-service data portal can be exported as CSV or JSON with one click. This enables data users to use LAICIs data in external tools (Excel, Python, R, Tableau) without developer assistance.

**Export Formats:**

| Format | MIME Type | Use Case |
|--------|-----------|----------|
| CSV | text/csv | Excel import, BI tools, regulatory submissions |
| JSON | application/json | Python/JavaScript integration, API-style consumption |

**Export Capabilities:**

| Capability | Specification |
|------------|---------------|
| Export scope | Current filtered query result (respects all active filters) |
| Export limit | Up to 10,000 records per export |
| CSV format | Standard CSV with header row, UTF-8 encoding, comma-delimited |
| JSON format | Array of objects, UTF-8 encoding, pretty-printed with 2-space indent |
| Filename convention | `laici_[scans/scammers]_[date]_[time].[csv/json]` |
| File delivery | Browser download (no server-side storage of exports) |
| Export logging | Every export logged to audit trail (actor, action="export", target, result) |

**Export Button Behavior:**
1. User applies filters in the data portal
2. User clicks "Export CSV" or "Export JSON"
3. Frontend fetches all matching records (up to 10,000) from the database via `__SMART_PAGE__.database`
4. Frontend generates the file in-browser (no server round-trip)
5. Browser triggers file download with the standard filename convention
6. Export action is logged to the audit trail with: timestamp, actor, action="export", target="scans_db" or "scammers_db", result="success", record_count

**UI Elements:**
- "Export CSV" button (green icon) in the data portal top bar
- "Export JSON" button (blue icon) in the data portal top bar
- Export count display: "Exporting X records..."
- Success notification: "Exported X records to laici_scans_20260115_1030.csv"
- Error notification (if > 10,000 records): "Too many records (X). Please narrow your filter to 10,000 or fewer."

**User Story:**
*As a data analyst (Dev), I want to export all CRITICAL risk scans from January 2026 as CSV with one click, get a file with all 127 matching records including all 22 database fields, and open it in Excel for my monthly fraud trend report — without filing a ticket with IT.*

**Acceptance Criteria:**
- CSV export produces valid CSV with header row and all filtered records
- JSON export produces valid JSON array with all filtered records
- Export respects all active filters in the data portal
- Export supports up to 10,000 records per export
- Filename follows the `laici_[type]_[date]_[time].[format]` convention
- Export is generated in-browser (no server round-trip)
- Every export is logged to the audit trail
- Export response time < 10 seconds for up to 5,000 records

---

### 6.7 Data Governance

**Description:**
Data governance policies ensuring responsible data management across the platform. Covers retention, data minimization, PII protection, consent management, and data lifecycle. These policies ensure PDPA compliance and build user trust.

**Retention Policy:**

| Data Type | Retention Period | Rationale | Disposal Method |
|-----------|-----------------|-----------|-----------------|
| Scan metadata (Scans DB) | Indefinite | Historical analysis, trend detection, audit trail | Never deleted (append-only) |
| Scammer profiles (Scammers DB) | Indefinite | Cross-referencing future scans, ongoing threat | Never deleted (append-only) |
| Financial Overview | Indefinite | Longitudinal trend analysis | Never deleted (append-only) |
| Knowledge base content | Indefinite | Accumulating intelligence | Never deleted (append-only) |
| Audit trail | 7 years | Regulatory compliance (PDPA, BNM, evidence retention) | Archived after 7 years |
| Media files (uploaded) | NOT stored | Privacy protection (PDPA) — processed in-memory, discarded | Deleted immediately after processing |
| OSINT raw data | 90 days raw, aggregated indefinitely | Storage efficiency | Raw entries purged after 90 days |
| Session data | 30 minutes (session timeout) | Security | Automatically cleared on timeout |

**Data Minimization Principles:**
1. **Collect only what is needed:** The Scans database stores metadata (filename, type, score) — not the media file itself. Media is processed in-memory and discarded immediately after detection.
2. **No PII without consent:** Scan metadata is anonymized — no names, ID numbers, or personal identifiers are stored. Only a `user_id` (platform identifier) is recorded for audit purposes.
3. **Aggregation preference:** The Financial Overview database stores aggregate statistics (counts, sums) rather than individual records, minimizing exposure of detailed transaction data.
4. **Purpose limitation:** Each data field has a defined purpose documented in the PRD. No field is collected "just in case."
5. **Access minimization:** RBAC ensures users see only the data their role permits. Viewer role cannot export data. API User role cannot access dashboard data.

**PII Protection:**
- No biometric data (face images, voice recordings) is stored persistently
- Uploaded media files are processed in-memory/temp files and discarded after detection
- Scammer database contains contact information (email, phone, website) that is publicly reported or OSINT-sourced — not private personal data
- No Malaysian ID numbers (IC/MyKad), bank account numbers, or credit card numbers are stored in any database
- User consent is required for scan logging — users are informed that scan metadata will be recorded

**Consent Management:**
- Upload zone displays: "By uploading media, you consent to LAICIs processing this file for deepfake detection and recording anonymized scan metadata. Your media file is not stored permanently."
- Users can opt out of scan logging (scan runs but metadata is not persisted) — available to Admin role only
- Scammer database entries are sourced from public reports, OSINT, and user submissions — no private data is collected

**Data Lifecycle:**

| Stage | Action | Owner |
|-------|--------|-------|
| Collection | Scan metadata captured during Step 6 (DELIVER) | Workflow orchestrator |
| Processing | Financial risk assessment in Step 7 | Financial Risk Assessor |
| Storage | Persisted to Scans DB (22 fields) | Library database API |
| Usage | Dashboard display, query portal, reporting | Frontend + data portal |
| Archival | Audit trail entries archived after 7 years | Admin (manual archival) |
| Deletion | Media files deleted immediately after processing | Workflow orchestrator (automatic) |

**User Story:**
*As a bank fraud analyst (Aisha), I want assurance that the customer photos I upload for KYC verification are not stored permanently — LAICIs processes them, records only the detection score and metadata, and deletes the original file — so I can confirm PDPA compliance to my compliance officer.*

**Acceptance Criteria:**
- Media files are NOT persisted — processed in-memory and discarded after detection
- Scan metadata is anonymized (no names, ID numbers, bank accounts)
- Audit trail is retained for 7 years
- OSINT raw data is purged after 90 days (aggregate stats retained)
- Upload zone displays consent notice
- Data governance policy is documented and accessible to Admin users
- No PII is stored without explicit user consent

---

## 7. SECURITY Feature Specifications

This section specifies all 10 security features in detail. Each specification includes description, requirements, implementation details, and user stories. Security is built into every feature of LAICIs v2.0 — not bolted on as an afterthought.

---

### 7.1 Authentication

**Description:**
Multi-layer authentication system that verifies user identity before granting access to any platform feature. Authentication is built on the WorkBuddy platform's OAuth 2.0 framework, supplemented by API key management for programmatic access and session management for security.

**Authentication Methods:**

| Method | Use Case | Technology |
|--------|----------|------------|
| WorkBuddy OAuth 2.0 | Dashboard access (all human users) | WorkBuddy platform authentication |
| API Key | REST API access (programmatic) | 256-bit key, hashed, rotated every 30 days |
| Session token | Maintains session after OAuth | 30-minute timeout, sliding expiration |

**OAuth 2.0 Flow:**
1. User navigates to the LAICIs dashboard URL
2. If not authenticated, redirected to WorkBuddy platform login
3. User enters WorkBuddy credentials (email/password or SSO)
4. WorkBuddy platform authenticates and returns OAuth 2.0 access token
5. Dashboard receives token, stores in browser session storage
6. All subsequent database and API calls include the token in the Authorization header
7. Token expires after 30 minutes of inactivity (sliding expiration)
8. On expiration, user is redirected to login again

**API Key Management:**

| Property | Specification |
|----------|---------------|
| Key length | 256 bits (32 bytes, hex-encoded to 64 characters) |
| Storage | Hashed (SHA-256) in the audit trail configuration — never stored in plaintext |
| Generation | Cryptographically secure random generation (Python `secrets` module) |
| Rotation | Mandatory rotation every 30 days — system sends notification 7 days before expiration |
| Revocation | Admin can revoke any API key immediately |
| Scope | Scoped to API User role only — no dashboard access |
| Rate limiting | Configurable per key (default: 100 requests per 5 minutes) |
| Transmission | HTTPS only — never sent over HTTP |

**Session Management:**

| Property | Specification |
|----------|---------------|
| Session timeout | 30 minutes of inactivity |
| Timeout type | Sliding expiration (reset on activity) |
| Warning | Warning popup at 25 minutes: "Your session will expire in 5 minutes. Click to extend." |
| Session ID | Cryptographically secure random string |
| Session storage | Browser session storage (cleared on tab close) |
| Concurrent sessions | Maximum 3 concurrent sessions per user |
| Session invalidation | On logout, password change, or admin force-logout |

**Account Lockout Policy:**

| Trigger | Action | Reset |
|---------|--------|-------|
| 5 consecutive failed login attempts | Account locked for 15 minutes | Auto-unlock after 15 minutes |
| 10 failed attempts in 24 hours | Account locked for 1 hour | Auto-unlock after 1 hour |
| 20 failed attempts in 24 hours | Account locked indefinitely | Admin manual unlock required |
| Successful login | Counter reset to 0 | N/A |

**UI Elements:**
- Login: WorkBuddy platform login page (OAuth 2.0 redirect)
- Session timeout warning: modal popup at 25 minutes with "Extend Session" and "Logout" buttons
- API key management: Admin-only page with "Generate New Key", "Revoke Key", and "Key Expiration" display
- Account lockout: error message "Account locked due to too many failed attempts. Please try again in X minutes."

**User Story:**
*As a bank fraud analyst (Aisha), I want to log in through WorkBuddy's secure OAuth system, have my session automatically timeout after 30 minutes of inactivity with a 5-minute warning, and know that my account locks after 5 failed attempts — so my analyst credentials cannot be brute-forced and my session can't be hijacked if I step away from my desk.*

**Acceptance Criteria:**
- OAuth 2.0 authentication is required for all dashboard access
- API keys are 256-bit, hashed, and rotated every 30 days
- Session timeout occurs after 30 minutes of inactivity with a 5-minute warning
- Account locks after 5 consecutive failed login attempts (15-minute auto-unlock)
- API keys are scoped to API User role only
- Session IDs are cryptographically secure

---

### 7.2 Role-Based Access Control (RBAC)

**Description:**
Four-role access control model that determines what each user can see and do on the platform. Roles are assigned by the Admin and determine access to dashboard sections, database operations, data exports, report generation, and system configuration.

**Role Definitions:**

**Admin:**
- Full access to all dashboard sections, modules, and features
- Can manage users (create, assign roles, revoke access)
- Can generate and revoke API keys
- Can view, search, and filter the audit trail
- Can generate all compliance report types
- Can run OSINT pipeline manually
- Can modify system configuration (pricing tiers, risk thresholds)
- Can access all data portal features (query, export, RAG Q&A)
- Can upload media and perform scans
- Can use the Scenario Planner and Recovery Assistant
- Typical user: Sarah (Corporate Security Manager), TECHBENG team members

**Analyst:**
- Can upload media and perform scans
- Can view detection results and financial risk assessment
- Can access the data portal (query, filter, sort)
- Can export data as CSV and JSON
- Can use RAG-powered Q&A
- Can generate compliance reports (BNM, PDRM, Board Governance)
- Can search the scammer database
- Can use the Scenario Planner and Recovery Assistant
- Can view the Market Intelligence Panel and Loss Prevention Tracker
- Cannot manage users or API keys
- Cannot view the audit trail
- Cannot modify system configuration
- Typical user: Aisha (Bank Fraud Analyst)

**Viewer:**
- Can view the dashboard (read-only access to all display sections)
- Can view detection results for scans performed by others
- Can view the Market Intelligence Panel and Loss Prevention Tracker
- Can view the scammer database search results
- Can use RAG-powered Q&A (read-only knowledge access)
- Cannot upload media or perform scans
- Cannot export data
- Cannot generate compliance reports
- Cannot view the audit trail
- Cannot modify any data
- Typical user: Rahman (Police CCID Officer — read-only for inter-agency data sharing)

**API User:**
- REST API access only — no dashboard UI access
- Can submit media for scanning via API endpoint
- Can query scan results via API endpoint
- Can query scammer data via API endpoint
- Rate-limited (default: 100 requests per 5 minutes)
- All API calls logged to audit trail
- Cannot access dashboard, data portal, or compliance reports
- Typical user: Dev (Data Analyst — programmatic integration)

**Permission Matrix:**

| Capability | Admin | Analyst | Viewer | API User |
|------------|-------|---------|--------|----------|
| Upload media / scan | Yes | Yes | No | Yes (API) |
| View detection results | Yes | Yes | Yes | Yes (API) |
| Data portal (query/filter) | Yes | Yes | Yes (read-only) | Yes (API) |
| Export CSV/JSON | Yes | Yes | No | Yes (API) |

| Capability | Admin | Analyst | Viewer | API User |
|------------|-------|---------|--------|----------|
| RAG Q&A | Yes | Yes | Yes | No |
| Compliance reports | Yes | Yes | No | No |
| Scenario Planner | Yes | Yes | No | No |
| Recovery Assistant | Yes | Yes | No | No |
| Audit trail (view) | Yes | No | No | No |

| Capability | Admin | Analyst | Viewer | API User |
|------------|-------|---------|--------|----------|
| User management | Yes | No | No | No |
| API key management | Yes | No | No | No |
| System config | Yes | No | No | No |
| OSINT manual trigger | Yes | Yes | No | No |

**Implementation:**
- Role is stored in the user profile on the WorkBuddy platform
- Dashboard reads role from the OAuth token on page load
- Each dashboard section checks the user's role before rendering
- API endpoints check the API key's role before processing
- Unauthorized access attempts are logged to the audit trail (action="unauthorized_access")

**UI Elements:**
- Role badge in dashboard header: "Logged in as: [Name] ([Role])" with color-coded badge (Admin=purple, Analyst=blue, Viewer=green, API User=gray)
- Unauthorized sections: hidden from navigation, not just disabled
- Unauthorized API calls: HTTP 403 Forbidden with JSON error `{"error": "insufficient_permissions", "required_role": "admin"}`

**User Story:**
*As a corporate security manager (Sarah), I want Admin access so I can manage my team's roles — give Aisha Analyst access to run scans, give Rahman Viewer access to read scammer data, and give Dev API User access for programmatic integration — so each person sees only what they need.*

**Acceptance Criteria:**
- 4 roles are defined with the exact permissions specified above
- Role badge displays in the dashboard header for all authenticated users
- Unauthorized sections are hidden from navigation (not just disabled)
- API endpoints return HTTP 403 for insufficient permissions
- All unauthorized access attempts are logged to the audit trail
- Role assignment is managed by Admin only

---

### 7.3 Input Validation

**Description:**
Comprehensive input validation on all user-provided data entering the platform. This prevents malicious file uploads, path traversal attacks, oversized payloads, and file type spoofing. Validation occurs at the system boundary (upload zone and API endpoints) before any processing begins.

**File Extension Whitelist:**

| Media Type | Allowed Extensions |
|------------|---------------------|
| Image | .jpg, .jpeg, .png, .webp, .bmp, .tiff |
| Video | .mp4, .mov, .avi, .mkv, .webm |

All other extensions are rejected with error: "File type not supported. Allowed: JPG, PNG, WebP, BMP, TIFF, MP4, MOV, AVI, MKV, WebM."

**File Size Limit:**
- Maximum: 50 MB (Sightengine API constraint)
- Minimum: 1 KB (reject empty/near-empty files)
- Error on violation: "File too large. Maximum size: 50 MB." or "File too small. Minimum size: 1 KB."

**Path Sanitization:**
- All file paths are sanitized using Python `os.path.basename()` to strip directory traversal sequences
- Reject paths containing: `..`, `~`, absolute paths, null bytes, URL-encoded sequences
- Sanitized filename is used for storage metadata — original path is never stored
- Example: Input `../../etc/passwd` → rejected; Input `photo.jpg` → accepted as `photo.jpg`

**Magic Bytes Verification:**
- File content is verified against the declared extension using magic bytes (file signatures):

| Extension | Expected Magic Bytes (hex) |
|-----------|---------------------------|
| JPG/JPEG | FF D8 FF |
| PNG | 89 50 4E 47 0D 0A 1A 0A |
| WebP | 52 49 46 46 (RIFF) |
| BMP | 42 4D (BM) |
| TIFF | 49 49 2A 00 or 4D 4D 00 2A |
| MP4 | ftyp box at offset 4 |
| MOV | ftyp box at offset 4 |
| WebM | 1A 45 DF A3 |

- If magic bytes do not match the declared extension, the file is rejected with error: "File content does not match declared type. Possible file spoofing detected."
- This prevents attackers from uploading malicious files with renamed extensions (e.g., `malware.exe` renamed to `photo.jpg`)

**Implementation:**
1. User selects file in upload zone or submits via API
2. Check file extension against whitelist → reject if not allowed
3. Check file size against limits → reject if too large or too small
4. Sanitize file path using `os.path.basename()` → reject if path traversal detected
5. Read first 16 bytes of file → compare against expected magic bytes for the declared extension
6. If all checks pass, proceed to scan; if any check fails, return error and log to audit trail

**Audit Trail Logging:**
- All validation failures are logged: timestamp, actor, action="input_validation_failed", target=filename, result="rejected", reason=specific_failure
- Repeated validation failures from the same user/IP trigger a security alert

**User Story:**
*As a corporate security manager (Sarah), I want the platform to reject any file that isn't a genuine image or video — checking not just the extension but the actual file content (magic bytes) — so attackers can't upload malicious files disguised as images to compromise the system.*

**Acceptance Criteria:**
- File extension whitelist enforces only allowed image and video formats
- File size limit of 50 MB is enforced (files > 50 MB rejected)
- Path sanitization strips all directory traversal sequences (`..`, `~`, null bytes)
- Magic bytes verification rejects files whose content doesn't match their declared extension
- All validation failures are logged to the audit trail with reason
- Validation occurs before any processing begins (fail fast)

---

### 7.4 Output Sanitization

**Description:**
Comprehensive output sanitization to prevent cross-site scripting (XSS), information disclosure, and error message leakage. All data sent from the platform to the user (HTML rendering, API responses, error messages) is sanitized before transmission.

**HTML Escaping (escapeHtml utility):**
- All user-provided content displayed in the dashboard is passed through an `escapeHtml()` JavaScript utility function before rendering
- The function escapes the following characters:

| Character | Escaped To |
|-----------|------------|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `"` | `&quot;` |
| `'` | `&#x27;` |
| `&` | `&amp;` |
| `/` | `&#x2F;` |

- Applied to: scan results display, scammer search results, scan history table, RAG Q&A answers, OSINT data display, user context field, compliance report content
- Example: Input `<script>alert('XSS')</script>` → rendered as `&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;` (displayed as text, not executed)

**API Response Filtering:**
- API responses contain only the data the client needs — no internal system information is exposed
- Filtered out of all API responses:

| Filtered Element | Reason |
|------------------|--------|
| Raw API responses from Sightengine/Gemini | Prevents third-party data leakage |
| Internal file paths (e.g., `/src/detection/ela_analysis.py`) | Prevents path disclosure |
| API keys and secrets | Prevents credential exposure |
| Internal error tracebacks | Prevents information disclosure |
| Database query strings | Prevents SQL injection reverse engineering |
| Server version information | Prevents fingerprinting |

- API responses are structured as: `{"success": true, "data": {...}, "error": null}` or `{"success": false, "data": null, "error": "Human-readable error message"}`

**Error Truncation:**
- All error messages displayed to users are truncated to 200 characters maximum
- Full error details are logged to the audit trail (for Admin debugging) but not shown to users
- Example: Full error "ELA analysis failed: Pillow cannot open file /c/Users/FARZANAH/WorkBuddy AI/TECHBENG/src/uploads/photo.jpg due to corrupted EXIF data at offset 0x1A2B" → displayed to user as "ELA analysis failed: Pillow cannot open file due to corrupted EXIF data."
- Prevents information leakage through verbose error messages

**Implementation:**
1. Before any data is rendered in the dashboard HTML, it passes through `escapeHtml()` in JavaScript
2. Before any API response is sent, the response object is filtered to remove internal fields
3. Before any error message is displayed, it is truncated to 200 characters
4. All sanitization actions are transparent to the user — they see clean, safe output

**User Story:**
*As a bank fraud analyst (Aisha), I want the platform to automatically escape any HTML in scan results and scammer data so that if a scammer's name field contains `<script>` tags, it's displayed as text rather than executed in my browser — protecting me from cross-site scripting attacks while I'm reviewing potentially malicious content.*

**Acceptance Criteria:**
- `escapeHtml()` utility function is applied to all user-facing HTML output
- API responses do not contain raw Sightengine/Gemini responses, file paths, API keys, or tracebacks
- Error messages are truncated to 200 characters for user display
- Full error details are available in the audit trail for Admin debugging
- No `<script>` tags in user-provided content are executed in the browser

---

### 7.5 Audit Trail

**Description:**
A comprehensive, append-only, immutable audit trail that records every user and system action on the platform. The audit trail serves three purposes: (1) chain-of-custody evidence for legal proceedings, (2) regulatory compliance documentation, and (3) security incident investigation. Every action — scan, query, export, report generation, OSINT update, login, configuration change — is logged with 7 fields.

**Audit Trail Fields (7):**

| # | Field | Type | Description | Example |
|---|-------|------|-------------|---------|
| 1 | `timestamp` | datetime (ISO 8601) | Exact date and time of the action | 2026-01-15T10:30:45Z |
| 2 | `actor` | string | User ID or "system" for automation | "user_aisha_001" or "system" |
| 3 | `action` | string | Type of action performed | "scan", "query", "export", "report_generated", "osint_update", "login", "unauthorized_access" |
| 4 | `target` | string | Object affected by the action | "scans_db", "scammers_db", "VD-20260115-001", "bnm_report" |
| 5 | `result` | string | Outcome of the action | "success" or "failure" or "rejected" |
| 6 | `ip_address` | string | IP address of the actor (if available) | "203.106.84.27" or "127.0.0.1" for system |
| 7 | `session_id` | string | Session identifier for correlating actions | "sess_8f3a2b1c4d5e6f7a" |

**Actions Logged:**

| Action | Description | Who |
|--------|-------------|-----|
| `login` | User authentication success/failure | All users |
| `logout` | User session termination | All users |
| `scan` | Media scan execution (Steps 1–7) | Analyst, Admin, API User |
| `query` | Data portal query execution | Analyst, Admin, API User |
| `export` | CSV or JSON data export | Analyst, Admin, API User |
| `report_generated` | Compliance report generation | Analyst, Admin |
| `osint_update` | OSINT pipeline execution (daily or manual) | System or Analyst/Admin |
| `rag_query` | RAG knowledge base Q&A query | All roles |
| `unauthorized_access` | Attempted access to unauthorized feature | Any (logged on failure) |
| `config_change` | System configuration modification | Admin |
| `key_generation` | API key generation | Admin |
| `key_revocation` | API key revocation | Admin |
| `role_change` | User role assignment/change | Admin |
| `input_validation_failed` | File upload validation failure | Any (logged on rejection) |

**Properties:**
- **Append-only:** Records can only be added, never modified or deleted
- **Immutable:** No user (including Admin) has permission to modify or delete audit trail entries
- **Searchable:** Admin can search by any field (timestamp range, actor, action, target, result)
- **Filterable:** Admin can filter by date range, action type, actor, result
- **Retention:** 7 years (regulatory compliance — PDPA, BNM evidence retention)
- **Storage:** WorkBuddy Library database (structured records)

**UI Elements:**
- Tab: "Compliance & Audit" → Sub-tab: "Audit Trail"
- Searchable, filterable table with columns: Timestamp, Actor, Action, Target, Result, IP, Session ID
- Filters: date range picker, action type dropdown, actor search, result filter (success/failure/rejected)
- Pagination: 50 entries per page
- "Export Audit Trail (CSV)" button — available to Admin only
- Access restricted to Admin role only (other roles cannot see this tab)

**User Story:**
*As a police officer (Rahman), I want every scan, query, and data export to be logged with timestamp, actor, action, target, result, IP, and session ID — in an append-only, immutable audit trail — so that when I testify in court, the defense cannot challenge the authenticity or integrity of the digital evidence. The audit trail IS the chain of custody.*

**Acceptance Criteria:**
- Audit trail logs all 14 action types listed above
- All 7 fields are captured for every entry
- Audit trail is append-only and immutable (no modification or deletion)
- Audit trail is searchable and filterable by Admin only
- Audit trail entries are retained for 7 years
- "Export Audit Trail (CSV)" produces a valid CSV with all entries matching the filter
- Access to the audit trail is restricted to Admin role

---

### 7.6 Security Dashboard Elements

**Description:**
Security-related visual elements integrated into the dashboard that provide real-time security awareness to all users. These elements ensure users are always informed about the security status of the platform, their role, their session, and any active security incidents.

**Elements:**

**1. Security Status Indicator:**
- Location: Top-right corner of dashboard header
- Display: Colored circle with icon

| Status | Color | Meaning |
|--------|-------|---------|
| Green (#2ed573) | All systems secure | All security checks passing, no active incidents |
| Yellow (#ffa502) | Elevated risk | Minor security event (e.g., failed login attempts, OSINT pipeline failure) |
| Red (#ff4757) | Critical security issue | Active security incident (e.g., breach detected, multiple unauthorized access attempts) |
| Gray (#7f8c8d) | Unknown/checking | Status being assessed (page load) |

- Tooltip: "Security Status: [GREEN/YELLOW/RED] — [description]. Last checked: [timestamp]."
- Click: Opens a modal with detailed security status (checks passed, active incidents, recent alerts)

**2. Role Badge:**
- Location: Dashboard header, next to username
- Display: Color-coded badge with role name

| Role | Color | Badge Text |
|------|-------|------------|
| Admin | Purple (#a55eea) | "ADMIN" |
| Analyst | Blue (#00d4ff) | "ANALYST" |
| Viewer | Green (#2ed573) | "VIEWER" |
| API User | Gray (#7f8c8d) | "API USER" |

- Tooltip: "[Role] — [list of key permissions for this role]"
- Click: Opens a modal showing the full permission matrix for the user's role

**3. Session Timeout Warning:**
- Location: Modal popup (centered)
- Trigger: 25 minutes of inactivity (5 minutes before 30-minute timeout)
- Display: "Your session will expire in 5 minutes due to inactivity. Click 'Extend Session' to continue working, or 'Logout' to end your session now."
- Buttons: "Extend Session" (resets timer to 30 minutes), "Logout" (terminates session immediately)
- If no action: Session expires at 30 minutes, user redirected to login with message "Session expired due to inactivity. Please log in again."
- Auto-extend: Any user activity (click, scroll, keystroke) resets the timer before the warning appears

**4. Security Incident Banner:**
- Location: Full-width banner at top of dashboard (below header, above content)
- Display: Only visible when an active security incident exists
- Color: Red background (#ff4757) with white text
- Content: "SECURITY INCIDENT: [brief description]. [Recommended action]. Click for details."
- Click: Opens incident details modal with: incident description, severity level, affected systems, recommended actions, and link to incident response playbook (Section 7.9)
- Auto-dismiss: When incident is resolved, banner disappears

**5. Audit Trail Tab:**
- Location: "Compliance & Audit" section in dashboard navigation
- Access: Admin role only
- Display: Searchable, filterable table of all audit trail entries (as specified in Section 7.5)
- Other roles: Tab is hidden from navigation entirely (not just disabled)

**User Story:**
*As a corporate security manager (Sarah), I want to see a green security status indicator in the dashboard header confirming all security checks are passing, a purple ADMIN badge showing my role, and a session timeout warning at 25 minutes so I can extend before losing my work — so I'm always aware of the platform's security state and my own session state while reviewing deepfake scans.*

**Acceptance Criteria:**
- Security status indicator displays correctly (green/yellow/red/gray) based on system state
- Role badge displays for all authenticated users with correct color and text
- Session timeout warning appears at 25 minutes with "Extend" and "Logout" buttons
- Security incident banner appears only when an active incident exists
- Audit trail tab is visible to Admin only and hidden from other roles
- All security elements update in real-time (no page refresh required)

---

### 7.7 Compliance Reports

**Description:**
A reporting engine that generates regulatory-compliant reports for BNM, PDRM, and internal governance bodies. Includes four report types, each with a defined structure, data sources, and output format. All report generation is logged to the audit trail for chain-of-custody.

**Report Types:**

**1. BNM Fraud Report:**
- Purpose: Monthly regulatory submission to Bank Negara Malaysia
- Data sources: Scans database (filtered by date range), Financial Overview database, Scammers database
- Structure:

| Section | Content |
|---------|---------|
| Report header | Report period, organization name, prepared by, date generated |
| Summary | Total scans, deepfakes detected, total exposure, total prevention value |
| Risk tier breakdown | Count and percentage by LOW/MODERATE/HIGH/CRITICAL |
| Scam category breakdown | Count and RM exposure by scam type |
| Scammer profiles identified | New scammers added during period, risk levels |
| Audit trail summary | Count of all actions during period, any security incidents |
| Certification | "This report was generated by LAICIs v2.0. All data is sourced from the LAICIs audit trail (chain-of-custody)." |

- Output: In-line HTML display + PDF download
- Access: Analyst and Admin roles

**2. PDRM Intelligence Brief:**
- Purpose: Intelligence briefing for PDRM CCID and senior officers
- Data sources: Scammers database, OSINT data from Data knowledge base node, Scans database
- Structure:

| Section | Content |
|---------|---------|
| Report header | Report period, prepared by, date generated |
| National scam overview | Market Intelligence Panel statistics (7 key stats) |
| Deepfake case trends | Count by month, YoY comparison, scam type breakdown |
| Scammer profiles | Top 10 scammers by risk level, new scammers during period |
| OSINT summary | Key OSINT findings during period (extracted from Data node) |
| Recommendations | Suggested enforcement actions, inter-agency coordination needs |
| Certification | Chain-of-custody statement from audit trail |

- Output: In-line HTML display + PDF download
- Access: Analyst and Admin roles

**3. Board Governance Report:**
- Purpose: Quarterly board-level risk assessment for corporate governance
- Data sources: Financial Overview database, Scans database, audit trail
- Structure:

| Section | Content |
|---------|---------|
| Report header | Report period, organization name, prepared by, date generated |
| Executive summary | Loss prevention value, ROI metrics, risk assessment |
| Loss prevention summary | Cumulative prevention value, breakdown by category/segment/month |
| Detection performance | Scan count, accuracy metrics, false positive/negative rates |
| Financial exposure | Total estimated exposure detected, risk tier distribution |
| Security posture | Audit trail summary, security incidents, vulnerability management status |
| STRIDE/OWASP compliance | Threat mitigation status (all 6 STRIDE threats, OWASP A01–A10) |
| Certification | Chain-of-custody statement, compliance with PDPA/CMA/BNM guidelines |

- Output: In-line HTML display + PDF download
- Access: Admin role only

**4. Audit Trail Log:**
- Purpose: Chain-of-custody evidence for legal proceedings and regulatory audits
- Data source: Audit trail (filtered by date range)
- Structure: Tabular export of all audit trail entries within the selected date range
- Output: CSV download (structured data) or PDF (formatted report)
- Access: Admin role only

**UI Elements:**
- Tab: "Compliance & Audit" → Sub-tab: "Generate Report"
- Report type selector: 4 buttons (BNM Fraud Report, PDRM Intelligence Brief, Board Governance Report, Audit Trail Log)
- Date range selector: From / To date picker
- "Generate Report" button
- Generated reports display in-line (HTML) with "Download PDF" or "Download CSV" button
- All report generation logged to audit trail (action="report_generated", target=report_type)

**User Story:**
*As a bank fraud analyst (Aisha), I want to generate a BNM compliance report covering January 2026 scans with one click — including scan count, deepfake count, total exposure, prevention value, risk tier breakdown, and audit trail certification — so I meet BNM's quarterly regulatory reporting deadline without spending 3 hours compiling it manually.*

**Acceptance Criteria:**
- All 4 report types can be generated with date range selection
- BNM Fraud Report includes: scan count, deepfake count, total exposure, prevention value, risk tier breakdown, scammer profiles, audit trail summary
- PDRM Intelligence Brief includes: national scam statistics, deepfake case trends, scammer profiles, OSINT summary
- Board Governance Report includes: loss prevention summary, ROI metrics, STRIDE/OWASP compliance status
- Audit Trail Log exports as CSV with all entries in the selected date range
- All report generation is logged to the audit trail
- Reports are accessible to the correct roles (BNM/PDRM: Analyst+Admin, Board/Audit: Admin only)

---

### 7.8 Threat Mitigation (STRIDE + OWASP)

**Description:**
Systematic threat mitigation documentation covering the STRIDE threat model (all 6 threat categories) and OWASP Top 10 (A01–A10). This section documents how LAICIs v2.0 mitigates each identified threat, providing assurance to security-conscious users and auditors.

#### STRIDE Threat Model (6 threats, all mitigated)

**S — Spoofing (Impersonating a legitimate user):**

| Threat | Mitigation |
|--------|-----------|
| Attacker impersonates a legitimate user | WorkBuddy OAuth 2.0 authentication with access tokens |
| Attacker brute-forces login credentials | Account lockout after 5 failed attempts (15-minute lockout) |
| Attacker uses stolen API key | 256-bit keys, 30-day rotation, Admin revocation capability |
| Attacker session hijacking | 30-minute session timeout, sliding expiration, HTTPS-only |

**T — Tampering (Modifying data or code):**

| Threat | Mitigation |
|--------|-----------|
| Attacker modifies scan results | Audit trail is append-only and immutable — no modification possible |
| Attacker tampers with database records | WorkBuddy Library SDK is the only access path — no direct database access |
| Attacker modifies audit trail | Audit trail is append-only — no modification or deletion by any user (including Admin) |
| Attacker tampers with uploaded media | Media is processed in-memory and discarded — no persistent storage to tamper with |

**R — Repudiation (Denying an action was performed):**

| Threat | Mitigation |
|--------|-----------|
| User denies performing a scan | Audit trail logs every scan with timestamp, actor, action, target, result, IP, session_id |
| User denies exporting data | Audit trail logs every export with record count |
| User denies generating a report | Audit trail logs every report generation with report type and date range |
| System denies OSINT update | Audit trail logs every OSINT run with data points collected |

**I — Information Disclosure (Exposing sensitive data):**

| Threat | Mitigation |
|--------|-----------|
| Attacker accesses API keys | Keys stored as environment variables only, never in code or database; API responses filter out keys |
| Attacker reads internal file paths | Path sanitization strips paths; API responses filter out internal paths; error truncation (200 chars) |
| Attacker accesses other users' data | RBAC restricts access to user's role; Viewer cannot export; API User scoped to API only |
| Attacker accesses raw Sightengine/Gemini responses | API response filtering removes raw third-party responses |
| Attacker accesses PII | No PII stored without consent; media not persisted; metadata anonymized |

**D — Denial of Service (Disrupting service availability):**

| Threat | Mitigation |
|--------|-----------|
| Attacker floods API with requests | Rate limiting: 100 requests per 5 minutes per API key |
| Attacker uploads oversized files | File size limit: 50 MB max |
| Attacker uploads many files rapidly | Sightengine rate limit: 10 scans per 5 minutes (code-enforced) |
| Attacker floods RAG Q&A | RAG queries limited to 20 per 5 minutes per user |
| API outage (Sightengine/Gemini) | Graceful degradation: ELA always available, scorer adjusts weights |

**E — Elevation of Privilege (Gaining unauthorized access levels):**

| Threat | Mitigation |
|--------|-----------|
| Viewer escalates to Analyst | RBAC enforced at section level — unauthorized sections hidden, not just disabled |
| Analyst escalates to Admin | User management and system config accessible to Admin role only |
| API User accesses dashboard | API keys scoped to API endpoints only — no dashboard UI access |
| Attacker exploits vulnerability | Input validation (magic bytes), output sanitization (HTML escaping), quarterly dependency scanning |

#### OWASP Top 10 (A01–A10, all addressed)

| OWASP ID | Threat | LAICIs Mitigation |
|----------|--------|---------------------|
| A01 | Broken Access Control | RBAC with 4 roles, hidden unauthorized sections, API endpoint authorization checks |
| A02 | Cryptographic Failures | API keys hashed (SHA-256), HTTPS-only transmission, no plaintext secrets in code |
| A03 | Injection | Path sanitization (no SQL — WorkBuddy Library SDK handles queries), HTML escaping on all output |
| A04 | Insecure Design | Security-by-architecture principles, STRIDE analysis, threat modeling from design phase |
| A05 | Security Misconfiguration | Environment variables for all secrets, no default credentials, minimal attack surface |
| A06 | Vulnerable Components | Quarterly dependency scanning (Section 7.10), code review before merge |
| A07 | Authentication Failures | OAuth 2.0, 5-failure lockout, 30-day key rotation, 30-min session timeout |
| A08 | Software/Data Integrity Failures | Immutable audit trail, append-only databases, magic bytes verification |
| A09 | Logging/Monitoring Failures | Comprehensive audit trail (14 action types, 7 fields), security dashboard elements |
| A10 | Server-Side Request Forgery | No server-side URL fetching from user input; WorkBuddy Library SDK handles all external calls |

**User Story:**
*As a corporate security manager (Sarah), I want documented evidence that LAICIs mitigates all 6 STRIDE threats and all 10 OWASP Top 10 vulnerabilities — so I can present this to my board's audit committee as assurance that the platform meets enterprise security standards.*

**Acceptance Criteria:**
- All 6 STRIDE threats are documented with specific mitigations
- All 10 OWASP Top 10 (A01–A10) are addressed with specific mitigations
- Threat mitigation documentation is included in the Board Governance Report
- STRIDE and OWASP status is displayed in the security dashboard elements
- Documentation is accessible to Admin and Analyst roles for compliance reporting

---

### 7.9 Incident Response

**Description:**
A structured incident response framework with 4 severity levels and a 7-step response playbook. When a security incident is detected (via audit trail monitoring, failed validation alerts, or external notification), the platform follows a defined response process to minimize impact and ensure recovery.

**Severity Levels:**

| Level | Name | Description | Examples | Response Time |
|-------|------|-------------|----------|---------------|
| SEV-1 | Critical | Active breach or data compromise | Unauthorized data access confirmed, API key compromise, audit trail tampering attempt | Immediate (< 1 hour) |
| SEV-2 | High | Serious security event requiring urgent action | Repeated unauthorized access attempts (10+), multiple input validation failures from same IP, OSINT pipeline compromise | < 4 hours |
| SEV-3 | Medium | Security event requiring investigation | Isolated unauthorized access attempt, single validation failure, session anomaly | < 24 hours |
| SEV-4 | Low | Minor security observation | Failed login attempt, expired API key used, minor configuration drift | < 72 hours |

**7-Step Response Playbook:**

| Step | Action | Owner | SEV-1 | SEV-2 | SEV-3 | SEV-4 |
|------|--------|-------|-------|-------|-------|-------|
| 1. Detect | Identify incident via audit trail, alerts, or user report | System/Admin | Auto | Auto | Daily review | Weekly review |
| 2. Classify | Assign severity level based on impact and scope | Admin | Immediate | < 1 hour | < 4 hours | < 24 hours |
| 3. Contain | Isolate affected systems, revoke compromised keys, block IPs | Admin | Immediate | < 4 hours | < 24 hours | < 72 hours |
| 4. Investigate | Analyze audit trail, determine root cause, assess impact | Admin | < 4 hours | < 24 hours | < 72 hours | < 1 week |
| 5. Eradicate | Remove threat vector, patch vulnerability, update controls | Admin | < 8 hours | < 48 hours | < 1 week | < 2 weeks |
| 6. Recover | Restore normal operations, verify systems are clean | Admin | < 24 hours | < 72 hours | < 1 week | < 2 weeks |
| 7. Review | Post-incident review, document lessons learned, update playbook | Admin + Team | < 1 week | < 2 weeks | < 1 month | < 1 month |

**Incident Detection Triggers:**

| Trigger | Detection Method | Severity |
|---------|-----------------|----------|
| 5+ failed login attempts from same IP | Audit trail monitoring (action="login", result="failure") | SEV-3 |
| 10+ failed login attempts in 24 hours | Audit trail monitoring | SEV-2 |
| 20+ failed login attempts in 24 hours | Audit trail monitoring | SEV-1 |
| Input validation failure with path traversal pattern | Audit trail monitoring (action="input_validation_failed") | SEV-2 |
| File spoofing detected (magic bytes mismatch) | Audit trail monitoring | SEV-3 |
| Unauthorized access attempt to restricted section | Audit trail monitoring (action="unauthorized_access") | SEV-3 |
| Repeated unauthorized access (5+ in 1 hour) | Audit trail monitoring | SEV-2 |
| API key used after revocation | API key validation check | SEV-1 |
| Audit trail tampering attempt | Immutable storage enforcement | SEV-1 |
| OSINT pipeline compromise (malicious data injection) | OSINT data validation | SEV-2 |

**UI Elements:**
- Security incident banner (as specified in Section 7.6): appears for SEV-1 and SEV-2 incidents
- Incident details modal: severity level, description, affected systems, recommended actions, playbook timeline
- "View Incident Response Playbook" link: opens the 7-step playbook with current step highlighted
- Incident log: table of past incidents with severity, status (open/resolved), and resolution summary

**User Story:**
*As a corporate security manager (Sarah), I want the platform to detect when someone makes 10 failed login attempts in 24 hours (SEV-2), display a red security incident banner, and show me the 7-step response playbook — detect, classify as SEV-2, contain by blocking the IP, investigate the audit trail, eradicate the threat, recover, and review — so I can respond systematically to security incidents instead of improvising under pressure.*

**Acceptance Criteria:**
- 4 severity levels are defined with correct response times
- 7-step playbook is documented for each severity level
- 10 incident detection triggers are implemented via audit trail monitoring
- Security incident banner appears for SEV-1 and SEV-2 incidents
- Incident details modal shows severity, description, affected systems, and playbook
- All incidents are logged to the audit trail
- Post-incident review is documented (Step 7)

---

### 7.10 Vulnerability Management

**Description:**
Proactive vulnerability management process to identify and remediate security weaknesses before they can be exploited. Covers dependency scanning, code review practices, and continuous improvement. This is a preventive measure, not a reactive one.

**Quarterly Dependency Scanning:**

| Aspect | Specification |
|--------|---------------|
| Frequency | Quarterly (every 3 months) |
| Tool | Python `pip audit` / `npm audit` / automated dependency scanner |
| Scope | All Python packages (Pillow, numpy, requests, torch, timm), all npm packages (if applicable), WorkBuddy Library SDK |
| Output | Vulnerability report: package name, CVE ID, severity, fixed version |
| Action | Update all packages with known vulnerabilities to fixed versions within 7 days of report |
| Logging | Scan results and remediation actions logged to audit trail (action="vulnerability_scan") |

**Code Review Before Merge:**

| Aspect | Specification |
|--------|---------------|
| Requirement | All code changes require review by at least one other team member before merge |
| Focus areas | Security: input validation, output sanitization, authentication checks, authorization checks; Logic: correctness, edge cases; Style: consistency with existing code |
| Tool | Git pull requests with inline review comments |
| Approval | Minimum 1 approval required before merge; security-sensitive changes require Admin approval |
| Automated checks | Linter (flake8 for Python), HTML validator, JavaScript syntax check |
| Logging | Code review completion logged to audit trail (action="code_review", target=PR_ID) |

**Continuous Improvement:**
- Security retrospective: quarterly review of security incidents, near-misses, and audit trail patterns
- Threat model update: STRIDE and OWASP documentation reviewed and updated quarterly
- Dependency watch: monitor CVE databases for new vulnerabilities in used packages between quarterly scans
- Training: team members complete security awareness training (input validation, XSS prevention, secure coding practices) at hackathon kickoff

**User Story:**
*As a corporate security manager (Sarah), I want the platform to undergo quarterly dependency scanning and mandatory code review before any merge — so I can assure my board that we proactively identify and remediate vulnerabilities before they can be exploited, rather than reacting after a breach.*

**Acceptance Criteria:**
- Dependency scanning runs quarterly with documented results
- All code changes require at least 1 review approval before merge
- Security-sensitive changes require Admin approval
- Automated linter checks run on all Python and JavaScript code
- Vulnerability scan results and remediation actions are logged to the audit trail
- STRIDE and OWASP documentation is reviewed and updated quarterly

---

## 8. Dashboard Layout

The LAICIs v2.0 dashboard has 10 sections, organized in a single-page HTML application with tabbed navigation. The dashboard uses a dark theme with CSS variables: `--bg: #0a0e1a`, `--accent: #00d4ff`, `--danger: #ff4757`, `--success: #2ed573`, `--purple: #a55eea`.

### 8.1 Header (Extended)

- Logo: "LAICIs v2.0" with tagline "Detect. Quantify. Query. Protect."
- Stat pills (left): Total Scans, Deepfakes Found, Scammers ID'd
- **NEW:** Loss Prevented (RM) — cumulative prevention value, color-coded (green/blue/purple)
- **NEW:** Risk Tier Breakdown — mini bar showing % of scans in each risk tier
- **SECURITY:** Security status indicator (green/yellow/red) — top-right corner
- **SECURITY:** Role badge — next to username, color-coded by role
- **SECURITY:** Session timer — countdown to 30-minute timeout (hidden until 5-minute warning)

### 8.2 Security Incident Banner (NEW)

- Full-width red banner below header
- Only visible when SEV-1 or SEV-2 security incident is active
- Content: "SECURITY INCIDENT: [description]. [Recommended action]. Click for details."
- Auto-dismisses when incident is resolved

### 8.3 Market Intelligence Panel (NEW)

- Full-width card below header (or banner)
- 3-column grid of 7 stat pills (Section 5.3)
- "Last updated: [date]" from OSINT automation
- Auto-refresh when OSINT pipeline completes

### 8.4 Upload Zone + Detection Results (Enhanced)

**Upload Zone:**
- Drag-and-drop area with file type icons
- File extension whitelist enforcement (Section 7.3)
- Consent notice: "By uploading media, you consent to LAICIs processing this file for deepfake detection and recording anonymized scan metadata."
- Segment selector dropdown (bank/corporate/government/sme/individual)
- Context input field (optional — "marketplace seller photo", "KYC onboarding", etc.)

**Detection Results (Enhanced):**
- Conic-gradient result circle (existing — detection score 0–1)
- **NEW:** Risk tier badge (LOW=green, MODERATE=yellow, HIGH=orange, CRITICAL=red)
- **NEW:** Estimated exposure (RM) — large font display
- **NEW:** Scam category tag/chip
- **NEW:** Prevention value (RM) — accent color
- **NEW:** Scammer match alert banner (if found in Scammers DB)
- **NEW:** Recovery recommendation snippet with "View Recovery Plan" button (if risk_tier >= HIGH)
- Component scores breakdown (existing — 5 modules)
- 7-step workflow visualization (new — steps highlighted during processing)

### 8.5 Detection Engine Status + Scan History (Enhanced)

**Detection Engine Status:**
- 5 module status cards: Sightengine (cloud), ELA (local), ML (local), Gemini (cloud), WeightedScorer
- Each card: module name, status (active/inactive/partial), latency, last run
- Scoring algorithm display: shows which weighting formula was used

**Scan History (Enhanced):**
- Sortable table: Date, Media Type, Score, Is AI?, **NEW:** Risk Tier, **NEW:** Exposure (RM), **NEW:** Scam Category
- Pagination: 10 records per page (latest first)
- Click row to expand full scan details (all 22 fields)
- "View Recovery Plan" button for scans with risk_tier >= HIGH

### 8.6 Scammer Database Search (Enhanced)

- Search bar: email, phone, website, scam type
- Results table: ID, Email, Phone, Website, Scam Type, Reports, **NEW:** Total Known Losses, **NEW:** Case Count, **NEW:** Risk Level
- Color-coded risk level badges (LOW=green, MEDIUM=yellow, HIGH=orange, CRITICAL=red)
- Click row to expand full scammer profile (all 16 fields)

### 8.7 Pricing & ROI Calculator (NEW)

- Interactive widget card (right column, below scammer search)
- Inputs: segment dropdown, volume slider, loss input, tier dropdown
- Outputs: ROI ratio, cost breakdown, prevention estimate, comparison, payback period
- "Save Calculation" and "Export as PDF" buttons

### 8.8 Data User Portal (NEW)

- Tab: "Data Portal" in dashboard navigation
- Sub-tabs: "Query Scans" | "Query Scammers" | "Ask the Knowledge Base"
- Left sidebar: filter controls
- Main area: results table (paginated, sortable) or chat interface
- Top bar: "Export CSV" and "Export JSON" buttons
- **SECURITY:** Access controlled by RBAC (Viewer: read-only, no export; API User: no access)

### 8.9 Compliance & Audit (NEW)

- Tab: "Compliance & Audit" in dashboard navigation
- Sub-tabs: "Generate Report" | "Audit Trail"
- Generate Report: report type selector, date range, "Generate" button, in-line display + PDF/CSV download
- Audit Trail: searchable/filterable table (Admin only)
- **SECURITY:** Audit Trail sub-tab hidden from non-Admin roles

### 8.10 Scenario Planner (NEW)

- Tab: "Scenario Planner" in dashboard navigation
- Input form: scenario type, target, channel, audience, segment
- Results: projected exposure (RM), response playbook (timeline), notification template, historical precedents
- "Save Scenario" and "Export Playbook as PDF" buttons
- **SECURITY:** Access controlled by RBAC (Admin and Analyst only)

---

## 9. User Stories Backlog

### Epic 1: Financial Intelligence (FINANCE)

| US# | Story | Persona | Priority |
|-----|-------|---------|----------|
| FIN-001 | As a fraud analyst, I want every scan to display an estimated RM exposure so I can prioritize response. | Aisha | P1 |
| FIN-002 | As a security manager, I want a cumulative loss prevention tracker so I can report value to my board. | Sarah | P1 |
| FIN-003 | As a prospect, I want a pricing calculator so I can see ROI before committing. | All | P2 |
| FIN-004 | As a police officer, I want national scam statistics on the dashboard so I can brief superiors. | Rahman | P1 |
| FIN-005 | As a fraud analyst, I want scammer profiles to show historical loss data so I can assess threat level. | Aisha | P1 |
| FIN-006 | As a security manager, I want to simulate deepfake scenarios so I can prepare response plans. | Sarah | P2 |
| FIN-007 | As a fraud analyst, I want recovery guidance when a deepfake is confirmed so I don't miss critical steps. | Aisha | P2 |
| FIN-008 | As a security manager, I want notification templates so I can communicate quickly during an incident. | Sarah | P2 |

### Epic 2: Data Efficiency (DATA)

| US# | Story | Persona | Priority |
|-----|-------|---------|----------|
| DAT-001 | As a data analyst, I want to filter and export scan results as CSV so I can build my own reports. | Dev | P2 |
| DAT-002 | As a police officer, I want to ask natural-language questions about scam statistics so I don't read full reports. | Rahman | P2 |
| DAT-003 | As a data analyst, I want the knowledge base to auto-update with OSINT so my queries are current. | Rahman | P1 |
| DAT-004 | As a data analyst, I want JSON API access to scan data so I can integrate with my tools. | Dev | P2 |
| DAT-005 | As a data analyst, I want the Financial Overview database to aggregate all scan data for trend analysis. | Dev | P1 |
| DAT-006 | As a fraud analyst, I want to filter scans by date and risk tier for BNM reporting. | Aisha | P2 |
| DAT-007 | As a data analyst, I want the dashboard to sync with databases in real-time so I see current data. | Dev | P2 |

### Epic 3: Security (SECURITY)

| US# | Story | Persona | Priority |
|-----|-------|---------|----------|
| SEC-001 | As a security manager, I want OAuth authentication so only authorized users access the platform. | Sarah | P1 |
| SEC-002 | As a security manager, I want role-based access control so team members see only what they need. | Sarah | P1 |
| SEC-003 | As a security manager, I want input validation (file whitelist, magic bytes) so attackers can't upload malicious files. | Sarah | P1 |
| SEC-004 | As a security manager, I want output sanitization (HTML escaping) so XSS attacks are prevented. | Sarah | P1 |
| SEC-005 | As a police officer, I want an audit trail of every action so evidence is admissible in court. | Rahman | P1 |
| SEC-006 | As a security manager, I want a security status indicator so I know the platform's security state at a glance. | Sarah | P2 |
| SEC-007 | As a security manager, I want incident response playbooks so I can respond to security events systematically. | Sarah | P2 |
| SEC-008 | As a security manager, I want quarterly vulnerability scanning so we proactively identify weaknesses. | Sarah | P2 |

### Epic 4: Compliance (FINANCE + SECURITY)

| US# | Story | Persona | Priority |
|-----|-------|---------|----------|
| COM-001 | As a fraud analyst, I want to generate BNM compliance reports with one click so I meet regulatory deadlines. | Aisha | P2 |
| COM-002 | As a police officer, I want a PDRM intelligence brief generated with one click so I can brief superiors. | Rahman | P2 |
| COM-003 | As a security manager, I want a board governance report so I can present quarterly results. | Sarah | P2 |
| COM-004 | As a police officer, I want the audit trail exportable as CSV for chain-of-custody in legal proceedings. | Rahman | P2 |
| COM-005 | As a security manager, I want STRIDE and OWASP compliance documented for board assurance. | Sarah | P2 |

---

## 10. Non-Functional Requirements

### 10.1 Performance

| Metric | Target |
|--------|--------|
| Image scan (full 7-step pipeline) | < 30 seconds end-to-end |
| Video scan (full 7-step pipeline) | < 120 seconds end-to-end |
| ELA analysis | < 5 seconds single image |
| ML inference | < 10 seconds single image |
| Sightengine API call | < 60 seconds (image), < 120 seconds (video) |
| Gemini full cycle | < 90 seconds (upload + poll + transcribe + analyze) |

| Metric | Target |
|--------|--------|
| Dashboard initial load | < 3 seconds first contentful paint |
| Data portal query (10K records) | < 5 seconds filtered + paginated |
| RAG Q&A response | < 10 seconds query to answer |
| CSV export (5K records) | < 10 seconds query to download |
| Compliance report generation | < 15 seconds report type + date range to output |
| Database↔dashboard sync | < 5 seconds scan completion to UI update |

### 10.2 Usability

- Dashboard requires no training for basic scan upload and result viewing
- Data portal requires minimal training (clear filter UI, tooltips on hover)
- RAG Q&A requires no training (natural language input, suggested questions)
- Compliance report generation requires only date range + report type selection
- All new features accessible from dashboard tabs (no separate applications)
- Recovery Assistant provides step-by-step guidance (checkboxes for tracking progress)
- Scenario Planner provides pre-filled templates and historical precedents

### 10.3 Accessibility

- WCAG 2.1 Level AA target
- Keyboard navigation for all dashboard tabs and features
- Screen reader compatible (semantic HTML, ARIA labels on all interactive elements)
- Color contrast ratio: 4.5:1 minimum (dark theme already compliant — white text on #0a0e1a)
- All interactive elements have focus indicators (accent color outline)
- Risk tier colors include text labels (not color-only — LOW/MODERATE/HIGH/CRITICAL text on colored badge)

### 10.4 Security

- API key storage: environment variables only (never in code, never in database)
- User authentication: WorkBuddy platform OAuth 2.0 (inherited)
- Data encryption: WorkBuddy platform TLS in transit (inherited)
- Audit logging: every data access, scan, query, export, report generation logged
- PDPA compliance: no personal data stored without consent; media not persisted
- Input validation: file type whitelist, size limit 50MB, path sanitization, magic bytes
- Output sanitization: HTML escaping on all user-facing output, API response filtering, error truncation
- Rate limiting: Sightengine 10/5min enforced; API tier 100/5min configurable
- Session management: 30-minute timeout, sliding expiration, 5-failure lockout

### 10.5 Localization

- Primary language: English (UI text, reports, RAG Q&A)
- Secondary (Phase 4): Bahasa Malaysia, Simplified Chinese
- Currency: Malaysian Ringgit (RM) throughout — no USD or other currencies
- Date format: DD/MM/YYYY (Malaysian standard)
- Time zone: Malaysia Time (UTC+8) for all timestamps
- Phone numbers: Malaysian format (+60 or 03/01 prefixes)
- Regulatory references: Malaysian only (BNM, PDRM, MCMC, CyberSecurity Malaysia, PDPA, CMA)

---

## 11. Dependencies

### 11.1 External API Dependencies

| API | Purpose | Required for MVP? | Fallback |
|-----|---------|-------------------|----------|
| Sightengine | Image/video AI detection | No (but primary) | ELA + ML model |
| Gemini | Video transcription & analysis | No (video only) | 100% Sightengine visual |
| WorkBuddy Library | Database storage, RAG search, automation, publishing | Yes (native) | None — platform requirement |
| WorkBuddy Cloud Service | Keyless LLM calls (optional) | No | Direct Gemini API |

### 11.2 Internal Dependencies

| Component | Dependency | Status |
|-----------|------------|--------|
| DORMATHON26_TECHBENG library space | spaceId: CSfJ5htmA2LY98nVeDfVD3 | Exists |
| Scans database | nodeId: fCCH5jUKxdxaQbWoVbiRVx | Exists (15 fields, needs +7) |
| Scammers database | nodeId: w7KwBxeUOZpa2WFiUJRqaB | Exists (11 fields, needs +5) |
| Financial Overview database | New — to be created | Needs creation (9 fields) |
| OSINT automation | ID: 2453f597-10da-4990-9203-06669db4c19d | Exists, needs configuration update |
| Dashboard HTML | Published at workbuddy.cc | Exists, needs enhancement |
| Data knowledge base node | Exists but empty | Needs population |
| Finance knowledge base node | Exists but empty | Needs population |

### 11.3 Skill Dependencies

| Skill | Purpose |
|-------|---------|
| `library` | Database operations, RAG search, doc creation, editing |
| `cloud-service` | Optional keyless LLM API (alternative to direct Gemini) |
| `sites` | Dashboard deployment and publishing to workbuddy.cc |

### 11.4 Environment Variables

| Variable | Purpose | Required |
|----------|---------|----------|
| `SIGHTENGINE_USER` | Sightengine API user | For full detection |
| `SIGHTENGINE_SECRET` | Sightengine API secret | For full detection |
| `GEMINI_API_KEY` | Google Gemini API key | For video analysis |
| `VERIGUARD_MODEL_PATH` | Path to ML model weights | For ML inference |
| `WORKBUDDY_CONFIG_DIR` | WorkBuddy auth config path | For library scripts |

---

## 12. Acceptance Criteria

### 12.1 Financial Acceptance Criteria

- [ ] Every scan result displays: risk_tier, estimated_exposure_rm, scam_category, prevention_value_rm
- [ ] Risk tier mapping is correct at all 4 tiers and boundary values (0.3, 0.5, 0.8)
- [ ] Prevention value equals 25% of the scam category average loss
- [ ] Loss prevention tracker updates within 5 seconds of scan completion
- [ ] Loss prevention tracker color changes at RM 100K (green→blue) and RM 1M (blue→purple)
- [ ] Market Intelligence Panel displays all 7 statistics with correct values and source attributions
- [ ] Market Intelligence Panel auto-updates when OSINT automation runs
- [ ] Pricing calculator produces ROI for all 5 customer segments
- [ ] Scenario Planner produces projected_exposure_rm for all 4 scenario types
- [ ] Scenario Planner response playbook includes all 3 time windows (0–4h, 4–48h, 1–30d)
- [ ] Recovery Assistant provides actionable steps for all 7 scam types
- [ ] Recovery Assistant regulatory filing deadlines are correct (BNM 24h, PDRM 48h, MCMC 72h)
- [ ] Recovery Assistant contact directory includes all 6 Malaysian contacts
- [ ] Scans database has all 22 fields (15 original + 7 financial)
- [ ] Scammers database has all 16 fields (11 original + 5 financial)
- [ ] Financial Overview database has all 9 fields and updates after every scan
- [ ] Finance knowledge base node contains all 6 sections with complete content

### 12.2 Data Acceptance Criteria

- [ ] Data portal supports filtering by all Scans database fields (22 fields)
- [ ] Data portal supports filtering by all Scammers database fields (16 fields)
- [ ] Results are paginated at 50 records per page
- [ ] Sorting works on all columns (ascending and descending)
- [ ] CSV export produces valid CSV with header row and all filtered records
- [ ] JSON export produces valid JSON array with all filtered records
- [ ] Export respects all active filters in the data portal
- [ ] Export supports up to 10,000 records per export
- [ ] RAG Q&A returns answers with source citations for 80%+ of queries
- [ ] RAG Q&A response time < 10 seconds per query
- [ ] 8 suggested questions displayed by default in RAG Q&A
- [ ] OSINT automation runs daily at 9 AM Malaysia time
- [ ] OSINT pipeline extracts structured data and appends to Data knowledge base node
- [ ] Financial Overview database updates after OSINT run
- [ ] Market Intelligence Panel refreshes after OSINT run
- [ ] Dashboard header counters update within 5 seconds of scan completion
- [ ] Scan History table prepends new records without page reload
- [ ] Page↔database relation bindings configured for all synced elements
- [ ] Data knowledge base node contains all 7 sections with complete content
- [ ] Media files are NOT persisted (processed in-memory, discarded)
- [ ] Audit trail retained for 7 years
- [ ] OSINT raw data purged after 90 days

### 12.3 Security Acceptance Criteria

- [ ] OAuth 2.0 authentication is required for all dashboard access
- [ ] API keys are 256-bit, hashed (SHA-256), and rotated every 30 days
- [ ] Session timeout occurs after 30 minutes of inactivity with 5-minute warning
- [ ] Account locks after 5 consecutive failed login attempts (15-minute auto-unlock)
- [ ] 4 roles defined (Admin, Analyst, Viewer, API User) with exact permissions specified
- [ ] Role badge displays in dashboard header for all authenticated users
- [ ] Unauthorized sections hidden from navigation (not just disabled)
- [ ] API endpoints return HTTP 403 for insufficient permissions
- [ ] File extension whitelist enforces only allowed image and video formats
- [ ] File size limit of 50 MB enforced
- [ ] Path sanitization strips all directory traversal sequences
- [ ] Magic bytes verification rejects files whose content doesn't match extension
- [ ] `escapeHtml()` utility applied to all user-facing HTML output
- [ ] API responses do not contain raw responses, file paths, API keys, or tracebacks
- [ ] Error messages truncated to 200 characters for user display
- [ ] Audit trail logs all 14 action types with 7 fields each
- [ ] Audit trail is append-only and immutable
- [ ] Audit trail is searchable and filterable by Admin only
- [ ] Security status indicator displays correctly (green/yellow/red/gray)
- [ ] Session timeout warning appears at 25 minutes
- [ ] Security incident banner appears for SEV-1 and SEV-2 incidents
- [ ] Audit trail tab visible to Admin only
- [ ] All 6 STRIDE threats documented with specific mitigations
- [ ] All 10 OWASP Top 10 (A01–A10) addressed with specific mitigations
- [ ] 4 severity levels defined with correct response times
- [ ] 7-step incident response playbook documented
- [ ] 10 incident detection triggers implemented
- [ ] Quarterly dependency scanning documented
- [ ] Code review required before merge (minimum 1 approval)

### 12.4 Compliance Acceptance Criteria

- [ ] BNM Fraud Report includes: scan count, deepfake count, total exposure, prevention value, risk tier breakdown, scammer profiles, audit trail summary
- [ ] PDRM Intelligence Brief includes: national statistics, case trends, scammer profiles, OSINT summary
- [ ] Board Governance Report includes: loss prevention, ROI metrics, STRIDE/OWASP compliance status
- [ ] Audit Trail Log exports as CSV with all entries in selected date range
- [ ] All report generation logged to audit trail
- [ ] Reports accessible to correct roles (BNM/PDRM: Analyst+Admin, Board/Audit: Admin only)
- [ ] Chain-of-custody: every scan, query, export, and report generation has audit trail entry

---

## 13. Out of Scope

The following items are explicitly out of scope for LAICIs v2.0 and deferred to v3.0 or later:

**Technical:**
- Mobile native app (iOS/Android) — web dashboard is responsive in Phase 4
- Real-time video stream analysis (live deepfake detection during video calls) — future v3.0
- Custom ML model training pipeline — Phase 4 fine-tuning on Malaysian data only
- GPU-accelerated ML inference — CPU-only in v2.0 due to hardware constraints
- WebSocket real-time push notifications — polling-based sync in v2.0

**Business:**
- Multi-country expansion (Singapore, Thailand, Indonesia) — future v3.0
- Automated deepfake generation for red-teaming — out of scope (detection only)
- Direct payment processing / billing integration — pricing tiers are informational in v2.0
- Customer self-service signup and provisioning — manual onboarding in v2.0

**Security:**
- Blockchain-based evidence storage — future consideration
- Integration with third-party SIEM/SOAR platforms — future API tier feature
- Biometric authentication (fingerprint, face unlock) — OAuth 2.0 is sufficient in v2.0
- Zero-trust network architecture — WorkBuddy platform security inherited in v2.0

**Data:**
- Multi-language knowledge base content (BM, CN) — English only in v2.0, Phase 4 for BM/CN
- Real-time streaming data ingestion (Kafka/Kinesis) — batch OSINT pipeline in v2.0
- Data warehouse / OLAP cube — WorkBuddy Library databases sufficient in v2.0
- Machine learning-powered anomaly detection on scan patterns — future v3.0

---

## Document Approval

This Product Requirements Document defines the complete feature-level specifications for LAICIs v2.0 across three domains — Finance, Data, and Security. It translates the business goals from the BRD into actionable product features, user stories, and acceptance criteria.

**Prepared by:** TECHBENG Team
**Date:** January 2026
**Document covers:** 13 sections, 25 feature specifications (8 FINANCE + 7 DATA + 10 SECURITY), 4 user personas, 4 epic backlogs (28 user stories), 10 dashboard sections, 5 NFR categories, 4 dependency categories, 4 acceptance criteria groups, and out-of-scope boundaries.
**Next Steps:** Proceed to System Requirements Document (SRD) for architecture and infrastructure specifications, and Software Requirements Specification (SRS) for detailed module-level implementation.
