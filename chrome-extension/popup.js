const BACKEND_URL = 'http://localhost:5000';

document.addEventListener('DOMContentLoaded', async () => {
  const statusPill = document.getElementById('backendStatus');
  const statusText = document.getElementById('statusText');
  const pageUrlInput = document.getElementById('pageUrlInput');
  const textContentInput = document.getElementById('textContentInput');
  const mediaFileInput = document.getElementById('mediaFileInput');
  const mediaDropzone = document.getElementById('mediaDropzone');
  const dropzoneText = document.getElementById('dropzoneText');

  const btnScanUrl = document.getElementById('btnScanUrl');
  const btnScanText = document.getElementById('btnScanText');
  const btnScanMedia = document.getElementById('btnScanMedia');

  const resultBox = document.getElementById('resultBox');
  const verdictPill = document.getElementById('verdictPill');
  const scoreDisplay = document.getElementById('scoreDisplay');
  const resultSummary = document.getElementById('resultSummary');
  const toolsList = document.getElementById('toolsList');

  const linkScanner = document.getElementById('linkScanner');
  const linkDashboard = document.getElementById('linkDashboard');

  // Check Backend Status
  async function checkBackend() {
    try {
      const res = await fetch(`${BACKEND_URL}/api/agent/status`, { signal: AbortSignal.timeout(3000) });
      if (res.ok) {
        statusPill.className = 'status-pill online';
        statusText.textContent = 'Core Online';
      } else {
        throw new Error('Status error');
      }
    } catch (e) {
      statusPill.className = 'status-pill offline';
      statusText.textContent = 'Backend Offline';
    }
  }
  checkBackend();

  // Get active tab URL
  if (chrome.tabs && chrome.tabs.query) {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs && tabs[0] && tabs[0].url) {
        if (!tabs[0].url.startsWith('chrome://')) {
          pageUrlInput.value = tabs[0].url;
        }
      }
    });
  }

  // Tab switching
  const tabBtns = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.panel');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const targetPanel = document.getElementById(btn.dataset.tab);
      if (targetPanel) targetPanel.classList.add('active');
    });
  });

  // Media selection
  let selectedFile = null;
  mediaDropzone.addEventListener('click', () => mediaFileInput.click());
  mediaFileInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files[0]) {
      selectedFile = e.target.files[0];
      dropzoneText.textContent = `Selected: ${selectedFile.name} (${(selectedFile.size/1024).toFixed(1)} KB)`;
      btnScanMedia.disabled = false;
    }
  });

  // UI Render Result
  function displayResult(data) {
    resultBox.classList.add('visible');
    const verdict = data.verdict || 'COMPLETED';
    verdictPill.textContent = verdict.replace(/_/g, ' ');
    
    if (verdict.includes('HIGH_RISK') || verdict.includes('CRITICAL')) {
      verdictPill.className = 'result-verdict verdict-danger';
    } else if (verdict.includes('SUSPICIOUS')) {
      verdictPill.className = 'result-verdict verdict-warn';
    } else {
      verdictPill.className = 'result-verdict verdict-safe';
    }

    const conf = Math.round((data.confidence || data.composite_score || 0));
    scoreDisplay.textContent = `${conf}% Risk`;

    // Summary and findings
    let summary = data.summary || '';
    if (data.report && data.report.findings && data.report.findings.length > 0) {
      summary = data.report.findings[0];
    }
    resultSummary.textContent = summary || 'Agent investigation executed with multi-model forensic verification.';

    // Tools List
    toolsList.replaceChildren();
    const tools = data.tools || data.tools_executed || [];
    tools.forEach(t => {
      const span = document.createElement('span');
      span.className = 'tool-badge';
      span.textContent = t.replace(/_/g, ' ');
      toolsList.appendChild(span);
    });

    // Save to chrome storage for dashboard
    if (chrome.storage && chrome.storage.local) {
      chrome.storage.local.set({ lastScan: data });
    }
  }

  // Scan URL
  btnScanUrl.addEventListener('click', async () => {
    const url = pageUrlInput.value.trim();
    if (!url) return;
    btnScanUrl.disabled = true;
    btnScanUrl.textContent = 'Agent Analyzing...';
    try {
      const res = await fetch(`${BACKEND_URL}/api/agent/investigate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          input_type: 'url',
          content: url,
          goal: 'Chrome Extension active tab verification',
          segment: 'individual'
        })
      });
      const data = await res.json();
      displayResult(data);
    } catch (err) {
      alert('Investigation failed. Ensure LAICIs backend is running on http://localhost:5000');
    } finally {
      btnScanUrl.disabled = false;
      btnScanUrl.textContent = 'Verify Page Authenticity ↗';
    }
  });

  // Scan Text
  btnScanText.addEventListener('click', async () => {
    const text = textContentInput.value.trim();
    if (!text) return;
    btnScanText.disabled = true;
    btnScanText.textContent = 'Analyzing with Gemini...';
    try {
      const res = await fetch(`${BACKEND_URL}/api/agent/investigate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          input_type: 'text',
          content: text,
          goal: 'Evaluate fraud, extortion, and mule account solicitations',
          segment: 'individual'
        })
      });
      const data = await res.json();
      displayResult(data);
    } catch (err) {
      alert('Investigation failed. Ensure LAICIs backend is running on http://localhost:5000');
    } finally {
      btnScanText.disabled = false;
      btnScanText.textContent = 'Analyze with Gemini & PDRM ↗';
    }
  });

  // Scan Media
  btnScanMedia.addEventListener('click', async () => {
    if (!selectedFile) return;
    btnScanMedia.disabled = true;
    btnScanMedia.textContent = 'Forensic Inspection Running...';
    const formData = new FormData();
    formData.append('input_type', 'media');
    formData.append('file', selectedFile);
    formData.append('goal', 'Chrome Extension media deepfake analysis');
    formData.append('segment', 'individual');

    try {
      const res = await fetch(`${BACKEND_URL}/api/agent/investigate`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      displayResult(data);
    } catch (err) {
      alert('Media scan failed. Ensure LAICIs backend is running on http://localhost:5000');
    } finally {
      btnScanMedia.disabled = false;
      btnScanMedia.textContent = 'Run Forensic Inspection ↗';
    }
  });

  // Links
  linkScanner.addEventListener('click', (e) => {
    e.preventDefault();
    if (chrome.tabs && chrome.tabs.create) {
      chrome.tabs.create({ url: `${BACKEND_URL}/` });
    } else {
      window.open(`${BACKEND_URL}/`, '_blank');
    }
  });

  linkDashboard.addEventListener('click', (e) => {
    e.preventDefault();
    if (chrome.tabs && chrome.tabs.create) {
      chrome.tabs.create({ url: `${BACKEND_URL}/results.html` });
    } else {
      window.open(`${BACKEND_URL}/results.html`, '_blank');
    }
  });
});