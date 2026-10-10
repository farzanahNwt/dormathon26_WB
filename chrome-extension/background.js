// LAICIs Background Service Worker (Manifest V3)
const BACKEND_URL = 'http://localhost:5000';

chrome.runtime.onInstalled.addListener(() => {
  // Create Context Menus
  chrome.contextMenus.create({
    id: 'laici_scan_image',
    title: 'Scan Image for AI Deepfakes with LAICIs',
    contexts: ['image']
  });

  chrome.contextMenus.create({
    id: 'laici_scan_text',
    title: 'Verify Selected Text for Fraud & Scams with LAICIs',
    contexts: ['selection']
  });

  chrome.contextMenus.create({
    id: 'laici_scan_page',
    title: 'Verify Page Authenticity with LAICIs',
    contexts: ['page']
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === 'laici_scan_image') {
    const srcUrl = info.srcUrl;
    if (srcUrl) {
      // Open LAICIs scanner with focus
      chrome.tabs.create({
        url: `${BACKEND_URL}/#scanner`
      });
    }
  } else if (info.menuItemId === 'laici_scan_text') {
    const text = info.selectionText || '';
    if (text) {
      // Execute fast check against backend
      try {
        const resp = await fetch(`${BACKEND_URL}/api/agent/investigate`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            input_type: 'text',
            content: text,
            goal: 'Context menu selection verification',
            segment: 'individual'
          })
        });
        if (resp.ok) {
          const result = await resp.json();
          // Store result in local storage for popup/results view
          await chrome.storage.local.set({ lastScan: result });
          chrome.tabs.create({ url: `${BACKEND_URL}/results.html` });
        } else {
          chrome.tabs.create({ url: `${BACKEND_URL}/#scanner` });
        }
      } catch (err) {
        chrome.tabs.create({ url: `${BACKEND_URL}/#scanner` });
      }
    }
  } else if (info.menuItemId === 'laici_scan_page') {
    const pageUrl = info.pageUrl || tab?.url || '';
    if (pageUrl) {
      chrome.tabs.create({ url: `${BACKEND_URL}/#scanner` });
    }
  }
});
