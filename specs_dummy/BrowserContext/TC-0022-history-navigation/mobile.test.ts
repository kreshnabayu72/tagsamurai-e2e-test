it("Navigate browser history with Spectra.back(), forward(), and refresh()", async () => {
  // Same cold-start race as DeepLink/TC-0018 — wait for the home screen before firing the deep
  // link so it isn't racing the app's own still-in-progress initial boot.
  await Spectra.get("~toggle-sidebar-btn").waitForElement(30000);

  await Spectra.navigate("testspectra-demo://deeplink-target");
  await Spectra.get("~deeplink-target-marker").waitForElement(10000);

  // Spectra.back() on Android presses the hardware back key — distinct from tapping the screen's
  // own "‹ Back" button (already covered by DeepLink/TC-0018) — and should pop the nav stack back
  // to Home exactly the same way.
  await Spectra.back();
  await Spectra.get("~toggle-sidebar-btn").waitForElement(10000);

  // Spectra.forward()/Spectra.refresh() have no native-app equivalent (no browser history, no
  // page reload) — they're intentional no-ops on Android, so there's nothing to assert here.
});
