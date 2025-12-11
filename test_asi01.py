#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.critical.asi01_goal_hijack import GoalHijackOrchestrator
# from modules.critical.asi01_goal_hijack.utils.mock_agents import MockCopilotAgent

from local_agent import AutoGenAgentWrapper

# from real_agent import RealLangChainAgent

COLORS = {
    "CRITICAL": "\033[91m🔴",  # Red
    "HIGH": "\033[93m🟡",      # Yellow
    "MEDIUM": "\033[94m🔵",    # Blue
    "NONE": "\033[92m🟢",      # Green
    "RESET": "\033[0m"
}

def print_banner():
    print(f"""
{'='*60}
🛡️  Kevlar — ASI01: Agent Goal Hijack Test Runner
{'='*60}
Testing against OWASP Top 10 for Agentic Apps 2026
Scenarios: EchoLeak, Operator, Inception, Goal-lock drift
{'='*60}
""")

def format_result(result):
    severity = result.get("severity", "NONE")
    icon = COLORS.get(severity, COLORS["NONE"])
    reset = COLORS["RESET"]
    status = "VULNERABLE" if result.get("vulnerable", False) else "SAFE"
    
    print(f"{icon} [{severity}] {status} — {result['scenario']}: {result.get('evidence', 'No evidence')}{reset}")

def main():
    print_banner()
    
   
    # agent = MockCopilotAgent()
    
    agent = AutoGenAgentWrapper(model_name="llama3.1")

    # agent = RealLangChainAgent()
    
    config = {
        "auto_stop_on_critical": False
    }
    
    orchestrator = GoalHijackOrchestrator(target_agent=agent, config=config)
    
    try:
        results = orchestrator.run_all_scenarios()
        
        print("\n📊 Test Summary:")
        print("-" * 60)
        for result in results:
            format_result(result)
        
       
        vuln_count = sum(1 for r in results if r.get("vulnerable", False))
        total = len(results)
        
        print("-" * 60)
        if vuln_count == 0:
            print("✅ All tests passed — Agent appears resilient to ASI01 attacks.")
        else:
            print(f"⚠️  {vuln_count}/{total} scenarios vulnerable to ASI01.")
            print("🔧 Recommended: Apply mitigations from OWASP ASI01 guidelines:")
            print("   • Treat all inputs as untrusted")
            print("   • Enforce least privilege for tools")
            print("   • Use intent capsules and human-in-the-loop for goal changes")
            
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()