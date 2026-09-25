---
id: TC-0019-read-custom-environment-variable
title: Verify a custom environmentVariables entry is readable via Spectra.env
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Verify a custom environmentVariables entry is readable via Spectra.env

## Test Steps
1. Read the DEMO_API_MODE variable via the typed Spectra.env
2. Assert it matches the value configured in spectra.config.ts's executionConfig.environmentVariables
