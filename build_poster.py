"""
ROUTE RIOT: AI-Based Smart Bus Occupancy Prediction and Passenger Redirection System
IEEE Information Theory Industry Conclave 2026 Poster Generator (v12 - Complete Zero Gap Masterpiece)

Fully grounded in all 16 slides of the official presentation:
- Complete team & guide metadata (Lokpradeep H, Dhikshita A, Harish P*, Guide: Prof. Rashmi Rani Samantaray, VVIT VTU Bengaluru).
- Complete slide details across all 11 cards, sized to perfection so all 3 columns fill 100% of the 495mm grid with zero gaps.
"""

import os
import subprocess

POSTER_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ROUTE RIOT - IEEE InfoTheory Industry Conclave 2026 Poster</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  @page {
    size: 420mm 594mm;
    margin: 0;
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  :root {
    --primary-navy: #041021;
    --navy-card: #081d3d;
    --navy-header: #051428;
    --ieee-blue: #00629b;
    --ieee-blue-light: #0284c7;
    --cyan-accent: #00c9b7;
    --cyan-glow: #38bdf8;
    --teal-glow: #059669;
    --amber-gold: #d97706;
    --amber-light: #f59e0b;
    --coral-alert: #dc2626;
    --bg-canvas: #f8fafc;
    --bg-card: #ffffff;
    --text-primary: #0f172a;
    --text-secondary: #1e293b;
    --text-muted: #475569;
    --border-subtle: #cbd5e1;
    --border-card: #94a3b8;
    --shadow-card: 0 4px 12px rgba(15, 23, 42, 0.07);
  }

  html, body {
    width: 420mm;
    height: 594mm;
    max-width: 420mm;
    max-height: 594mm;
    overflow: hidden;
    background-color: var(--bg-canvas);
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: var(--text-primary);
    line-height: 1.25;
    letter-spacing: -0.01em;
  }

  .poster-container {
    width: 420mm;
    height: 594mm;
    padding: 4.8mm 6.5mm 4.2mm 6.5mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    background: radial-gradient(circle at 10% 5%, #e6f0fa 0%, #f8fafc 40%, #eaf1f9 100%);
  }

  .poster-container::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
      radial-gradient(#94a3b8 0.75px, transparent 0.75px),
      radial-gradient(#94a3b8 0.75px, #f8fafc 0.75px);
    background-size: 22px 22px;
    background-position: 0 0, 11px 11px;
    opacity: 0.16;
    pointer-events: none;
    z-index: 0;
  }

  .header-wrapper, .main-grid, .footer-bar {
    position: relative;
    z-index: 1;
  }

  /* ==========================================================================
     HEADER SECTION (HEIGHT: ~66mm)
     ========================================================================== */
  .header-wrapper {
    background: linear-gradient(135deg, #030d1c 0%, #061933 42%, #004573 100%);
    border-radius: 4.2mm;
    padding: 3mm 5.5mm 2.6mm 5.5mm;
    color: #ffffff;
    box-shadow: 0 6px 20px rgba(4, 16, 33, 0.25);
    border: 1.3px solid rgba(255, 255, 255, 0.18);
    display: flex;
    flex-direction: column;
    gap: 1.3mm;
  }

  .header-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1.1px solid rgba(255, 255, 255, 0.15);
    padding-bottom: 1.2mm;
  }

  .logo-group-left, .logo-group-right {
    display: flex;
    align-items: center;
    gap: 3.2mm;
  }

  .event-conclave-badge {
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(8px);
    border: 1.2px solid rgba(0, 201, 183, 0.55);
    border-radius: 2.5mm;
    padding: 1mm 4mm;
    display: flex;
    align-items: center;
    gap: 2.6mm;
  }

  .conclave-title {
    font-size: 8.8pt;
    font-weight: 800;
    letter-spacing: 0.04em;
    color: #ffffff;
    text-transform: uppercase;
  }

  .conclave-theme {
    background: linear-gradient(90deg, #00c9b7, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 8.4pt;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .header-title-block {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5mm;
  }

  .project-brand {
    display: flex;
    align-items: center;
    gap: 3mm;
  }

  .brand-badge {
    background: linear-gradient(135deg, #00c9b7, #0091da);
    color: #041021;
    font-size: 14pt;
    font-weight: 900;
    padding: 0.8mm 3.6mm;
    border-radius: 2mm;
    letter-spacing: 0.07em;
    box-shadow: 0 3px 8px rgba(0, 201, 183, 0.4);
  }

  .project-main-title {
    font-size: 25pt;
    font-weight: 800;
    letter-spacing: -0.025em;
    line-height: 1.1;
    background: linear-gradient(90deg, #ffffff 0%, #f0f9ff 65%, #bae6fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .project-subtitle {
    font-size: 10.8pt;
    font-weight: 600;
    color: #e2e8f0;
    max-width: 400mm;
    letter-spacing: 0.01em;
    line-height: 1.2;
  }

  .header-bottom-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(0, 0, 0, 0.35);
    border-radius: 2.2mm;
    padding: 1.2mm 3.8mm;
    font-size: 8.9pt;
    border: 1.1px solid rgba(255, 255, 255, 0.12);
  }

  .authors-list {
    display: flex;
    align-items: center;
    gap: 3.5mm;
  }

  .author-item {
    display: flex;
    align-items: center;
    gap: 1.1mm;
    font-weight: 600;
    color: #ffffff;
  }

  .author-item span.lead {
    color: #00c9b7;
    font-weight: 800;
    font-size: 9.6pt;
  }

  .author-item .sup {
    font-size: 7.2pt;
    color: #fbbf24;
    font-weight: 800;
  }

  .affiliation-info {
    color: #94a3b8;
    font-size: 8.6pt;
  }
  .affiliation-info strong {
    color: #e2e8f0;
  }

  /* ==========================================================================
     MAIN 3-COLUMN CONTENT GRID (HEIGHT: ~495mm)
     ========================================================================== */
  .main-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 4.2mm;
    height: 495mm;
    margin-top: 1.5mm;
    margin-bottom: 1.5mm;
  }

  .column {
    display: flex;
    flex-direction: column;
    height: 100%;
    gap: 3.2mm;
  }

  /* Section Card Styling */
  .poster-card {
    background: var(--bg-card);
    border-radius: 3.2mm;
    border: 1.2px solid #cbd5e1;
    padding: 2.8mm 3.4mm;
    box-shadow: var(--shadow-card);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }

  .poster-card.accent-navy {
    border-top: 3.2mm solid var(--ieee-blue);
  }
  .poster-card.accent-cyan {
    border-top: 3.2mm solid var(--cyan-accent);
  }
  .poster-card.accent-amber {
    border-top: 3.2mm solid var(--amber-gold);
  }
  .poster-card.accent-emerald {
    border-top: 3.2mm solid var(--teal-glow);
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 1.8mm;
    margin-bottom: 1.4mm;
    padding-bottom: 0.8mm;
    border-bottom: 1.2px solid #e2e8f0;
    flex-shrink: 0;
  }

  .badge-number {
    width: 5.6mm;
    height: 5.6mm;
    border-radius: 1.4mm;
    background: var(--primary-navy);
    color: #ffffff;
    font-size: 8pt;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'JetBrains Mono', monospace;
  }

  .poster-card.accent-cyan .badge-number {
    background: #00877e;
  }
  .poster-card.accent-amber .badge-number {
    background: #b45309;
  }
  .poster-card.accent-emerald .badge-number {
    background: #047857;
  }

  .card-title {
    font-size: 10.4pt;
    font-weight: 800;
    color: var(--primary-navy);
    letter-spacing: -0.015em;
    text-transform: uppercase;
  }

  .card-body {
    font-size: 8pt;
    color: var(--text-secondary);
    display: flex;
    flex-direction: column;
    gap: 2mm;
    flex: 1;
    justify-content: flex-start;
    line-height: 1.25;
  }

  p {
    margin-bottom: 0;
    line-height: 1.24;
  }

  strong {
    color: var(--text-primary);
    font-weight: 700;
  }

  /* Tables */
  .custom-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 7pt;
    line-height: 1.18;
  }

  .custom-table th {
    background: #0f172a;
    color: #ffffff;
    font-weight: 700;
    padding: 1.1mm 1.3mm;
    text-align: left;
    border: 1px solid #1e293b;
    font-size: 6.8pt;
  }

  .custom-table td {
    padding: 1mm 1.3mm;
    border: 1px solid #cbd5e1;
    color: #1e293b;
    vertical-align: top;
  }

  .custom-table tr:nth-child(even) td {
    background: #f8fafc;
  }

  /* 3-Tier Crowd Cards */
  .crowd-tier-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5mm;
  }

  .crowd-tier-card {
    border-radius: 1.8mm;
    padding: 1.5mm 1mm;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .crowd-tier-card.low {
    background: #dcfce7;
    border: 1.2px solid #86efac;
    color: #166534;
  }

  .crowd-tier-card.mod {
    background: #fef3c7;
    border: 1.2px solid #fde68a;
    color: #92400e;
  }

  .crowd-tier-card.high {
    background: #fee2e2;
    border: 1.2px solid #fca5a5;
    color: #991b1b;
  }

  .tier-badge {
    font-size: 7.4pt;
    font-weight: 800;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }

  .tier-range {
    font-size: 7pt;
    font-weight: 800;
    margin-top: 0.2mm;
  }

  .tier-desc {
    font-size: 6.3pt;
    margin-top: 0.3mm;
    line-height: 1.14;
  }

  /* App Mockup Container */
  .app-preview-card {
    background: #071529;
    border-radius: 2.4mm;
    padding: 2mm 2.4mm;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    gap: 1.6mm;
    border: 1.2px solid #334155;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.20);
  }

  .app-preview-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #1e293b;
    padding-bottom: 0.7mm;
    font-size: 7.4pt;
  }

  .crowd-pill {
    padding: 0.5mm 1.8mm;
    border-radius: 1mm;
    font-size: 6.4pt;
    font-weight: 800;
    text-transform: uppercase;
  }
  .crowd-pill.high { background: #fee2e2; color: #b91c1c; border: 1px solid #f87171; }
  .crowd-pill.mod { background: #fef3c7; color: #b45309; border: 1px solid #fbbf24; }
  .crowd-pill.low { background: #dcfce7; color: #15803d; border: 1px solid #4ade80; }

  /* ==========================================================================
     FOOTER BAR (HEIGHT: ~23mm)
     ========================================================================== */
  .footer-bar {
    background: linear-gradient(135deg, #030d1c 0%, #061933 100%);
    border-radius: 3.8mm;
    padding: 2.2mm 4.8mm;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1.2px solid rgba(255, 255, 255, 0.16);
    box-shadow: 0 4px 14px rgba(4, 16, 33, 0.20);
  }

  .footer-left {
    display: flex;
    flex-direction: column;
    gap: 0.5mm;
    max-width: 255mm;
  }

  .footer-headline {
    font-size: 9.4pt;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 2mm;
  }

  .footer-headline span.tag {
    background: #00c9b7;
    color: #041021;
    font-size: 7.2pt;
    font-weight: 900;
    padding: 0.4mm 2.2mm;
    border-radius: 1mm;
    text-transform: uppercase;
  }

  .footer-subtext {
    font-size: 7.6pt;
    color: #94a3b8;
    line-height: 1.20;
  }

  .footer-subtext strong {
    color: #e2e8f0;
  }

  .footer-center-meta {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 0.4mm;
    border-left: 1.2px solid rgba(255, 255, 255, 0.15);
    border-right: 1.2px solid rgba(255, 255, 255, 0.15);
    padding: 0 4mm;
  }

  .event-venue-text {
    font-size: 8pt;
    font-weight: 800;
    color: #ffffff;
  }

  .event-date-text {
    font-size: 7.4pt;
    color: #38bdf8;
    font-weight: 700;
  }

  .footer-right-qr {
    display: flex;
    align-items: center;
    gap: 2.6mm;
  }

  .qr-box {
    width: 15mm;
    height: 15mm;
    background: #ffffff;
    border-radius: 1.5mm;
    padding: 0.7mm;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.30);
  }

  .qr-box svg {
    width: 100%;
    height: 100%;
  }

  .qr-label-block {
    display: flex;
    flex-direction: column;
    gap: 0.3mm;
  }

  .qr-scan-title {
    font-size: 7.4pt;
    font-weight: 800;
    color: #00c9b7;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .qr-scan-desc {
    font-size: 6.3pt;
    color: #cbd5e1;
    max-width: 38mm;
    line-height: 1.16;
  }
</style>
</head>
<body>

<div class="poster-container">

  <!-- ========================================================================
       HEADER
       ======================================================================== -->
  <header class="header-wrapper">
    <div class="header-top">
      <!-- Left: IEEE & Chapter Logos -->
      <div class="logo-group-left">
        <!-- IEEE Bangalore Section Emblem -->
        <svg width="118" height="35" viewBox="0 0 118 35" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="118" height="35" rx="4" fill="rgba(255,255,255,0.08)"/>
          <g transform="translate(6, 3)">
            <polygon points="15,1 29,15 15,29 1,15" stroke="#00C9B7" stroke-width="2.2" fill="none"/>
            <circle cx="15" cy="15" r="5.5" fill="#0091DA"/>
            <path d="M15,4 L15,26 M4,15 L26,15" stroke="#00C9B7" stroke-width="1.4"/>
            <path d="M9,9 L21,21 M9,21 L21,9" stroke="#00C9B7" stroke-width="1"/>
          </g>
          <text x="39" y="23" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-weight="900" font-size="14.5" letter-spacing="1.5">IEEE</text>
          <text x="83" y="16" fill="#38BDF8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="7.2">BANGALORE</text>
          <text x="83" y="25" fill="#94A3B8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="6.3">SECTION</text>
        </svg>

        <!-- IEEE Information Theory Society Bangalore Chapter Badge -->
        <svg width="142" height="35" viewBox="0 0 142 35" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="142" height="35" rx="4" fill="rgba(255,255,255,0.08)"/>
          <circle cx="17" cy="17.5" r="12" fill="#0A2144" stroke="#F59E0B" stroke-width="2"/>
          <text x="17" y="22.5" fill="#F59E0B" font-family="'JetBrains Mono', monospace" font-weight="900" font-size="11" text-anchor="middle">IT</text>
          <text x="37" y="15.5" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-weight="800" font-size="8.4">IEEE INFOTHEORY</text>
          <text x="37" y="25.5" fill="#F59E0B" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="6.8">BANGALORE CHAPTER</text>
        </svg>
      </div>

      <!-- Center: Conclave Title & Theme -->
      <div class="event-conclave-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#00C9B7" stroke-width="2.6">
          <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
        </svg>
        <span class="conclave-title">IEEE InfoTheory Industry Conclave 2026</span>
        <span style="color:rgba(255,255,255,0.4)">|</span>
        <span class="conclave-theme">Theory ➔ Technology ➔ Impact</span>
      </div>

      <!-- Right: University & VVIT Partner Badges -->
      <div class="logo-group-right">
        <!-- CHRIST University Host -->
        <div style="text-align: right;">
          <div style="font-size: 7.8pt; font-weight: 800; color: #FFFFFF; letter-spacing: 0.04em;">CHRIST (Deemed to be University)</div>
          <div style="font-size: 6.6pt; color: #38BDF8; font-weight: 600;">Yeshwanthpur Campus, Bengaluru</div>
        </div>
        <!-- VVIT Emblem SVG with motto -->
        <svg width="118" height="35" viewBox="0 0 118 35" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="118" height="35" rx="4" fill="rgba(255,255,255,0.08)"/>
          <g transform="translate(6, 3)">
            <circle cx="14.5" cy="14.5" r="12.5" fill="#0A3622" stroke="#10B981" stroke-width="1.8"/>
            <path d="M9 19 L14.5 10 L20 19 L17 19 L14.5 14 L12 19 Z" fill="#FFFFFF"/>
            <circle cx="14.5" cy="17.5" r="1.5" fill="#F59E0B"/>
          </g>
          <text x="36" y="15" fill="#FFFFFF" font-family="'Plus Jakarta Sans'" font-size="7.6" font-weight="800">VVIT (VTU)</text>
          <text x="36" y="25" fill="#10B981" font-family="'Plus Jakarta Sans'" font-size="6.3" font-weight="700">Bengaluru - 77</text>
        </svg>
      </div>
    </div>

    <!-- Main Project Title -->
    <div class="header-title-block">
      <div class="project-brand">
        <span class="brand-badge">ROUTE RIOT</span>
        <h1 class="project-main-title">AI-Based Smart Bus Occupancy Prediction and Passenger Redirection System</h1>
      </div>
      <p class="project-subtitle">
        Bridging Hybrid Edge Sensing (YOLO & ToF) with Predictive AI & Multi-Modal Redirection for Bengaluru Transport
      </p>
    </div>

    <!-- Authors, Affiliation, Guide -->
    <div class="header-bottom-meta">
      <div class="authors-list">
        <div class="author-item">
          <span class="lead">Lokpradeep H</span><span class="sup">1</span>
        </div>
        <div style="color:rgba(255,255,255,0.35)">•</div>
        <div class="author-item">
          <span class="lead">Dhikshita A</span><span class="sup">1</span>
        </div>
        <div style="color:rgba(255,255,255,0.35)">•</div>
        <div class="author-item">
          <span class="lead">Harish P</span><span class="sup">1,*</span>
        </div>
        <div style="color:rgba(255,255,255,0.35)">•</div>
        <span style="color:#FCD34D; font-weight:800; font-size:8.8pt;">Guide: Prof. Rashmi Rani Samantaray</span>
      </div>
      <div class="affiliation-info">
        <span class="sup">1</span>Department of Computer Science & Engineering, <strong>Vijaya Vittala Institute of Technology (VTU)</strong>, Bengaluru | <strong>*Presenter</strong>
      </div>
    </div>
  </header>


  <!-- ========================================================================
       MAIN 3-COLUMN BODY (495mm Total Height)
       ======================================================================== -->
  <main class="main-grid">

    <!-- ====================================================================
         COLUMN 1: CONTEXT, PROBLEM STATEMENT, OBJECTIVES, LITERATURE SURVEY
         ==================================================================== -->
    <div class="column">

      <!-- Card 1: Abstract & Context (Slides 2 & 3) -->
      <section class="poster-card accent-navy" style="flex: 1.05 1 0;">
        <div class="card-header">
          <div class="badge-number">01</div>
          <h2 class="card-title">Abstract & Introduction</h2>
        </div>
        <div class="card-body">
          <p>
            Bengaluru’s public transport network serves an immense, constantly shifting commuter demand. While existing transit apps show vehicle GPS coordinates and ETAs, commuters remain <strong>completely unaware of in-cabin crowd density</strong> and impending congestion spikes before boarding.
          </p>
          <p>
            <strong>Route Riot</strong> is an intelligent public-transport assistance framework that combines <strong>YOLO-based computer vision</strong> for camera-equipped buses with <strong>ESP32 + Time-of-Flight (ToF) sensors</strong> for non-camera fleets. Occupancy streams are normalized through a high-throughput <strong>FastAPI backend</strong> to establish live passenger states and forecast upcoming surges.
          </p>

          <!-- Core Flow Badge (Slide 3) -->
          <div style="background:#eff6ff; border:1.2px solid #bfdbfe; border-radius:1.8mm; padding:1.4mm 1.8mm; text-align:center;">
            <span style="font-size:7.4pt; font-family:'JetBrains Mono'; font-weight:800; color:#1e40af;">
              SENSE ➔ DETECT ➔ PREDICT ➔ REDIRECT
            </span>
            <div style="font-size:6.4pt; color:#3b82f6; font-weight:600; margin-top:0.4mm;">
              Camera / ToF ➔ Common Event ➔ AI Forecast ➔ Multi-Modal Alternative
            </div>
          </div>

          <!-- Key Project Innovations (Slide 2 & 3) -->
          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.6mm; padding:1.2mm 1.6mm;">
            <span style="font-size:6.8pt; font-weight:800; color:#0f172a; text-transform:uppercase;">Key Novelties:</span>
            <ul style="font-size:6.4pt; color:#334155; margin-top:0.3mm; padding-left:3mm; line-height:1.22;">
              <li><strong>Dual Sensing:</strong> Bridges advanced AI cameras with low-cost ToF hardware.</li>
              <li><strong>Predictive Layer:</strong> Anticipates stop-by-stop crowding 15–20 minutes prior.</li>
              <li><strong>Multi-Modal Sync:</strong> Directs passengers to parallel BMTC routes and Namma Metro.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Card 2: Problem Statement & Commuter Scenarios (Slide 5) -->
      <section class="poster-card accent-amber" style="flex: 1.25 1 0;">
        <div class="card-header">
          <div class="badge-number">02</div>
          <h2 class="card-title">Problem Statement & Scenarios</h2>
        </div>
        <div class="card-body">
          <div style="background:#fef2f2; border:1.2px solid #fecaca; border-radius:1.6mm; padding:1.2mm 1.8mm;">
            <span style="font-size:7.4pt; font-weight:800; color:#991b1b;">THE CORE PROBLEM (SLIDE 5):</span>
            <p style="font-size:7.1pt; color:#7f1d1d; margin-top:0.3mm; line-height:1.18;">
              Bengaluru's bus passengers often do not know the actual crowd level of an approaching bus or how crowded it may become during their journey. <em>A bus being nearby does not necessarily mean it is the best travel choice.</em>
            </p>
          </div>

          <!-- Scenario Comparison (Slide 5) -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.6mm;">
            <div style="background:#f8fafc; border:1.1px solid #cbd5e1; border-radius:1.6mm; padding:1.4mm;">
              <span style="font-size:7pt; font-weight:800; color:#475569;">⚠️ Normal Scenario:</span>
              <ul style="font-size:6.4pt; color:#334155; margin-top:0.4mm; padding-left:3mm; line-height:1.20;">
                <li>Passenger wants to travel</li>
                <li>Bus location is available & ETA is known</li>
                <li>Passenger boards arriving bus blindly</li>
                <li>Actual in-cabin crowd level is unknown</li>
                <li><strong>Result: Severe overcrowding & discomfort</strong></li>
              </ul>
            </div>
            <div style="background:#f0fdf4; border:1.1px solid #86efac; border-radius:1.6mm; padding:1.4mm;">
              <span style="font-size:7pt; font-weight:800; color:#166534;">✅ Crowd-Uncertainty / Route Riot:</span>
              <ul style="font-size:6.4pt; color:#14532d; margin-top:0.4mm; padding-left:3mm; line-height:1.20;">
                <li>Bus is already highly occupied (>70%)</li>
                <li>More passengers expected at next stops</li>
                <li>Nearby alternate bus (500K) has lower crowd</li>
                <li>Namma Metro option is also available</li>
                <li><strong>Result: Informed, comfortable journey</strong></li>
              </ul>
            </div>
          </div>

          <!-- Commuter Experience Comparison Bar -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.4mm; font-size:6.3pt;">
            <div style="background:#fee2e2; border:1px solid #fca5a5; border-radius:1.4mm; padding:1mm; color:#991b1b;">
              <strong>Blind Commute:</strong> Unpredictable boarding, severe fatigue, missed alternatives.
            </div>
            <div style="background:#dcfce7; border:1px solid #86efac; border-radius:1.4mm; padding:1mm; color:#166534;">
              <strong>Route Riot:</strong> Pre-boarding clarity, optimal comfort, multi-modal flexibility.
            </div>
          </div>

          <div style="background:#f1f5f9; border:1px solid #cbd5e1; border-radius:1.4mm; padding:1.1mm 1.5mm; font-size:6.8pt; color:#334155;">
            <strong>Takeaway:</strong> Without predictive occupancy information, passengers miss better available alternatives departing just minutes apart.
          </div>
        </div>
      </section>

      <!-- Card 3: Project Objectives (Slide 7) -->
      <section class="poster-card accent-emerald" style="flex: 1.15 1 0;">
        <div class="card-header">
          <div class="badge-number">03</div>
          <h2 class="card-title">Key Project Objectives</h2>
        </div>
        <div class="card-body">
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.4mm;">
            <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#15803d;">1. Real-Time Awareness</span>
              <p style="font-size:6.1pt; color:#166534; margin-top:0.2mm;">Provide clear, instant bus crowd conditions to eliminate daily commuter uncertainty.</p>
            </div>
            <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#1d4ed8;">2. Predictive Management</span>
              <p style="font-size:6.1pt; color:#1e40af; margin-top:0.2mm;">Analyze historical patterns to anticipate crowd spikes before they become severe.</p>
            </div>
            <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#b45309;">3. Intelligent Redirection</span>
              <p style="font-size:6.1pt; color:#92400e; margin-top:0.2mm;">Help passengers respond to crowded buses by identifying suitable BMTC & Metro routes.</p>
            </div>
            <div style="background:#fdf4ff; border:1px solid #f5d0fe; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#a21caf;">4. Hybrid Fleet Framework</span>
              <p style="font-size:6.1pt; color:#86198f; margin-top:0.2mm;">Unify camera-equipped (YOLO) and non-camera (ToF) vehicles into one common metric.</p>
            </div>
            <div style="background:#faf5ff; border:1px solid #e9d5ff; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#7e22ce;">5. Improved Travel Experience</span>
              <p style="font-size:6.1pt; color:#6b21a8; margin-top:0.2mm;">Reduce inconvenience of overcrowded cabins through actionable passenger decision support.</p>
            </div>
            <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:1.5mm; padding:1.3mm 1.4mm;">
              <span style="font-size:6.8pt; font-weight:800; color:#0369a1;">6. Transport Intelligence</span>
              <p style="font-size:6.1pt; color:#0c4a6e; margin-top:0.2mm;">Build a robust dataset supporting future AI transit demand analysis and smart fleet planning.</p>
            </div>
          </div>

          <!-- Quantitative Benchmarks -->
          <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.5mm; padding:1.1mm 1.5mm; display:flex; justify-content:space-between; align-items:center; font-size:6.4pt;">
            <span>⚡ <strong>Latency Target:</strong> &lt;1.5s Sensor-to-App</span>
            <span>🎯 <strong>Prediction Precision:</strong> &gt;88%</span>
            <span>💰 <strong>Fleet Retrofit:</strong> &lt;₹3,500/Bus</span>
          </div>
        </div>
      </section>

      <!-- Card 4: Literature Survey & Research Gaps (Slide 4 & 6) -->
      <section class="poster-card accent-cyan" style="flex: 1.25 1 0;">
        <div class="card-header">
          <div class="badge-number">04</div>
          <h2 class="card-title">Literature Survey & Gaps</h2>
        </div>
        <div class="card-body">
          <table class="custom-table">
            <thead>
              <tr>
                <th style="width:26%;">Study / Domain</th>
                <th style="width:37%;">Parameters / Focus</th>
                <th style="width:37%;">Identified Research Gap</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Vision Counting</strong> (2022)</td>
                <td>Camera-based passenger counting</td>
                <td>Occlusion in dense crowds reduces detection accuracy.</td>
              </tr>
              <tr>
                <td><strong>YOLO People Detection</strong> (2023)</td>
                <td>Object detection for passenger count</td>
                <td>Detection alone does not predict future route crowding.</td>
              </tr>
              <tr>
                <td><strong>IoT Distance Sensing</strong> (2021)</td>
                <td>ToF doorway entry/exit counting</td>
                <td>Cannot resolve multi-door simultaneous passenger boarding.</td>
              </tr>
              <tr>
                <td><strong>ML Demand Forecast</strong> (2023)</td>
                <td>Historical ridership & passenger flow</td>
                <td>Demand model is separated from real-time vehicle occupancy.</td>
              </tr>
              <tr>
                <td><strong>Smart Mobility Apps</strong> (2024)</td>
                <td>Real-time transit info & ETA tracking</td>
                <td>Lacks integration between crowd prediction and multi-modal transit.</td>
              </tr>
            </tbody>
          </table>

          <div style="background:#ecfeff; border:1.1px solid #a5f3fc; border-radius:1.5mm; padding:1.2mm 1.6mm;">
            <p style="font-size:6.8pt; color:#0e7490; font-weight:700; line-height:1.16;">
              💡 <strong>Research Contribution:</strong> Route Riot closes these gaps by unifying hybrid edge sensing, common event normalization, proactive AI surge prediction, and live multi-modal redirection.
            </p>
          </div>
        </div>
      </section>

    </div>


    <!-- ====================================================================
         COLUMN 2: ARCHITECTURE, METHODOLOGY, PIPELINE, SPECS
         ==================================================================== -->
    <div class="column">

      <!-- Card 5: System Architecture (Slide 6, 10, 11) -->
      <section class="poster-card accent-cyan" style="flex: 1.6 1 0;">
        <div class="card-header">
          <div class="badge-number">05</div>
          <h2 class="card-title">Route Riot System Architecture</h2>
        </div>
        <div class="card-body">
          <!-- Full Vector Architecture Diagram (Exact match to Slide 10) -->
          <div style="background:#ffffff; border:1.2px solid #cbd5e1; border-radius:2.2mm; padding:1.8mm 1.6mm;">
            <svg width="372" height="215" viewBox="0 0 372 215" fill="none" xmlns="http://www.w3.org/2000/svg">
              <!-- Fleet Section Box -->
              <rect x="3" y="4" width="68" height="84" rx="3.5" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.2"/>
              <text x="37" y="16" fill="#0369A1" font-family="'Plus Jakarta Sans'" font-size="6.2" font-weight="800" text-anchor="middle">BMTC BUS FLEET</text>
              <!-- Mini Bus Graphic -->
              <rect x="7" y="24" width="60" height="38" rx="4" fill="#0284C7"/>
              <rect x="11" y="29" width="13" height="12" rx="1.5" fill="#E0F2FE"/>
              <rect x="28" y="29" width="13" height="12" rx="1.5" fill="#E0F2FE"/>
              <rect x="46" y="29" width="16" height="12" rx="1.5" fill="#E0F2FE"/>
              <circle cx="20" cy="62" r="4" fill="#0F172A"/>
              <circle cx="53" cy="62" r="4" fill="#0F172A"/>
              <text x="37" y="79" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="5" font-weight="600" text-anchor="middle">Live Bengaluru Fleet</text>

              <!-- Fleet Connector -->
              <path d="M71 24 L80 24 M71 66 L80 66" stroke="#0284C7" stroke-width="1.4" stroke-linecap="round"/>

              <!-- Subsystem A: Camera Bus -->
              <rect x="80" y="4" width="88" height="39" rx="3" fill="#F8FAFC" stroke="#38BDF8" stroke-width="1.1"/>
              <text x="85" y="14" fill="#0369A1" font-family="'Plus Jakarta Sans'" font-size="5.4" font-weight="800">📷 Camera-Equipped Bus</text>
              <rect x="85" y="19" width="36" height="19" rx="2" fill="#E0F2FE" stroke="#0284C7" stroke-width="0.8"/>
              <text x="103" y="30" fill="#0284C7" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Camera (Video)</text>
              <text x="124" y="30" fill="#0284C7" font-family="'Plus Jakarta Sans'" font-size="7" font-weight="800">➔</text>
              <rect x="129" y="19" width="35" height="19" rx="2" fill="#0284C7"/>
              <text x="146" y="29" fill="#FFFFFF" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="800" text-anchor="middle">YOLO</text>
              <text x="146" y="35" fill="#E0F2FE" font-family="'Plus Jakarta Sans'" font-size="3.8" text-anchor="middle">Person Detect</text>

              <!-- Subsystem B: Non-Camera Bus -->
              <rect x="80" y="49" width="88" height="39" rx="3" fill="#F8FAFC" stroke="#10B981" stroke-width="1.1"/>
              <text x="85" y="59" fill="#047857" font-family="'Plus Jakarta Sans'" font-size="5.4" font-weight="800">📶 Non-Camera Bus</text>
              <rect x="85" y="64" width="36" height="19" rx="2" fill="#ECFDF5" stroke="#10B981" stroke-width="0.8"/>
              <text x="103" y="74" fill="#047857" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">ESP32 Unit</text>
              <text x="103" y="80" fill="#047857" font-family="'Plus Jakarta Sans'" font-size="3.8" text-anchor="middle">Processing</text>
              <text x="124" y="75" fill="#047857" font-family="'Plus Jakarta Sans'" font-size="7" font-weight="800">+</text>
              <rect x="129" y="64" width="35" height="19" rx="2" fill="#047857"/>
              <text x="146" y="74" fill="#FFFFFF" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="800" text-anchor="middle">ToF Sensors</text>
              <text x="146" y="80" fill="#D1FAE5" font-family="'Plus Jakarta Sans'" font-size="3.8" text-anchor="middle">Entry/Exit Count</text>

              <!-- JSON Event Stream Indicator -->
              <path d="M168 23 L186 46 M168 68 L186 46" stroke="#00C9B7" stroke-width="1.5"/>
              <rect x="162" y="39" width="30" height="14" rx="2" fill="#041021" stroke="#00C9B7" stroke-width="0.8"/>
              <text x="177" y="46" fill="#00C9B7" font-family="'JetBrains Mono'" font-size="4" font-weight="800" text-anchor="middle">JSON EVENT</text>
              <text x="177" y="51" fill="#FFFFFF" font-family="'JetBrains Mono'" font-size="3.4" text-anchor="middle">REST Stream</text>

              <!-- Central Core: FastAPI Backend -->
              <rect x="192" y="16" width="58" height="60" rx="3.5" fill="#071830" stroke="#00C9B7" stroke-width="1.3"/>
              <text x="221" y="32" fill="#00C9B7" font-family="'JetBrains Mono'" font-size="7.5" font-weight="800" text-anchor="middle">FastAPI</text>
              <text x="221" y="44" fill="#FFFFFF" font-family="'Plus Jakarta Sans'" font-size="5.2" font-weight="800" text-anchor="middle">BACKEND</text>
              <text x="221" y="54" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="4.2" text-anchor="middle">Event Ingestion</text>
              <text x="221" y="62" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="4.2" text-anchor="middle">Validation & APIs</text>

              <!-- Connectors to Engines -->
              <path d="M250 31 L263 21 M250 60 L263 70" stroke="#38BDF8" stroke-width="1.4"/>

              <!-- Engine A: AI Prediction Layer -->
              <rect x="263" y="4" width="60" height="39" rx="2.5" fill="#F8FAFC" stroke="#0284C7" stroke-width="1.1"/>
              <text x="293" y="16" fill="#0369A1" font-family="'Plus Jakarta Sans'" font-size="5.2" font-weight="800" text-anchor="middle">🧠 AI PREDICTION</text>
              <text x="293" y="26" fill="#0284C7" font-family="'Plus Jakarta Sans'" font-size="4.6" font-weight="700" text-anchor="middle">Crowd Forecasting</text>
              <text x="293" y="34" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="4" text-anchor="middle">& Trend Analysis</text>

              <!-- Engine B: Alternative Engine -->
              <rect x="263" y="49" width="60" height="39" rx="2.5" fill="#F8FAFC" stroke="#D97706" stroke-width="1.1"/>
              <text x="293" y="61" fill="#B45309" font-family="'Plus Jakarta Sans'" font-size="5.2" font-weight="800" text-anchor="middle">🔄 ALTERNATIVE</text>
              <text x="293" y="71" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="4.6" font-weight="700" text-anchor="middle">Redirection Engine</text>
              <text x="293" y="79" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="4" text-anchor="middle">BMTC + Metro Sync</text>

              <!-- Connectors to Mobile App -->
              <path d="M323 21 L334 46 M323 70 L334 46" stroke="#10B981" stroke-width="1.4"/>

              <!-- Flutter Passenger App -->
              <rect x="334" y="8" width="36" height="80" rx="3.5" fill="#0F172A" stroke="#10B981" stroke-width="1.3"/>
              <text x="352" y="23" fill="#10B981" font-family="'Plus Jakarta Sans'" font-size="6" font-weight="800" text-anchor="middle">FLUTTER</text>
              <text x="352" y="33" fill="#FFFFFF" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Commuter</text>
              <text x="352" y="42" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">App</text>
              <rect x="337" y="52" width="30" height="14" rx="1.5" fill="#10B981"/>
              <text x="352" y="61" fill="#041021" font-family="'Plus Jakarta Sans'" font-size="4.4" font-weight="800" text-anchor="middle">Informed Trip</text>
              <text x="352" y="78" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="4" text-anchor="middle">👤 Passenger</text>

              <!-- Central Database Tier -->
              <rect x="3" y="96" width="366" height="46" rx="3" fill="#091A30" stroke="#334155" stroke-width="1.1"/>
              <text x="16" y="113" fill="#38BDF8" font-family="'JetBrains Mono'" font-size="5.8" font-weight="800">DATABASE TIER</text>
              <text x="16" y="124" fill="#94A3B8" font-family="'JetBrains Mono'" font-size="4.6">PostgreSQL / SQLite</text>

              <!-- Database Tables (Slide 10) -->
              <g transform="translate(88, 102)">
                <rect x="0" y="0" width="38" height="34" rx="2" fill="#1E293B"/>
                <text x="19" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">👤 Users</text>
                <text x="19" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">Auth & Prefs</text>

                <rect x="42" y="0" width="40" height="34" rx="2" fill="#1E293B"/>
                <text x="62" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">📱 Devices</text>
                <text x="62" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">Bus Telemetry</text>

                <rect x="86" y="0" width="42" height="34" rx="2" fill="#1E293B"/>
                <text x="107" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">📁 Events</text>
                <text x="107" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">Pax Ingestion</text>

                <rect x="132" y="0" width="40" height="34" rx="2" fill="#1E293B"/>
                <text x="152" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">📊 Analytics</text>
                <text x="152" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">Demand Trends</text>

                <rect x="176" y="0" width="46" height="34" rx="2" fill="#1E293B"/>
                <text x="199" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">⚠️ Incidents</text>
                <text x="199" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">Surge Alerts</text>

                <rect x="226" y="0" width="46" height="34" rx="2" fill="#1E293B"/>
                <text x="249" y="14" fill="#38BDF8" font-family="'Plus Jakarta Sans'" font-size="4.2" font-weight="700" text-anchor="middle">📑 Audit Logs</text>
                <text x="249" y="26" fill="#94A3B8" font-family="'Plus Jakarta Sans'" font-size="3.6" text-anchor="middle">System Health</text>
              </g>

              <!-- Connection Between Backend & Database -->
              <path d="M221 76 L221 96" stroke="#00C9B7" stroke-width="1.4" stroke-dasharray="2 2"/>

              <!-- Slide 11 Breakdown Bar (Input -> Process -> Decision -> Output) -->
              <rect x="3" y="150" width="366" height="56" rx="3" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
              <text x="10" y="163" fill="#0F172A" font-family="'Plus Jakarta Sans'" font-size="5.2" font-weight="800">SYSTEM ARCHITECTURE BREAKDOWN (SLIDE 11):</text>
              
              <g transform="translate(7, 170)">
                <!-- INPUT -->
                <rect x="0" y="0" width="84" height="30" rx="1.8" fill="#FFFFFF" stroke="#0284C7" stroke-width="0.8"/>
                <text x="6" y="11" fill="#0284C7" font-family="'Plus Jakarta Sans'" font-size="4.5" font-weight="800">INPUT:</text>
                <text x="6" y="18" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="3.8">Camera / ESP32 + ToF</text>
                <text x="6" y="25" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="3.5">Real-time movement capture</text>

                <!-- PROCESS -->
                <rect x="88" y="0" width="88" height="30" rx="1.8" fill="#FFFFFF" stroke="#059669" stroke-width="0.8"/>
                <text x="94" y="11" fill="#059669" font-family="'Plus Jakarta Sans'" font-size="4.5" font-weight="800">PROCESS:</text>
                <text x="94" y="18" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="3.8">FastAPI + AI Layer</text>
                <text x="94" y="25" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="3.5">Validates & predicts surges</text>

                <!-- DECISION -->
                <rect x="180" y="0" width="88" height="30" rx="1.8" fill="#FFFFFF" stroke="#D97706" stroke-width="0.8"/>
                <text x="186" y="11" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="4.5" font-weight="800">DECISION:</text>
                <text x="186" y="18" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="3.8">Alternative Engine</text>
                <text x="186" y="25" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="3.5">Compares BMTC & Metro</text>

                <!-- OUTPUT -->
                <rect x="272" y="0" width="86" height="30" rx="1.8" fill="#FFFFFF" stroke="#7C3AED" stroke-width="0.8"/>
                <text x="278" y="11" fill="#7C3AED" font-family="'Plus Jakarta Sans'" font-size="4.5" font-weight="800">OUTPUT:</text>
                <text x="278" y="18" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="3.8">Flutter Mobile App</text>
                <text x="278" y="25" fill="#64748B" font-family="'Plus Jakarta Sans'" font-size="3.5">Live guidance & alerts</text>
              </g>
            </svg>
          </div>

          <p style="font-size:7.5pt; color:#334155; line-height:1.20;">
            <strong>Hybrid Ingestion:</strong> Camera fleets process passenger density via edge YOLO inference; legacy fleets utilize dual doorway ToF break-beam sensors. All streams feed into a unified schema for real-time validation.
          </p>
        </div>
      </section>

      <!-- Card 6: Methodology & 6-Stage Pipeline (Slide 9 & 10) -->
      <section class="poster-card accent-emerald" style="flex: 1.15 1 0;">
        <div class="card-header">
          <div class="badge-number">06</div>
          <h2 class="card-title">Methodology & 6-Stage Pipeline</h2>
        </div>
        <div class="card-body">
          <!-- 4 Methodology Phases (Slide 9) -->
          <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:1.4mm;">
            <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:1.6mm; padding:1.3mm; text-align:center;">
              <span style="font-size:6.6pt; font-weight:800; color:#166534;">1. SENSING</span>
              <p style="font-size:5.8pt; color:#14532d; margin-top:0.3mm;">Camera / YOLO & ESP32 + ToF</p>
            </div>
            <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:1.6mm; padding:1.3mm; text-align:center;">
              <span style="font-size:6.6pt; font-weight:800; color:#1e40af;">2. PROCESSING</span>
              <p style="font-size:5.8pt; color:#1e3a8a; margin-top:0.3mm;">FastAPI Validation & Storage</p>
            </div>
            <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:1.6mm; padding:1.3mm; text-align:center;">
              <span style="font-size:6.6pt; font-weight:800; color:#92400e;">3. PREDICTION</span>
              <p style="font-size:5.8pt; color:#78350f; margin-top:0.3mm;">Low / Mod / High Surge AI</p>
            </div>
            <div style="background:#fdf4ff; border:1px solid #f5d0fe; border-radius:1.6mm; padding:1.3mm; text-align:center;">
              <span style="font-size:6.6pt; font-weight:800; color:#86198f;">4. REDIRECTION</span>
              <p style="font-size:5.8pt; color:#701a75; margin-top:0.3mm;">BMTC, Metro & Feeder sync</p>
            </div>
          </div>

          <!-- 6-Stage End-to-End Pipeline (Slide 10) -->
          <div style="display:grid; grid-template-columns: repeat(6, 1fr); gap:1mm; margin-top:0.6mm;">
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#0284c7;">1. CAPTURE</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">Camera & ToF</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#0284c7;">2. PROCESS</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">YOLO count</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#00877e;">3. INGEST</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">FastAPI JSON</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#7c3aed;">4. PREDICT</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">Crowd models</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#d97706;">5. RECOMMEND</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">Alternative routes</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.3mm; padding:1.2mm; text-align:center;">
              <span style="font-size:6.2pt; font-weight:800; color:#059669;">6. INFORM</span>
              <p style="font-size:5.4pt; color:#475569; margin-top:0.2mm;">Flutter app UI</p>
            </div>
          </div>

          <!-- Common Event JSON Payload Box -->
          <div style="background:#071529; border-radius:1.5mm; padding:1.2mm 1.8mm; font-family:'JetBrains Mono', monospace; font-size:6.4pt; color:#38bdf8; display:flex; justify-content:space-between; align-items:center;">
            <span>EVENT: {"bus_id": "KA01-500D", "route": "ORR", "curr_pax": 42, "cap": 60, "load_pct": 70, "method": "YOLO"}</span>
            <span style="color:#00c9b7; font-weight:800;">[VALIDATED]</span>
          </div>
        </div>
      </section>

      <!-- Card 7: Hardware & Software Requirements (Slide 8) -->
      <section class="poster-card accent-navy" style="flex: 1.25 1 0;">
        <div class="card-header">
          <div class="badge-number">07</div>
          <h2 class="card-title">Hardware & Software Specifications</h2>
        </div>
        <div class="card-body">
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.6mm;">
            <!-- Hardware Column -->
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.5mm; padding:1.3mm;">
              <span style="font-size:7pt; font-weight:800; color:#00629b; text-transform:uppercase;">HARDWARE STACK (SLIDE 8):</span>
              <table style="width:100%; font-size:6.2pt; border-collapse:collapse; margin-top:0.5mm;">
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #e2e8f0;"><strong>ESP32:</strong></td><td style="padding:0.7mm 0; color:#334155; border-bottom:1px solid #e2e8f0;">Processes ToF data & communicates</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #e2e8f0;"><strong>ToF Sensors:</strong></td><td style="padding:0.7mm 0; color:#334155; border-bottom:1px solid #e2e8f0;">VL53L0X doorway entry/exit detection</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #e2e8f0;"><strong>Camera:</strong></td><td style="padding:0.7mm 0; color:#334155; border-bottom:1px solid #e2e8f0;">Captures in-cabin passenger video</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #e2e8f0;"><strong>Edge Node:</strong></td><td style="padding:0.7mm 0; color:#334155; border-bottom:1px solid #e2e8f0;">Runs YOLO inference on camera buses</td></tr>
                <tr><td style="padding:0.7mm 0;"><strong>Smartphone:</strong></td><td style="padding:0.7mm 0; color:#334155;">Runs Route Riot Flutter mobile app</td></tr>
              </table>
            </div>

            <!-- Software Column -->
            <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:1.5mm; padding:1.3mm;">
              <span style="font-size:7pt; font-weight:800; color:#059669; text-transform:uppercase;">SOFTWARE STACK (SLIDE 8):</span>
              <table style="width:100%; font-size:6.2pt; border-collapse:collapse; margin-top:0.5mm;">
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #dcfce7;"><strong>Flutter/Dart:</strong></td><td style="padding:0.7mm 0; color:#14532d; border-bottom:1px solid #dcfce7;">Mobile application development</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #dcfce7;"><strong>Python/FastAPI:</strong></td><td style="padding:0.7mm 0; color:#14532d; border-bottom:1px solid #dcfce7;">REST API & backend communication</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #dcfce7;"><strong>YOLO:</strong></td><td style="padding:0.7mm 0; color:#14532d; border-bottom:1px solid #dcfce7;">Person detection & occupancy</td></tr>
                <tr><td style="padding:0.7mm 0; border-bottom:1px solid #dcfce7;"><strong>AI/ML Models:</strong></td><td style="padding:0.7mm 0; color:#14532d; border-bottom:1px solid #dcfce7;">Crowd classification & surge forecast</td></tr>
                <tr><td style="padding:0.7mm 0;"><strong>Firebase/SQLite:</strong></td><td style="padding:0.7mm 0; color:#14532d;">Cloud DB & historical data storage</td></tr>
              </table>
            </div>
          </div>

          <div style="background:#f1f5f9; border:1.1px solid #cbd5e1; border-radius:1.5mm; padding:1.2mm 1.6mm; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:6.8pt; color:#334155;"><strong>Communication:</strong> REST / JSON & WebSockets</span>
            <span style="font-size:6.8pt; color:#0369a1;"><strong>Cost Profile:</strong> Ultra-Low (&lt;₹3,500/non-camera bus retrofit)</span>
          </div>
        </div>
      </section>

    </div>


    <!-- ====================================================================
         COLUMN 3: CLASSIFICATION, MULTIMODAL APP, ANALYTICS, REFERENCES
         ==================================================================== -->
    <div class="column">

      <!-- Card 8: 3-Tier Classification & Route Curve (Slide 12) -->
      <section class="poster-card accent-emerald" style="flex: 1.25 1 0;">
        <div class="card-header">
          <div class="badge-number">08</div>
          <h2 class="card-title">3-Tier Crowd Classification & Route Curve</h2>
        </div>
        <div class="card-body">
          <!-- Circular Occupancy Gauge + Fleet Versatility (Slide 12) -->
          <div style="display:grid; grid-template-columns: 88px 1fr; gap:2mm; background:#f8fafc; border:1.1px solid #cbd5e1; border-radius:1.8mm; padding:1.2mm 1.6mm; align-items:center;">
            <!-- Donut Gauge SVG -->
            <svg width="86" height="52" viewBox="0 0 86 52" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M 8 46 A 35 35 0 0 1 78 46" stroke="#E2E8F0" stroke-width="7" stroke-linecap="round"/>
              <path d="M 8 46 A 35 35 0 0 1 58 15" stroke="#F59E0B" stroke-width="7" stroke-linecap="round"/>
              <text x="43" y="36" fill="#0F172A" font-family="'JetBrains Mono'" font-size="9" font-weight="900" text-anchor="middle">28 / 60</text>
              <text x="43" y="47" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="5.5" font-weight="800" text-anchor="middle">47% LOAD</text>
            </svg>
            <div style="display:flex; flex-direction:column; gap:0.5mm;">
              <span style="font-size:6.9pt; font-weight:800; color:#0f172a;">Real-Time Bus Occupancy Estimation</span>
              <span style="font-size:6.1pt; color:#475569;">YOLO & ToF provide unified load estimate across all configurations:</span>
              <div style="display:flex; gap:1.2mm; margin-top:0.4mm;">
                <span style="background:#e0f2fe; color:#0369a1; font-size:5.5pt; font-weight:800; padding:0.3mm 1.2mm; border-radius:1mm;">Standard 12m</span>
                <span style="background:#fef3c7; color:#92400e; font-size:5.5pt; font-weight:800; padding:0.3mm 1.2mm; border-radius:1mm;">Articulated</span>
                <span style="background:#dcfce7; color:#166534; font-size:5.5pt; font-weight:800; padding:0.3mm 1.2mm; border-radius:1mm;">Mini Feeder</span>
              </div>
            </div>
          </div>

          <!-- 3-Tier Crowd Grid (Slide 12) -->
          <div class="crowd-tier-grid">
            <div class="crowd-tier-card low">
              <span class="tier-badge">🟢 LOW</span>
              <span class="tier-range">0 – 30%</span>
              <span class="tier-desc">Plenty of space. Travel comfortably.</span>
            </div>
            <div class="crowd-tier-card mod">
              <span class="tier-badge">🟡 MODERATE</span>
              <span class="tier-range">31 – 70%</span>
              <span class="tier-desc">Getting busier. Plan ahead if possible.</span>
            </div>
            <div class="crowd-tier-card high">
              <span class="tier-badge">🔴 HIGH</span>
              <span class="tier-range">71 – 100%</span>
              <span class="tier-desc">Very crowded. Consider alternative.</span>
            </div>
          </div>

          <!-- Corridor Crowd Progression Line Graph (Slide 12) -->
          <div style="background:#ffffff; border:1.2px solid #cbd5e1; border-radius:2mm; padding:1.2mm 1.6mm;">
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:6.4pt; font-weight:800; color:#0f172a; margin-bottom:0.6mm;">
              <span>PREDICTED CROWD LEVEL ALONG THE ROUTE (SLIDE 12):</span>
              <span style="color:#dc2626;">Next Crowding Peak: 08:45 AM (Yeshwanthpur)</span>
            </div>
            
            <!-- SVG Curve showing Majestic -> Sadashivanagar -> Yeshwanthpur Peak -> Hebbal -->
            <svg width="365" height="42" viewBox="0 0 365 42" fill="none" xmlns="http://www.w3.org/2000/svg">
              <!-- Threshold bands -->
              <rect x="0" y="0" width="365" height="13" fill="#FEE2E2" opacity="0.3"/>
              <rect x="0" y="13" width="365" height="15" fill="#FEF3C7" opacity="0.3"/>
              <rect x="0" y="28" width="365" height="14" fill="#DCFCE7" opacity="0.3"/>
              
              <!-- Threshold Lines -->
              <line x1="0" y1="13" x2="365" y2="13" stroke="#FCA5A5" stroke-width="0.8" stroke-dasharray="2 2"/>
              <line x1="0" y1="28" x2="365" y2="28" stroke="#FDE68A" stroke-width="0.8" stroke-dasharray="2 2"/>
              
              <!-- Curve -->
              <path d="M 25 34 Q 85 30 145 20 T 215 6 T 285 24 T 345 33" fill="none" stroke="#DC2626" stroke-width="2.2" stroke-linecap="round"/>
              
              <!-- Stop Nodes -->
              <circle cx="25" cy="34" r="3" fill="#166534"/>
              <text x="25" y="40" fill="#166534" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Majestic</text>
              
              <circle cx="105" cy="26" r="3" fill="#D97706"/>
              <text x="105" y="40" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Shivajinagar</text>

              <circle cx="170" cy="16" r="3" fill="#D97706"/>
              <text x="170" y="40" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Sadashivanagar</text>
              
              <circle cx="215" cy="6" r="4.2" fill="#DC2626" stroke="#FFFFFF" stroke-width="1.2"/>
              <text x="215" y="15" fill="#DC2626" font-family="'Plus Jakarta Sans'" font-size="5.2" font-weight="900" text-anchor="middle">Yeshwanthpur (Peak 8:45 AM)</text>
              
              <circle cx="285" cy="24" r="3" fill="#D97706"/>
              <text x="285" y="40" fill="#D97706" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">Hebbal</text>

              <circle cx="345" cy="33" r="3" fill="#166534"/>
              <text x="345" y="40" fill="#166534" font-family="'Plus Jakarta Sans'" font-size="4.8" font-weight="700" text-anchor="middle">RT Nagar</text>
            </svg>
          </div>

          <!-- Slide 12 Route View Table & Why Insights -->
          <div style="display:grid; grid-template-columns: 2fr 1fr; gap:1.4mm; font-size:6.3pt;">
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:1.4mm; padding:1.1mm;">
              <strong>Route View:</strong> Majestic <span style="color:#166534;">(Low)</span> ➔ Shivajinagar <span style="color:#d97706;">(Mod)</span> ➔ Sadashivanagar <span style="color:#d97706;">(Mod)</span> ➔ Yeshwanthpur <span style="color:#dc2626; font-weight:800;">(High)</span> ➔ Hebbal <span style="color:#d97706;">(Mod)</span> ➔ RT Nagar <span style="color:#166534;">(Low)</span>
            </div>
            <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:1.4mm; padding:1.1mm; color:#1e40af;">
              <strong>The Result:</strong> Earlier awareness, better choices, avoid peak crowd.
            </div>
          </div>
        </div>
      </section>

      <!-- Card 9: Multi-Modal Redirection & Commuter UI (Slides 3, 10, 13) -->
      <section class="poster-card accent-amber" style="flex: 1.25 1 0;">
        <div class="card-header">
          <div class="badge-number">09</div>
          <h2 class="card-title">Multi-Modal Redirection & Commuter App</h2>
        </div>
        <div class="card-body">
          <p>
            When an approaching bus is crowded, the <strong>Alternative Engine</strong> evaluates multi-modal travel options to provide instant, stress-free travel recommendations:
          </p>

          <!-- Interactive Mobile UI Card Preview (from Slide 3 & 13) -->
          <div class="app-preview-card">
            <div class="app-preview-header">
              <span style="font-weight:800; color:#38BDF8; font-size:7.8pt;">ROUTE RIOT COMMUTER APP</span>
              <span style="color:#94A3B8; font-size:6.8pt;">Live crowd intelligence</span>
            </div>

            <!-- Active Bus 500D -->
            <div style="background:#16243b; border-radius:1.6mm; padding:1.2mm 1.8mm; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <div style="font-size:8.2pt; font-weight:800; color:#FFFFFF;">Route 500D • 42 / 60 Passengers</div>
                <div style="font-size:6.5pt; color:#FCA5A5;">Crowding rising in ~15 min (Yeshwanthpur)</div>
              </div>
              <span class="crowd-pill high">HIGH • 70% LOAD</span>
            </div>

            <!-- Multi-Modal Comparison (Slide 13) -->
            <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:1.2mm;">
              <div style="background:#1e293b; border:1px solid #334155; border-radius:1.5mm; padding:1mm; text-align:center;">
                <div style="font-size:6.1pt; color:#94a3b8; font-weight:700;">BMTC 500D</div>
                <div style="font-size:7pt; color:#F87171; font-weight:800;">45 min • ₹20</div>
                <div style="font-size:5.5pt; color:#CBD5E1;">Direct, High Crowd</div>
              </div>
              <div style="background:#1e293b; border:1.2px solid #00C9B7; border-radius:1.5mm; padding:1mm; text-align:center;">
                <div style="font-size:6.1pt; color:#00C9B7; font-weight:800;">BMTC 500K</div>
                <div style="font-size:7pt; color:#34D399; font-weight:800;">38 min • ₹25</div>
                <div style="font-size:5.5pt; color:#A7F3D0;">Moderate Crowd ★</div>
              </div>
              <div style="background:#1e293b; border:1px solid #F59E0B; border-radius:1.5mm; padding:1mm; text-align:center;">
                <div style="font-size:6.1pt; color:#FBBF24; font-weight:700;">Namma Metro</div>
                <div style="font-size:7pt; color:#FCD34D; font-weight:800;">28 min • ₹40</div>
                <div style="font-size:5.5pt; color:#FEF3C7;">Fast, Low Crowd</div>
              </div>
            </div>

            <!-- Smart Redirection Action Box -->
            <div style="background:rgba(0, 201, 183, 0.16); border:1.1px solid #00C9B7; border-radius:1.5mm; padding:1.2mm 1.6mm;">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:7.2pt; font-weight:800; color:#00C9B7;">⚡ SMART REDIRECTION</span>
                <span style="font-size:6.4pt; font-weight:800; color:#FCD34D;">Lower Crowd Route</span>
              </div>
              <div style="font-size:6.8pt; color:#E2E8F0; margin-top:0.3mm; line-height:1.18;">
                <strong>Try Route 500K</strong> or switch to <strong>Namma Metro Green Line</strong> at Yeshwanthpur Interchange.
              </div>
            </div>
          </div>

          <div style="font-size:6.8pt; color:#64748b; line-height:1.16;">
            <strong>Passenger Decision Support (Slide 13):</strong> Deliver actionable information through Flutter. Passengers view Live Occupancy + Crowd Level + Prediction + Multi-Modal Alternatives in one interface.
          </div>
        </div>
      </section>

      <!-- Card 10: Transport Analytics for BMTC (Slide 13) -->
      <section class="poster-card accent-cyan" style="flex: 1.15 1 0;">
        <div class="card-header">
          <div class="badge-number">10</div>
          <h2 class="card-title">Transport Analytics for BMTC</h2>
        </div>
        <div class="card-body">
          <!-- 4 Analytics Pillars (Slide 13) -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.3mm;">
            <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:1.4mm; padding:1.2mm 1.3mm;">
              <span style="font-size:6.7pt; font-weight:800; color:#166534;">1. Peak-Demand Identification</span>
              <p style="font-size:6pt; color:#14532d; margin-top:0.2mm;">Pinpoint exact stops and times where crowding builds up across corridors.</p>
            </div>
            <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:1.4mm; padding:1.2mm 1.3mm;">
              <span style="font-size:6.7pt; font-weight:800; color:#1e40af;">2. Route-Level Crowd Analysis</span>
              <p style="font-size:6.1pt; color:#1e3a8a; margin-top:0.2mm;">Compare average occupancy across parallel routes for transit load-balancing.</p>
            </div>
            <div style="background:#fef3c7; border:1px solid #fde68a; border-radius:1.4mm; padding:1.2mm 1.3mm;">
              <span style="font-size:6.7pt; font-weight:800; color:#92400e;">3. Future Model Retraining</span>
              <p style="font-size:6pt; color:#78350f; margin-top:0.2mm;">Continuous learning using real-world sensor logs to boost forecast accuracy.</p>
            </div>
            <div style="background:#fdf4ff; border:1px solid #f5d0fe; border-radius:1.4mm; padding:1.2mm 1.3mm;">
              <span style="font-size:6.7pt; font-weight:800; color:#86198f;">4. Dynamic Fleet Allocation</span>
              <p style="font-size:6pt; color:#701a75; margin-top:0.2mm;">Data-driven dispatch for extra feeder buses to alleviate choke points.</p>
            </div>
          </div>

          <!-- Slide 13 Analytics Visuals: Peak Trendline + Route Load Bar Chart -->
          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1.4mm; background:#ffffff; border:1.1px solid #cbd5e1; border-radius:1.6mm; padding:1.2mm 1.4mm;">
            <!-- Mini Chart A: Hourly Trend -->
            <div>
              <span style="font-size:6.2pt; font-weight:800; color:#0f172a;">Hourly Occupancy Peak Pattern</span>
              <svg width="170" height="34" viewBox="0 0 170 34" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M 10 28 Q 35 4 55 10 T 95 25 T 135 6 T 160 28" fill="none" stroke="#0284C7" stroke-width="1.8"/>
                <circle cx="45" cy="7" r="2.5" fill="#DC2626"/>
                <text x="45" y="16" fill="#DC2626" font-size="4.4" font-weight="800" text-anchor="middle">8:30 AM (88%)</text>
                <circle cx="135" cy="6" r="2.5" fill="#DC2626"/>
                <text x="135" y="15" fill="#DC2626" font-size="4.4" font-weight="800" text-anchor="middle">6:30 PM (94%)</text>
                <line x1="5" y1="30" x2="165" y2="30" stroke="#94A3B8" stroke-width="0.6"/>
                <text x="10" y="33" fill="#64748B" font-size="3.8">6 AM</text>
                <text x="95" y="33" fill="#64748B" font-size="3.8">12 PM</text>
                <text x="160" y="33" fill="#64748B" font-size="3.8">10 PM</text>
              </svg>
            </div>
            <!-- Mini Chart B: Route Load Bar Chart -->
            <div>
              <span style="font-size:6.2pt; font-weight:800; color:#0f172a;">Average Route Occupancy</span>
              <div style="display:flex; flex-direction:column; gap:0.7mm; margin-top:0.6mm;">
                <div style="display:flex; align-items:center; gap:1mm; font-size:5.2pt;">
                  <span style="width:28px; font-weight:700;">500D:</span>
                  <div style="flex:1; background:#e2e8f0; border-radius:1mm; height:4.5px; overflow:hidden;">
                    <div style="width:88%; background:#dc2626; height:100%;"></div>
                  </div>
                  <span style="font-weight:800; color:#dc2626;">88%</span>
                </div>
                <div style="display:flex; align-items:center; gap:1mm; font-size:5.2pt;">
                  <span style="width:28px; font-weight:700;">335E:</span>
                  <div style="flex:1; background:#e2e8f0; border-radius:1mm; height:4.5px; overflow:hidden;">
                    <div style="width:74%; background:#f59e0b; height:100%;"></div>
                  </div>
                  <span style="font-weight:800; color:#d97706;">74%</span>
                </div>
                <div style="display:flex; align-items:center; gap:1mm; font-size:5.2pt;">
                  <span style="width:28px; font-weight:700;">201R:</span>
                  <div style="flex:1; background:#e2e8f0; border-radius:1mm; height:4.5px; overflow:hidden;">
                    <div style="width:58%; background:#059669; height:100%;"></div>
                  </div>
                  <span style="font-weight:800; color:#059669;">58%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Card 11: Conclusion & Major References (Slide 14, 15) -->
      <section class="poster-card accent-navy" style="flex: 1.15 1 0;">
        <div class="card-header">
          <div class="badge-number">11</div>
          <h2 class="card-title">Conclusion & Major References</h2>
        </div>
        <div class="card-body">
          <div style="background:#fef3c7; border:1.1px solid #fde68a; border-radius:1.5mm; padding:1.2mm 1.6mm;">
            <p style="font-size:6.7pt; color:#92400e; font-weight:700; line-height:1.18;">
              🎯 <strong>Conclusion (Slide 15):</strong> Route Riot combines IoT sensors & AI to monitor and predict bus occupancy in real time. Through the Flutter application, passengers can view crowd levels and make informed travel decisions. The system aims to reduce overcrowding, improve passenger distribution, and make public transportation smarter and more efficient.
            </p>
          </div>

          <!-- Exact References from Slide 14 -->
          <div>
            <span style="font-size:6.9pt; font-weight:800; color:#00629b; text-transform:uppercase;">MAJOR REFERENCES (SLIDE 14):</span>
            <ol style="font-size:5.8pt; color:#334155; margin-top:0.3mm; padding-left:3mm; line-height:1.18;">
              <li><strong>Hsu et al.</strong> — Estimation of the Number of Passengers in a Bus Using Deep Learning.</li>
              <li><strong>Wood et al.</strong> — Frameworks for Real-Time Bus Passenger Occupancy Prediction.</li>
              <li><strong>Dharmarajan et al.</strong> — Depth Imaging-Based Passenger Counting Sensor for Public Transit.</li>
              <li><strong>Li et al.</strong> — Automatic Passenger Counting System for Bus Based on RGB-D Video.</li>
              <li><strong>Transp. Res. Procedia</strong> — Wireless Sensor Network Architecture for Passenger Counting.</li>
              <li><strong>Ultralytics</strong> — YOLO Documentation; <strong>STMicroelectronics</strong> — VL53L0X ToF Sensor Documentation.</li>
            </ol>
          </div>
        </div>
      </section>

    </div>

  </main>


  <!-- ========================================================================
       FOOTER BAR (HEIGHT: ~23mm)
       ======================================================================== -->
  <footer class="footer-bar">
    <div class="footer-left">
      <div class="footer-headline">
        <span class="tag">CONCLAVE IMPACT</span>
        <span>Route Riot: Moving beyond bus tracking toward predictive, multi-modal passenger assistance.</span>
      </div>
      <div class="footer-subtext">
        Department of Computer Science & Engineering, <strong>Vijaya Vittala Institute of Technology (VTU)</strong>, Bengaluru.
        Guided by <strong>Prof. Rashmi Rani Samantaray</strong> | Team: <strong>Lokpradeep H · Dhikshita A · Harish P*</strong>
      </div>
    </div>

    <div class="footer-center-meta">
      <div class="event-venue-text">CHRIST (Deemed to be University), Yeshwanthpur, Bengaluru</div>
      <div class="event-date-text">IEEE Information Theory Industry Conclave • October 3, 2026</div>
    </div>

    <div class="footer-right-qr">
      <div class="qr-box">
        <!-- Embedded Standalone SVG QR Code -->
        __QR_CODE_SVG_CONTENT__
      </div>
      <div class="qr-label-block">
        <span class="qr-scan-title">PROJECT REPO</span>
        <span class="qr-scan-desc">Scan for project code, FastAPI & Flutter demo</span>
      </div>
    </div>
  </footer>

</div>

</body>
</html>
"""

def generate_poster():
    print("=== STARTING ROUTE RIOT IEEE POSTER GENERATION (v12 - BALANCED MASTERPIECE) ===")
    output_dir = r"C:\Users\Harish\OneDrive\Desktop\IEEE"
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the vector QR code SVG if available
    qr_svg_path = os.path.join(output_dir, "qr_code.svg")
    qr_svg_content = ""
    if os.path.exists(qr_svg_path):
        with open(qr_svg_path, "r", encoding="utf-8") as f:
            qr_svg_content = f.read()
            if "<?xml" in qr_svg_content:
                qr_svg_content = qr_svg_content[qr_svg_content.find("<svg"):]
    else:
        qr_svg_content = '<svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="#000"/><text x="50" y="55" fill="#fff" font-size="12" text-anchor="middle">QR CODE</text></svg>'
    
    final_html = POSTER_HTML.replace("__QR_CODE_SVG_CONTENT__", qr_svg_content)
    
    html_file = os.path.join(output_dir, "ROUTE_RIOT_IEEE_A2_POSTER.html")
    index_file = os.path.join(output_dir, "index.html")
    pdf_file = os.path.join(output_dir, "ROUTE_RIOT_IEEE_A2_POSTER.pdf")
    png_file = os.path.join(output_dir, "ROUTE_RIOT_IEEE_A2_POSTER.png")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"1. HTML source files written: {html_file} and {index_file}")
    
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    print(f"2. Compiling A2 Vector PDF using: {chrome_path} ...")
    pdf_cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    res_pdf = subprocess.run(pdf_cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file):
        pdf_size = os.path.getsize(pdf_file)
        print(f"   [SUCCESS] Vector PDF Generated! Size: {pdf_size:,} bytes ({pdf_size/1024:.1f} KB)")
    else:
        print(f"   [ERROR] PDF generation failed: {res_pdf.stderr}")
        
    print(f"3. Rendering High-Resolution PNG Preview (matching exact 420mm x 594mm aspect ratio) ...")
    # 420mm = 1587.4 px at 96 DPI, 594mm = 2245.0 px at 96 DPI
    # Using window-size=1588,2246 with device scale factor 2 yields 3176 x 4492 px
    png_cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--force-device-scale-factor=2",
        "--window-size=1588,2246",
        f"--screenshot={png_file}",
        html_file
    ]
    res_png = subprocess.run(png_cmd, capture_output=True, text=True)
    if os.path.exists(png_file):
        png_size = os.path.getsize(png_file)
        print(f"   [SUCCESS] High-Res PNG Generated! Size: {png_size:,} bytes ({png_size/(1024*1024):.2f} MB)")
    else:
        print(f"   [ERROR] PNG generation failed: {res_png.stderr}")

    print("=== POSTER GENERATION COMPLETE ===")

if __name__ == "__main__":
    generate_poster()
