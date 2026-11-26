# Security Baseline Scan Report

## Project
Microfinance Lending Platform

## 1. Static Application Security Testing (SAST)

**Tool:** Semgrep  
**Version:** 1.187.0

**Command executed:**
```powershell
semgrep scan --config p/python .
```

**Actual tool output:**
```text
┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘

⠋ Loading rules from registry...
Scanning 11 files (only git-tracked) with 151 Code rules:

  CODE RULES
  Scanning 2 files with 151 python rules.

  SUPPLY CHAIN RULES

  💎 Sign in with `semgrep login` and run
     `semgrep ci` to find dependency vulnerabilities and
     advanced cross-file findings.

  PROGRESS

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 0 (0 blocking)
 • Rules run: 151
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 151 rules on 2 files: 0 findings.
💎 Missed out on 923 pro rules since you aren't logged in!
⚡ Supercharge Semgrep OSS when you create a free account at https://sg.run/rules.
(need more rules? `semgrep login` for additional free Semgrep Registry rules)

✨ If Semgrep missed a finding, please send us feedback to let us know!
   See https://semgrep.dev/docs/reporting-false-negatives/
```

## 2. Dependency Vulnerability Scan

**Tool:** pip-audit  
**Version:** 2.10.1

**Command executed:**
```powershell
pip-audit -r requirements.txt
```

**Actual tool output:**
```text
WARNING:venv:Actual environment location may have moved due to redirects, links or junctions.
  Requested location: "C:\Users\LAPTOP~1\AppData\Local\Temp\tmp8wqyhf63\Scripts\python.exe"
  Actual location:    "C:\Users\Laptop Station\AppData\Local\Temp\tmp8wqyhf63\Scripts\python.exe"
No known vulnerabilities found
```

## 3. Overall Results

- Semgrep completed successfully with 0 findings.
- pip-audit reported no known vulnerabilities in the dependencies listed in requirements.txt.
- Both scans were executed successfully.

**Note:** These scans provide a baseline security check. Zero findings does not guarantee that the application is completely secure.