
# MBSE Day 1 – Block Definition Diagram (BDD)

![Safety Monitoring System BDD](safety_monitoring_system_bdd.png)

---

## 🧭 Overview

This diagram models a **Safety Monitoring System** using a simplified **SysML-style Block Definition Diagram (BDD)**. It reflects a typical safety-critical system with clear component structure, behaviors, and inter-block relationships.

---

## 📦 Modeled Blocks

### `Safety Monitoring System`
- Top-level system composed of 3 internal components.
- Represents the system responsible for handling safety events and communication.

### `Safety Analyzer`
- Monitors safety-related data.
- Reports potential hazards or anomalies.

### `Incident Reporter`
- Gathers, logs, and prepares safety incident data.
- Interfaces with communication systems for delivery.

### `Communication Interface`
- Transmits incident reports to external systems or users.

---

## 🔗 Key Relationships

- `Safety Monitoring System` **composes** all 3 components.
- `Safety Analyzer` **monitors** `Incident Reporter`.
- `Incident Reporter` **uses** `Communication Interface`.

---

## 🔧 Technical Notes

- Each block shows one attribute and one method for simplicity.
- Color coding improves visual comprehension and readability.
- Modeled using [draw.io](https://draw.io), mimicking SysML conventions.

---

## 💡 Why This Matters

This BDD demonstrates model-based thinking for safety-critical systems — an approach that combines:
- **System Architecture**
- **Safety Engineering**
- **Software and Communications Integration**

🔗 Built by: Sean Mayers  
🎯 Career Transition: From NASA/DoD system safety → MBSE + System Architecture

---

> ✅ This is part of Sean's ongoing MBSE portfolio to prepare for $145K+ roles in aerospace, defense, and intelligent systems.

