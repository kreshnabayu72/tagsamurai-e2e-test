it("Confirm custom rationale dialog Deny never triggers the real permission request", async () => {
  await Spectra.get("~nav-to-permission-demo").click();

  await Spectra.get("~request-camera-permission-btn").click();
  await Spectra.get("~rationale-deny-btn").shouldBeVisible();
  await Spectra.get("~rationale-deny-btn").click();

  // Deliberately never calls the real permission API — the status must reflect the custom
  // dialog's own decision, not any OS-level request.
  await Spectra.get("~permission-status-text").shouldHaveText("Declined in rationale dialog");

  await Spectra.get("~back-to-home-btn").click();
});
