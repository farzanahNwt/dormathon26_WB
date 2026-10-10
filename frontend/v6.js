(() => {
  const tabs = [...document.querySelectorAll('[data-kind]')];
  const panels = [...document.querySelectorAll('[data-panel]')];
  const form = document.getElementById('smartForm');
  if (!form) return;

  const el = id => document.getElementById(id);
  const preview = el('smartPreview');
  const file = el('smartFile');
  const url = el('smartUrl');
  const text = el('smartText');
  const goal = el('smartGoal');

  const badge = el('smartBadge');
  const headline = el('smartHeadline');
  const message = el('smartMessage');
  const selected = el('smartSelected');
  const result = el('smartResult');
  const submit = el('smartSubmit');

  let kind = 'media';
  let objectUrl = null;
  let selectedSegment = 'individual';
  const segmentPills = [...document.querySelectorAll('.segment-pill')];
  segmentPills.forEach(p => p.addEventListener('click', () => {
    selectedSegment = p.dataset.segment || 'individual';
    segmentPills.forEach(b => {
      const isChosen = b === p;
      b.style.background = isChosen ? 'var(--leaf)' : '#fff';
      b.style.color = isChosen ? '#fff' : 'var(--ink)';
      b.classList.toggle('chosen', isChosen);
    });
  }));
  const stages = ['understand', 'plan', 'execute', 'validate', 'integrate', 'deliver', 'financial_risk_assess'];

  function update(steps = {}) {
    stages.forEach(k => {
      const row = document.querySelector(`[data-step="${k}"]`);
      if (!row) return;
      const state = steps[k] || 'waiting';
      row.classList.remove('done', 'running', 'failed');
      if (state === 'done' || state === 'running') row.classList.add(state);
      if (state === 'error' || state === 'failed') row.classList.add('failed');
      const tag = row.querySelector('i');
      if (tag) {
        tag.textContent = state === 'done' ? 'Verified' : state === 'running' ? 'Running…' : state === 'failed' ? 'Failed' : 'Waiting';
      }
    });
  }

  function switchTab(targetKind) {
    kind = targetKind;
    tabs.forEach(b => {
      const yes = b.dataset.kind === targetKind;
      b.classList.toggle('chosen', yes);
      b.setAttribute('aria-selected', String(yes));
    });
    panels.forEach(p => p.hidden = p.dataset.panel !== targetKind);
    badge.textContent = 'AWAITING INPUT';
    headline.textContent = 'Ready to investigate.';
    message.textContent = 'WorkBuddy Agent dynamically chooses tools based on input characteristics.';
    update();
    selected.replaceChildren();
    selected.innerHTML = '<strong>Agent-selected tools</strong><p>No tools selected or executed.</p>';
    result.hidden = true;
  }

  tabs.forEach(t => t.addEventListener('click', () => {
    switchTab(t.dataset.kind);
  }));

  const presetPills = [...document.querySelectorAll('.preset-pill')];
  presetPills.forEach(pill => pill.addEventListener('click', () => {
    const pType = pill.dataset.preset;
    if (pType === 'url') {
      switchTab('url');
      url.value = 'https://fake-petronas-job.com';
      goal.value = 'Verify recruitment portal authenticity and credential-harvesting indicators.';
      url.focus();
    } else if (pType === 'text') {
      switchTab('text');
      text.value = 'URGENT: RM 4,500 required immediately. Please transfer to Maybank 564276123456 before 5:00 PM to avoid legal prosecution under PDRM warrant.';
      goal.value = 'Evaluate financial extortion and mule account risk under PDRM CCID.';
      text.focus();
    } else if (pType === 'media') {
      switchTab('media');
      goal.value = 'Verify synthetic facial features and image compression inconsistencies.';
      file.focus();
    }
  }));

  file.addEventListener('change', () => {
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = null;
    preview.replaceChildren();
    const f = file.files[0];
    if (!f) {
      preview.textContent = 'Choose an image or MP4';
      return;
    }
    if (!['image/jpeg', 'image/png', 'image/webp', 'video/mp4'].includes(f.type) || f.size > 30 * 1024 * 1024) {
      preview.textContent = 'Unsupported format or larger than 30 MB';
      return;
    }
    objectUrl = URL.createObjectURL(f);
    const node = document.createElement(f.type.startsWith('video/') ? 'video' : 'img');
    node.src = objectUrl;
    if (node.tagName === 'VIDEO') node.controls = true;
    node.alt = 'Selected file preview';
    preview.append(node);
    const caption = document.createElement('small');
    caption.textContent = f.name + ' · ' + (f.size / 1048576).toFixed(2) + ' MB';
    preview.append(caption);
  });

  function showResult(data, submittedFile) {
    if (!data || typeof data !== 'object') throw Error('Invalid response');
    const status = String(data.status || 'completed');
    badge.textContent = status.toUpperCase();
    headline.textContent = String(data.summary || 'Investigation completed');
    message.textContent = String(data.message || 'Review evidence and limitations.');
    update(data.steps || {});

    // Render tool badges
    selected.replaceChildren();
    const h = document.createElement('strong');
    h.textContent = 'Agent-selected & verified tools';
    selected.append(h);

    const toolsContainer = document.createElement('div');
    toolsContainer.style.display = 'flex';
    toolsContainer.style.flexWrap = 'wrap';
    toolsContainer.style.gap = '6px';
    toolsContainer.style.marginTop = '8px';

    const toolNames = Array.isArray(data.tools) ? data.tools : [];
    if (toolNames.length > 0) {
      toolNames.forEach(tName => {
        const tBadge = document.createElement('span');
        tBadge.style.cssText = 'background:#1a2e22;color:#34d399;font-size:0.75rem;padding:3px 8px;border-radius:12px;font-family:monospace;display:inline-block;';
        tBadge.textContent = '✓ ' + tName;
        toolsContainer.append(tBadge);
      });
      selected.append(toolsContainer);
    } else {
      const p = document.createElement('p');
      p.textContent = 'No verified tool execution details returned.';
      selected.append(p);
    }

    // Render rich result card
    result.hidden = false;
    result.replaceChildren();

    const resultBox = document.createElement('div');
    resultBox.style.cssText = 'background:rgba(255,255,255,0.96);border:1px solid rgba(0,0,0,0.1);border-radius:16px;padding:20px;margin-top:14px;box-shadow:0 10px 30px rgba(0,0,0,0.06);';

    const fin = data.financial_risk || {};
    const tierColor = fin.badge_color || '#10B981';
    const isSynthetic = (data.confidence || 0) >= 50;
    const pt = (data.tool_details && data.tool_details.pytorch) || {};
    const ela = (data.tool_details && data.tool_details.ela) || {};
    const mules = (data.tool_details && data.tool_details.semak_mule) || [];
    const hasMuleMatch = mules.some(m => m.is_flagged);

    const badgeLabel = fin.has_financial_intent
      ? `${fin.risk_tier} FINANCIAL RISK`
      : 'INFORMATIONAL · RM 0.00 EXPOSURE';

    resultBox.innerHTML = `
      <div style="display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #f1f5f9;padding-bottom:12px;margin-bottom:14px;flex-wrap:wrap;gap:8px;">
        <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:1.2px;font-weight:800;color:#64748b;">LAICIS FORENSIC VERDICT</span>
        <span style="background:${tierColor};color:#fff;font-weight:700;font-size:0.75rem;padding:4px 12px;border-radius:20px;letter-spacing:0.5px;">${badgeLabel}</span>
      </div>

      <div style="font-size:1.25rem;font-weight:800;color:#0f172a;margin-bottom:6px;line-height:1.3;">
        ${data.verdict ? data.verdict.replace(/_/g, ' ') : 'Investigation Completed'}
      </div>
      <div style="font-size:0.85rem;color:#475569;margin-bottom:14px;display:flex;align-items:center;gap:8px;">
        <span>Composite Synthetic Confidence: <strong style="color:#0f172a;">${data.confidence || 0}%</strong></span>
        <span style="background:#f1f5f9;color:#475569;font-size:0.7rem;padding:2px 8px;border-radius:6px;font-family:monospace;">tf_efficientnetv2_s</span>
      </div>

      <!-- Forensic Signals Matrix -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:8px;margin-bottom:16px;">
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:10px;">
          <div style="font-size:0.7rem;color:#64748b;font-weight:600;text-transform:uppercase;">PyTorch Model</div>
          <div style="font-size:0.9rem;font-weight:700;color:${pt.is_ai_generated ? '#dc2626' : '#059669'};margin-top:2px;">
            ${pt.label_name || (isSynthetic ? 'AI Generated' : 'Camera-Captured')}
          </div>
          <div style="font-size:0.7rem;color:#94a3b8;">${pt.ai_probability ? (pt.ai_probability * 100).toFixed(1) + '% AI Prob' : 'Local Weights'}</div>
        </div>
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:10px;">
          <div style="font-size:0.7rem;color:#64748b;font-weight:600;text-transform:uppercase;">ELA Compression</div>
          <div style="font-size:0.9rem;font-weight:700;color:${ela.risk_level === 'HIGH' ? '#dc2626' : '#059669'};margin-top:2px;">
            ${ela.risk_level || 'NORMAL'}
          </div>
          <div style="font-size:0.7rem;color:#94a3b8;">${ela.tampering_score ? (ela.tampering_score * 100).toFixed(0) + '% Tamper' : 'Compression check'}</div>
        </div>
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:10px;">
          <div style="font-size:0.7rem;color:#64748b;font-weight:600;text-transform:uppercase;">PDRM CCID Registry</div>
          <div style="font-size:0.9rem;font-weight:700;color:${hasMuleMatch ? '#dc2626' : '#059669'};margin-top:2px;">
            ${hasMuleMatch ? '⚠️ MULE MATCH' : 'CLEAN'}
          </div>
          <div style="font-size:0.7rem;color:#94a3b8;">Semak Mule Portal</div>
        </div>
        ${data.tool_details && data.tool_details.gemini ? `
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:10px;">
          <div style="font-size:0.7rem;color:#64748b;font-weight:600;text-transform:uppercase;">Gemini Multimodal</div>
          <div style="font-size:0.9rem;font-weight:700;color:${data.tool_details.gemini.is_ai_generated || data.tool_details.gemini.is_scam ? '#dc2626' : '#059669'};margin-top:2px;">
            ${data.tool_details.gemini.is_ai_generated || data.tool_details.gemini.is_scam ? 'AI / Scam Flag' : 'Unflagged'}
          </div>
          <div style="font-size:0.7rem;color:#94a3b8;">${Math.round((data.tool_details.gemini.ai_confidence || data.tool_details.gemini.confidence || 0) * 100)}% Reasoning</div>
        </div>
        ` : ''}
      </div>

      <!-- Calibrated Financial Assessment & Justification -->
      <div style="background:#f8fafc;border:1px solid #e2e8f0;border-left:4px solid ${tierColor};padding:14px 16px;border-radius:10px;margin-bottom:16px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
          <span style="font-size:0.75rem;text-transform:uppercase;color:#475569;font-weight:700;">MALAYSIAN FINANCIAL RISK ASSESSMENT</span>
          <span style="font-size:0.75rem;color:#64748b;">BNM RMiT Standard</span>
        </div>
        <div style="font-size:1.35rem;font-weight:800;color:#0f172a;margin:2px 0;">
          ${fin.exposure_formatted || 'RM 0.00'}
        </div>
        ${fin.exposure_rm > 0 ? `
          <div style="font-size:0.75rem;color:#059669;font-weight:600;margin-bottom:8px;">
            Potential Loss Prevented: <strong>${fin.prevention_value_formatted || 'RM 0.00'}</strong> (30% benchmark)
          </div>
        ` : ''}
        <div style="font-size:0.8rem;color:#334155;line-height:1.45;background:#ffffff;padding:10px;border-radius:6px;border:1px solid #e2e8f0;margin-top:6px;">
          <strong>Justification:</strong> ${fin.justification || 'No transactional demands or payment identifiers attached. Zero direct monetary exposure.'}
        </div>
      </div>

      <!-- Action Guidance -->
      <div style="font-size:0.82rem;color:#334155;background:#f0fdf4;border:1px solid #bbf7d0;padding:10px 14px;border-radius:8px;margin-bottom:16px;">
        <strong>Recommended Step:</strong> ${fin.action_advice || 'Verify sender identity independently before initiating any funds transfer.'}
      </div>

      <div style="display:flex;gap:10px;align-items:center;border-top:1px solid #f1f5f9;padding-top:14px;flex-wrap:wrap;">
        <a href="results.html" style="background:#0f172a;color:#fff;padding:9px 18px;border-radius:8px;text-decoration:none;font-size:0.85rem;font-weight:600;display:inline-flex;align-items:center;gap:6px;">
          Open Complete Investigation Dashboard ↗
        </a>
        <span style="font-size:0.75rem;color:#64748b;">Audit ID: <code style="background:#f1f5f9;padding:2px 6px;border-radius:4px;color:#0f172a;">${data.audit?.audit_id || 'AUD-VERIFIED'}</code></span>
      </div>
    `;

    result.append(resultBox);

    // Save to sessionStorage for results.html
    const sessionObj = {
      inputType: kind,
      goal: goal.value,
      status: status,
      receivedAt: new Date().toISOString(),
      response: data
    };
    try {
      sessionStorage.setItem('laicis_latest_agent', JSON.stringify(sessionObj));
      sessionStorage.setItem('laicis_latest', JSON.stringify({
        name: submittedFile ? submittedFile.name : (kind === 'url' ? url.value : 'Suspicious Message Text'),
        type: submittedFile ? submittedFile.type : kind,
        size: submittedFile ? submittedFile.size : (text.value ? text.value.length : 0),
        status: 'received',
        date: new Date().toISOString(),
        response: (data.verdict || 'Completed') + ' (' + (data.confidence || 0) + '% confidence)',
        agentData: data
      }));
    } catch {}
  }

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const f = file.files[0];

    if (kind === 'media' && (!f || !['image/jpeg', 'image/png', 'image/webp', 'video/mp4'].includes(f.type) || f.size > 30 * 1024 * 1024)) {
      message.textContent = 'Please select a supported media file under 30 MB.';
      return;
    }
    if (kind === 'url') {
      try {
        const parsed = new URL(url.value);
        if (!['http:', 'https:'].includes(parsed.protocol)) throw Error();
      } catch {
        message.textContent = 'Enter a valid http:// or https:// URL.';
        return;
      }
    }
    if (kind === 'text' && !text.value.trim()) {
      message.textContent = 'Paste some content or message to check.';
      return;
    }

    update();
    result.hidden = true;
    selected.replaceChildren();
    const empty = document.createElement('p');
    empty.textContent = 'WorkBuddy agent is actively analyzing input and choosing tools…';
    selected.append(empty);

    const endpoint = window.LAICIs_CONFIG?.agentApiUrl || '/api/agent/investigate';

    submit.disabled = true;
    badge.textContent = 'INVESTIGATING';
    headline.textContent = 'Agent executing pipeline…';
    message.textContent = 'Executing multi-model forensic analysis and BNM RMiT risk assessment.';

    // Progress animation
    let stepIdx = 0;
    const progressTimer = setInterval(() => {
      if (stepIdx < stages.length) {
        const currentSteps = {};
        for (let i = 0; i <= stepIdx; i++) {
          currentSteps[stages[i]] = i === stepIdx ? 'running' : 'done';
        }
        update(currentSteps);
        stepIdx++;
      }
    }, 450);

    const data = new FormData();
    data.append('input_type', kind);
    data.append('goal', goal.value.trim());
    data.append('segment', selectedSegment);
    if (kind === 'media') data.append('file', f);
    else data.append('content', kind === 'url' ? url.value.trim() : text.value.trim());

    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 90000);
      let response;
      try {
        response = await fetch(endpoint, {
          method: 'POST',
          body: data,
          signal: controller.signal
        });
      } finally {
        clearTimeout(timeout);
        clearInterval(progressTimer);
      }

      if (!response.ok) throw Error('HTTP ' + response.status);
      const resJson = await response.json();
      showResult(resJson, f);

    } catch (err) {
      clearInterval(progressTimer);
      badge.textContent = 'UNAVAILABLE';
      headline.textContent = 'Could not complete check';
      message.textContent = (err.name === 'AbortError' ? 'Request timed out' : err.message) + '. No verified results are available.';
      update();
    } finally {
      submit.disabled = false;
    }
  });
})();