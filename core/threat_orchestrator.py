сlass ThreatOrchestrator:
    # Ranks derived from Appendix D (real incidents) + AIVSS scoring
    THREAT_RANK = {
        "ASI01": 1,  # Goal Hijack — EchoLeak, Operator, Inception
        "ASI05": 2,  # RCE — Shell injection, eval(), tool chaining
        "ASI03": 3,  # Identity Abuse — Confused deputy, memory-based escalation
        "ASI02": 4,  # Tool Misuse — EDR bypass, over-privileged APIs
        "ASI04": 5,  # Supply Chain — MCP poisoning, typo-squatting
        "ASI06": 6,  # Memory Poisoning — RAG bleed, cross-tenant context
        "ASI07": 7,  # Insecure Comms — MITM, descriptor forgery
        "ASI08": 8,  # Cascading Failures — Financial trading collapse, auto-remediation loops
        "ASI09": 9,  # Human Trust Exploitation — Fake explainability, emotional manipulation
        "ASI10": 10 # Rogue Agents — Self-replication, goal drift
    }

    def run_all_tests(self, target):
        ordered_asi = sorted(self.THREAT_RANK, key=self.THREAT_RANK.get)
        for asi_id in ordered_asi:
            print(f"[+] Executing Kevlar module: {asi_id}")
            self._load_and_run_module(asi_id, target)