---
id: TC-0017-bypass-captcha-with-test-mode-flag
title: Bypass a live reCAPTCHA widget via an app-level test-only flag
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: unsupported
---

# Bypass a live reCAPTCHA widget via an app-level test-only flag

Real reCAPTCHA renders inside a cross-origin iframe (`google.com`), which Google explicitly
discourages driving via browser automation — there's no `Spectra.intercept()`-style network mock
for a live third-party widget's challenge/response flow. The demo embeds the real widget (site key
`6LcWK4QtAAAAAAeA8IAN20JceGQ7L-RWE-LfhZnB`) for visual completeness, but the test itself uses the
same pattern real projects use in CI: an app-level `window.__bypassCaptcha` flag the submit
handler honors instead of ever attempting to automate the actual challenge.

Mobile coverage is `unsupported`: a native captcha SDK (rather than a page-context script tag)
would need its own test-only bypass hook, which is outside what a generic web-style demo can show.

## Test Steps
1. Open the captcha matcher section
2. Click submit without the bypass flag and assert the widget refuses
3. Set the app-level bypass flag via browser.evaluate
4. Click submit again
5. Assert the submission message indicates the form was bypassed for automated testing
