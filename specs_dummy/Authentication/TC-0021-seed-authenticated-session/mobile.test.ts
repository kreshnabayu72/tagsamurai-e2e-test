it("Seed an authenticated session via Spectra.seedSession() instead of the real login UI", async () => {
  // The deep link asks the app to log itself in against a known test account and persist the
  // result itself — no login form was ever touched.
  await Spectra.seedSession();

  await AuthPage.statusBadge.shouldHaveText("Authenticated as demo@testspectra.dev");

  // Return to the home screen so later suites in the same batch don't inherit this route.
  await Spectra.get("~back-to-home-btn").click();
});
