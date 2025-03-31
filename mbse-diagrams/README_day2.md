
## MBSE Day 2 – Internal Block Diagram (IBD)

![Safety Monitoring System IBD](safety_monitoring_system_ibd.png)

---

### 🧭 Overview

This Internal Block Diagram (IBD) shows the **internal structure** of the `Safety Monitoring System`, expanding on the Block Definition Diagram (BDD) from MBSE Day 1.

The IBD focuses on **interfaces and internal connections** between the components — modeling how information (incident data, status, and transmission commands) flows within the system.

---

### 🔧 Modeled Components & Ports

Each internal block exposes **ports** that represent key data flow:

#### `Safety Analyzer`
- `incidentOut : string`
- `reportStatus : boolean`
- `transmitData : string`

#### `Incident Reporter`
- Receives `incidentStatus:string` from analyzer
- Outputs incident data to `Communication Interface`

#### `Communication Interface`
- Receives structured report data
- Sends it externally

---

### 🔁 Data Flow

- `Safety Analyzer` ➝ `Incident Reporter`: `incidentStatus : string`
- `Incident Reporter` ➝ `Communication Interface`: `reportData : string`

---

### 📘 MBSE Concepts Demonstrated
- Internal Block Diagram (IBD)
- Interfaces and connectors
- Value types on ports
- Composition and behavior flow
- System decomposition

---

> ✅ This is part of Sean Mayers' MBSE modeling portfolio designed for $145K+ roles in system architecture, aerospace, and safety-critical systems.
