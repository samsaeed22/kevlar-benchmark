# Kevlar: OWASP Top 10 for Agentic Apps 2026 Red Team Benchmark

🛡️ **Full-coverage security benchmark** for AI agents based on [OWASP Top 10 for Agentic Applications (2026)](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

> Licensed under CC BY-SA 4.0 — Attribution required.  
> Designed for **authorized red teaming only**.

## Coverage
- **Critical**: ASI01 (Goal Hijack), ASI05 (RCE), ASI03 (Identity Abuse), ASI02 (Tool Misuse), ASI04 (Supply Chain)
- **High**: ASI06 (Memory Poisoning), ASI07 (Inter-Agent Comms), ASI08 (Cascading Failures)
- **Medium**: ASI09 (Human Trust Exploitation), ASI10 (Rogue Agents)

## Quick Start
```bash
gh repo create my-kevlar-run --template https://github.com/toxy4ny/kevlar-benchmark --public
cd my-kevlar-run
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt