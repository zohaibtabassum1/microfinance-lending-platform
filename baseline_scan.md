# Security Baseline Scan Report

## Project
Microfinance Lending Platform

---

## 1. Static Application Security Testing (SAST) – Initial Scan

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

---

## 2. Dependency Vulnerability Scan – Initial Scan

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

---

## 3. Initial Baseline Results

- Semgrep completed successfully with 0 findings using the Python-specific configuration.
- The initial Semgrep scan ran 151 rules against 2 Python targets.
- pip-audit reported no known vulnerabilities in the dependencies listed in `requirements.txt`.
- Both scans were executed successfully.

**Note:** These scans provide a baseline security check. Zero findings does not guarantee that the application is completely secure.

---

# Follow-up Security Scan – 26 November 2026

## Reason for Semgrep Configuration Change

The initial scan used `--config p/python`, which applies Python-specific security rules and scanned 2 Python files.

Following supervisor feedback, the configuration was changed to `--config auto` to broaden the security analysis across the project, including HTML templates and other supported files.

The configuration was changed to improve scan coverage, not to reduce or hide security findings. Results from the two configurations are documented separately and should not be directly compared as identical scans.

The first `auto` scan covered 11 targets. The latest scan covered 13 tracked targets. The target count is reported separately for each run because the set of tracked project files can change as the project is updated.

## 1. Semgrep – Auto Configuration (First Follow-up Scan)

**Command executed:**

```powershell
semgrep scan --config auto .
```

**Results from the first follow-up scan:**

- Rules run: 307
- Targets scanned: 11
- Parsed lines: approximately 100%
- Findings: 1 blocking finding

**Finding:**

- Rule: `python.django.security.django-no-csrf-token`
- Location: `templates/login.html`
- Reported issue: Semgrep identified the form as missing a CSRF token under its Django-specific rule.

At the time of this scan, the finding was investigated and the login and loan application forms were checked for CSRF protection.

## 2. Semgrep – Auto Configuration (Latest Scan)

**Date:** 26 November 2026

**Command executed:**

```powershell
semgrep scan --config auto .
```

**Actual scan summary:**

```text
Findings: 1 (1 blocking)
Rules run: 307
Targets scanned: 13
Parsed lines: ~100.0%
Ran 307 rules on 13 files: 1 finding.
```

**Finding:**

- Rule: `python.django.security.django-no-csrf-token`
- Location: `templates/login.html`
- Reported issue: Semgrep identified the form as missing a CSRF token under its Django-specific rule.
- Actual code: The form contains a CSRF token generated using Flask-WTF's `csrf_token()` function.
- Status: The finding remains in the latest scan and is documented for manual review.

**Manual investigation:**

This project uses Flask and Jinja templates, not Django. Flask-WTF provides CSRF protection.

The login form contains:

```html
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

The loan application form also contains its CSRF token.

The following tests were performed:

- CSRF token added to the login form.
- CSRF token added to the loan application form.
- A POST request without a CSRF token was rejected with HTTP 400.
- Normal login submission worked successfully in the browser.
- Normal loan application submission worked successfully in the browser.

**Assessment:**

The finding appears to be a framework-specific false positive because the Semgrep rule targets Django templates and does not recognize the Flask-WTF/Jinja implementation.

Manual testing confirmed that CSRF validation works as expected. The finding has not been suppressed and remains documented for review.

---

## 3. pip-audit – Updated Dependencies

**Tool:** pip-audit
**Version:** 2.10.1

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

The audit completed successfully after Flask-WTF was added to `requirements.txt`.

The Windows virtual-environment path warning did not prevent the audit from completing.

---

## 4. Follow-up Results

- The initial Semgrep `p/python` scan ran 151 rules against 2 Python targets and reported 0 findings.
- The first Semgrep `auto` scan ran 307 rules against 11 targets and reported 1 Django-specific finding.
- The latest Semgrep `auto` scan ran 307 rules against 13 targets and reported the same Django-specific finding in `templates/login.html`.
- pip-audit reported no known vulnerabilities in the updated dependencies.
- Manual CSRF testing confirmed that requests without a valid token are rejected.
- Login and loan application forms were tested successfully in the browser.

---

## 5. Overall Security Assessment

The project was checked using Semgrep for static application security testing and pip-audit for dependency vulnerability scanning.

The initial Python-specific Semgrep scan reported zero findings. The broader `auto` scans reported one Django-specific finding that remains under manual review because the application uses Flask/Jinja and Flask-WTF.

Both initial and updated pip-audit scans reported no known vulnerabilities in the dependencies listed in `requirements.txt`.

CSRF protection was also tested manually. Requests without a valid CSRF token were rejected, while normal browser form submissions worked successfully.

**Security note:** These scans and manual tests provide a baseline security assessment for this educational project. They do not guarantee that the application is completely secure or production-ready.

## Known Security Gap: Missing Authentication Check on Profile Route

During supervisor review, a broken access control issue was identified in the `/profile` route.

Currently, the route does not verify whether a user is logged in before displaying borrower information. This means someone can access `/profile` directly without authenticating.

**Risk:** Unauthorized users may view borrower information.

**Status:** Identified and documented, but intentionally not fixed in this task, as the supervisor confirmed it is not a completion requirement.

**Future improvement:** Add server-side authentication checks to protected routes so only authenticated users can access borrower information. This issue should be addressed in the next security-focused task.