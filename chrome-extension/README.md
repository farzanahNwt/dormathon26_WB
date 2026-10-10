# 🛡️ LAICIs — Chrome / Edge Browser Extension (Manifest V3)

Real-time deepfake forensics, phishing detection, and scam intelligence powered by **Tencent WorkBuddy** and **Google Gemini**.

---

## 🚀 How to Install in Google Chrome or Microsoft Edge

1. Open **Google Chrome** (or Edge/Brave) and navigate to:
   ```text
   chrome://extensions/
   ```
2. In the top right corner, toggle **Developer mode** to **ON**.
3. Click the **"Load unpacked"** button in the top left.
4. Select either of these directories:
   - Root folder: `c:\Users\eric.shamsurizal\OneDrive - U Mobile Sdn Bhd\Desktop\lAIci\chrome-extension`
   - Or: `c:\Users\eric.shamsurizal\OneDrive - U Mobile Sdn Bhd\Desktop\lAIci\LAICIs-V6.2-Track2-Focused\LAICIs-V6.2-Track2-Focused\extension`
5. The **LAICIs — AI Media & Fraud Verification Agent** icon will appear in your browser extension toolbar! Pin it for quick access.

---

## ⚡ Extension Capabilities

- **🟢 Real-time Backend Pulse**: Automatically connects to the local WorkBuddy backend (`http://localhost:5000/api/agent/status`).
- **🌐 Active Tab Instant Scan**: Automatically reads the URL of the tab you are currently viewing and checks for phishing, domain spoofing, and fake portal indicators.
- **💬 Message & SMS Analyzer**: Paste suspicious WhatsApp messages, job solicitations, or bank alerts directly into the popup to trigger Gemini linguistic reasoning and PDRM Semak Mule database cross-referencing.
- **🖼️ Deepfake Media Inspector**: Drag & drop or upload suspicious images directly in the extension popup to run EfficientNetV2 PyTorch CNN, Error Level Analysis (ELA), Sightengine, and Gemini Multimodal visual inspection.
- **🖱️ Right-Click Context Menus**:
  - Right-click any image on the web → **"Scan Image for AI Deepfakes with LAICIs"**
  - Right-click highlighted text on the web → **"Verify Selected Text for Fraud & Scams with LAICIs"**
  - Right-click webpage background → **"Verify Page Authenticity with LAICIs"**
- **↗️ One-Click Studio & Dashboard Launchers**: Instant navigation to `http://localhost:5000/` and `http://localhost:5000/results.html`.
