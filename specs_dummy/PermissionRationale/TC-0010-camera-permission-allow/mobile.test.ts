it("Confirm custom rationale dialog Allow triggers real permission request and grants camera access", async () => {
  // Navigate to the dedicated permission-rationale route (real router path, not a hash/scroll
  // section) via the header link.
  await Spectra.get("~nav-to-permission-demo").click();

  await Spectra.get("~permission-status-text").shouldHaveText("Not requested");

  await Spectra.get("~request-camera-permission-btn").click();

  // The custom rationale dialog appears first — no real permission dialog yet.
  await Spectra.get("~rationale-allow-btn").shouldBeVisible();

  await Spectra.get("~rationale-allow-btn").click();

  // Confirming the custom dialog triggers the real Android permission request. Grant it
  // on-demand right now, exactly like a real device automation flow would — the app itself
  // is resilient to the resulting race (see permission-rationale.tsx's recheck loop), so the
  // status still lands on "Granted" below regardless of exactly when this call resolves
  // relative to the OS dialog.
  await Spectra.grantPermission("android.permission.CAMERA");

  await Spectra.get("~permission-status-text").shouldHaveText("Granted");

  // Return to the home screen so later suites in the same batch don't inherit this route.
  await Spectra.get("~back-to-home-btn").click();
});
