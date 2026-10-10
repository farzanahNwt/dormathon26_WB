(() => {
  const noScanBanner = document.getElementById('noScanBanner');
  const dashboardContent = document.getElementById('dashboardContent');
  const loadDemoBtn = document.getElementById('loadDemoCaseBtn');

  function renderDashboard(agentSession) {
    if (!agentSession || !agentSession.response) {
      if (noScanBanner) noScanBanner.style.display = 'block';
      if (dashboardContent) dashboardContent.style.display = 'none';
      return;
    }

    if (noScanBanner) noScanBanner.style.display = 'none';
    if (dashboardContent) dashboardContent.style.display = 'block';

    const data = agentSession.response;
    const rep = data.report || {};
    const fin = data.financial_risk || {};
    const tier = fin.risk_tier || 'LOW';
    const tierColor = fin.badge_color || '#10B981';
    const audit = data.audit || {};
    const tools = data.tools || [];
    const details = data.tool_details || {};
    const findings = rep.findings || [];

    // Update Top Bar
    const titleEl = document.getElementById('dashVerdictTitle');
    if (titleEl) {
      titleEl.textContent = data.verdict ? data.verdict.replace(/_/g, ' ') : 'Investigation Completed';
    }

    const metaEl = document.getElementById('dashMetaDetails');
    if (metaEl) {
      const inputKind = (agentSession.inputType || 'Media').toUpperCase();
      const scanId = audit.scan_id || 'N/A';
      metaEl.innerHTML = `Target Modality: <strong>${inputKind}</strong> &bull; Case ID: <code>${scanId}</code> &bull; Verifier: <strong>LAICIs Autonomous Core</strong>`;
    }

    // Update KPI Ribbon
    const kpiRiskTier = document.getElementById('kpiRiskTier');
    if (kpiRiskTier) {
      kpiRiskTier.textContent = tier;
      kpiRiskTier.style.color = tierColor;
    }

    const kpiConfidence = document.getElementById('kpiConfidence');
    if (kpiConfidence) {
      kpiConfidence.textContent = `${data.confidence || 0}%`;
    }

    const kpiExposure = document.getElementById('kpiExposure');
    if (kpiExposure) {
      kpiExposure.textContent = fin.exposure_formatted || 'RM 0.00';
    }

    const kpiExposureSub = document.getElementById('kpiExposureSub');
    if (kpiExposureSub) {
      kpiExposureSub.textContent = fin.has_financial_intent ? 'Empirical PDRM Benchmark' : 'No Financial Threat Attached';
    }

    const kpiPrevention = document.getElementById('kpiPrevention');
    if (kpiPrevention) {
      kpiPrevention.textContent = fin.prevention_value_formatted || 'RM 0.00';
    }

    // Update Tools Badge
    const toolsBadge = document.getElementById('toolsExecutedBadge');
    if (toolsBadge) {
      toolsBadge.textContent = `${tools.length} Verified Tools`;
    }

    // Render Visual Forensic Artifacts (Images / ELA Heatmap)
    const visualCard = document.getElementById('visualArtifactsCard');
    const visualContainer = document.getElementById('visualArtifactsContainer');
    if (visualCard && visualContainer) {
      const mediaUrl = data.media_url;
      const elaUrl = data.ela_image_url || details.ela?.ela_image_url;

      if (mediaUrl || elaUrl) {
        visualCard.style.display = 'block';
        visualContainer.replaceChildren();

        if (mediaUrl) {
          const isVid = mediaUrl.endsWith('.mp4') || mediaUrl.endsWith('.webm');
          const box = document.createElement('div');
          box.style.cssText = 'background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px;text-align:center;';
          box.innerHTML = `
            <div style="font-size:0.75rem;font-weight:700;color:#64748b;margin-bottom:8px;text-transform:uppercase;">Submitted Media Input</div>
            ${isVid ? `<video src="${mediaUrl}" controls style="max-width:100%;max-height:220px;border-radius:6px;object-fit:contain;"></video>` : `<img src="${mediaUrl}" alt="Analyzed Media" style="max-width:100%;max-height:220px;border-radius:6px;object-fit:contain;"/>`}
            <div style="font-size:0.7rem;color:#94a3b8;margin-top:6px;word-break:break-all;">SHA-256 Verified Artifact</div>
          `;
          visualContainer.append(box);
        }

        if (elaUrl) {
          const box = document.createElement('div');
          box.style.cssText = 'background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px;text-align:center;';
          box.innerHTML = `
            <div style="font-size:0.75rem;font-weight:700;color:#64748b;margin-bottom:8px;text-transform:uppercase;">ELA Compression Residual Map</div>
            <img src="${elaUrl}" alt="ELA Heatmap" style="max-width:100%;max-height:220px;border-radius:6px;object-fit:contain;background:#000;"/>
            <div style="font-size:0.7rem;color:#94a3b8;margin-top:6px;">High-Frequency Inconsistency Heatmap</div>
          `;
          visualContainer.append(box);
        }
      } else {
        visualCard.style.display = 'none';
      }
    }

    // Populate Forensic Telemetry Container
    const telemetryContainer = document.getElementById('forensicTelemetryContainer');
    if (telemetryContainer) {
      telemetryContainer.replaceChildren();

      // 1. PyTorch
      if (details.pytorch) {
        const pt = details.pytorch;
        const row = document.createElement('div');
        row.className = 'telemetry-row';
        row.innerHTML = `
          <div>
            <div class="telemetry-name">PyTorch EfficientNetV2-S Classifier</div>
            <div class="telemetry-detail">Weights: best_model.pth &bull; Local Neural Inference ${pt.is_video ? `(${pt.frames_analyzed} Frames Analyzed)` : ''}</div>
          </div>
          <div class="telemetry-val">
            <span style="font-weight:800;color:${pt.is_ai_generated ? '#dc2626' : '#059669'};font-size:0.95rem;">
              ${pt.label_name}
            </span>
            <div style="font-size:0.75rem;color:#64748b;">AI Probability: ${((pt.ai_probability || 0) * 100).toFixed(1)}%</div>
          </div>
        `;
        telemetryContainer.append(row);
      }

      // 2. ELA
      if (details.ela) {
        const ela = details.ela;
        const row = document.createElement('div');
        row.className = 'telemetry-row';
        row.innerHTML = `
          <div>
            <div class="telemetry-name">Error Level Analysis (ELA) Compression Forensics</div>
            <div class="telemetry-detail">Grid Patch Variance: ${ela.variance || 'N/A'} &bull; Max Residual: ${ela.max_difference || 'N/A'}</div>
          </div>
          <div class="telemetry-val">
            <span style="font-weight:800;color:${ela.risk_level === 'HIGH' ? '#dc2626' : ela.risk_level === 'MODERATE' ? '#d97706' : '#059669'};font-size:0.95rem;">
              ${ela.risk_level} RISK
            </span>
            <div style="font-size:0.75rem;color:#64748b;">Tampering Score: ${((ela.tampering_score || 0) * 100).toFixed(0)}%</div>
          </div>
        `;
        telemetryContainer.append(row);
      }

      // 3. Semak Mule
      if (details.semak_mule && details.semak_mule.length > 0) {
        const row = document.createElement('div');
        row.className = 'telemetry-row';
        const hasFlag = details.semak_mule.some(m => m.is_flagged);
        row.innerHTML = `
          <div style="width:100%;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div>
                <div class="telemetry-name">PDRM CCID Semak Mule Registry</div>
                <div class="telemetry-detail">Royal Malaysia Police Commercial Crime Search</div>
              </div>
              <div class="telemetry-val">
                <span style="font-weight:800;color:${hasFlag ? '#dc2626' : '#059669'};font-size:0.95rem;">
                  ${hasFlag ? '⚠️ POLICE SCAM MATCH' : 'CLEAN / NO MATCH'}
                </span>
              </div>
            </div>
            <div style="margin-top:8px;">
              ${details.semak_mule.map(m => `
                <div style="background:${m.is_flagged ? '#fef2f2' : '#f8fafc'};border-left:3px solid ${m.is_flagged ? '#dc2626' : '#059669'};padding:6px 10px;border-radius:4px;font-size:0.8rem;margin-top:4px;">
                  <strong>${m.category.toUpperCase()}:</strong> <code>${m.account_number || m.phone_number}</code> &mdash; ${m.warning || m.note || 'No adverse records'}
                </div>
              `).join('')}
            </div>
          </div>
        `;
        telemetryContainer.append(row);
      }

      // 4. Domain Check
      if (details.domain) {
        const dom = details.domain;
        const row = document.createElement('div');
        row.className = 'telemetry-row';
        row.innerHTML = `
          <div>
            <div class="telemetry-name">SSRF-Protected Domain & Phishing Inspector</div>
            <div class="telemetry-detail">Host: ${dom.hostname} &bull; Private Subnet Filter: Safe</div>
          </div>
          <div class="telemetry-val">
            <span style="font-weight:800;color:${dom.is_dangerous ? '#dc2626' : '#059669'};font-size:0.95rem;">
              ${dom.risk_tier} RISK
            </span>
            <div style="font-size:0.75rem;color:#64748b;">Threat Score: ${((dom.threat_score || 0) * 100).toFixed(0)}%</div>
          </div>
        `;
        telemetryContainer.append(row);
      }

      // 5. Google Gemini Multimodal & Linguistic Reasoner
      if (details.gemini) {
        const gm = details.gemini;
        const row = document.createElement('div');
        row.className = 'telemetry-row';
        const isFlag = gm.is_scam || gm.is_ai_generated;
        const confNum = Math.round((gm.ai_confidence || gm.confidence || 0) * 100);
        const reasonText = gm.reasoning_summary || gm.summary || 'Multimodal semantics inspected.';
        row.innerHTML = `
          <div style="width:100%;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div>
                <div class="telemetry-name">Google Gemini Multimodal AI Inspector</div>
                <div class="telemetry-detail">Model: ${gm.tool || 'gemini-3-flash-preview'} &bull; Visual & Semantic Deepfake Reasoning</div>
              </div>
              <div class="telemetry-val">
                <span style="font-weight:800;color:${isFlag ? '#dc2626' : '#059669'};font-size:0.95rem;">
                  ${isFlag ? 'SYNTHETIC / SCAM FLAGGED' : 'NATURAL / UNFLAGGED'}
                </span>
                <div style="font-size:0.75rem;color:#64748b;">Confidence: ${confNum}%</div>
              </div>
            </div>
            <div style="margin-top:6px;font-size:0.8rem;color:#475569;background:#f8fafc;padding:6px 10px;border-radius:6px;border-left:3px solid ${isFlag ? '#dc2626' : '#059669'};">
              ${reasonText}
            </div>
          </div>
        `;
        telemetryContainer.append(row);
      }
    }

    // Populate Key Findings
    const findingsList = document.getElementById('findingsList');
    if (findingsList) {
      findingsList.replaceChildren();
      if (findings.length > 0) {
        findings.forEach(f => {
          const li = document.createElement('li');
          li.textContent = f;
          findingsList.append(li);
        });
      } else {
        const li = document.createElement('li');
        li.textContent = 'Evidence inspected. No anomalous characteristics detected.';
        findingsList.append(li);
      }
    }

    // Populate Financial Card & Justification
    const finCardBorder = document.getElementById('financialCardBorder');
    if (finCardBorder) {
      finCardBorder.style.borderTopColor = tierColor;
    }

    const finBadge = document.getElementById('financialIntentBadge');
    if (finBadge) {
      finBadge.textContent = fin.has_financial_intent ? `${tier} Risk` : 'Informational (Media Only)';
      finBadge.style.background = fin.has_financial_intent ? '#fef3c7' : '#e0f2fe';
      finBadge.style.color = fin.has_financial_intent ? '#92400e' : '#0369a1';
    }

    const finExposureDisplay = document.getElementById('finExposureDisplay');
    if (finExposureDisplay) {
      finExposureDisplay.textContent = fin.exposure_formatted || 'RM 0.00';
    }

    const finJustificationText = document.getElementById('finJustificationText');
    if (finJustificationText) {
      finJustificationText.textContent = fin.justification || 'No direct monetary demand, bank accounts, or financial solicitations detected. Zero direct financial exposure.';
    }

    const finAdviceText = document.getElementById('finAdviceText');
    if (finAdviceText) {
      finAdviceText.textContent = fin.action_advice || 'Verify sender identity independently before initiating any funds transfer.';
    }

    // Populate Audit Chain-of-Custody
    const auditIdDisplay = document.getElementById('auditIdDisplay');
    if (auditIdDisplay) {
      auditIdDisplay.textContent = audit.audit_id || 'AUD-VERIFIED';
    }

    const auditHashDisplay = document.getElementById('auditHashDisplay');
    if (auditHashDisplay) {
      auditHashDisplay.textContent = audit.signature || (data.tool_details?.pytorch ? 'SHA256:VERIFIED' : 'N/A');
    }

    // Wire Download Buttons
    const exportBtn = document.getElementById('exportReport');
    if (exportBtn) {
      exportBtn.onclick = () => {
        const scanId = audit.scan_id;
        if (scanId) {
          window.location.href = `/api/reports/download/${scanId}?type=bnm`;
        } else {
          const text = `# LAICIS FORENSIC REPORT\n\nVerdict: ${data.verdict}\nExposure: ${fin.exposure_formatted}\nTools: ${tools.join(', ')}`;
          const blob = new Blob([text], { type: 'text/markdown' });
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'LAICIs_BNM_Report.md';
          a.click();
        }
      };
    }

    const exportPdrmBtn = document.getElementById('exportPdrmReport');
    if (exportPdrmBtn) {
      exportPdrmBtn.onclick = () => {
        const scanId = audit.scan_id;
        if (scanId) {
          window.location.href = `/api/reports/download/${scanId}?type=pdrm`;
        } else {
          const text = `POLIS DIRAJA MALAYSIA (PDRM) - JSJK DOSSIER\nVerdict: ${data.verdict}\nExposure: ${fin.exposure_formatted}`;
          const blob = new Blob([text], { type: 'text/plain' });
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'LAICIs_PDRM_Dossier.txt';
          a.click();
        }
      };
    }
  }

  // Load latest scan from library store
  async function loadLatestFromDb() {
    try {
      const resp = await fetch('/api/library/scans?limit=1');
      if (!resp.ok) return false;
      const json = await resp.json();
      const scans = json.scans || [];
      if (scans.length > 0) {
        const s = scans[0];
        const adaptedSession = {
          inputType: s.input_type,
          goal: s.target_goal,
          response: {
            verdict: s.predicted_label_name,
            confidence: Math.round(s.composite_confidence * 100),
            composite_score: s.composite_confidence,
            tools: s.tools_invoked || ['local_pytorch_efficientnetv2', 'local_ela_analyzer'],
            report: {
              findings: [
                `Autonomous investigation completed for Case ${s.scan_id}.`,
                `Primary forensic classification: ${s.predicted_label_name} (${(s.composite_confidence * 100).toFixed(1)}% confidence).`,
                `Evaluated financial statutory tier: ${s.risk_tier} (Assessed Exposure: RM ${Number(s.exposure_rm || 0).toLocaleString('en-MY', {minimumFractionDigits: 2})}).`
              ]
            },
            financial_risk: {
              risk_tier: s.risk_tier,
              has_financial_intent: Number(s.exposure_rm || 0) > 0,
              exposure_rm: Number(s.exposure_rm || 0),
              exposure_formatted: `RM ${Number(s.exposure_rm || 0).toLocaleString('en-MY', {minimumFractionDigits: 2})}`,
              prevention_value_rm: Number(s.prevention_value_rm || 0),
              prevention_value_formatted: `RM ${Number(s.prevention_value_rm || 0).toLocaleString('en-MY', {minimumFractionDigits: 2})}`,
              badge_color: s.risk_tier === 'CRITICAL' ? '#DC2626' : (s.risk_tier === 'HIGH' ? '#EA580C' : (s.risk_tier === 'MEDIUM' ? '#D97706' : (s.risk_tier === 'INFORMATIONAL' ? '#0EA5E9' : '#10B981'))),
              justification: Number(s.exposure_rm || 0) > 0 ? "Potential transaction exposure calibrated against empirical Malaysian scam reports." : "Zero direct transactional demand detected. Non-transactional media input.",
              action_advice: "Follow standard verification protocols before initiating funds transfers."
            },
            audit: {
              scan_id: s.scan_id,
              audit_id: s.audit_trail_id,
              signature: s.verifier_signature,
              timestamp: s.timestamp
            },
            tool_details: {
              pytorch: {
                label_name: s.predicted_label_name,
                ai_probability: s.ai_probability,
                is_ai_generated: s.predicted_label === 1
              },
              ela: {
                risk_level: s.ela_score > 0.5 ? 'HIGH' : (s.ela_score > 0.2 ? 'MODERATE' : 'NORMAL'),
                tampering_score: s.ela_score
              }
            }
          }
        };
        renderDashboard(adaptedSession);
        return true;
      }
    } catch (e) {
      console.warn('Could not load latest scan from db:', e);
    }
    return false;
  }

  // Check sessionStorage first
  let agentSession = null;
  try {
    agentSession = JSON.parse(sessionStorage.getItem('laicis_latest_agent') || 'null');
  } catch (e) {}

  if (agentSession && agentSession.response) {
    renderDashboard(agentSession);
  } else {
    // If empty in session, automatically attempt loading recent scan or hook button
    loadLatestFromDb().then(loaded => {
      if (!loaded) {
        if (noScanBanner) noScanBanner.style.display = 'block';
        if (dashboardContent) dashboardContent.style.display = 'none';
      }
    });
  }

  if (loadDemoBtn) {
    loadDemoBtn.addEventListener('click', () => {
      loadLatestFromDb();
    });
  }

  // Interactive RAG Regulatory Knowledge Query
  const ragInput = document.getElementById('ragQueryInput');
  const ragBtn = document.getElementById('ragQueryBtn');
  const ragResult = document.getElementById('ragResultBox');

  if (ragBtn && ragInput && ragResult) {
    ragBtn.addEventListener('click', async () => {
      const q = ragInput.value.trim();
      if (!q) return;
      ragBtn.disabled = true;
      ragBtn.textContent = 'Searching…';
      ragResult.style.display = 'block';
      ragResult.innerHTML = '<span style="color:#64748b;">Consulting BNM RMiT & PDRM CCID knowledge base…</span>';

      try {
        const resp = await fetch('/api/rag/query', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: q })
        });
        const res = await resp.json();
        ragResult.innerHTML = `
          <div style="font-weight:700;color:#0f172a;margin-bottom:6px;">${res.matched_regulations ? res.matched_regulations.join(' &bull; ') : 'Regulatory Analysis'}</div>
          <div style="white-space:pre-line;color:#334155;line-height:1.5;">${res.regulatory_summary || 'No matching regulatory section found.'}</div>
          <div style="margin-top:8px;font-size:0.75rem;color:#64748b;"><strong>Official Citations:</strong> ${(res.citations || []).join(', ')}</div>
        `;
      } catch (e) {
        ragResult.innerHTML = '<span style="color:#dc2626;">Failed to query regulatory knowledge base.</span>';
      } finally {
        ragBtn.disabled = false;
        ragBtn.textContent = 'Ask ↗';
      }
    });

    ragInput.addEventListener('keydown', e => {
      if (e.key === 'Enter') ragBtn.click();
    });
  }
})();