"""
LAICIs - Tencent WorkBuddy Agent Server & Web Runtime
Serves the Track 2 Agent API (/api/agent/investigate) and hosts the LAICIs UI.
"""

import os
import sys
import tempfile
from flask import Flask, request, jsonify, send_from_directory, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename

# Ensure backend src is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Load .env configuration
env_file = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

from src.workbuddy.agent import WorkBuddyInvestigationAgent
from src.reports.generator import ReportGenerator
from src.library.store import LibraryStore
from src.rag.knowledge_base import RAGKnowledgeBase

# Locate the frontend static directory across clean and nested layouts
_frontend_candidates = [
    os.path.abspath(os.path.join(BASE_DIR, "..", "frontend")),
    os.path.abspath(os.path.join(BASE_DIR, "frontend")),
    os.path.abspath(os.path.join(BASE_DIR, "..", "LAICIs-V6.2-Track2-Focused", "LAICIs-V6.2-Track2-Focused")),
]
FRONTEND_DIR = next((p for p in _frontend_candidates if os.path.exists(p)), _frontend_candidates[0])
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=""
)
CORS(app)

# Initialize Agent & Core Services
agent = WorkBuddyInvestigationAgent()
store = LibraryStore()
rag = RAGKnowledgeBase()





# --------------------------------------------------------------------------
# TRACK 2 AGENT API ENDPOINT (matches TRACK2-INTEGRATION.md contract)
# --------------------------------------------------------------------------
@app.route("/api/agent/investigate", methods=["POST"])
def api_investigate():
    """
    POST multipart/form-data:
      - input_type: 'media' | 'url' | 'text'
      - file: binary file (when media)
      - content: string (when url or text)
      - goal: string (optional)
      - segment: 'individual' | 'sme' | 'enterprise' (optional)
    """
    json_data = request.get_json(silent=True) or {}
    input_type = (json_data.get("input_type") or request.form.get("input_type") or "media").strip().lower()
    goal = (json_data.get("goal") or request.form.get("goal") or "").strip()
    segment = (json_data.get("segment") or request.form.get("segment") or "individual").strip().lower()
    content = (json_data.get("content") or request.form.get("content") or "").strip()

    file_path = None
    file_name = ""

    if input_type == "media":
        if "file" not in request.files or not request.files["file"].filename:
            return jsonify({"status": "failed", "error": "No file uploaded for media check."}), 400

        uploaded_file = request.files["file"]
        file_name = secure_filename(uploaded_file.filename)
        file_path = os.path.join(UPLOAD_DIR, file_name)
        uploaded_file.save(file_path)

    try:
        result = agent.investigate(
            input_type=input_type,
            content=content,
            file_path=file_path,
            file_name=file_name,
            goal=goal,
            segment=segment
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "status": "failed",
            "summary": "Agent execution encountered an unhandled error",
            "message": str(e),
            "tools": [],
            "steps": {"understand": "failed"},
            "report": {
                "findings": [],
                "limitations": ["Investigation could not complete due to runtime exception."],
                "recommendations": ["Retry with valid input."]
            }
        }), 500


# --------------------------------------------------------------------------
# WORKBUDDY RUNTIME & EXTENSION APIS
# --------------------------------------------------------------------------
@app.route("/api/agent/status", methods=["GET"])
def api_status():
    """Returns runtime health and loaded agent tools."""
    return jsonify({
        "status": "online",
        "system": "LAICIs Agentic Forensic Core",
        "workbuddy_runtime": "Tencent WorkBuddy Compatible (Track 2)",
        "models": {
            "pytorch_efficientnetv2": "LOADED (best_model.pth)",
            "local_ela_analyzer": "ACTIVE",
            "pdrm_semak_mule": "ACTIVE",
            "domain_inspector": "ACTIVE (SSRF protected)"
        },
        "statistics": store.get_financial_overview()
    })


@app.route("/api/agent/tools", methods=["GET"])
def api_tools():
    """Returns list of registered WorkBuddy agent tools."""
    return jsonify({"tools": agent.tools.get_registered_tools()})


@app.route("/api/library/scans", methods=["GET"])
def api_scans():
    """Returns recent scans from the 22-field database."""
    limit = int(request.args.get("limit", 20))
    return jsonify({"scans": store.get_recent_scans(limit)})


@app.route("/api/library/scammers", methods=["GET"])
def api_scammers():
    """Returns Malaysian scam registry (16 fields)."""
    q = request.args.get("q", "")
    if q:
        return jsonify({"scammers": store.search_scammer(q)})
    return jsonify({"scammers": store.get_scammers()})


@app.route("/api/library/financial", methods=["GET"])
def api_financial():
    """Returns financial overview metrics (9 fields)."""
    return jsonify({"overview": store.get_financial_overview()})


@app.route("/api/library/audit", methods=["GET"])
def api_audit():
    """Returns cryptographic audit trail."""
    limit = int(request.args.get("limit", 20))
    return jsonify({"audits": store.get_audits(limit)})


@app.route("/api/workbuddy/manifest", methods=["GET"])
def api_manifest():
    """Returns official Tencent WorkBuddy Agent Manifest."""
    manifest_path = os.path.join(BASE_DIR, "workbuddy_manifest.json")
    if os.path.exists(manifest_path):
        import json
        with open(manifest_path, "r", encoding="utf-8") as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Manifest not found"}), 404


@app.route("/api/workbuddy/mcp", methods=["GET"])
def api_mcp():
    """Returns official Tencent WorkBuddy / CodeBuddy MCP Server configuration."""
    from src.workbuddy.tencent_sdk_bridge import build_tencent_mcp_server, LAICI_AGENT_DEFINITION
    mcp_config = build_tencent_mcp_server()
    return jsonify({
        "status": "active",
        "mcp_server": {
            "type": mcp_config.get("type", "sdk"),
            "name": mcp_config.get("name", "laici-forensics-mcp"),
            "tools_registered_count": len(LAICI_AGENT_DEFINITION.tools)
        },
        "agent_definition": {
            "description": LAICI_AGENT_DEFINITION.description,
            "prompt": LAICI_AGENT_DEFINITION.prompt,
            "tools": LAICI_AGENT_DEFINITION.tools
        }
    })


@app.route("/api/rag/query", methods=["POST"])
def api_rag():
    """Query regulatory knowledge base (BNM RMiT, MCMC, PDRM)."""
    data = request.get_json() or {}
    q = data.get("query", "").strip()
    if not q:
        return jsonify({"error": "Empty query"}), 400
    res = rag.answer_query(q)
    return jsonify(res)


@app.route("/api/reports/download/<scan_id>", methods=["GET"])
def api_download_report(scan_id):
    """Generate and return official markdown report."""
    scan = store.get_scan_by_id(scan_id)
    if not scan:
        return jsonify({"error": "Scan ID not found"}), 404

    rep_type = request.args.get("type", "bnm").lower()
    if rep_type == "pdrm":
        report_text = ReportGenerator.generate_pdrm_dossier(scan)
        filename = f"PDRM_CCID_Dossier_{scan_id}.txt"
    else:
        report_text = ReportGenerator.generate_bnm_report(scan)
        filename = f"BNM_RMiT_Report_{scan_id}.md"

    return Response(
        report_text,
        mimetype="text/markdown",
        headers={"Content-Disposition": f"attachment;filename={filename}"}
    )


# --------------------------------------------------------------------------
# STATIC FRONTEND ROUTES (Catch-all placed at bottom)
# --------------------------------------------------------------------------
@app.route("/favicon.ico")
def favicon():
    return Response(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="45" fill="#bd2949"/><circle cx="50" cy="30" r="15" fill="#255d44"/></svg>',
        mimetype="image/svg+xml"
    )


@app.route("/uploads/<path:filename>")
def serve_upload(filename):
    """Serve uploaded media and generated forensic images (e.g. ELA maps)."""
    return send_from_directory(UPLOAD_DIR, filename)


@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:path>")
def static_proxy(path):
    file_path = os.path.join(FRONTEND_DIR, path)
    if os.path.isfile(file_path):
        return send_from_directory(FRONTEND_DIR, path)
    return send_from_directory(FRONTEND_DIR, "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting LAICIs WorkBuddy Server on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
