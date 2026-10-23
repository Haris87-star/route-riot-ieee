# ROUTE RIOT: IEEE Information Theory Industry Conclave 2026 Poster

**Theme:** *From Theory ➔ Technology ➔ Impact*  
**Event:** IEEE InfoTheory Industry Conclave 2026  
**Date:** Saturday, 3 October 2026 | **Time:** 2:00 PM onwards  
**Venue:** CHRIST (Deemed to be University), Yeshwanthpur Campus, Bengaluru  
**Organized by:** IEEE Information Theory Society Bangalore Chapter & IEEE Bangalore Section  
**Authors:** Lokpradeep H, Dhikshita A, Harish P (*Presenter)  
**Affiliation:** Department of Computer Science & Engineering, Vijaya Vittala Institute of Technology (VTU), Bengaluru  

---

## 📁 Generated Files in Workspace

| File Name | Description | Recommended Use |
| :--- | :--- | :--- |
| **[`ROUTE_RIOT_IEEE_A2_POSTER.pdf`](file:///C:/Users/Harish/OneDrive/Desktop/IEEE/ROUTE_RIOT_IEEE_A2_POSTER.pdf)** | **True Vector A2 Print-Ready PDF** (420 mm × 594 mm, Portrait) | **Send this file directly to the print shop for printing.** High-precision vector typography, crisp SVGs, zero raster pixelation. |
| **[`ROUTE_RIOT_IEEE_A2_POSTER.png`](file:///C:/Users/Harish/OneDrive/Desktop/IEEE/ROUTE_RIOT_IEEE_A2_POSTER.png)** | **Ultra High-Resolution Preview Image** (2384 × 3370 px) | Instant visual inspection, digital sharing, WhatsApp, or submission attachments. |
| **[`index.html`](file:///C:/Users/Harish/OneDrive/Desktop/IEEE/index.html)** | **Complete Standalone Web Source** | Open in any browser (Chrome/Edge/Firefox), zoom infinitely, or display on 4K digital screens. |
| **[`build_poster.py`](file:///C:/Users/Harish/OneDrive/Desktop/IEEE/build_poster.py)** | **Automated Python Build Pipeline** | One-command compilation: `python build_poster.py` rebuilds both PDF and PNG. |

---

## 🖨️ Printing Instructions for Print Shop

1. **Poster Dimensions:** Exactly **A2 size (420 mm × 594 mm)** in **Portrait** orientation.
2. **Paper Stock:**
   - **Recommended:** 220 GSM – 260 GSM Semi-Gloss / Satin / Matte Paper (prevents glare under conference spotlights while preserving deep IEEE navy tones).
3. **Color Profile:** 
   - Full CMYK / High-Gamut RGB color print.
4. **Mounting:** 
   - Foam-core board (5mm) or standard poster display stand mounting.

---

## 🎤 1-to-3 Minute Pitch Guide for the Judges

> **"Good afternoon respected judges. We are presenting ROUTE RIOT, a cyber-physical framework bridging Information Theory, edge computing, and real-time passenger redirection for BMTC public transport."**

1. **The Core Problem (Theory Gap):**
   - BMTC runs over 6,000 buses carrying 3.5M commuters daily. 
   - Current systems display GPS locations and ETAs, but remain *completely blind to onboard crowd density*.
   - This causes severe occupancy asymmetry (one bus at 120% crush load while trailing buses run at 35%) and chronic bus bunching.

2. **The Theoretical Formulation (From Theory):**
   - We model commuter arrival stochasticity using **Shannon Demand Entropy** $H(X_s) = -\sum p_k \log_2 p_k$ to quantify surge vulnerability.
   - We quantify headway irregularity via the **Bus Bunching Index (BBI)** $\sigma_h / \mu_h$.
   - Redirection is driven by a multi-objective cost function balancing wait time, travel time, and a nonlinear crowd discomfort penalty.

3. **The Technological Innovation (To Technology):**
   - **Ultra-low cost edge unit (<₹3,500/bus):** ESP32 + dual Time-of-Flight (ToF) directional infrared distance sensors at doors + lightweight YOLOv8n edge vision.
   - **100% Privacy by Design:** Zero video leaves the bus. Everything runs in volatile RAM at the edge; only anonymized scalar vectors are transmitted over MQTT.
   - **Spatial-Temporal GCN:** Forecasts crowd progression 3–5 stops (15–30 min) in advance along arterial corridors.
   - **Commuter App:** Built in Flutter, providing intuitive 3-tier crowd states (Low/Moderate/High) and 1-tap redirection to trailing buses, parallel feeders, or Namma Metro.

4. **The Real-World Impact (To Impact):**
   - Benchmarked on Bengaluru’s Silk Board ↔ Hebbal Outer Ring Road corridor:
     - **-28.4% Commuter Wait Time** during morning peak hours.
     - **-34.2% Reduction in Bus Bunching Index (BBI)**.
     - **+31.8% Increase in Fleet Load Entropy Balance**.
     - **22.8% Multimodal Diversion** to Namma Metro & parallel feeders.
   - Enables BMTC to unlock ~31% additional carrying capacity from existing fleets without purchasing new buses.

---

## 🛡️ Quick Answers to Tough Judge Questions

- **Q: How do you handle sensor error or disagreements between camera and ToF sensors?**  
  *A:* We employ a Bayesian Kalman state fusion filter. If a door sensor misses rapid entry bursts, the periodic in-cabin YOLO density scan recalibrates the true occupancy. If telemetry is stale (>15 seconds), it is automatically discarded.

- **Q: Is video recorded or streamed to the cloud? What about passenger privacy?**  
  *A:* Absolutely no video is streamed or saved. Frames are processed directly in volatile RAM on the edge board and immediately overwritten. Only numbers (`bus_id`, `occupancy_ratio`, `timestamp`) are sent via MQTT.

- **Q: What if the passenger doesn't want to switch routes?**  
  *A:* Route Riot is strictly advisory. We do not enforce redirection; commuters retain autonomous choice. However, real-time ETA and crowd comparisons naturally incentivize commuters to distribute across available capacity.
