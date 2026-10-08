it("Bypass a live reCAPTCHA widget via an app-level test-only flag", async () => {
  await MatchersPage.open("captcha");

  // Baseline: without the flag (and no completed challenge), the widget refuses to submit —
  // proving the success below is specifically driven by the bypass flag, not a stale state.
  await Spectra.get("#captcha-submit-btn").click();
  await Spectra.get("#captcha-submit-message").shouldContainText("complete the reCAPTCHA challenge");

  // Set BEFORE submitting — see this TC's spec.md for why this has to be an app-level bypass
  // rather than a network-level mock (real reCAPTCHA lives in a cross-origin iframe with no
  // request/response Spectra.intercept() could fulfill).
  await Spectra.browser.evaluate("window.__bypassCaptcha = true");

  await Spectra.get("#captcha-submit-btn").click();
  await Spectra.get("#captcha-submit-message").shouldContainText("bypassed for automated test");
});
