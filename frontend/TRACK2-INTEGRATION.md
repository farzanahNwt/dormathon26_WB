# LAICIs V6 — Track 2 contract

The AI Detection Agent is the **agentic component**, not the whole LAICIs product. Desktop website, browser extension and mobile are client interfaces.

## Runtime
Set `window.LAICIs_CONFIG.agentApiUrl` in `config.js` to a verified, accessible service that orchestrates the detector through WorkBuddy. **This repository contains only the frontend, not the WorkBuddy service.**

POST `multipart/form-data`:
- `input_type`: `media`, `url`, or `text`
- `file`: JPG/PNG/WEBP/MP4 up to 30 MB when media
- `content`: URL or text for other types
- `goal`: optional plain-language context

Expected JSON response example (SCHEMA ONLY — not actual findings):
```json
{
 "status":"completed",
 "summary":"Investigation completed",
 "message":"Review the limitations and independent verification steps",
 "tools":["tool-name-actually-called"],
 "steps":{"understand":"done","plan":"done","execute":"done","validate":"done","integrate":"done","deliver":"done"},
 "report":{"findings":[],"limitations":[],"recommendations":[]}
}
```
Do not report any stage as completed unless backed by an execution record. Do not return fake classifier probabilities or unsupported phishing/AI-authorship claims. For URL scanning, prevent server-side request forgery and use reputation checks without indiscriminately fetching arbitrary URLs. Establish CORS, auth, rate limits, payload checks, and retention/deletion policy.

DORMATHON Track 2 pages 31–32: one goal, dynamic planning, tool calls, validating, integrating, delivering; WorkBuddy as primary execution platform. If runtime connectivity is unavailable, demonstrate a genuine WorkBuddy-native agent run separately and disclose web limitations.
