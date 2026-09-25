it("Seed an authenticated session via Spectra.seedSession() instead of the real login UI", async () => {
  // Logs in via a direct host-side API call and applies the resulting HttpOnly cookie straight
  // to the browser — no login form was ever touched.
  await Spectra.seedSession();

  await AuthPage.open();
  await AuthPage.checkStatusButton.click();
  await AuthPage.statusBadge.shouldHaveText("Authenticated as demo@testspectra.dev");
});
