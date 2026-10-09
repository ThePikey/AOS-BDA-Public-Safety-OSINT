# 📡 AOS Public Safety BDA & AHJ Permitting OSINT Crawler

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Public Safety Standards](https://img.shields.io/badge/Standards-FCC_Part_90_%7C_IFC_510_%7C_NFPA_1225-green.svg)](https://www.fcc.gov/)
[![Branding: Cedar AI](https://img.shields.io/badge/Brand-Cedar_AI_%2F_AOS-gold.svg)](https://github.com/ThePikey)

An open-source OSINT crawler, compliance auditor, and LLM wrapper pipeline for **Public Safety Bi-Directional Amplifiers (BDA / ERCES)** and **Municipal Authority Having Jurisdiction (AHJ) Fire Permitting**.

---

## 🎯 Purpose & Domain Scope

Public safety first-responders (police, fire, EMS) rely on in-building radio coverage across 700 MHz FirstNet, 800 MHz NPSPAC, UHF, and VHF bands. When commercial buildings attenuate RF signals, **Emergency Responder Communication Enhancement Systems (ERCES)** and BDAs are required by law under:

* **FCC 47 CFR § 90.219**: Federal registration, Class A/B booster classification, max 5W ERP, and uplink noise limits ($\le -43\text{ dBm/MHz}$).
* **IFC Section 510**: International Fire Code mandatory 20-grid in-building emergency radio coverage (95% general, 99% critical areas).
* **NFPA 1221 / NFPA 1225**: National Fire Protection Association standards for secondary power runtime (12h / 24h battery backup) and annual recertification.

This application crawls public FCC signal booster filings, queries local municipal fire prevention bureau permits, and formats structured compliance payloads ready for LLMs (OpenAI, Anthropic Claude, Ollama, LangChain).

---

## ⚡ Architecture Overview

```
[ FCC Signal Booster Registry ] ──┐
                                  ├──► [ BDA OSINT Crawler Engine ] ──► [ Local SQLite DB ]
[ Municipal AHJ Fire Permits ]  ──┘                 │
                                                    ▼
                                       [ LLM Prompt Transformer ]
                                                    │
                                                    ▼
                                  [ Automated Audit PDF / JSON Report ]
```

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/ThePikey/AOS-BDA-Public-Safety-OSINT.git
cd AOS-BDA-Public-Safety-OSINT
pip install -r requirements.txt
```

### 2. Crawl & Ingest BDA Records
```bash
python3 src/bda_crawler_public.py --city "Roseburg" --state "OR" --export-json
```

### 3. LLM Wrapper Integration
The crawler outputs pre-formatted audit prompts formatted for downstream LLM analysis:
```python
from src.bda_crawler_public import search_fcc_and_ahj, generate_llm_compliance_prompt

records = search_fcc_and_ahj(query_city="Roseburg", query_state="OR")
for rec in records:
    llm_prompt = generate_llm_compliance_prompt(rec)
    print(llm_prompt)
```

---

## 🛡 License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

Developed in collaboration with **Cedar AI & the Autocatalytic Omega System (AOS)**.  
Sole Architect: Joshua Edward Osborne (Oz).
