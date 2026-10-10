# LAICIs V6.2 — Track 2 Focused Frontend

This is a slimmed-down edit of V6.1, based on the DORMATHON 2026 Track 2 criteria (pages 27, 31–32).

## Included
- `index.html`: landing message, unified Smart Detection for file/URL/text, agent execution status, how-the-agent-works shelf, limitations and privacy FAQ.
- `results.html`: report/results layout. Actual verified findings require integration.
- `mobile.html`: detection-only mobile UI (no dashboard).
- `extension/`: optional minimal browser extension launcher (not a scanning engine).
- Anime.js powered scroll animations; reduced motion supported.

## Removed
- Desktop dashboard and fake sample statistics/history.
- Unnecessary platform-marketing sections, generic features section and lengthy sales case cards.
- Unused scripts and old reference image.

## Run
Extract the ZIP; open `index.html` on desktop and `mobile.html` on phone-sized viewport. For reliable development use a local server, e.g. `python -m http.server 8000` from this folder, then open `http://localhost:8000`.

## Agent integration
Set `window.LAICIs_CONFIG.agentApiUrl` in `config.js` after coordinating the live WorkBuddy-driven endpoint with your backend team; refer to `TRACK2-INTEGRATION.md`. The frontend alone does not constitute agentic execution, nor does the included extension actually classify media.

Submission still requires public GitHub, deployed URL, slide PDF and team/campus by 11 October 2026 09:30 MYT.
