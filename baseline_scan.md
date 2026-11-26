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

## Follow-up Security Scan – 26 November 2026

After adding CSRF protection using Flask-WTF, the security scans were run again.

### 1. Semgrep – Auto Configuration

**Command executed:**

```powershell
semgrep scan --config auto .
```

**Actual scan results:**

- Rules run: 307
- Targets scanned: 11
- Parsed lines: approximately 100%
- Findings: 1 blocking finding

**Finding:**

- Rule: `python.django.security.django-no-csrf-token`
- Location: `templates/login.html`
- Description: Semgrep reported a missing CSRF token in a manually created Django template form.

**Manual investigation:**

This project uses Flask and Jinja templates, not Django. The application uses Flask-WTF for CSRF protection.

The following tests were performed:

- CSRF token added to the login form.
- CSRF token added to the loan application form.
- A POST request without a CSRF token was rejected with HTTP 400.
- Normal login and loan application submissions worked successfully in the browser.

**Assessment:**

The finding appears to be framework-specific because the rule targets Django templates. Manual testing confirmed that Flask-WTF CSRF validation is working. The finding has not been suppressed and is documented for review.

### 2. pip-audit – Updated Dependencies

**Command executed:**

```powershell
pip-audit -r requirements.txt
```

**Actual tool output:**

```text
WARNING:venv:Actual environment location may have moved due to redirects, links or junctions.
  Requested location: "C:\Users\LAPTOP~1\AppData\Local\Temp\tmpoj39yk8o\Scripts\python.exe"
  Actual location:    "C:\Users\Laptop Station\AppData\Local\Temp\tmpoj39yk8o\Scripts\python.exe"
No known vulnerabilities found
```

The audit completed successfully after Flask-WTF was added to requirements.txt.

The Windows virtual-environment path warning did not prevent the audit from completing.

### 3. Follow-up Results

- Semgrep auto scanned 11 files using 307 rules and reported 1 Django-specific finding requiring manual review.
- pip-audit reported no known vulnerabilities in the updated dependencies.
- CSRF protection was manually tested and worked as expected.
- Login and loan application forms were tested successfully.